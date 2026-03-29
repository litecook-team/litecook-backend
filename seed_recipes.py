import os
import django
from django.core.files import File
from django.core.files.storage import default_storage
from django.utils.text import slugify
from unidecode import unidecode

# Налаштування середовища Django для запуску скрипта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from recipes.models.recipe import Recipe, RecipeIngredient, RecipeStep, Difficulty, MealTime, Diet, DishType, Cuisine, UnitChoice
from recipes.models.ingredient import Ingredient

# Формат даних для рецептів
RECIPES_DATA = [
    {
        "title": "Вівсянка з ягодами та горіхами",
        "description": "Смачний і поживний сніданок, який заряджає енергією на весь день. Поєднання ніжної вівсянки, свіжих ягід і хрустких горіхів робить страву не тільки корисною, а й дуже апетитною.",
        "source": "",
        "cooking_time": 10,
        "portions": 1,
        "calories": 320,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.EUROPEAN],
        "meal_times": [MealTime.BREAKFAST],
        "dietary_tags": [Diet.VEGETARIAN],
        "dish_types": [DishType.PORRIDGE],
        "ingredients": [
            ("Вівсяні пластівці", 80, UnitChoice.G),
            ("Мигдальне молоко", 200, UnitChoice.ML),
            ("Полуниця", 50, UnitChoice.G),
            ("Чорниця", 50, UnitChoice.G),
            ("Мед", 1, UnitChoice.TSP),
            ("Волоський горіх", 20, UnitChoice.G), # Виправлено
        ],
        "steps": [
            "Доведіть мигдальне молоко до кипіння.",
            "Додайте вівсяні пластівці та варіть 5 хвилин.",
            "Перекладіть кашу у тарілку.",
            "Додайте ягоди, мед та подрібнені горіхи."
        ]
    },
    {
        "title": "Запечені овочі з травами",
        "description": "Ароматна страва з сезонних овочів, запечених із пряними травами та оливковою олією. Легка, корисна та насичена смаком — ідеально підходить як гарнір або самостійна страва.",
        "source": "",
        "cooking_time": 30,
        "portions": 2,
        "calories": 150,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.MEDITERRANEAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.VEGAN],
        "dish_types": [DishType.GARNISH],
        "ingredients": [
            ("Кабачок", 1, UnitChoice.PCS),
            ("Болгарський перець", 1, UnitChoice.PCS),
            ("Морква", 1, UnitChoice.PCS),
            ("Броколі", 100, UnitChoice.G),
            ("Оливкова олія", 2, UnitChoice.TBSP),
            ("Часник", 2, UnitChoice.CLOVE),
            ("Орегано", 1, UnitChoice.TSP),
            ("Сіль", None, UnitChoice.TASTE), # Розділено
            ("Чорний перець", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Наріжте овочі великими шматками.",
            "Викладіть їх на деко.",
            "Додайте оливкову олію та спеції.",
            "Запікайте 20 хвилин при 180°C."
        ]
    },
    {
        "title": "Куряче філе з лимоном та зеленню",
        "description": "Соковите куряче філе з ніжним цитрусовим ароматом і свіжою зеленню. Легка у приготуванні страва, яка чудово підходить для обіду або вечері. Ідеальний варіант для збалансованого та дієтичного харчування.",
        "source": "",
        "cooking_time": 30,
        "portions": 2,
        "calories": 280,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.EUROPEAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.DIETARY],
        "dish_types": [DishType.MAIN, DishType.MEAT],
        "ingredients": [
            ("Куряче філе", 2, UnitChoice.PCS),
            ("Лимон", 1, UnitChoice.PCS),
            ("Оливкова олія", 2, UnitChoice.TBSP),
            ("Часник", 2, UnitChoice.CLOVE),
            ("Петрушка", 10, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE), # Розділено
            ("Чорний перець", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Натріть курку сіллю та перцем.",
            "Змішайте оливкову олію, лимонний сік та часник.",
            "Полийте соусом курку.",
            "Запікайте 25 хв при 180°C.",
            "Перед подачею посипте петрушкою."
        ]
    },
    {
        "title": "Салат з кіноа, авокадо та овочами",
        "description": "Свіжий і поживний салат із кіноа та овочів, який поєднує користь і насичений смак. Легкий, але ситний варіант для обіду або вечері, що чудово підходить для веганського раціону.",
        "source": "",
        "cooking_time": 20,
        "portions": 2,
        "calories": 340,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.MEDITERRANEAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.VEGAN],
        "dish_types": [DishType.SALAD],
        "ingredients": [
            ("Кіноа", 100, UnitChoice.G),
            ("Авокадо", 1, UnitChoice.PCS),
            ("Огірок", 1, UnitChoice.PCS),
            ("Помідори чері", 100, UnitChoice.G),
            ("Листя салату", 50, UnitChoice.G),
            ("Оливкова олія", 2, UnitChoice.TBSP),
            ("Лимонний сік", 1, UnitChoice.TBSP),
            ("Сіль", None, UnitChoice.TASTE), # Розділено
            ("Чорний перець", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Промийте кіноа та відваріть у підсоленій воді приблизно 15 хвилин, охолодіть.",
            "Наріжте огірок, авокадо та помідори.",
            "У мисці змішайте кіноа, овочі та листя салату.",
            "Заправте оливковою олією, лимонним соком, додайте сіль та перець.",
            "Акуратно перемішайте та подавайте."
        ]
    },
    {
        "title": "Смузі з бананом та шпинатом",
        "description": "Освіжаючий і корисний напій, який поєднує солодкість банана та користь зелені. Ідеальний варіант для швидкого сніданку або перекусу, що заряджає енергією та вітамінами.",
        "source": "",
        "cooking_time": 5,
        "portions": 1,
        "calories": 190,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.INTERNATIONAL],
        "meal_times": [MealTime.BREAKFAST, MealTime.SNACK],
        "dietary_tags": [Diet.VEGETARIAN],
        "dish_types": [DishType.SMOOTHIE, DishType.DRINK],
        "ingredients": [
            ("Банан", 1, UnitChoice.PCS),
            ("Шпинат", 50, UnitChoice.G),
            ("Мигдальне молоко", 200, UnitChoice.ML),
            ("Насіння чіа", 1, UnitChoice.TSP),
            ("Мед", 1, UnitChoice.TSP),
        ],
        "steps": [
            "Очистіть банан.",
            "Покладіть усі інгредієнти у блендер.",
            "Збийте до однорідної консистенції."
        ]
    },
    {
        "title": "Томатний суп з базиліком",
        "description": "Легкий і ароматний суп із насиченим томатним смаком та свіжим базиліком. Чудовий варіант для обіду, який зігріває та дарує відчуття домашнього затишку.",
        "source": "",
        "cooking_time": 25,
        "portions": 2,
        "calories": 120,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.ITALIAN],
        "meal_times": [MealTime.LUNCH],
        "dietary_tags": [Diet.VEGAN],
        "dish_types": [DishType.SOUP],
        "ingredients": [
            ("Помідор", 400, UnitChoice.G), # Виправлено
            ("Цибуля ріпчаста", 1, UnitChoice.PCS), # Виправлено
            ("Часник", 2, UnitChoice.CLOVE),
            ("Базилік", 10, UnitChoice.G),
            ("Оливкова олія", 1, UnitChoice.TBSP),
            ("Овочевий бульйон", 400, UnitChoice.ML),
            ("Сіль", None, UnitChoice.TASTE), # Розділено
            ("Чорний перець", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Наріжте цибулю та часник і обсмажте на оливковій олії.",
            "Додайте нарізані помідори.",
            "Влийте овочевий бульйон і варіть 10 хв."
        ]
    },
    {
        "title": "Паста з грибами та часником",
        "description": "Ніжна паста з ароматними грибами та часником — проста, але дуже смачна страва. Ідеально підходить для швидкого обіду або вечері з італійським настроєм.",
        "source": "",
        "cooking_time": 25,
        "portions": 2,
        "calories": 480,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.ITALIAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.VEGETARIAN],
        "dish_types": [DishType.PASTA, DishType.FLOUR],
        "ingredients": [
            ("Паста", 150, UnitChoice.G),
            ("Печериці", 200, UnitChoice.G),
            ("Часник", 2, UnitChoice.CLOVE),
            ("Оливкова олія", 2, UnitChoice.TBSP),
            ("Петрушка", 10, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE), # Розділено
            ("Чорний перець", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Відваріть пасту до готовності.",
            "Наріжте гриби і обсмажте з часником.",
            "Додайте пасту до грибів.",
            "Посипте петрушкою та перемішайте."
        ]
    },
    {
        "title": "Соус гуакамоле",
        "description": "Класичний мексиканський соус із кремового авокадо та свіжих овочів. Чудово підходить як закуска або доповнення до основних страв.",
        "source": "",
        "cooking_time": 10,
        "portions": 2,
        "calories": 220,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.MEXICAN],
        "meal_times": [MealTime.SNACK],
        "dietary_tags": [Diet.VEGAN],
        "dish_types": [DishType.SAUCE, DishType.SNACK],
        "ingredients": [
            ("Авокадо", 2, UnitChoice.PCS),
            ("Лайм", 1, UnitChoice.PCS),
            ("Помідор", 1, UnitChoice.PCS),
            ("Цибуля червона", 0.5, UnitChoice.PCS), # Виправлено
            ("Кінза", 5, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Розімніть авокадо виделкою.",
            "Додайте нарізаний помідор та цибулю.",
            "Додайте сік лайма.",
            "Посипте кінзою та перемішайте."
        ]
    },
    {
        "title": "Лосось запечений з овочами",
        "description": "Ніжний лосось у поєднанні з овочами — корисна та збалансована страва. Ідеальний варіант для легкої вечері або здорового обіду.",
        "source": "",
        "cooking_time": 30,
        "portions": 2,
        "calories": 450,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.MEDITERRANEAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.DIETARY],
        "dish_types": [DishType.MAIN, DishType.FISH],
        "ingredients": [
            ("Філе лосося", 2, UnitChoice.PCS),
            ("Броколі", 150, UnitChoice.G),
            ("Кабачок", 1, UnitChoice.PCS),
            ("Лимон", 0.5, UnitChoice.PCS),
            ("Оливкова олія", 1, UnitChoice.TBSP),
            ("Сіль", None, UnitChoice.TASTE), # Розділено
            ("Чорний перець", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Наріжте овочі.",
            "Викладіть їх на деко разом із лососем.",
            "Полийте оливковою олією та лимонним соком.",
            "Запікайте 20 хв при 180°C."
        ]
    },
    {
        "title": "Салат з нутом та овочами",
        "description": "Поживний і ситний салат із нутом та свіжими овочами. Відмінний варіант для веганського обіду або вечері.",
        "source": "",
        "cooking_time": 20,
        "portions": 2,
        "calories": 320,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.MEDITERRANEAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.VEGAN],
        "dish_types": [DishType.SALAD],
        "ingredients": [
            ("Нут", 150, UnitChoice.G),
            ("Огірок", 1, UnitChoice.PCS),
            ("Помідор", 2, UnitChoice.PCS), # Виправлено
            ("Петрушка", 10, UnitChoice.G),
            ("Лимонний сік", 1, UnitChoice.TBSP),
            ("Оливкова олія", 1, UnitChoice.TBSP),
            ("Сіль", None, UnitChoice.TASTE), # Розділено
            ("Чорний перець", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Відваріть нут або використайте готовий.",
            "Наріжте овочі.",
            "Змішайте нут з овочами.",
            "Заправте лимонним соком та оливковою олією."
        ]
    },
    {
        "title": "Йогуртовий десерт з ягодами",
        "description": "Легкий і ніжний десерт із йогурту та свіжих ягід. Ідеальний варіант для перекусу або корисного солодкого.",
        "source": "",
        "cooking_time": 5,
        "portions": 1,
        "calories": 260,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.EUROPEAN],
        "meal_times": [MealTime.SNACK],
        "dietary_tags": [Diet.VEGETARIAN],
        "dish_types": [DishType.DESSERT],
        "ingredients": [
            ("Йогурт", 200, UnitChoice.G),
            ("Полуниця", 50, UnitChoice.G),
            ("Чорниця", 50, UnitChoice.G),
            ("Мед", 1, UnitChoice.TSP),
            ("Горіхи", 20, UnitChoice.G),
        ],
        "steps": [
            "Викладіть йогурт у склянку.",
            "Додайте ягоди.",
            "Полийте медом.",
            "Посипте горіхами."
        ]
    },
    {
        "title": "Креветки з часником",
        "description": "Ароматні креветки, обсмажені з часником і лимонним соком. Швидка та вишукана страва для легкої вечері або закуски.",
        "source": "",
        "cooking_time": 10,
        "portions": 2,
        "calories": 230,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.MEDITERRANEAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.DIETARY],
        "dish_types": [DishType.SNACK, DishType.SEAFOOD],
        "ingredients": [
            ("Креветки очищені", 300, UnitChoice.G),
            ("Часник", 3, UnitChoice.CLOVE),
            ("Оливкова олія", 1, UnitChoice.TBSP),
            ("Лимонний сік", 1, UnitChoice.TBSP),
            ("Петрушка", 10, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
            ("Чорний перець", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Розморозьте креветки та промийте їх водою.",
            "Подрібніть часник.",
            "Розігрійте оливкову олію на сковороді.",
            "Додайте часник і обсмажте 30 секунд.",
            "Додайте креветки на сковороду.",
            "Смажте 3-4 хвилини, помішуючи.",
            "Додайте лимонний сік.",
            "Посоліть та поперчіть.",
            "Посипте подрібненою петрушкою перед подачею."
        ]
    },
    {
        "title": "Український борщ",
        "description": "Традиційна українська страва з насиченим смаком і ароматом. Ситний і поживний суп, який ідеально підходить для обіду.",
        "source": "",
        "cooking_time": 50,
        "portions": 4,
        "calories": 350,
        "difficulty": Difficulty.HARD,
        "cuisine": [Cuisine.UKRAINIAN],
        "meal_times": [MealTime.LUNCH],
        "dietary_tags": [Diet.TRADITIONAL],
        "dish_types": [DishType.SOUP],
        "ingredients": [
            ("Буряк", 2, UnitChoice.PCS),
            ("Картопля", 2, UnitChoice.PCS),
            ("Морква", 1, UnitChoice.PCS),
            ("Капуста білокачанна", 200, UnitChoice.G),
            ("Цибуля ріпчаста", 1, UnitChoice.PCS),
            ("Томатна паста", 1, UnitChoice.TBSP),
            ("Часник", 2, UnitChoice.CLOVE),
            ("Рослинна олія", 1, UnitChoice.TBSP),
            ("Вода", 1, UnitChoice.L),
            ("Сіль", None, UnitChoice.TASTE),
            ("Чорний перець", None, UnitChoice.TASTE),
            ("Кріп", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Очистіть і наріжте буряк соломкою.",
            "Наріжте картоплю кубиками.",
            "Нашаткуйте капусту.",
            "Натріть моркву.",
            "Наріжте цибулю.",
            "Обсмажте цибулю та моркву.",
            "Додайте буряк і томатну пасту.",
            "Додайте картоплю у бульйон і варіть 10 хв.",
            "Додайте капусту та зажарку.",
            "Варіть ще 10 хв.",
            "Додайте часник та кріп."
        ]
    },
    {
        "title": "Французький омлет з сиром",
        "description": "Ніжний і повітряний омлет із розплавленим сиром — класичний варіант швидкого сніданку. Легка текстура та насичений смак роблять цю страву ідеальною для тих, хто цінує простоту та витонченість у приготуванні.",
        "source": "",
        "cooking_time": 10,
        "portions": 1,
        "calories": 300,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.FRENCH],
        "meal_times": [MealTime.BREAKFAST],
        "dietary_tags": [Diet.VEGETARIAN],
        "dish_types": [DishType.OMELET],
        "ingredients": [
            ("Яйця", 3, UnitChoice.PCS),
            ("Голландський сир", 50, UnitChoice.G),
            ("Вершкове масло", 10, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
            ("Чорний перець", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Розбийте яйця у миску, збийте яйця виделкою.",
            "Додайте сіль і перець.",
            "Вилийте яйця на розігріту сковорідку з маслом.",
            "Посипте сиром.",
            "Готуйте на середньому вогні, складіть омлет навпіл."
        ]
    },
    {
        "title": "Американські панкейки",
        "description": "Пухкі та ніжні панкейки — ідеальний варіант для сніданку або десерту. Чудово поєднуються з ягодами, медом або сиропом.",
        "source": "",
        "cooking_time": 25,
        "portions": 3,
        "calories": 420,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.AMERICAN],
        "meal_times": [MealTime.BREAKFAST],
        "dietary_tags": [Diet.VEGETARIAN],
        "dish_types": [DishType.DESSERT, DishType.FLOUR],
        "ingredients": [
            ("Пшеничне борошно", 150, UnitChoice.G),
            ("Яйця", 1, UnitChoice.PCS),
            ("Молоко", 200, UnitChoice.ML),
            ("Цукор", 1, UnitChoice.TBSP),
            ("Розпушувач", 1, UnitChoice.TSP),
            ("Вершкове масло", 20, UnitChoice.G),
        ],
        "steps": [
            "Просійте борошно.",
            "Додайте цукор.",
            "Додайте розпушувач.",
            "Розбийте яйце.",
            "Влийте молоко.",
            "Перемішайте тісто.",
            "Розігрійте сковороду.",
            "Вилийте невеликі порції тіста.",
            "Смажте до золотистої скоринки.",
            "Переверніть панкейк."
        ]
    },
    {
        "title": "Китайський салат з огірком",
        "description": "Легкий і освіжаючий салат із пікантною заправкою. Чудовий варіант для швидкого перекусу.",
        "source": "",
        "cooking_time": 10,
        "portions": 2,
        "calories": 140,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.CHINESE],
        "meal_times": [MealTime.SNACK],
        "dietary_tags": [Diet.VEGAN],
        "dish_types": [DishType.SALAD],
        "ingredients": [
            ("Огірок", 2, UnitChoice.PCS),
            ("Часник", 2, UnitChoice.CLOVE),
            ("Соєвий соус", 1, UnitChoice.TBSP),
            ("Рисовий оцет", 1, UnitChoice.TSP),
            ("Кунжутна олія", 1, UnitChoice.TSP),
        ],
        "steps": [
            "Наріжте огірки кружальцями.",
            "Подрібніть часник.",
            "Змішайте соєвий соус та оцет.",
            "Додайте кунжутну олію.",
            "Перемішайте огірки з соусом."
        ]
    },
    {
        "title": "Японський місо-суп",
        "description": "Традиційний японський суп із ніжним смаком місо та тофу. Легка і корисна страва для обіду.",
        "source": "",
        "cooking_time": 15,
        "portions": 2,
        "calories": 180,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.JAPANESE],
        "meal_times": [MealTime.LUNCH],
        "dietary_tags": [Diet.VEGETARIAN],
        "dish_types": [DishType.SOUP],
        "ingredients": [
            ("Місо паста", 2, UnitChoice.TBSP),
            ("Тофу", 100, UnitChoice.G),
            ("Водорості вакаме", 5, UnitChoice.G),
            ("Цибуля зелена", 1, UnitChoice.PCS),
            ("Вода", 500, UnitChoice.ML),
        ],
        "steps": [
            "Закип'ятіть воду.",
            "Додайте водорості.",
            "Наріжте тофу кубиками.",
            "Додайте тофу у воду.",
            "Розчиніть місо пасту.",
            "Перемішайте суп.",
            "Додайте зелену цибулю."
        ]
    },
    {
        "title": "Азійський імбирний чай",
        "description": "Теплий та зігріваючий напій із яскравим смаком імбиру. Допомагає підтримати імунітет і чудово підходить для холодної пори або як корисний щоденний напій.",
        "source": "",
        "cooking_time": 10,
        "portions": 2,
        "calories": 80,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.ASIAN],
        "meal_times": [MealTime.SNACK],
        "dietary_tags": [Diet.VEGETARIAN],
        "dish_types": [DishType.DRINK],
        "ingredients": [
            ("Вода", 400, UnitChoice.ML),
            ("Імбир", 10, UnitChoice.G),
            ("Лимон", 1, UnitChoice.SLICE),
            ("Мед", 1, UnitChoice.TSP),
        ],
        "steps": [
            "Наріжте імбир тонкими скибками.",
            "Закип'ятіть воду.",
            "Додайте імбир у воду.",
            "Варіть 5 хв.",
            "Додайте лимон, мед, перемішайте."
        ]
    },
    {
        "title": "Свинина запечена з часником",
        "description": "Соковита свинина з насиченим ароматом часнику та спецій. Запікання дозволяє зберегти ніжність м'яса та розкрити його смак, роблячи страву ідеальною для ситного обіду або вечері.",
        "source": "",
        "cooking_time": 45,
        "portions": 2,
        "calories": 520,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.EUROPEAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL],
        "dish_types": [DishType.MAIN, DishType.MEAT],
        "ingredients": [
            ("Свинина", 400, UnitChoice.G),
            ("Часник", 3, UnitChoice.CLOVE),
            ("Оливкова олія", 1, UnitChoice.TBSP),
            ("Паприка", 1, UnitChoice.TSP),
            ("Сіль", None, UnitChoice.TASTE),
            ("Чорний перець", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Наріжте свинину шматками.",
            "Подрібніть часник.",
            "Натріть м'ясо сіллю, перцем і паприкою.",
            "Додайте часник.",
            "Полийте оливковою олією.",
            "Перемішайте м'ясо.",
            "Викладіть у форму для запікання.",
            "Розігрійте духовку до 180°C.",
            "Запікайте 35 хв."
        ]
    },
    {
        "title": "Крем-суп з гарбуза",
        "description": "Ніжний і кремовий суп із гарбуза з м'яким солодкуватим смаком. Легка та поживна страва, яка чудово зігріває та підходить для осіннього меню.",
        "source": "",
        "cooking_time": 40,
        "portions": 3,
        "calories": 210,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.EUROPEAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.VEGETARIAN],
        "dish_types": [DishType.SOUP],
        "ingredients": [
            ("Гарбуз", 400, UnitChoice.G),
            ("Картопля", 1, UnitChoice.PCS),
            ("Морква", 1, UnitChoice.PCS),
            ("Цибуля ріпчаста", 1, UnitChoice.PCS),
            ("Вершки", 100, UnitChoice.ML),
            ("Оливкова олія", 1, UnitChoice.TBSP),
            ("Сіль", None, UnitChoice.TASTE),
            ("Чорний перець", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Очистіть гарбуз та наріжте гарбуз кубиками.",
            "Наріжте картоплю, моркву, цибулю.",
            "Обсмажте цибулю на олії.",
            "Додайте моркву і гарбуз, картоплю.",
            "Залийте водою та варіть 20 хв.",
            "Збийте блендером.",
            "Додайте вершки."
        ]
    },
    {
        "title": "Сирники",
        "description": "Традиційна страва з ніжного сиру з рум'яною скоринкою та м'якою текстурою всередині. Ідеально підходять для сніданку або десерту та чудово поєднуються з медом, ягодами або сметаною.",
        "source": "",
        "cooking_time": 25,
        "portions": 3,
        "calories": 340,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.UKRAINIAN],
        "meal_times": [MealTime.BREAKFAST, MealTime.SNACK],
        "dietary_tags": [Diet.VEGETARIAN],
        "dish_types": [DishType.DESSERT, DishType.FLOUR],
        "ingredients": [
            ("Кисломолочний сир", 300, UnitChoice.G),
            ("Яйця", 1, UnitChoice.PCS),
            ("Пшеничне борошно", 3, UnitChoice.TBSP),
            ("Цукор", 1, UnitChoice.TBSP),
            ("Рослинна олія", 1, UnitChoice.TBSP),
        ],
        "steps": [
            "Покладіть сир у миску.",
            "Додайте яйце, цукор, борошно.",
            "Перемішайте тісто, сформуйте невеликі сирники.",
            "Розігрійте сковороду, налийте олію.",
            "Викладіть сирники, смажте до золотистої скоринки."
        ]
    },
    {
        "title": "Шоколадний мус",
        "description": "Легкий і повітряний десерт із насиченим шоколадним смаком. Тане в роті та дарує справжнє задоволення — ідеальний варіант для солодкого завершення дня.",
        "source": "",
        "cooking_time": 140,
        "portions": 3,
        "calories": 410,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.FRENCH],
        "meal_times": [MealTime.SNACK],
        "dietary_tags": [Diet.VEGETARIAN],
        "dish_types": [DishType.DESSERT],
        "ingredients": [
            ("Темний шоколад", 150, UnitChoice.G),
            ("Вершки", 200, UnitChoice.ML),
            ("Цукор", 1, UnitChoice.TBSP),
            ("Яйця", 2, UnitChoice.PCS),
        ],
        "steps": [
            "Розтопіть шоколад на водяній бані.",
            "Відокремте жовтки від білків.",
            "Додайте жовтки до шоколаду.",
            "Збийте вершки.",
            "Збийте білки з цукром.",
            "Змішайте шоколад з вершками.",
            "Обережно додайте білки.",
            "Перемішайте масу.",
            "Розкладіть у склянки.",
            "Поставте у холодильник на 2 години."
        ]
    },
    {
        "title": "Вареники з картоплею",
        "description": "Класична українська страва з ніжним тістом і ситною картопляною начинкою. Домашній смак і аромат роблять її ідеальним вибором для обіду або сімейної вечері.",
        "source": "",
        "cooking_time": 60,
        "portions": 3,
        "calories": 450,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.UKRAINIAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL],
        "dish_types": [DishType.MAIN, DishType.FLOUR],
        "ingredients": [
            ("Пшеничне борошно", 300, UnitChoice.G),
            ("Вода", 150, UnitChoice.ML),
            ("Картопля", 400, UnitChoice.G),
            ("Цибуля ріпчаста", 1, UnitChoice.PCS),
            ("Рослинна олія", 1, UnitChoice.TBSP),
            ("Сіль", None, UnitChoice.TASTE),
            ("Чорний перець", None, UnitChoice.TASTE),
        ],
        "steps": [
            "Просійте борошно, додайте воду, замісіть тісто.",
            "Очистіть картоплю та відваріть.",
            "Зробіть пюре.",
            "Обсмажте цибулю та додайте у пюре.",
            "Розкачайте тісто і виріжте кружечки.",
            "Покладіть начинку та зліпіть вареники.",
            "Відваріть у киплячій воді.",
            "Додайте смажену цибулю до готових вареників."
        ]
    }
]

def run():
    print("🧹 Очищення старих рецептів...")
    Recipe.objects.all().delete()
    print("✅ Базу рецептів очищено. Починаємо завантаження нових...\n")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(base_dir, 'seed_recipe_images')
    extensions = ['.jpg', '.jpeg', '.png', '.webp']

    added_count = 0

    for data in RECIPES_DATA:
        print(f"🔄 Створюємо: {data['title']}...")

        recipe = Recipe.objects.create(
            title=data["title"],
            description=data["description"],
            source=data.get("source", ""),
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

        for index, step_text in enumerate(data["steps"], start=1):
            RecipeStep.objects.create(
                recipe=recipe,
                step_number=index,
                text=step_text
            )

        recipe.update_seasonality()
        print(f"✅ Успішно додано: {data['title']}\n")
        added_count += 1

    print(f"🎉 Готово! Додано нових рецептів: {added_count}")

if __name__ == '__main__':
    run()