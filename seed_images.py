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

        # Генеруємо можливі варіанти назв файлів
        search_names = [ingredient.name]

        # 1. Заміна апострофа на підкреслення (М'ята -> М_ята, Кеш'ю -> Кеш_ю)
        if "'" in ingredient.name or "’" in ingredient.name:
            search_names.append(ingredient.name.replace("'", "_").replace("’", "_"))

        image_found = False

        # Шукаємо файл за всіма можливими назвами та розширеннями
        for search_name in search_names:
            if image_found:
                break

            for ext in extensions:
                file_name_local = f"{search_name}{ext}"
                file_path = os.path.join(images_dir, file_name_local)

                if os.path.exists(file_path):
                    # БЕЗПЕЧНА НАЗВА ДЛЯ БАЗИ
                    safe_name = slugify(unidecode(ingredient.name))
                    file_name_db = f"{safe_name}{ext}"

                    media_path = f'ingredients/images/{file_name_db}'
                    if default_storage.exists(media_path):
                        default_storage.delete(media_path)

                    with open(file_path, 'rb') as f:
                        # Зберігаємо під новою англійською назвою
                        ingredient.image.save(file_name_db, File(f), save=True)

                    print(f"✅ Додано фото: {file_name_local} -> {file_name_db}")
                    updated_count += 1
                    image_found = True
                    break  # Зупиняємо пошук інших форматів для цього файлу

    print(f"\n🎉 Готово! Успішно додано зображень: {updated_count}")


if __name__ == '__main__':
    run()