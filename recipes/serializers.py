from rest_framework import serializers
from .models.ingredient import Ingredient
from .models.recipe import Recipe, RecipeIngredient, RecipeStep
from .models.favorite import FavoriteRecipe
from .models.weekly_menu import WeeklyMenu

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='ingredient.name')
    ingredient_image = serializers.ImageField(source='ingredient.image', read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'ingredient', 'ingredient_name', 'ingredient_image', 'amount', 'unit')

class RecipeStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ('step_number', 'text')


class RecipeSerializer(serializers.ModelSerializer):
    recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True)
    steps = RecipeStepSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    is_favorited = serializers.SerializerMethodField()
    is_added_to_menu = serializers.SerializerMethodField()

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    # Поля для відображення збігів (read_only=True, required=False)
    match_count = serializers.IntegerField(read_only=True, required=False)
    total_count = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = Recipe
        fields = '__all__'

    def get_is_favorited(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return FavoriteRecipe.objects.filter(user=request.user, recipe=obj).exists()
        return False

    def get_is_added_to_menu(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return WeeklyMenu.objects.filter(user=request.user, recipe=obj).exists()
        return False

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRecipe
        fields = '__all__'
        read_only_fields = ('user',) # Юзер буде підставлятися автоматично, його не треба передавати в JSON

    def to_representation(self, instance):
        # Отримуємо стандартну відповідь (з ID рецепту)
        representation = super().to_representation(instance)
        # Підміняємо ID на повні дані рецепту тільки при віддачі на фронтенд
        representation['recipe'] = RecipeSerializer(instance.recipe, context=self.context).data
        return representation

class WeeklyMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyMenu
        fields = '__all__'
        read_only_fields = ('user',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['recipe'] = RecipeSerializer(instance.recipe, context=self.context).data
        return representation

class RecipeMatchSerializer(serializers.ModelSerializer):
    match_count = serializers.IntegerField(read_only=True)
    total_count = serializers.IntegerField(read_only=True)
    image_url = serializers.ImageField(source='image', read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'image_url', 'cooking_time', 'difficulty',
            'calories', 'match_count', 'total_count'
        ]