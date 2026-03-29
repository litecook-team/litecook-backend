from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Sum, Q

# Імпортуємо інструменти для кастомної фільтрації
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, NumberFilter, MultipleChoiceFilter
import random

from .models.favorite import FavoriteRecipe
from .models.weekly_menu import WeeklyMenu
from .models.ingredient import Ingredient
from .models.recipe import Recipe, Difficulty
from .serializers import IngredientSerializer, RecipeSerializer, FavoriteSerializer, WeeklyMenuSerializer, RecipeMatchSerializer


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

    class Meta:
        model = Recipe
        fields = ['is_seasonal']

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
        if self.action in ['list', 'retrieve', 'random_recipe']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    @action(detail=False, methods=['get'])
    def random_recipe(self, request):
        random_rec = self.get_queryset().order_by('?').first()
        if random_rec:
            serializer = self.get_serializer(random_rec)
            return Response(serializer.data)
        return Response({"detail": "Немає рецептів"}, status=404)

    # === ЕНДПОІНТ ДЛЯ ПІДБОРУ РЕЦЕПТІВ ===
    @action(detail=False, methods=['get'])
    def match(self, request):
        """
        Шукає рецепти за наявними інгредієнтами і сортує за кількістю збігів.
        Очікує: /api/recipes/match/?ingredients=1,2,3
        """
        ingredients_param = request.query_params.get('ingredients')

        if not ingredients_param:
            return Response([])  # Якщо нічого не передали, повертаємо пустий список

        ingredient_ids = [int(i.strip()) for i in ingredients_param.split(',') if i.strip().isdigit()]

        if not ingredient_ids:
            return Response([])

        queryset = self.get_queryset().annotate(
            total_count=Count('recipe_ingredients', distinct=True),
            match_count=Count(
                'recipe_ingredients',
                filter=Q(recipe_ingredients__ingredient_id__in=ingredient_ids),
                distinct=True
            )
        ).filter(
            match_count__gt=0  # Беремо тільки ті, де збігся хоча б 1
        ).order_by(
            '-match_count',  # Спочатку ті, де збігів найбільше (напр. 9)
            'total_count'  # Якщо збігів однаково, вище той, де загалом треба менше інгредієнтів
        )

        # Пагінація
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = RecipeMatchSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = RecipeMatchSerializer(queryset, many=True, context={'request': request})
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
            return Response({"error": "Запис не знайдено"}, status=404)


class WeeklyMenuViewSet(viewsets.ModelViewSet):
    serializer_class = WeeklyMenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WeeklyMenu.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def shopping_list(self, request):
        day = request.query_params.get('day_of_week')
        # Читаємо параметр з фронтенду (за замовчуванням True)
        use_fridge = request.query_params.get('use_fridge', 'true').lower() == 'true'

        menus = self.get_queryset()
        if day:
            menus = menus.filter(day_of_week=day)

        from .models.recipe import RecipeIngredient
        from users.models import UserIngredient

        raw_required = menus.values(
            'recipe__recipe_ingredients__ingredient_id',
            'recipe__recipe_ingredients__ingredient__name',
            'recipe__recipe_ingredients__unit'
        ).annotate(
            total_required=Sum('recipe__recipe_ingredients__amount')
        )

        merged_requirements = {}
        for req in raw_required:
            ing_id = req['recipe__recipe_ingredients__ingredient_id']
            if not ing_id:
                continue

            ing_name = req['recipe__recipe_ingredients__ingredient__name']
            unit = req['recipe__recipe_ingredients__unit']
            amount = req['total_required']

            if amount is None:
                amount = 0
            else:
                amount = float(amount)

            if unit == 'kg':
                unit = 'g'
                amount *= 1000
            elif unit == 'l':
                unit = 'ml'
                amount *= 1000

            key = (ing_id, ing_name, unit)
            if key not in merged_requirements:
                merged_requirements[key] = amount
            else:
                merged_requirements[key] += amount

        user_inventory = UserIngredient.objects.filter(user=request.user)
        inventory_dict = {}
        for item in user_inventory:
            unit = item.unit
            amount = float(item.amount) if item.amount else 0

            if unit == 'kg':
                unit = 'g'
                amount *= 1000
            elif unit == 'l':
                unit = 'ml'
                amount *= 1000

            key = (item.ingredient_id, unit)
            inventory_dict[key] = inventory_dict.get(key, 0) + amount

        final_list = []
        for (ing_id, ing_name, unit), total_req in merged_requirements.items():
            # ГОЛОВНА ЗМІНА: Якщо use_fridge == False, ми ігноруємо холодильник (беремо 0)
            have_amount = inventory_dict.get((ing_id, unit), 0) if use_fridge else 0

            to_buy_base = total_req - have_amount
            if to_buy_base < 0:
                to_buy_base = 0

            display_amount = to_buy_base
            display_unit = unit

            # Конвертація відбувається вже на базі правильного to_buy_base
            if unit == 'g' and display_amount >= 1000:
                display_amount = display_amount / 1000.0
                display_unit = 'kg'
            elif unit == 'ml' and display_amount >= 1000:
                display_amount = display_amount / 1000.0
                display_unit = 'l'

            if display_amount == int(display_amount):
                display_amount = int(display_amount)
            else:
                display_amount = round(display_amount, 2)

            final_list.append({
                'ingredient_id': ing_id,
                'ingredient_name': ing_name,
                'unit': display_unit,
                'required_amount': total_req,
                'already_have': have_amount,
                'to_buy': display_amount,
                'is_fully_stocked': to_buy_base == 0 and total_req > 0,
                '_sort_weight': to_buy_base
            })

        # Тепер сортування завжди буде ідеальним, адже _sort_weight підлаштовується під тогл!
        final_list.sort(key=lambda x: (x['_sort_weight'] > 0, x['_sort_weight']), reverse=True)

        for item in final_list:
            item.pop('_sort_weight', None)

        return Response(final_list)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

