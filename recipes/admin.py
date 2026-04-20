from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from .models.recipe import RecipeIngredient
# from django.contrib.admin.widgets import FilteredSelectMultiple

from .models.ingredient import Ingredient
from .models.recipe import Recipe, RecipeIngredient, RecipeStep, Cuisine, MealTime, Diet, DishType, RecipeOfDay
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
class RecipeIngredientAdminForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Якщо ми редагуємо вже існуючий запис і інгредієнт вибрано
        if self.instance and self.instance.pk and self.instance.ingredient_id:
            # Отримуємо дозволені одиниці для цього інгредієнта
            allowed_units = self.instance.ingredient.get_allowed_units()

            # Фільтруємо стандартні Choices, залишаючи тільки дозволені
            filtered_choices = [
                (code, label) for code, label in self.fields['unit'].choices
                if code in allowed_units
            ]
            # Оновлюємо випадаючий список
            self.fields['unit'].choices = filtered_choices

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    form = RecipeIngredientAdminForm  # <--- підключення форми
    extra = 1
    # додаємо autocomplete_fields, щоб зручніше шукати серед сотень інгредієнтів
    autocomplete_fields = ['ingredient']

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
    # Шукатимемо за назвою рецепту
    search_fields = ('title',)

@admin.register(RecipeOfDay)
class RecipeOfDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'recipe') # Що показувати в колонках
    list_filter = ('date',)           # Фільтр по даті збоку
    ordering = ('-date',)             # Найновіші дати зверху


# ПОШУК ДЛЯ ІНГРЕДІЄНТІВ
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'is_seasonal')
    list_filter = ('is_seasonal',)

admin.site.register(FavoriteRecipe)
admin.site.register(WeeklyMenu)