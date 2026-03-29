from django.contrib import admin
from django import forms
# from django.contrib.admin.widgets import FilteredSelectMultiple

from .models.ingredient import Ingredient
from .models.recipe import Recipe, RecipeIngredient, RecipeStep, Cuisine, MealTime, Diet, DishType
from .models.favorite import FavoriteRecipe
from .models.weekly_menu import WeeklyMenu

# ================= СТВОРЮЄМО ЗРУЧНУ ФОРМУ ДЛЯ АДМІНКИ =================
class RecipeAdminForm(forms.ModelForm):
    # Використовуємо рідний віджет чекбоксів
    cuisine = forms.MultipleChoiceField(
        choices=Cuisine.choices,
        required=False,
        widget=forms.CheckboxSelectMultiple(),  # <--- ВБУДОВАНИЙ ВІДЖЕТ
        label="Кухня"
    )
    meal_times = forms.MultipleChoiceField(
        choices=MealTime.choices,
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        label="Прийом їжі"
    )
    dietary_tags = forms.MultipleChoiceField(
        choices=Diet.choices,
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        label="Тип харчування / Дієта"
    )
    dish_types = forms.MultipleChoiceField(
        choices=DishType.choices,
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        label="Типи страв"
    )

    class Meta:
        model = Recipe
        fields = '__all__'


# ================= НАЛАШТУВАННЯ АДМІН-ПАНЕЛІ =================
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeStepInline(admin.TabularInline):
    model = RecipeStep
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    form = RecipeAdminForm
    inlines = [RecipeIngredientInline, RecipeStepInline]

    list_display = ('title', 'cooking_time', 'calories', 'difficulty', 'is_seasonal')
    list_filter = ('difficulty', 'is_seasonal')
    readonly_fields = ('is_seasonal', 'seasonal_months')


admin.site.register(Ingredient)
admin.site.register(FavoriteRecipe)
admin.site.register(WeeklyMenu)