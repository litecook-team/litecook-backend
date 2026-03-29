from rest_framework.test import APITestCase
from rest_framework import status
from users.models import CustomUser, UserIngredient
from recipes.models.ingredient import Ingredient, IngredientCategory
from recipes.models.recipe import Recipe, RecipeIngredient, Difficulty, Cuisine
from recipes.models.weekly_menu import WeeklyMenu


class RecipeApiTests(APITestCase):
    def setUp(self):
        # Створюємо юзера
        self.user = CustomUser.objects.create_user(email='test@litecook.com', password='password123', first_name='Іван')

        # Створюємо інгредієнти
        self.potato = Ingredient.objects.create(name="Картопля", category=IngredientCategory.VEGETABLES)
        self.chicken = Ingredient.objects.create(name="Курка", category=IngredientCategory.MEAT_BIRD)
        self.tomato = Ingredient.objects.create(name="Помідор", category=IngredientCategory.VEGETABLES)

        # Створюємо Рецепт 1 (Тільки Картопля + Курка) - Українська кухня
        self.recipe1 = Recipe.objects.create(
            title="Запечена картопля з куркою", cooking_time=45, calories=350,
            difficulty=Difficulty.EASY, cuisine=[Cuisine.UKRAINIAN]
        )
        RecipeIngredient.objects.create(recipe=self.recipe1, ingredient=self.potato, amount=500, unit='g')
        RecipeIngredient.objects.create(recipe=self.recipe1, ingredient=self.chicken, amount=300, unit='g')

        # Створюємо Рецепт 2 (Курка + Помідор) - Італійська кухня
        self.recipe2 = Recipe.objects.create(
            title="Курка по-італійськи", cooking_time=30, calories=250,
            difficulty=Difficulty.MEDIUM, cuisine=[Cuisine.ITALIAN]
        )
        RecipeIngredient.objects.create(recipe=self.recipe2, ingredient=self.chicken, amount=400, unit='g')
        RecipeIngredient.objects.create(recipe=self.recipe2, ingredient=self.tomato, amount=200, unit='g')

    def test_get_recipes_list(self):
        """Тест: Користувач може отримати список усіх рецептів (GET /api/recipes/)"""
        response = self.client.get('/api/recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Безпечно дістаємо дані: якщо це словник - беремо 'results', якщо ні - беремо сам список
        data = response.data.get('results', response.data) if isinstance(response.data, dict) else response.data
        self.assertEqual(len(data), 2)

    def test_filter_recipes_by_cuisine(self):
        """Тест: Фільтр масивів. Чи знайдемо ми італійські страви?"""
        response = self.client.get('/api/recipes/?cuisine=it')
        data = response.data.get('results', response.data) if isinstance(response.data, dict) else response.data
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], "Курка по-італійськи")

    def test_filter_recipes_by_multiple_ingredients(self):
        """Тест: Пошук за наявними інгредієнтами (AND логіка)"""
        response = self.client.get(f'/api/recipes/?ingredients={self.potato.id},{self.chicken.id}')
        data = response.data.get('results', response.data) if isinstance(response.data, dict) else response.data
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], "Запечена картопля з куркою")

    def test_protected_endpoints(self):
        """Тест: Гості не можуть додавати в улюблені (401 Unauthorized)"""
        response = self.client.post('/api/favorites/', {'recipe': self.recipe1.id})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Авторизуємо юзера і пробуємо ще раз
        self.client.force_authenticate(user=self.user)
        response_auth = self.client.post('/api/favorites/', {'recipe': self.recipe1.id})
        self.assertEqual(response_auth.status_code, status.HTTP_201_CREATED)

    def test_smart_shopping_list_math(self):
        """Тест: Розумний список покупок перевіряє Холодильник і рахує різницю"""
        self.client.force_authenticate(user=self.user)

        # Додаємо Рецепт 1 (треба 500г картоплі, 300г курки) у меню
        WeeklyMenu.objects.create(user=self.user, recipe=self.recipe1, day_of_week=1, meal_type='lunch')

        # Юзер каже, що в нього вдома (у холодильнику) ВЖЕ Є 200г картоплі
        UserIngredient.objects.create(user=self.user, ingredient=self.potato, amount=200, unit='g')

        # Запитуємо список покупок
        response = self.client.get('/api/weekly-menu/shopping_list/')
        data = response.data

        self.assertEqual(len(data), 2)  # У списку має бути 2 продукти (картопля, курка)

        # Перевіряємо математику для картоплі: Треба 500, Є 200 -> Купити 300. Не повністю забезпечено (False)
        potato_item = next(item for item in data if item['ingredient_name'] == 'Картопля')
        self.assertEqual(potato_item['required_amount'], 500)
        self.assertEqual(potato_item['already_have'], 200)
        self.assertEqual(potato_item['to_buy'], 300)
        self.assertFalse(potato_item['is_fully_stocked'])

        # Перевіряємо математику для курки: Треба 300, Є 0 -> Купити 300
        chicken_item = next(item for item in data if item['ingredient_name'] == 'Курка')
        self.assertEqual(chicken_item['to_buy'], 300)