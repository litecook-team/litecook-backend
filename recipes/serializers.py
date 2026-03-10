from rest_framework import serializers
from .models.ingredient import Ingredient
from .models.recipe import Recipe
from .models.favorite import FavoriteRecipe
from .models.weekly_menu import WeeklyMenu

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__' # Беремо всі колонки з таблиці

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRecipe
        fields = '__all__'
        read_only_fields = ('user',) # Юзер буде підставлятися автоматично, його не треба передавати в JSON

class WeeklyMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyMenu
        fields = '__all__'
        read_only_fields = ('user',)