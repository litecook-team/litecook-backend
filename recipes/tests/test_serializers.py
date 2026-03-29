from django.test import TestCase
from django.test.client import RequestFactory
from django.db.models import Count

from users.models import CustomUser
from recipes.models.recipe import Recipe, Difficulty
from recipes.models.favorite import FavoriteRecipe
from recipes.serializers import RecipeSerializer


class RecipeSerializerTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@litecook.com', password='password123', first_name='Іван')
        self.recipe = Recipe.objects.create(
            title="Простий рецепт", cooking_time=10, calories=100, difficulty=Difficulty.EASY
        )
        self.factory = RequestFactory()

    def test_recipe_serializer_contains_expected_fields(self):
        """Тестуємо, чи серіалізатор віддає всі потрібні поля, включаючи нові дати та анотації"""

        annotated_recipe = Recipe.objects.annotate(likes_count=Count('favorited_by')).get(id=self.recipe.id)

        serializer = RecipeSerializer(instance=annotated_recipe)
        data = serializer.data

        self.assertEqual(data['title'], "Простий рецепт")
        self.assertIn('created_at', data)
        self.assertIn('updated_at', data)
        self.assertIn('is_favorited', data)
        self.assertEqual(data['likes_count'], 0)

    def test_is_favorited_dynamic_field(self):
        """Тестуємо, чи правильно працює динамічне поле 'is_favorited' залежно від юзера"""
        request = self.factory.get('/api/recipes/')
        request.user = self.user

        # Тут анотація не потрібна, бо is_favorited вираховується функцією get_is_favorited
        serializer = RecipeSerializer(instance=self.recipe, context={'request': request})
        self.assertFalse(serializer.data['is_favorited'])

        FavoriteRecipe.objects.create(user=self.user, recipe=self.recipe)

        serializer_liked = RecipeSerializer(instance=self.recipe, context={'request': request})
        self.assertTrue(serializer_liked.data['is_favorited'])