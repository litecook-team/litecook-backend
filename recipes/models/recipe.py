from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва рецепта")

    description = models.TextField(verbose_name="Опис")

    cooking_time = models.PositiveIntegerField(verbose_name="Час приготування (хв)")
    calories = models.PositiveIntegerField(blank=True, null=True, verbose_name="Калорії")

    instructions = models.TextField(verbose_name="Покрокове приготування")

    image = models.ImageField(upload_to='recipes/images/', blank=True, null=True, verbose_name="Фото рецепта")

    # Категорії (Веган, Десерти, Ланчі)
    dietary_tags = models.CharField(max_length=255, blank=True, null=True, verbose_name="Дієтичні теги")

    # Зв'язок багато-до-багатьох з інгредієнтами
    ingredients = models.ManyToManyField('recipes.Ingredient', through='RecipeIngredient', related_name='recipes')

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепти"

    def __str__(self):
        return self.title

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey('recipes.Ingredient', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Кількість", help_text="Наприклад: 200, 1.5")
    unit = models.CharField(max_length=50, verbose_name="Одиниця виміру", help_text="Наприклад: грам, шт, мл, ст. л.")

    class Meta:
        verbose_name = "Інгредієнт у рецепті"
        verbose_name_plural = "Інгредієнти у рецептах"

    def __str__(self):
        return f"{self.ingredient.name} - {self.quantity} {self.unit}"