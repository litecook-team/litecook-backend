from django.contrib import admin
from .models.ingredient import Ingredient
from .models.recipe import Recipe, RecipeIngredient
from .models.favorite import FavoriteRecipe
from .models.weekly_menu import WeeklyMenu

# Цей клас дозволяє додавати інгредієнти прямо під час створення рецепта на одній сторінці
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ('title', 'cooking_time', 'calories') # Колонки, які буде видно в списку

admin.site.register(Ingredient)
admin.site.register(FavoriteRecipe)
admin.site.register(WeeklyMenu)