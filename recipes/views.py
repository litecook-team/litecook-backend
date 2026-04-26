from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Sum, Q

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from datetime import date
from .models import RecipeOfDay

# Імпортуємо інструменти для кастомної фільтрації
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, NumberFilter, MultipleChoiceFilter
import random

from .models.favorite import FavoriteRecipe
from .models.weekly_menu import WeeklyMenu
from .models.ingredient import Ingredient
from .models.recipe import Recipe, Difficulty
from .serializers import IngredientSerializer, RecipeSerializer, FavoriteSerializer, WeeklyMenuSerializer, RecipeMatchSerializer

# === ФУНКЦІЯ ДЛЯ ПРОСТОГО ПЕРЕКЛАДУ ПОВІДОМЛЕНЬ API ===
def t_view(key, request):
    lang = getattr(request, 'LANGUAGE_CODE', 'uk')[:2] if request else 'uk'
    msgs = {
        'no_recipes': {
            'uk': "Рецептів не знайдено",
            'en': "No recipes found",
            'pl': "Nie znaleziono przepisów"
        },
        'not_found': {
            'uk': "Запис не знайдено",
            'en': "Record not found",
            'pl': "Nie znaleziono rekordu"
        },
        'email_req': {
            'uk': "Email та файл обов'язкові",
            'en': "Email and file are required",
            'pl': "E-mail i plik są wymagane"
        },
        'sent': {
            'uk': "Відправлено на пошту!",
            'en': "Sent to email!",
            'pl': "Wysłano na e-mail!"
        },
        'not_in_menu': {
            'uk': "Рецепт не знайдено в меню",
            'en': "Recipe not found in menu",
            'pl': "Przepis nie znaleziony w menu"
        },
        'pdf_subject': {
            'uk': "Ваш список продуктів | LITE cook",
            'en': "Your shopping list | LITE cook",
            'pl': "Twoja lista zakupów | LITE cook"
        },
        'pdf_body': {
            'uk': "Привіт! Ваш красивий список продуктів у прикріпленому PDF-файлі. Зручних та смачних покупок!",
            'en': "Hello! Your shopping list is attached as a PDF file. Happy and tasty shopping!",
            'pl': "Cześć! Twoja lista zakupów znajduje się w załączonym pliku PDF. Udanych zakupów!"
        }
    }
    return msgs.get(key, {}).get(lang, msgs.get(key, {}).get('uk'))

# ================= ПОТУЖНИЙ КАСТОМНИЙ ФІЛЬТР РЕЦЕПТІВ =================
class RecipeFilter(FilterSet):
    # 1. Пошук по інгредієнтах (очікує ID через кому: ?ingredients=1,5,12)
    ingredients = CharFilter(method='filter_by_ingredients')

    # 2. Час приготування (менше або дорівнює: ?max_time=30)
    max_time = NumberFilter(field_name='cooking_time', lookup_expr='lte')

    # 3. Складність (дозволяє обрати кілька: ?difficulty=easy&difficulty=medium)
    difficulty = MultipleChoiceFilter(choices=Difficulty.choices)

    # 4. Сезонність (очікує пори року через кому: ?season=summer,autumn)
    season = CharFilter(method='filter_by_season')

    # 5. Масиви: Кухня, Прийоми їжі, Дієти, Типи страв (очікують значення через кому: ?cuisine=ua,it)
    cuisine = CharFilter(method='filter_array_overlap', field_name='cuisine')
    meal_times = CharFilter(method='filter_array_overlap', field_name='meal_times')
    dietary_tags = CharFilter(method='filter_array_overlap', field_name='dietary_tags')
    dish_types = CharFilter(method='filter_array_overlap', field_name='dish_types')
    # Реєстрація кастомного поля для пошуку
    search_query = CharFilter(method='filter_search_query')

    # 3 НОВІ ФІЛЬТРИ:
    max_calories = NumberFilter(field_name='calories', lookup_expr='lte')  # Менше або дорівнює (калорії)
    months = CharFilter(method='filter_by_months')  # Фільтр по конкретних місяцях
    ingredient_categories = CharFilter(method='filter_by_ingredient_categories')  # Фільтр по категоріях інгредієнтів

    class Meta:
        model = Recipe
        fields = ['is_seasonal']

    # Метод обробки нашого розумного пошуку
    def filter_search_query(self, queryset, name, value):
        if not value: return queryset
        # Якщо це запит на /match/, ми не фільтруємо тут, бо match робить це сам!
        if 'match' in self.request.path: return queryset

        # Якщо є кома, розбиваємо по комі. Якщо ні - по пробілу.
        if ',' in value:
            terms = [t.strip() for t in value.split(',') if t.strip()]
        else:
            terms = [t.strip() for t in value.split() if t.strip()]

        # Звичайний пошук (якщо не match): Шукаємо хоча б ОДНЕ з введених слів у назві або інгредієнтах (OR)
        query = Q()
        for term in terms:
            query |= Q(title__icontains=term) | Q(ingredients__name__icontains=term)

        return queryset.filter(query).distinct()

    def filter_by_ingredients(self, queryset, name, value):
        """ Шукає рецепти, які містять ВСІ обрані інгредієнти (І те, І те) """
        if not value:
            return queryset
        # Розбиваємо рядок "1,5,12" на масив чисел [1, 5, 12]
        ingredient_ids = [int(id.strip()) for id in value.split(',') if id.strip().isdigit()]

        for ing_id in ingredient_ids:
            # Ланцюжок .filter() гарантує, що рецепт має КОЖЕН з цих інгредієнтів
            queryset = queryset.filter(ingredients__id=ing_id)
        return queryset

    def filter_array_overlap(self, queryset, name, value):
        """ Шукає збіг хоча б по одному елементу (АБО / OR). Наприклад, АБО Українська, АБО Італійська """
        if not value:
            return queryset
        values_list = [v.strip() for v in value.split(',')]
        # Магія PostgreSQL __overlap: чи є хоча б один збіг між масивом рецепта і списком користувача
        filter_kwarg = {f"{name}__overlap": values_list}
        return queryset.filter(**filter_kwarg)

    def filter_by_season(self, queryset, name, value):
        """ Об'єднує місяці всіх обраних сезонів і шукає перетин """
        if not value:
            return queryset

        seasons_map = {
            'winter': [12, 1, 2],
            'spring': [3, 4, 5],
            'summer': [6, 7, 8],
            'autumn': [9, 10, 11],
        }

        selected_seasons = [s.strip().lower() for s in value.split(',')]
        target_months = set()

        # Об'єднуємо всі місяці для вибраних сезонів
        for season in selected_seasons:
            if season in seasons_map:
                target_months.update(seasons_map[season])

        if target_months:
            return queryset.filter(seasonal_months__overlap=list(target_months))
        return queryset

    # === ЛОГІКА ДЛЯ НОВИХ ФІЛЬТРІВ ===
    def filter_by_months(self, queryset, name, value):
        """ Шукає рецепти, які підходять для обраних конкретних місяців """
        if not value: return queryset
        month_ids = [int(m.strip()) for m in value.split(',') if m.strip().isdigit()]
        if month_ids:
            return queryset.filter(seasonal_months__overlap=month_ids)
        return queryset

    def filter_by_ingredient_categories(self, queryset, name, value):
        """ Шукає рецепти, в яких є інгредієнти з обраних категорій """
        if not value: return queryset
        categories = [c.strip() for c in value.split(',')]
        # Використовуємо .distinct(), щоб рецепт не дублювався, якщо там кілька овочів
        return queryset.filter(ingredients__category__in=categories).distinct()


# ================= VIEWSET РЕЦЕПТІВ =================
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.annotate(likes_count=Count('favorited_by')).all()
    serializer_class = RecipeSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Підключаємо наш супер-фільтр
    filterset_class = RecipeFilter

    # Пошук по тексту (Назва рецепта або назва інгредієнта)
    search_fields = ['title', 'ingredients__name']

    ordering_fields = ['likes_count', 'cooking_time', 'calories']

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'random_recipe', 'match']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_queryset(self):
        # Базовий запит з підрахунком лайків
        qs = Recipe.objects.annotate(likes_count=Count('favorited_by')).all()

        # АВТОМАТИЧНА ФІЛЬТРАЦІЯ ЗА ПРОФІЛЕМ КОРИСТУВАЧА
        if self.request.user.is_authenticated:
            user = self.request.user

            # 1. Приховуємо рецепти, що містять алергени користувача (БЕЗПЕКА)
            # allergies - це ManyToManyField, тому перевіряємо через .exists()
            if user.allergies.exists():
                allergy_ids = user.allergies.values_list('id', flat=True)
                qs = qs.exclude(ingredients__id__in=allergy_ids)

            # 2. Сувора фільтрація: показувати тільки рецепти, що відповідають обраним дієтам
            # Використовуємо `or []`, щоб безпечно обробити значення None з бази даних
            user_diets = user.dietary_preferences or []
            valid_diets = [d for d in user_diets if d]
            if valid_diets:
                qs = qs.filter(dietary_tags__overlap=valid_diets)

            # 3. Сувора фільтрація: показувати тільки обрані кухні
            user_cuisines = user.favorite_cuisines or []
            valid_cuisines = [c for c in user_cuisines if c]
            if valid_cuisines:
                qs = qs.filter(cuisine__overlap=valid_cuisines)

        return qs

    @action(detail=False, methods=['get'])
    def random_recipe(self, request):
        today = date.today()

        # 1. Перевіряємо, чи вже був згенерований рецепт на сьогодні
        try:
            daily_record = RecipeOfDay.objects.get(date=today)
            recipe = daily_record.recipe
        except RecipeOfDay.DoesNotExist:
            # 2. Якщо немає — генеруємо випадковий і ЗБЕРІГАЄМО його в базу
            recipe = Recipe.objects.order_by('?').first()
            if recipe:
                RecipeOfDay.objects.create(date=today, recipe=recipe)

        # Перевірка на випадок, якщо база рецептів взагалі порожня
        if not recipe:
            return Response({"detail": t_view('no_recipes', request)}, status=404)

        # 3. Віддаємо рецепт як зазвичай
        serializer = self.get_serializer(recipe)
        return Response(serializer.data)

    # === ЕНДПОІНТ ДЛЯ ПІДБОРУ РЕЦЕПТІВ ===
    @action(detail=False, methods=['get'])
    def match(self, request):
        """
        Шукає рецепти за наявними інгредієнтами (за ID або за НАЗВОЮ) і сортує за кількістю збігів.
        Очікує: /api/recipes/match/?ingredients=1,2,3 (ЛОГІКА "АБО" - знайти рецепти хоча б з одним інгредієнтом)
        """
        ingredients_param = request.query_params.get('ingredients')
        search_query = request.query_params.get('search_query')

        ingredient_ids = []

        # 1. Якщо фронтенд передав точні ID інгредієнтів (головний сценарій)
        if ingredients_param:
            ingredient_ids = [int(i.strip()) for i in ingredients_param.split(',') if i.strip().isdigit()]

        # 2. Фолбек: якщо передали текст (якщо фронтенд чомусь не зміг знайти ID)
        elif search_query:
            if ',' in search_query:
                terms = [t.strip().lower() for t in search_query.split(',') if t.strip()]
            else:
                terms = [t.strip().lower() for t in search_query.split() if t.strip()]

            if terms:
                # Використовуємо name__in для точного збігу слів
                matched_ingredients = Ingredient.objects.filter(name__in=terms).values_list('id', flat=True)
                ingredient_ids = list(matched_ingredients)

        queryset = self.get_queryset()

        # === ГОЛОВНИЙ ФІКС ===
        # Ми повинні застосувати інші фільтри (калорії, кухня тощо),
        # АЛЕ ми мусимо ПРИХОВАТИ параметр 'ingredients' від стандартного RecipeFilter.
        # Бо якщо ми цього не зробимо, RecipeFilter застосує свою логіку "І" (AND),
        # а нам потрібна логіка "АБО" (OR), яку ми самі зробимо нижче.
        mutable_query_params = request.query_params.copy()
        if 'ingredients' in mutable_query_params:
            del mutable_query_params['ingredients']

        filterset = RecipeFilter(mutable_query_params, request=request, queryset=queryset)
        if filterset.is_valid():
            queryset = filterset.qs

        # Якщо ввели інгредієнти, але їх немає в базі взагалі - повертаємо пусто
        if (ingredients_param or search_query) and not ingredient_ids:
            return Response([])

        # 3. Анотуємо та фільтруємо за логікою "АБО" (якщо є хоча б один з інгредієнтів)
        if ingredient_ids:
            queryset = queryset.annotate(
                total_count=Count('recipe_ingredients', distinct=True),
                match_count=Count(
                    'recipe_ingredients',
                    filter=Q(recipe_ingredients__ingredient_id__in=ingredient_ids),
                    distinct=True
                )
            ).filter(
                match_count__gt=0  # Ось тут працює "АБО": якщо є хоча б 1 збіг, залишаємо рецепт
            ).order_by(
                '-match_count',
                'total_count'
            )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = RecipeSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = RecipeSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

# ================= ІНШІ VIEWSETS =================
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteRecipe.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        # Дозволяє видаляти за ID рецепта: /api/favorites/ID_РЕЦЕПТА/
        return FavoriteRecipe.objects.get(user=self.request.user, recipe_id=self.kwargs['pk'])

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=204)
        except FavoriteRecipe.DoesNotExist:
            return Response({"error": t_view('not_found', request)}, status=404)


class WeeklyMenuViewSet(viewsets.ModelViewSet):
    serializer_class = WeeklyMenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WeeklyMenu.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def shopping_list(self, request):
        day = request.query_params.get('day_of_week')
        use_fridge = request.query_params.get('use_fridge', 'true').lower() == 'true'

        menus = self.get_queryset()
        if day:
            menus = menus.filter(day_of_week=day)

        from .models.recipe import RecipeIngredient
        from users.models import UserIngredient

        # === ФІКС: Отримуємо поточну мову з фронтенду ===
        lang = getattr(request, 'LANGUAGE_CODE', 'uk')[:2] if request else 'uk'

        # Додаємо вибірку name_en та name_pl з бази
        raw_required = menus.values(
            'recipe__recipe_ingredients__ingredient_id',
            'recipe__recipe_ingredients__ingredient__name',
            'recipe__recipe_ingredients__ingredient__name_en',
            'recipe__recipe_ingredients__ingredient__name_pl',
            'recipe__recipe_ingredients__unit',
            'recipe__recipe_ingredients__ingredient__image'
        ).annotate(
            total_required=Sum('recipe__recipe_ingredients__amount')
        )

        def normalize_unit(amount, unit):
            if amount is None: return None, unit
            amount = float(amount)
            if unit == 'kg': return amount * 1000, 'g'
            if unit == 'l': return amount * 1000, 'ml'
            if unit == 'glass': return amount * 200, 'ml'
            if unit == 'tbsp': return amount * 15, 'ml'
            if unit == 'tsp': return amount * 5, 'ml'
            if unit == 'drop': return amount * 0.05, 'ml'
            if unit == 'bunch': return amount * 40, 'g'
            if unit == 'sprig': return amount * 2, 'g'
            if unit == 'clove': return amount * 4, 'g'
            return amount, unit

        merged_requirements = {}
        for req in raw_required:
            ing_id = req['recipe__recipe_ingredients__ingredient_id']
            if not ing_id:
                continue

            # === ФІКС: Визначаємо назву інгредієнта залежно від обраної мови ===
            ing_name = req['recipe__recipe_ingredients__ingredient__name']
            if lang == 'en' and req['recipe__recipe_ingredients__ingredient__name_en']:
                ing_name = req['recipe__recipe_ingredients__ingredient__name_en']
            elif lang == 'pl' and req['recipe__recipe_ingredients__ingredient__name_pl']:
                ing_name = req['recipe__recipe_ingredients__ingredient__name_pl']

            image = req['recipe__recipe_ingredients__ingredient__image']

            amount, unit = normalize_unit(req['total_required'], req['recipe__recipe_ingredients__unit'])

            key = (ing_id, ing_name, unit, image)
            if key not in merged_requirements:
                merged_requirements[key] = amount
            else:
                if amount is not None and merged_requirements[key] is not None:
                    merged_requirements[key] += amount

        user_inventory = UserIngredient.objects.filter(user=request.user)
        inventory_dict = {}
        for item in user_inventory:
            # Нормалізуємо кількість і одиницю для ХОЛОДИЛЬНИКА
            amount, unit = normalize_unit(item.amount, item.unit)
            if amount is not None:
                key = (item.ingredient_id, unit)
                inventory_dict[key] = inventory_dict.get(key, 0) + amount

        final_list = []
        for (ing_id, ing_name, unit, image), total_req in merged_requirements.items():

            have_amount = 0
            has_any_amount = False  # Додаємо прапорець, чи є хоч щось в холодильнику
            inv_display_unit = unit  # За замовчуванням одиниця залишку така ж, як у рецепті

            if use_fridge:
                # Шукаємо точний збіг (наприклад, pcs і pcs, або ml і ml)
                if (ing_id, unit) in inventory_dict:
                    have_amount = inventory_dict[(ing_id, unit)]
                    has_any_amount = True
                    inv_display_unit = unit

                # КУЛІНАРНА МАГІЯ: Об'єм <-> Вага
                elif unit == 'ml' and (ing_id, 'g') in inventory_dict:
                    have_amount = inventory_dict[(ing_id, 'g')]
                    has_any_amount = True
                    inv_display_unit = 'g'

                elif unit == 'g' and (ing_id, 'ml') in inventory_dict:
                    have_amount = inventory_dict[(ing_id, 'ml')]
                    has_any_amount = True
                    inv_display_unit = 'ml'

                # === НОВА МАГІЯ: Штуки <-> Вага (Грами) ===
                elif unit == 'pcs' and (ing_id, 'g') in inventory_dict:
                    avg_weight = 150  # Дефолт для фруктів/овочів (Авокадо, Банан)
                    name_check = ing_name.lower()
                    if 'яйц' in name_check or 'egg' in name_check or 'jajk' in name_check:
                        avg_weight = 50
                    elif 'лимон' in name_check or 'lemon' in name_check or 'cytryna' in name_check:
                        avg_weight = 100
                    elif 'часник' in name_check or 'garlic' in name_check or 'czosnek' in name_check:
                        avg_weight = 5  # Зубчик часнику

                    # Переводимо грами з холодильника в штуки
                    have_amount = inventory_dict[(ing_id, 'g')] / avg_weight
                    has_any_amount = True
                    inv_display_unit = 'g'

                elif unit == 'g' and (ing_id, 'pcs') in inventory_dict:
                    avg_weight = 150
                    name_check = ing_name.lower()
                    if 'яйц' in name_check or 'egg' in name_check or 'jajk' in name_check:
                        avg_weight = 50
                    elif 'лимон' in name_check or 'lemon' in name_check or 'cytryna' in name_check:
                        avg_weight = 100
                    elif 'часник' in name_check or 'garlic' in name_check or 'czosnek' in name_check:
                        avg_weight = 5

                    # Переводимо штуки з холодильника в грами
                    have_amount = inventory_dict[(ing_id, 'pcs')] * avg_weight
                    has_any_amount = True
                    inv_display_unit = 'pcs'
                # ==========================================

                # МАГІЯ ДЛЯ "ЗА СМАКОМ" (taste) ТА "ДРІБОК" (pinch)
                elif unit in ['taste', 'pinch']:
                    for (inv_ing_id, inv_unit), inv_amount in inventory_dict.items():
                        if inv_ing_id == ing_id and inv_amount > 0:
                            has_any_amount = True
                            have_amount = inv_amount
                            inv_display_unit = inv_unit  # ВАЖЛИВО: ловимо реальні грами/мл з холодильника!
                            break

            # ================= РОЗРАХУНОК "ЩО КУПИТИ" =================
            display_unit = unit

            # Якщо рецепт просить "За смаком" (None)
            if total_req is None:
                # ПОРІГ БЕЗПЕКИ: вважаємо, що продукту достатньо, ТІЛЬКИ якщо його >= 15 грамів/мл
                is_enough_for_taste = has_any_amount and have_amount >= 70

                if is_enough_for_taste:
                    # Вистачає з головою - повністю приховуємо
                    to_buy_base = 0
                    display_amount = 0
                else:
                    # Занадто мало (або зовсім немає) - треба купити.
                    # Ставимо 1, щоб пройшло фільтр, але display_amount = None для напису "за смаком"
                    to_buy_base = 1
                    display_amount = None
            else:
                # Стандартний математичний розрахунок для звичайних одиниць
                to_buy_base = max(0, total_req - have_amount)
                display_amount = to_buy_base

            # Зворотна конвертація для красивого виводу (якщо вийшло більше 1000 г, покажемо в кг)
            if display_amount is not None and display_amount > 0:
                if unit == 'g' and display_amount >= 1000:
                    display_amount, display_unit = display_amount / 1000.0, 'kg'
                elif unit == 'ml' and display_amount >= 1000:
                    display_amount, display_unit = display_amount / 1000.0, 'l'

                # Прибираємо зайві нулі після коми (наприклад, 1.0 -> 1)
                if display_amount == int(display_amount):
                    display_amount = int(display_amount)
                else:
                    display_amount = round(display_amount, 2)

            final_list.append({
                'ingredient_id': ing_id,
                'ingredient_name': ing_name,
                'ingredient_image': f"/media/{image}" if image else None,
                'unit': display_unit,
                'inventory_unit': inv_display_unit,
                'required_amount': total_req,
                'already_have': have_amount,
                'to_buy': display_amount,
                # is_fully_stocked тепер враховує і "за смаком"
                'is_fully_stocked': to_buy_base == 0,
                '_sort_weight': to_buy_base
            })

        # Спочатку ті продукти, які треба купити
        final_list.sort(key=lambda x: (x['_sort_weight'] > 0, x['_sort_weight']), reverse=True)
        for item in final_list: item.pop('_sort_weight', None)

        return Response(final_list)

    @action(detail=False, methods=['post'])
    def email_pdf(self, request):
        email = request.data.get('email')
        pdf_file = request.FILES.get('pdf_file')

        if not email or not pdf_file:
            return Response({"error": t_view('email_req', request)}, status=400)

        # Передаємо frontend_url, щоб у листі завантажився ваш фірмовий фон 'exit.jpg'
        context = {
            'frontend_url': settings.FRONTEND_URL,
            'lang': getattr(request, 'LANGUAGE_CODE', 'uk')[:2]
        }

        # 3. Рендеримо нашу нову красиву HTML-версію
        html_content = render_to_string('emails/shopping_list_email.html', context)

        # 4. Формуємо лист
        mail = EmailMultiAlternatives(
            subject=t_view('pdf_subject', request),
            body=t_view('pdf_body', request),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email]
        )

        # 5. Додаємо HTML версію та PDF файл
        mail.attach_alternative(html_content, "text/html")
        mail.attach(pdf_file.name, pdf_file.read(), 'application/pdf')

        # 6. Відправляємо
        mail.send()

        return Response({"message": t_view('sent', request)})

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['delete'], url_path=r'remove-recipe/(?P<recipe_id>[^/.]+)')
    def remove_recipe(self, request, recipe_id=None):
        # Шукаємо і видаляємо всі записи з цим рецептом для поточного користувача
        deleted, _ = self.get_queryset().filter(recipe_id=recipe_id).delete()

        if deleted:
            return Response(status=204)  # 204 No Content - успішне видалення
        return Response({"error": t_view('not_in_menu', request)}, status=404)


# ================= АСИСТЕНТ GEMINI AI =================
import os
import google.generativeai as genai
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from users.models import SiteSettings


class AIChatThrottle(UserRateThrottle):
    rate = '30/minute'  # Захист від спаму: не більше 30 повідомлень на хвилину від юзера


class AIChatView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [AIChatThrottle]

    # GET-метод, щоб фронтенд міг дізнатися чи увімкнений ШІ
    def get(self, request):
        settings_obj = SiteSettings.load()
        return Response({"is_enabled": settings_obj.is_ai_enabled})

    def post(self, request):
        # Перевіряємо чи адмін не вимкнув чат
        settings_obj = SiteSettings.load()
        if not settings_obj.is_ai_enabled:
            return Response({"error": "AI-асистент тимчасово вимкнений адміністратором."}, status=403)

        user_message = request.data.get('message')
        current_path = request.data.get('current_path', '/')
        chat_history = request.data.get('history', [])

        if not user_message:
            return Response({"error": "Повідомлення порожнє"}, status=400)

        page_context = self.get_page_context(current_path)

        # === ВДОСКОНАЛЕНА ІНСТРУКЦІЯ ДЛЯ ШІ ===
        system_instruction = f"""
Ти — 'LITE cook AI', привітний, стильний та лаконічний персональний кулінарний асистент платформи LITE cook.
Твоє завдання — допомагати користувачу, надихати його на готування та чітко відповідати на запитання про сайт.

СТРУКТУРА САЙТУ ТА ПОСИЛАННЯ (ЗАВЖДИ ВИКОРИСТОВУЙ ЇХ, ЯКЩО РЕКОМЕНДУЄШ СТОРІНКУ):
- [Головна сторінка](/)
- [Підібрати рецепт](/recipes)
- [Улюблені](/favorites)
- [Тижневе меню](/menu)
- [Мій профіль](/profile)
- [Про нас](/about)
- [Політика конфіденційності](/privacy) (має підсторінки: Збір даних, Використання, Куки, Контроль, Переглянути повністю)

ІНФОРМАЦІЯ ПРО ПРОЄКТ:
LITE cook — це сучасна платформа для підбору рецептів на основі інгредієнтів, що є вдома у користувача, з можливістю планування тижневого меню та генерації списку покупок у PDF.

ЄДИНІ 10 ФІЛЬТРІВ НА СТОРІНЦІ "ПІДІБРАТИ РЕЦЕПТ":
1. Інгредієнти (це теж фільтр)
2. Групи продуктів
3. Прийом їжі
4. Тип страви
5. Кухня
6. Складність
7. Час приготування
8. Калорійність
9. Дієтичні обмеження
10. Сезонність

КОНТЕКСТ КОРИСТУВАЧА:
Зараз користувач знаходиться за адресою: {current_path}.
Деталі: {page_context}.

ПРАВИЛА ПОВЕДІНКИ (СУВОРО!):
1. Відповідай коротко, лаконічно, без "води" (максимум 1-3 невеликі абзаци).
2. Якщо перераховуєш фільтри або функції — роби один звичайний маркований список. НІКОЛИ не роби вкладених багаторівневих списків.
3. Згадуючи сторінку сайту, ОБОВ'ЯЗКОВО роби її клікабельною (використовуй Markdown: [Назва сторінки](/url)).
4. Відповідай ТІЛЬКИ на теми кулінарії та функціоналу LITE cook. На інші теми тактовно відмовляй: "Вибачте, я фахівець виключно з кулінарії та платформи LITE cook ✨".
"""

        try:
            if not getattr(settings, 'GEMINI_API_KEY', None) and not os.environ.get("GEMINI_API_KEY"):
                print("ПОМИЛКА: Ключ GEMINI_API_KEY не знайдено!")
                return Response({"error": "Ключ ШІ не налаштовано."}, status=500)

            genai.configure(api_key=getattr(settings, 'GEMINI_API_KEY', os.environ.get("GEMINI_API_KEY")))

            target_model = "gemini-2.0-flash"
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods and 'flash' in m.name.lower():
                    target_model = m.name
                    break

            model = genai.GenerativeModel(
                model_name=target_model,
                system_instruction=system_instruction
            )

            formatted_history = []
            for msg in chat_history:
                role = "user" if msg['role'] == 'user' else "model"
                formatted_history.append({"role": role, "parts": [msg['text']]})

            chat = model.start_chat(history=formatted_history)
            response = chat.send_message(user_message)

            return Response({"reply": response.text})

        except Exception as e:
            error_msg = str(e)
            print("Gemini Error:", error_msg)
            return Response({"error": error_msg}, status=500)

    def get_page_context(self, path):
        # ФІКС: Виправили опис сторінки рецептів
        if 'profile' in path:
            return "Тут користувач може керувати аватаром, іменем, паролем, алергіями, улюбленими кухнями та дієтами. А також вести віртуальний холодильник ('Мої продукти') і читати кулінарні поради."
        elif 'menu' in path:
            return "Тут користувач планує страви на тиждень і генерує PDF список покупок (враховуючи свій віртуальний холодильник)."
        elif 'recipes' in path:
            return "Це сторінка пошуку. Тут користувач підбирає рецепти, використовуючи 10 доступних фільтрів (включаючи пошук за конкретними інгредієнтами)."
        elif 'favorites' in path:
            return "Тут зберігаються улюблені рецепти користувача."
        elif 'about' in path:
            return "Це сторінка 'Про нас'."
        elif 'privacy' in path:
            return "Це сторінка 'Політика конфіденційності'."
        return "Це загальна сторінка сайту."

    # def get_page_context(self, path):
    #     # Маппінг шляхів до описів
    #     if 'profile' in path:
    #         return "Користувач у своєму профілі. Він може додавати, змінювати, видаляти аватарку (своє фотозображення), редагувати ім'я, міняти пароль, додавати алергії (інгредієнти на які у користувача алергії), дієти (харчові обмеження яких дотримується користувач, наприклад користувач вегетаріанець) або наповнювати свій віртуальний холодильник (Мої продукти, додавати продукти які є у користувача вдома). Також може ознайомитися із порадами (всього 3 поради) від LITE cook, а також бачити статистику по своїх улюблених рецептах, кухнях, алергіях, харчових обмеженнях, його продуктах (кількість)."
    #     elif 'menu' in path:
    #         return "Користувач на сторінці Тижневого меню. Він може розпланувати рецепти по днях тижня та прийомах їжі, а також згенерувати список покупок на конкретний день або цілий тиждень (з урахуванням або без урахування його продуктів в холодильнику)."
    #     elif 'recipes' in path:
    #         return "Користувач на сторінці пошуку рецептів. Тут він може шукати рецепти за наявними інгредієнтами або використовувати фільтри (кухня, складність, сезонність, групи продуктів, прийом їжі, тип страви, час приготування, калорійність, дієтичні обмеження)."
    #     elif 'favorites' in path:
    #         return "Користувач переглядає свої збережені (улюблені) рецепти."
    #     return "Користувач на головній або загальній сторінці сайту. Він бачить рецепт дня від LITE cook, а також три переваги чому варто користуватися саме сайтом LITE cook."