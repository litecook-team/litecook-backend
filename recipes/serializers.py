from rest_framework import serializers
from .models.ingredient import Ingredient
from .models.recipe import Recipe, RecipeIngredient, RecipeStep
from .models.favorite import FavoriteRecipe
from .models.weekly_menu import WeeklyMenu

# Допоміжна функція для визначення мови
def get_lang(serializer_instance):
    request = serializer_instance.context.get('request')
    return getattr(request, 'LANGUAGE_CODE', 'uk')[:2] if request else 'uk'

class IngredientSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Ingredient
        fields = '__all__'

    def get_name(self, obj):
        lang = get_lang(self)
        if lang == 'en' and obj.name_en: return obj.name_en
        if lang == 'pl' and obj.name_pl: return obj.name_pl
        return obj.name

class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.SerializerMethodField()
    ingredient_image = serializers.ImageField(source='ingredient.image', read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'ingredient', 'ingredient_name', 'ingredient_image', 'amount', 'unit')

    def get_ingredient_name(self, obj):
        lang = get_lang(self)
        if lang == 'en' and obj.ingredient.name_en: return obj.ingredient.name_en
        if lang == 'pl' and obj.ingredient.name_pl: return obj.ingredient.name_pl
        return obj.ingredient.name

class RecipeStepSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    class Meta:
        model = RecipeStep
        fields = ('step_number', 'text')

    def get_text(self, obj):
        lang = get_lang(self)
        if lang == 'en' and obj.text_en: return obj.text_en
        if lang == 'pl' and obj.text_pl: return obj.text_pl
        return obj.text

class RecipeSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    source = serializers.SerializerMethodField()
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

    def get_title(self, obj):
        lang = get_lang(self)
        if lang == 'en' and obj.title_en: return obj.title_en
        if lang == 'pl' and obj.title_pl: return obj.title_pl
        return obj.title

    def get_description(self, obj):
        lang = get_lang(self)
        if lang == 'en' and obj.description_en: return obj.description_en
        if lang == 'pl' and obj.description_pl: return obj.description_pl
        return obj.description

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

    def get_source(self, obj):
        lang = get_lang(self)
        if lang == 'en' and obj.source_en: return obj.source_en
        if lang == 'pl' and obj.source_pl: return obj.source_pl
        return obj.source

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
    title = serializers.SerializerMethodField()
    match_count = serializers.IntegerField(read_only=True)
    total_count = serializers.IntegerField(read_only=True)
    image_url = serializers.ImageField(source='image', read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'image_url', 'cooking_time', 'difficulty',
            'calories', 'match_count', 'total_count'
        ]

    def get_title(self, obj):
        lang = get_lang(self)
        if lang == 'en' and obj.title_en: return obj.title_en
        if lang == 'pl' and obj.title_pl: return obj.title_pl
        return obj.title