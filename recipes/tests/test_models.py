from django.test import TestCase
from django.db import IntegrityError

# Імпортуємо всі наші моделі з додатку recipes
from recipes.models.ingredient import Ingredient, IngredientCategory, Month
from recipes.models.recipe import Recipe, RecipeIngredient, RecipeStep, Difficulty, MealTime, Cuisine
from recipes.models.favorite import FavoriteRecipe
from recipes.models.weekly_menu import WeeklyMenu

# Імпортуємо моделі юзера (щоб імітувати реального користувача)
from users.models import CustomUser, UserIngredient


class LitecookCompleteFlowTests(TestCase):
    """
    Глобальний тест усього проєкту "від А до Я",
    який перевіряє всю бізнес-логіку і базу даних.
    """

    def setUp(self):
        # 1. Створюємо тестового користувача (як після реєстрації)
        self.user = CustomUser.objects.create_user(
            email='test@litecook.com',
            password='strongpassword123',
            first_name='Іван'
        )

        # 2. Адміністратор додає інгредієнти в базу
        self.ing_potato = Ingredient.objects.create(name="Картопля", category=IngredientCategory.VEGETABLES)
        self.ing_chicken = Ingredient.objects.create(name="Куряче філе", category=IngredientCategory.MEAT_BIRD)
        self.ing_salt = Ingredient.objects.create(name="Сіль", category=IngredientCategory.SWEETS)  # бакалія

        # 3. Адміністратор створює новий рецепт
        self.recipe = Recipe.objects.create(
            title="Запечена картопля з куркою",
            description="Дуже смачний і простий рецепт.",
            cooking_time=45,
            portions=2,
            calories=350,
            difficulty=Difficulty.EASY,
            cuisine=[Cuisine.UKRAINIAN],
            meal_times=[MealTime.LUNCH, MealTime.DINNER]
        )

    def test_01_recipe_creation_and_defaults(self):
        """Тестуємо, чи правильно створюється рецепт і чи працюють дефолтні масиви"""
        # Перевіряємо базові поля
        self.assertEqual(self.recipe.title, "Запечена картопля з куркою")
        self.assertEqual(self.recipe.portions, 2)

        # Перевіряємо, що масиви, які ми не вказали, стали пустими списками [], а не None!
        self.assertEqual(self.recipe.dietary_tags, [])
        self.assertEqual(self.recipe.dish_types, [])
        self.assertEqual(self.recipe.seasonal_months, [])
        self.assertFalse(self.recipe.is_seasonal)

    def test_02_recipe_ingredients_and_steps(self):
        """Тестуємо додавання інгредієнтів та кроків приготування до рецепта"""
        # Додаємо інгредієнти до рецепта
        RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.ing_potato, amount=500, unit='g')
        RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.ing_chicken, amount=300, unit='g')

        # Перевіряємо, чи рецепт бачить свої інгредієнти
        self.assertEqual(self.recipe.ingredients.count(), 2)

        # Додаємо кроки приготування
        step1 = RecipeStep.objects.create(recipe=self.recipe, step_number=1, text="Наріжте картоплю.")
        step2 = RecipeStep.objects.create(recipe=self.recipe, step_number=2, text="Запечіть у духовці.")

        self.assertEqual(self.recipe.steps.count(), 2)
        self.assertEqual(self.recipe.steps.first().text, "Наріжте картоплю.")

        # ПЕРЕВІРКА НА ПОМИЛКУ: Спробуємо додати ще один "Крок 1" (має вибити помилку БД)
        with self.assertRaises(IntegrityError):
            RecipeStep.objects.create(recipe=self.recipe, step_number=1,
                                      text="Цей крок має зламатися, бо номер 1 вже є!")

    def test_03_user_favorites_logic(self):
        """Тестуємо логіку улюблених рецептів користувача"""
        # Користувач додає рецепт в улюблені
        fav = FavoriteRecipe.objects.create(user=self.user, recipe=self.recipe)
        self.assertEqual(FavoriteRecipe.objects.count(), 1)
        self.assertEqual(fav.recipe.title, "Запечена картопля з куркою")

        # ПЕРЕВІРКА НА ПОМИЛКУ: Користувач не може додати той самий рецепт вдруге
        with self.assertRaises(IntegrityError):
            FavoriteRecipe.objects.create(user=self.user, recipe=self.recipe)

    def test_04_weekly_menu_logic(self):
        """Тестуємо розумне Тижневе меню користувача"""
        # Користувач планує рецепт на Понеділок (1), Сніданок
        WeeklyMenu.objects.create(user=self.user, recipe=self.recipe, day_of_week=1, meal_type='breakfast')

        # Користувач планує той самий рецепт на Понеділок (1), Обід (це дозволено)
        WeeklyMenu.objects.create(user=self.user, recipe=self.recipe, day_of_week=1, meal_type='lunch')

        self.assertEqual(WeeklyMenu.objects.filter(user=self.user).count(), 2)

        # ПЕРЕВІРКА НА ПОМИЛКУ: Користувач намагається додати ЩЕ ОДИН сніданок на Понеділок (має бути помилка)
        recipe2 = Recipe.objects.create(title="Інший рецепт", cooking_time=10, calories=100, difficulty=Difficulty.EASY)
        with self.assertRaises(IntegrityError):
            WeeklyMenu.objects.create(user=self.user, recipe=recipe2, day_of_week=1, meal_type='breakfast')

    def test_05_user_inventory_fridge(self):
        """Тестуємо віртуальний холодильник (інвентар) користувача"""
        # Користувач додає в холодильник 1 кг картоплі
        UserIngredient.objects.create(user=self.user, ingredient=self.ing_potato, amount=1, unit='kg')

        self.assertEqual(self.user.inventory.count(), 1)

        # Перевіряємо, чи працює строкове представлення (__str__)
        fridge_item = UserIngredient.objects.first()
        self.assertIn("Картопля", str(fridge_item))
        self.assertIn("1", str(fridge_item))

        # ПЕРЕВІРКА НА ПОМИЛКУ: Не можна створити два окремих записи "Картопля" для одного юзера
        # (юзер має оновлювати існуючий запис, а не створювати дублікат)
        with self.assertRaises(IntegrityError):
            UserIngredient.objects.create(user=self.user, ingredient=self.ing_potato, amount=2, unit='kg')