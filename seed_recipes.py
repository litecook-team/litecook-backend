import os
import django
from django.core.files import File
from django.core.files.storage import default_storage
from django.utils.text import slugify
from unidecode import unidecode

# 1. СПОЧАТКУ НАЛАШТОВУЄМО СЕРЕДОВИЩЕ DJANGO
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# 2. І ТІЛЬКИ ПІСЛЯ ЦЬОГО ІМПОРТУЄМО ДАНІ ТА МОДЕЛІ
from seed_data.recipes_part1 import RECIPES_DATA_1
from seed_data.recipes_part2 import RECIPES_DATA_2
from seed_data.recipes_part3 import RECIPES_DATA_3
from seed_data.recipes_part4 import RECIPES_DATA_4
from seed_data.recipes_part5 import RECIPES_DATA_5
from seed_data.recipes_part6 import RECIPES_DATA_6
from seed_data.recipes_part7 import RECIPES_DATA_7
from seed_data.recipes_part8 import RECIPES_DATA_8

from recipes.models.recipe import Recipe, RecipeIngredient, RecipeStep
from recipes.models.ingredient import Ingredient

ALL_RECIPES = (
    RECIPES_DATA_1 + RECIPES_DATA_2 + RECIPES_DATA_3 + RECIPES_DATA_4 +
    RECIPES_DATA_5 + RECIPES_DATA_6 + RECIPES_DATA_7 + RECIPES_DATA_8
)

def run():
    print("🧹 Очищення старих рецептів...")
    Recipe.objects.all().delete()
    print("✅ Базу рецептів очищено. Починаємо завантаження нових...\n")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(base_dir, 'seed_recipe_images')
    extensions = ['.jpg', '.jpeg', '.png', '.webp']

    added_count = 0

    for data in ALL_RECIPES:
        print(f"🔄 Створюємо: {data['title']}...")

        recipe = Recipe.objects.create(
            title=data["title"],
            title_en=data.get("title_en"),
            title_pl=data.get("title_pl"),
            description=data["description"],
            description_en=data.get("description_en"),
            description_pl=data.get("description_pl"),
            source=data.get("source", ""),
            source_en=data.get("source_en", ""),
            source_pl=data.get("source_pl", ""),
            cooking_time=data["cooking_time"],
            portions=data["portions"],
            calories=data["calories"],
            difficulty=data["difficulty"],
            cuisine=data["cuisine"],
            meal_times=data["meal_times"],
            dietary_tags=data["dietary_tags"],
            dish_types=data["dish_types"]
        )

        if os.path.exists(images_dir):
            for ext in extensions:
                file_name_local = f"{recipe.title}{ext}"
                file_path = os.path.join(images_dir, file_name_local)

                if os.path.exists(file_path):
                    safe_name = slugify(unidecode(recipe.title))
                    file_name_db = f"{safe_name}{ext}"

                    media_path = f'recipes/images/{file_name_db}'
                    if default_storage.exists(media_path):
                        default_storage.delete(media_path)

                    with open(file_path, 'rb') as f:
                        recipe.image.save(file_name_db, File(f), save=True)
                    break

        for ing_name, amount, unit in data["ingredients"]:
            try:
                ingredient_obj = Ingredient.objects.get(name__iexact=ing_name)
                RecipeIngredient.objects.create(
                    recipe=recipe,
                    ingredient=ingredient_obj,
                    amount=amount,
                    unit=unit
                )
            except Ingredient.DoesNotExist:
                print(f"   ❌ Помилка: Інгредієнт '{ing_name}' не знайдено в базі! Пропущено.")

        for index, step_data in enumerate(data["steps"], start=1):
            RecipeStep.objects.create(
                recipe=recipe,
                step_number=index,
                text=step_data["uk"],
                text_en=step_data.get("en"),
                text_pl=step_data.get("pl")
            )

        recipe.update_seasonality()
        print(f"✅ Успішно додано: {data['title']}\n")
        added_count += 1

    print(f"🎉 Готово! Додано нових рецептів: {added_count}")

if __name__ == '__main__':
    run()