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
    # ДОДАНО:
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


class Ingredient(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва інгредієнта")
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
        verbose_name = "Інгредієнт"
        verbose_name_plural = "Інгредієнти"
        ordering = ['name']

    def __str__(self):
        return self.name