import os
import django

# Налаштування середовища Django для запуску скрипта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from recipes.models.ingredient import Ingredient, IngredientCategory

# Дані у форматі: ("Назва", "Категорія", Сезонний (True/False), [Місяці])
INGREDIENTS_DATA = [
    # ================= ФРУКТИ, ЯГОДИ ТА ЦИТРУСОВІ =================
    ("Інжир", IngredientCategory.FRUITS, True, [9, 10]),
    ("Абрикос", IngredientCategory.FRUITS, True, [7, 8]),
    ("Авокадо", IngredientCategory.FRUITS, False, []),
    ("Айва", IngredientCategory.FRUITS, True, [9, 10]),
    ("Ананас", IngredientCategory.FRUITS, False, []),
    ("Апельсин", IngredientCategory.FRUITS, False, []),
    ("Аґрус", IngredientCategory.FRUITS, True, [6, 7]),
    ("Банан", IngredientCategory.FRUITS, False, []),
    ("Виноград", IngredientCategory.FRUITS, True, [8, 9, 10]),
    ("Вишня", IngredientCategory.FRUITS, True, [6, 7]),
    ("Гранат", IngredientCategory.FRUITS, False, []),
    ("Грейпфрут", IngredientCategory.FRUITS, False, []),
    ("Груша", IngredientCategory.FRUITS, True, [8, 9, 10, 11]),
    ("Диня", IngredientCategory.FRUITS, True, [8, 9]),
    ("Журавлина", IngredientCategory.FRUITS, True, [9, 10]),
    ("Кавун", IngredientCategory.FRUITS, True, [8, 9]),
    ("Кокос", IngredientCategory.FRUITS, False, []),
    ("Ківі", IngredientCategory.FRUITS, False, []),
    ("Лайм", IngredientCategory.FRUITS, False, []),
    ("Лимон", IngredientCategory.FRUITS, False, []),
    ("Лохина", IngredientCategory.FRUITS, True, [7, 8]),
    ("Малина", IngredientCategory.FRUITS, True, [7, 8]),
    ("Манго", IngredientCategory.FRUITS, False, []),
    ("Мандарин", IngredientCategory.FRUITS, False, []),
    ("Нектарин", IngredientCategory.FRUITS, True, [7, 8]),
    ("Ожина", IngredientCategory.FRUITS, True, [7, 8]),
    ("Персик", IngredientCategory.FRUITS, True, [7, 8]),
    ("Полуниця", IngredientCategory.FRUITS, True, [5, 6]),
    ("Слива", IngredientCategory.FRUITS, True, [8, 9]),
    ("Хурма", IngredientCategory.FRUITS, True, [9, 10]),
    ("Червона смородина", IngredientCategory.FRUITS, True, [6, 7]),
    ("Черешня", IngredientCategory.FRUITS, True, [6, 7]),
    ("Чорна смородина", IngredientCategory.FRUITS, True, [6, 7]),
    ("Чорниця", IngredientCategory.FRUITS, True, [7, 8]),
    ("Яблуко", IngredientCategory.FRUITS, True, [8, 9, 10, 11]),

    # ================= СПЕЦІЇ ТА ПРИПРАВИ (І РІДИНИ) =================
    ("Бульйон", IngredientCategory.OILS_LIQUIDS, False, []),
    ("Вода", IngredientCategory.OILS_LIQUIDS, False, []),
    ("Лимонний сік", IngredientCategory.OILS_LIQUIDS, False, []),
    ("Овочевий бульйон", IngredientCategory.OILS_LIQUIDS, False, []),
    ("Оливкова олія", IngredientCategory.OILS_LIQUIDS, False, []),
    ("Рослинна олія", IngredientCategory.OILS_LIQUIDS, False, []),
    ("Томатна паста", IngredientCategory.OILS_LIQUIDS, False, []),
    ("Орегано", IngredientCategory.SPICES, False, []),
    ("Перець", IngredientCategory.SPICES, False, []),
    ("Сіль", IngredientCategory.SPICES, False, []),
    ("Чорний перець", IngredientCategory.SPICES, False, []),

    # ================= СИРИ =================
    ("Бринза", IngredientCategory.CHEESE, False, []),
    ("Брі", IngredientCategory.CHEESE, False, []),
    ("Гауда", IngredientCategory.CHEESE, False, []),
    ("Голландський сир", IngredientCategory.CHEESE, False, []),
    ("Горгонзола", IngredientCategory.CHEESE, False, []),
    ("Дорблю", IngredientCategory.CHEESE, False, []),
    ("Едам", IngredientCategory.CHEESE, False, []),
    ("Камамбер", IngredientCategory.CHEESE, False, []),
    ("Кисломолочний сир", IngredientCategory.CHEESE, False, []),
    ("Крем-сир", IngredientCategory.CHEESE, False, []),
    ("Маскарпоне", IngredientCategory.CHEESE, False, []),
    ("Моцарела", IngredientCategory.CHEESE, False, []),
    ("Пармезан", IngredientCategory.CHEESE, False, []),
    ("Рокфор", IngredientCategory.CHEESE, False, []),
    ("Сулугуні", IngredientCategory.CHEESE, False, []),
    ("Фета", IngredientCategory.CHEESE, False, []),
    ("Філадельфія", IngredientCategory.CHEESE, False, []),
    ("Чеддер", IngredientCategory.CHEESE, False, []),

    # ================= РИБА ТА МОРЕПРОДУКТИ =================
    ("Лосось", IngredientCategory.FISH_RED, False, []),
    ("Тунець", IngredientCategory.FISH_RED, False, []),
    ("Форель", IngredientCategory.FISH_RED, False, []),
    ("Філе лосося", IngredientCategory.FISH_RED, False, []),
    ("Восьминіг", IngredientCategory.SEAFOOD, False, []),
    ("Кальмар", IngredientCategory.SEAFOOD, False, []),
    ("Креветки", IngredientCategory.SEAFOOD, False, []),
    ("Мідії", IngredientCategory.SEAFOOD, False, []),
    ("Креветки очищені", IngredientCategory.SEAFOOD, False, []),
    ("Дорадо", IngredientCategory.FISH_WHITE, False, []),
    ("Минтай", IngredientCategory.FISH_WHITE, False, []),
    ("Судак", IngredientCategory.FISH_WHITE, False, []),
    ("Тріска", IngredientCategory.FISH_WHITE, False, []),
    ("Хек", IngredientCategory.FISH_WHITE, False, []),

    # ================= ОВОЧІ ТА КОРЕНЕПЛОДИ =================
    ("Артишок", IngredientCategory.VEGETABLES, True, [6, 7, 8]),
    ("Баклажан", IngredientCategory.VEGETABLES, True, [8, 9, 10]),
    ("Батат", IngredientCategory.VEGETABLES, True, [9, 10]),
    ("Броколі", IngredientCategory.VEGETABLES, True, [9, 10]),
    ("Бруква", IngredientCategory.VEGETABLES, False, []),
    ("Брюссельська капуста", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Буряк", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Гарбуз", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Горох", IngredientCategory.VEGETABLES, True, [6, 7]),
    ("Зелена квасоля", IngredientCategory.VEGETABLES, True, [7, 8, 9]),
    ("Кабачок", IngredientCategory.VEGETABLES, True, [6, 7, 8]),
    ("Капуста білокачанна", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Капуста кейл", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Капуста пекінська", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Капуста савойська", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Капуста цвітна", IngredientCategory.VEGETABLES, True, [8, 9, 10]),
    ("Капуста червонокачанна", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Картопля", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Кольрабі", IngredientCategory.VEGETABLES, True, [6, 7, 8, 9, 10]),
    ("Коренева селера", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Кукурудза", IngredientCategory.VEGETABLES, True, [7, 8]),
    ("Морква", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Огірок", IngredientCategory.VEGETABLES, True, [6, 7, 8, 9]),
    ("Окра", IngredientCategory.VEGETABLES, False, []),
    ("Пастернак", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Патисон", IngredientCategory.VEGETABLES, True, [6, 7, 8]),
    ("Перець болгарський", IngredientCategory.VEGETABLES, True, [7, 8, 9]),
    ("Перець гострий", IngredientCategory.VEGETABLES, True, [7, 8, 9]),
    ("Помідор", IngredientCategory.VEGETABLES, True, [7, 8, 9]),
    ("Порей", IngredientCategory.VEGETABLES, True, [8, 9, 10]),
    ("Редис", IngredientCategory.VEGETABLES, True, [4, 5]),
    ("Редька", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Ріпа", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Спаржа", IngredientCategory.VEGETABLES, True, [5, 6]),
    ("Стеблова селера", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Топінамбур", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Фенхель", IngredientCategory.VEGETABLES, True, [8, 9, 10]),
    ("Хрін", IngredientCategory.VEGETABLES, True, [9, 10, 11]),
    ("Цибуля зелена", IngredientCategory.VEGETABLES, True, [5, 6]),
    ("Цибуля ріпчаста", IngredientCategory.VEGETABLES, True, [7, 8, 9]),
    ("Цибуля червона", IngredientCategory.VEGETABLES, True, [7, 8, 9]),
    ("Цибуля шалот", IngredientCategory.VEGETABLES, True, [7, 8, 9]),
    ("Цукіні", IngredientCategory.VEGETABLES, True, [6, 7, 8]),
    ("Часник", IngredientCategory.VEGETABLES, True, [7, 8, 9]),
    ("Болгарський перець", IngredientCategory.VEGETABLES, True, [7, 8, 9]),
    ("Помідори чері", IngredientCategory.VEGETABLES, True, [7, 8, 9]),

    # ================= МОЛОЧНІ ПРОДУКТИ ТА ЯЙЦЯ =================
    ("Вершки", IngredientCategory.DAIRY, False, []),
    ("Вершкове масло", IngredientCategory.DAIRY, False, []),
    ("Йогурт", IngredientCategory.DAIRY, False, []),
    ("Кефір", IngredientCategory.DAIRY, False, []),
    ("Молоко", IngredientCategory.DAIRY, False, []),
    ("Сметана", IngredientCategory.DAIRY, False, []),
    ("Яйця", IngredientCategory.DAIRY, False, []),
    ("Мигдальне молоко", IngredientCategory.DAIRY, False, []),

    # ================= М'ЯСО ТА ПТИЦЯ =================
    ("Брискет", IngredientCategory.MEAT_BEEF, False, []),
    ("Прайм-ріб", IngredientCategory.MEAT_BEEF, False, []),
    ("Рибай", IngredientCategory.MEAT_BEEF, False, []),
    ("Сирлоїн", IngredientCategory.MEAT_BEEF, False, []),
    ("Солонина", IngredientCategory.MEAT_BEEF, False, []),
    ("Стейк фланк", IngredientCategory.MEAT_BEEF, False, []),
    ("Стейк флет-айрон", IngredientCategory.MEAT_BEEF, False, []),
    ("Телятина", IngredientCategory.MEAT_BEEF, False, []),
    ("Філе-міньйон", IngredientCategory.MEAT_BEEF, False, []),
    ("Яловича вирізка", IngredientCategory.MEAT_BEEF, False, []),
    ("Яловича лопатка", IngredientCategory.MEAT_BEEF, False, []),
    ("Яловичий фарш", IngredientCategory.MEAT_BEEF, False, []),
    ("Яловичі ребра", IngredientCategory.MEAT_BEEF, False, []),

    ("Бекон", IngredientCategory.MEAT_PORK, False, []),
    ("Свиняча вирізка", IngredientCategory.MEAT_PORK, False, []),
    ("Свиняча лопатка", IngredientCategory.MEAT_PORK, False, []),
    ("Свинячий фарш", IngredientCategory.MEAT_PORK, False, []),
    ("Свинячі відбивні", IngredientCategory.MEAT_PORK, False, []),
    ("Свинячі ребра", IngredientCategory.MEAT_PORK, False, []),
    # ("Свинина", IngredientCategory.MEAT_PORK, False, []),

    ("Індиче філе", IngredientCategory.MEAT_BIRD, False, []),
    ("Качка", IngredientCategory.MEAT_BIRD, False, []),
    ("Курка ціла", IngredientCategory.MEAT_BIRD, False, []),
    ("Куряча грудка", IngredientCategory.MEAT_BIRD, False, []),
    ("Курячий фарш", IngredientCategory.MEAT_BIRD, False, []),
    ("Курячі крильця", IngredientCategory.MEAT_BIRD, False, []),
    ("Курячі ніжки", IngredientCategory.MEAT_BIRD, False, []),
    ("Курячі стегна", IngredientCategory.MEAT_BIRD, False, []),
    ("Фарш з індички", IngredientCategory.MEAT_BIRD, False, []),
    ("Куряче філе", IngredientCategory.MEAT_BIRD, False, []),

    ("Ковбаса", IngredientCategory.MEAT_PRODUCTS, False, []),
    ("Сосиски", IngredientCategory.MEAT_PRODUCTS, False, []),
    ("Шинка", IngredientCategory.MEAT_PRODUCTS, False, []),

    ("Баранина", IngredientCategory.MEAT_OTHER, False, []),
    ("Дичина", IngredientCategory.MEAT_OTHER, False, []),
    ("Козлятина", IngredientCategory.MEAT_OTHER, False, []),
    ("Оленина", IngredientCategory.MEAT_OTHER, False, []),
    ("Фарш з баранини", IngredientCategory.MEAT_OTHER, False, []),

    # ================= КРУПИ ТА БОБОВІ =================
    ("Амарант", IngredientCategory.GRAINS, False, []),
    ("Булгур", IngredientCategory.GRAINS, False, []),
    ("Білий рис", IngredientCategory.GRAINS, False, []),
    ("Гречка", IngredientCategory.GRAINS, False, []),
    ("Дикий рис", IngredientCategory.GRAINS, False, []),
    ("Коричневий рис", IngredientCategory.GRAINS, False, []),
    ("Кіноа", IngredientCategory.GRAINS, False, []),
    ("Нут", IngredientCategory.GRAINS, False, []),
    ("Овес", IngredientCategory.GRAINS, False, []),
    ("Просо", IngredientCategory.GRAINS, False, []),
    ("Сочевиця", IngredientCategory.GRAINS, False, []),
    ("Спельта", IngredientCategory.GRAINS, False, []),
    ("Ячмінь", IngredientCategory.GRAINS, False, []),
    ("Вівсяні пластівці", IngredientCategory.GRAINS, False, []),
    ("Паста", IngredientCategory.GRAINS, False, []),

    # ================= КОНДИТЕРСЬКІ ІНГРЕДІЄНТИ =================
    ("Шоколад", IngredientCategory.SWEETS, False, []),
    ("Мед", IngredientCategory.SWEETS, False, []),

    # ================= ЗЕЛЕНЬ ТА ТРАВИ =================
    ("Базилік", IngredientCategory.GREENS, True, [6, 7, 8, 9]),
    ("Крес-салат", IngredientCategory.GREENS, True, [5, 6, 7]),
    ("Кріп", IngredientCategory.GREENS, True, [5, 6, 7, 8]),
    ("Кінза", IngredientCategory.GREENS, True, [6, 7, 8, 9]),
    ("Листя салату", IngredientCategory.GREENS, True, [5, 6, 7]),
    ("М'ята", IngredientCategory.GREENS, True, [6, 7, 8, 9]),
    ("Мангольд", IngredientCategory.GREENS, True, [6, 7, 8, 9, 10]),
    ("Петрушка", IngredientCategory.GREENS, True, [5, 6, 7, 8]),
    ("Розмарин", IngredientCategory.GREENS, True, [6, 7, 8, 9, 10]),
    ("Рукола", IngredientCategory.GREENS, True, [5, 6, 7]),
    ("Тим'ян", IngredientCategory.GREENS, True, [6, 7, 8, 9, 10]),
    ("Шпинат", IngredientCategory.GREENS, True, [5, 6, 7]),
    ("Щавель", IngredientCategory.GREENS, True, [5, 6, 7]),

    # ================= ГРИБИ =================
    ("Білі гриби", IngredientCategory.MUSHROOMS, True, [8, 9, 10]),
    ("Гливи", IngredientCategory.MUSHROOMS, False, []),
    ("Лисички", IngredientCategory.MUSHROOMS, True, [8, 9, 10]),
    ("Маслюки", IngredientCategory.MUSHROOMS, True, [8, 9, 10]),
    ("Опеньки", IngredientCategory.MUSHROOMS, True, [8, 9, 10]),
    ("Печериці", IngredientCategory.MUSHROOMS, False, []),
    ("Портобелло", IngredientCategory.MUSHROOMS, False, []),
    ("Шиїтаке", IngredientCategory.MUSHROOMS, False, []),

    # ================= ГОРІХИ ТА НАСІННЯ =================
    ("Арахіс", IngredientCategory.NUTS, False, []),
    ("Волоський горіх", IngredientCategory.NUTS, False, []),
    ("Гарбузове насіння", IngredientCategory.NUTS, False, []),
    ("Кеш'ю", IngredientCategory.NUTS, False, []),
    ("Мигдаль", IngredientCategory.NUTS, False, []),
    ("Насіння льону", IngredientCategory.NUTS, False, []),
    ("Насіння чіа", IngredientCategory.NUTS, False, []),
    ("Соняшникове насіння", IngredientCategory.NUTS, False, []),
    ("Горіхи", IngredientCategory.NUTS, False, []),

    # ================= БОРОШНО =================
    ("Борошно з білого рису", IngredientCategory.FLOUR, False, []),
    ("Вівсяне борошно", IngredientCategory.FLOUR, False, []),
    ("Кукурудзяне борошно", IngredientCategory.FLOUR, False, []),
    ("Кукурудзяне борошно грубого помелу", IngredientCategory.FLOUR, False, []),
    ("Мигдальне борошно", IngredientCategory.FLOUR, False, []),
    ("Пшеничне борошно", IngredientCategory.FLOUR, False, []),
    ("Тапіокове борошно", IngredientCategory.FLOUR, False, []),
    ("Цільнозернове борошно", IngredientCategory.FLOUR, False, []),

    # ================= АЛЬТЕРНАТИВНІ БІЛКИ =================
    ("Сейтан", IngredientCategory.ALT_PROTEIN, False, []),
    ("Текстурований рослинний білок", IngredientCategory.ALT_PROTEIN, False, []),
    ("Темпе", IngredientCategory.ALT_PROTEIN, False, []),
    ("Тофу", IngredientCategory.ALT_PROTEIN, False, []),

    # ================= НОВІ ІНГРЕДІЄНТИ =================
    ("Цукор", IngredientCategory.SWEETS, False, []),
    ("Розпушувач", IngredientCategory.SWEETS, False, []),
    ("Соєвий соус", IngredientCategory.OILS_LIQUIDS, False, []),
    ("Рисовий оцет", IngredientCategory.OILS_LIQUIDS, False, []),
    ("Кунжутна олія", IngredientCategory.OILS_LIQUIDS, False, []),
    ("Місо паста", IngredientCategory.OILS_LIQUIDS, False, []),
    ("Водорості вакаме", IngredientCategory.SEAFOOD, False, []),
    ("Імбир", IngredientCategory.SPICES, False, []),
    ("Темний шоколад", IngredientCategory.SWEETS, False, []),
    ("Паприка", IngredientCategory.SPICES, False, []),
    ("М'ясний фарш", IngredientCategory.MEAT_PRODUCTS, False, []),
    ("Сир твердий", IngredientCategory.CHEESE, False, []),
    ("Панірувальні сухарі", IngredientCategory.GRAINS, False, []),
]


def run():
    print("Починаємо завантаження інгредієнтів...\n")
    added_count = 0

    for name, category, is_seasonal, months in INGREDIENTS_DATA:
        # get_or_create гарантує, що ми не створимо дублікатів
        # Якщо інгредієнт з такою назвою вже є (наприклад з минулого запуску),
        # він його просто пропустить
        obj, created = Ingredient.objects.get_or_create(
            name=name,
            defaults={
                'category': category,
                'is_seasonal': is_seasonal,
                'seasonal_months': months
            }
        )
        if created:
            print(f"✅ Додано: {name}")
            added_count += 1
        else:
            # Можемо закоментувати цей принт, щоб не засмічувати консоль,
            # якщо запускатимемо кілька разів
            pass

    print(f"\n🎉 Готово! Успішно додано нових інгредієнтів: {added_count}")


if __name__ == '__main__':
    run()