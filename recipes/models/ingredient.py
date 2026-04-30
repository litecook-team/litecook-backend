from django.db import models
from django.contrib.postgres.fields import ArrayField


class IngredientCategory(models.TextChoices):
    CHEESE = 'cheese', 'Сири'
    MUSHROOMS = 'mushrooms', 'Гриби'
    FRUITS = 'fruits', 'Фрукти, ягоди та цитрусові'
    VEGETABLES = 'vegetables', 'Овочі та коренеплоди'
    GREENS = 'greens', 'Зелень та трави'
    MEAT_BEEF = 'meat_beef', "М'ясо та птиця / Яловичина і телятина"
    MEAT_PORK = 'meat_pork', "М'ясо та птиця / Свинина"
    MEAT_BIRD = 'meat_bird', "М'ясо та птиця / Птиця"
    MEAT_OTHER = 'meat_other', "М'ясо та птиця / Інше м'ясо"
    MEAT_PRODUCTS = 'meat_products', "М'ясо та птиця / М'ясні вироби"
    FISH_RED = 'fish_red', "Риба та морепродукти / Червона риба"
    FISH_WHITE = 'fish_white', "Риба та морепродукти / Біла риба"
    SEAFOOD = 'seafood', "Риба та морепродукти / Морепродукти"
    ALT_PROTEIN = 'alt_protein', 'Альтернативні білки'
    FLOUR = 'flour', 'Борошно'
    GRAINS = 'grains', 'Крупи та бобові'
    NUTS = 'nuts', 'Горіхи та насіння'
    DAIRY = 'dairy', 'Молочні продукти та яйця'
    SWEETS = 'sweets', 'Кондитерські інгредієнти'
    SPICES = 'spices', 'Спеції та приправи'
    OILS_LIQUIDS = 'oils_liquids', 'Спеції та приправи / Олії та рідини'


class Month(models.IntegerChoices):
    JANUARY = 1, 'Січень'
    FEBRUARY = 2, 'Лютий'
    MARCH = 3, 'Березень'
    APRIL = 4, 'Квітень'
    MAY = 5, 'Травень'
    JUNE = 6, 'Червень'
    JULY = 7, 'Липень'
    AUGUST = 8, 'Серпень'
    SEPTEMBER = 9, 'Вересень'
    OCTOBER = 10, 'Жовтень'
    NOVEMBER = 11, 'Листопад'
    DECEMBER = 12, 'Грудень'

# ================= ЖОРСТКІ ПРАВИЛА ОДИНИЦЬ ВИМІРУ =================

# 1. Загальні правила для категорій (використовуємо рядки для уникнення циклічних імпортів)
CATEGORY_UNIT_MAP = {
    IngredientCategory.FRUITS: ['g', 'kg'],
    IngredientCategory.VEGETABLES: ['g', 'kg'],
    IngredientCategory.DAIRY: ['g', 'kg', 'ml', 'l'],
    IngredientCategory.OILS_LIQUIDS: ['ml', 'l', 'tbsp', 'tsp'],
    IngredientCategory.SPICES: ['taste', 'pinch', 'tsp', 'g'],
    IngredientCategory.MEAT_BEEF: ['g', 'kg'],
    IngredientCategory.MEAT_PORK: ['g', 'kg'],
    IngredientCategory.MEAT_BIRD: ['g', 'kg'],
    IngredientCategory.MEAT_PRODUCTS: ['g', 'kg', 'slice'],
    IngredientCategory.GRAINS: ['g', 'kg', 'tbsp', 'glass'],
    IngredientCategory.CHEESE: ['g', 'kg', 'slice'],
    IngredientCategory.SEAFOOD: ['g', 'kg'],
    IngredientCategory.FISH_RED: ['g', 'kg'],
    IngredientCategory.FISH_WHITE: ['g', 'kg'],
    IngredientCategory.SWEETS: ['g', 'tsp', 'tbsp'],
    IngredientCategory.GREENS: ['bunch', 'g', 'sprig', 'taste'],
    IngredientCategory.MUSHROOMS: ['g', 'kg'],
    IngredientCategory.NUTS: ['g', 'kg', 'tsp', 'tbsp'],
    IngredientCategory.FLOUR: ['g', 'kg', 'tbsp', 'glass'],
    IngredientCategory.ALT_PROTEIN: ['g', 'kg'],
}

# 2. Винятки: конкретні інгредієнти, які мають специфічні одиниці
EXACT_UNIT_MATCH = {
    'Яйця': ['pcs'],
    'Перепелині яйця': ['pcs'],
    'Лимон': ['pcs', 'slice', 'g'],
    'Лайм': ['pcs', 'slice', 'g'],
    'Авокадо': ['pcs', 'g'],
    'Банан': ['pcs', 'g'],
    'Часник': ['clove', 'g'],
    'Вода': ['ml', 'l'],
    'Бульйон': ['ml', 'l'],
    'Овочевий бульйон': ['ml', 'l'],
    'Сіль': ['taste', 'pinch', 'tsp', 'g'],
    'Перець чорний': ['taste', 'pinch', 'tsp', 'g'],
    'Хліб': ['slice', 'g'],
    'Кокосове молоко': ['ml', 'l', 'can'],
    'Томатна паста': ['g', 'tbsp', 'can'],
    'Пападам': ['pcs'],
    'Вершкове масло': ['g', 'kg'],
    'Шоколад': ['g', 'pcs'],
    'Темний шоколад': ['g', 'pcs'],
    'Розпушувач': ['g', 'tsp'],
    'Желатин': ['g', 'tsp'],
}

class Ingredient(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва інгредієнта")
    name_en = models.CharField(max_length=150, blank=True, null=True, verbose_name="Назва (EN)")
    name_pl = models.CharField(max_length=150, blank=True, null=True, verbose_name="Назва (PL)")
    # =================================

    image = models.ImageField(upload_to='ingredients/images/', blank=True, null=True, verbose_name="Фото інгредієнта")
    category = models.CharField(
        max_length=50,
        choices=IngredientCategory.choices,
        verbose_name="Категорія"
    )

    is_seasonal = models.BooleanField(default=False, verbose_name="Сезонний інгредієнт")

    # Вибір декількох місяців
    seasonal_months = ArrayField(
        models.IntegerField(choices=Month.choices),
        blank=True, null=True,
        verbose_name="Місяці сезонності"
    )

    class Meta:
        verbose_name = "Ingredient (Інгредієнт)"
        verbose_name_plural = "Ingredients (Інгредієнти)"
        ordering = ['name']

    def __str__(self):
        return self.name

    # Метод для отримання дозволених одиниць
    def get_allowed_units(self):
        """Повертає список дозволених одиниць виміру для цього конкретного інгредієнта"""
        if self.name in EXACT_UNIT_MATCH:
            return EXACT_UNIT_MATCH[self.name]
        return CATEGORY_UNIT_MAP.get(self.category, ['g'])