import os
import django
from django.core.files import File
from django.core.files.storage import default_storage
from django.utils.text import slugify
from unidecode import unidecode

# Налаштування середовища Django для запуску скрипта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from recipes.models.ingredient import Ingredient

def run():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(base_dir, 'seed_images')

    if not os.path.exists(images_dir):
        print(f"❌ Помилка: Не знайдено папку '{images_dir}'.")
        return

    print("🔍 Починаємо пошук та завантаження зображень...\n")
    ingredients = Ingredient.objects.all()
    updated_count = 0
    extensions = ['.jpg', '.jpeg', '.png', '.webp']

    for ingredient in ingredients:
        # Якщо в інгредієнта вже є фото, пропускаємо його
        if ingredient.image:
            continue

        # Шукаємо файл з назвою інгредієнта та одним із розширень
        for ext in extensions:
            # 1. Локальна назва
            file_name_local = f"{ingredient.name}{ext}"
            file_path = os.path.join(images_dir, file_name_local)

            if os.path.exists(file_path):
                # 2. БЕЗПЕЧНА НАЗВА ДЛЯ БАЗИ
                safe_name = slugify(unidecode(ingredient.name))
                file_name_db = f"{safe_name}{ext}"

                media_path = f'ingredients/images/{file_name_db}'
                if default_storage.exists(media_path):
                    default_storage.delete(media_path)

                with open(file_path, 'rb') as f:
                    # Зберігаємо під новою англійською назвою
                    ingredient.image.save(file_name_db, File(f), save=True)

                print(f"✅ Додано фото для: {ingredient.name} -> {file_name_db}")
                updated_count += 1
                break   # Зупиняємо пошук інших форматів для цього інгредієнта

    print(f"\n🎉 Готово! Успішно додано зображень: {updated_count}")

if __name__ == '__main__':
    run()