from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .ingredient import Month
from datetime import date
from django.core.exceptions import ValidationError

# ================= КЛАСИ CHOICES ДЛЯ РЕЦЕПТІВ =================

class Difficulty(models.TextChoices):
    EASY = 'easy', 'Легкий'
    MEDIUM = 'medium', 'Середній'
    HARD = 'hard', 'Важкий'


class MealTime(models.TextChoices):
    BREAKFAST = 'breakfast', 'Сніданок'
    LUNCH = 'lunch', 'Обід'
    DINNER = 'dinner', 'Вечеря'
    SNACK = 'snack', 'Перекус'


class Diet(models.TextChoices):
    TRADITIONAL = 'traditional', 'Традиційний (без обмежень)'
    VEGETARIAN = 'vegetarian', 'Вегетаріанський'
    VEGAN = 'vegan', 'Веганський'
    DIETARY = 'dietary', 'Дієтичний'
    GLUTEN_FREE = 'gluten_free', 'Безглютеновий'
    LACTOSE_FREE = 'lactose_free', 'Безлактозний'
    SUGAR_FREE = 'sugar_free', 'Без цукру'
    HIGH_PROTEIN = 'high_protein', 'Високобілковий'
    MEAT = 'meat_diet', 'М’ясний'
    SEAFOOD_DIET = 'seafood_diet', 'Морський (Морепродукти)'

class DishType(models.TextChoices):
    FIRST = 'first', 'Перша страва'
    MAIN = 'main', 'Основна страва'
    GARNISH = 'garnish', 'Гарнір'
    SALAD = 'salad', 'Салат'
    SNACK = 'snack', 'Закуска'
    DESSERT = 'dessert', 'Десерт'
    DRINK = 'drink', 'Напій'
    SAUCE = 'sauce', 'Соус'
    SOUP = 'soup', 'Суп'
    PASTA = 'pasta', 'Паста'
    SMOOTHIE = 'smoothie', 'Смузі'
    PORRIDGE = 'porridge', 'Каша'
    OMELET = 'omelet', 'Омлет / Яєчна страва'
    FLOUR = 'flour', 'Борошняна страва'
    MEAT = 'meat', 'М’ясна страва'
    FISH = 'fish', 'Рибна страва'
    SEAFOOD = 'seafood', 'Морепродукти'
    COLD_SNACK = 'cold_snack', 'Холодна закуска'
    HOT_SNACK = 'hot_snack', 'Гаряча закуска'
    FESTIVE = 'festive', 'Святкова страва'
    ASPIC = 'aspic', 'Заливне'
    STEW = 'stew', 'Рагу / тушкована страва'

class Cuisine(models.TextChoices):
    EUROPEAN = 'eu', '🇪🇺 Європейська кухня'
    MEDITERRANEAN = 'mediterranean', '🌊 Середземноморська кухня'
    ITALIAN = 'it', '🇮🇹 Італійська кухня'
    MEXICAN = 'mx', '🇲🇽 Мексиканська кухня'
    INTERNATIONAL = 'intl', '🌍 Міжнародна кухня'
    UKRAINIAN = 'ua', '🇺🇦 Українська кухня'
    FRENCH = 'fr', '🇫🇷 Французька кухня'
    AMERICAN = 'us', '🇺🇸 Американська кухня'
    CHINESE = 'cn', '🇨🇳 Китайська кухня'
    JAPANESE = 'jp', '🇯🇵 Японська кухня'
    ASIAN = 'asian', '🥢 Азійська кухня'
    BRITISH = 'gb', '🇬🇧 Британська кухня'
    AUTHOR = 'author', '👨‍🍳 Авторська кухня'
    INDIAN = 'in', '🇮🇳 Індійська кухня'


class UnitChoice(models.TextChoices):
    G = 'g', 'Грам (г)'
    KG = 'kg', 'Кілограм (кг)'
    ML = 'ml', 'Мілілітр (мл)'
    L = 'l', 'Літр (л)'
    TSP = 'tsp', 'Чайна ложка (ч. л.)'
    TBSP = 'tbsp', 'Столова ложка (ст. л.)'
    GLASS = 'glass', 'Склянка (скл.)'
    PCS = 'pcs', 'Штука (шт.)'
    PACK = 'pack', 'Упаковка / Пачка (уп.)'
    CAN = 'can', 'Банка'
    LEAF = 'leaf', 'Лист'
    CLOVE = 'clove', 'Зубчик'
    PINCH = 'pinch', 'Дрібка'
    BUNCH = 'bunch', 'Пучок'
    SPRIG = 'sprig', 'Гілочка'
    STALK = 'stalk', 'Стебло'
    DROP = 'drop', 'Крапля'
    CM = 'cm', 'Сантиметр (см)'
    TASTE = 'taste', 'За смаком'
    GARNISH = 'garnish', 'Для подачі / прикраси'
    FRYING = 'frying', 'Для смаження'
    SLICE = 'slice', 'Часточка'


# ================= МОДЕЛІ =================

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва рецепта")
    description = models.TextField(verbose_name="Опис")

    title_en = models.CharField(max_length=200, blank=True, null=True, verbose_name="Назва (EN)")
    title_pl = models.CharField(max_length=200, blank=True, null=True, verbose_name="Назва (PL)")
    description_en = models.TextField(blank=True, null=True, verbose_name="Опис (EN)")
    description_pl = models.TextField(blank=True, null=True, verbose_name="Опис (PL)")
    # =================================

    image = models.ImageField(upload_to='recipes/images/', verbose_name="Фото рецепта")

    source = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Джерело рецепту",
        help_text="Вкажіть автора, ресторан або додайте посилання (URL) на оригінал"
    )

    source_en = models.CharField(max_length=500, blank=True, null=True, verbose_name="Джерело (EN)")
    source_pl = models.CharField(max_length=500, blank=True, null=True, verbose_name="Джерело (PL)")

    cooking_time = models.PositiveIntegerField(verbose_name="Час приготування (хв)")
    portions = models.PositiveIntegerField(default=1, verbose_name="Кількість порцій")
    calories = models.PositiveIntegerField(verbose_name="Калорії на 1 порцію")

    difficulty = models.CharField(max_length=20, choices=Difficulty.choices, verbose_name="Складність")

    # поля для автоматичної сезонності
    is_seasonal = models.BooleanField(default=False, verbose_name="Сезонний рецепт")
    seasonal_months = ArrayField(models.IntegerField(choices=Month.choices), blank=True, default=list)
    cuisine = ArrayField(models.CharField(max_length=50, choices=Cuisine.choices), blank=True, default=list)
    meal_times = ArrayField(models.CharField(max_length=20, choices=MealTime.choices), blank=True, default=list)
    dietary_tags = ArrayField(models.CharField(max_length=30, choices=Diet.choices), blank=True, default=list)
    dish_types = ArrayField(models.CharField(max_length=30, choices=DishType.choices), blank=True, default=list)

    ingredients = models.ManyToManyField('recipes.Ingredient', through='RecipeIngredient', related_name='recipes')

    # ================= Метадані часу =================
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    class Meta:
        verbose_name = "Recipe (Рецепт)"
        verbose_name_plural = "Recipes (Рецепти)"
        # сортуємо за датою створення (найновіші зверху)
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def update_seasonality(self):
        """Автоматичний розрахунок сезонності: якщо є хоча б 1 сезонний інгредієнт"""
        ingredients = self.ingredients.all()

        seasonal_ings = [ing for ing in ingredients if ing.is_seasonal and ing.seasonal_months]

        if seasonal_ings:
            self.is_seasonal = True
            months_set = set()
            for ing in seasonal_ings:
                months_set.update(ing.seasonal_months)
            self.seasonal_months = sorted(list(months_set))
        else:
            self.is_seasonal = False
            self.seasonal_months = []

        # не додаємо 'updated_at' сюди, бо auto_now=True оновить його автоматично
        self.save(update_fields=['is_seasonal', 'seasonal_months', 'updated_at'])


class RecipeIngredient(models.Model):
    """
    Проміжна модель, яка з'єднує рецепт, інгредієнт, їх кількість та одиницю виміру.
    """
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='recipe_ingredients',
                               verbose_name="Рецепт")
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, verbose_name="Інгредієнт")

    # Кількість (може бути пустим, якщо це "За смаком" або "Дрібка")
    amount = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Кількість")
    unit = models.CharField(max_length=20, choices=UnitChoice.choices, default=UnitChoice.G,
                            verbose_name="Одиниця виміру")

    class Meta:
        verbose_name = "Інгредієнт в рецепті"
        verbose_name_plural = "Інгредієнти в рецепті"
        # Щоб один і той самий інгредієнт не додали двічі в один рецепт
        unique_together = ('recipe', 'ingredient')

    # ВАЛІДАЦІЯ
    def clean(self):
        super().clean()
        if self.ingredient:
            allowed_units = self.ingredient.get_allowed_units()
            if self.unit not in allowed_units:
                # Отримуємо назви дозволених одиниць
                allowed_labels = [dict(UnitChoice.choices).get(u) for u in allowed_units]
                raise ValidationError({
                    'unit': f"Одиниця виміру '{self.get_unit_display()}' недопустима для інгредієнта '{self.ingredient.name}'. "
                            f"Дозволені одиниці: {', '.join(allowed_labels)}."
                })

    def save(self, *args, **kwargs):
        self.clean()  # Викликаємо валідацію перед кожним збереженням
        super().save(*args, **kwargs)

    def __str__(self):
        if self.amount is not None:
            # Видаляємо зайві нулі після коми для красивого відображення (напр. 200.00 -> 200)
            clean_amount = self.amount.normalize()
            return f"{clean_amount} {self.get_unit_display()} - {self.ingredient.name}"
        return f"{self.get_unit_display()} - {self.ingredient.name}"

# Сигнали, які викликають перерахунок сезонності
@receiver([post_save, post_delete], sender=RecipeIngredient)
def trigger_seasonality_update(sender, instance, **kwargs):
    if instance.recipe:
        instance.recipe.update_seasonality()


class RecipeStep(models.Model):
    """
    Модель для покрокової інструкції приготування.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps', verbose_name="Рецепт")
    step_number = models.PositiveIntegerField(verbose_name="Номер кроку")
    text = models.TextField(verbose_name="Опис кроку")

    text_en = models.TextField(blank=True, null=True, verbose_name="Опис кроку (EN)")
    text_pl = models.TextField(blank=True, null=True, verbose_name="Опис кроку (PL)")

    class Meta:
        verbose_name = "Крок приготування"
        verbose_name_plural = "Покрокове приготування"
        ordering = ['step_number']  # Завжди сортувати за номером кроку
        unique_together = ('recipe', 'step_number')  # Запобігає дублюванню кроків (напр. двох "Крок 1")

    def __str__(self):
        return f"Крок {self.step_number} для {self.recipe.title}"

class RecipeOfDay(models.Model):
    # Унікальна дата (за замовчуванням - сьогодні)
    date = models.DateField(unique=True, default=date.today, verbose_name="Дата")
    # Зв'язок з вашим основним рецептом
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, verbose_name="Рецепт")

    class Meta:
        verbose_name = "Recipe of the Day (Рецепт дня)"
        verbose_name_plural = "Recipes of the Day (Рецепти дня)"

    def __str__(self):
        return f"Рецепт дня на {self.date}: {self.recipe.title}"