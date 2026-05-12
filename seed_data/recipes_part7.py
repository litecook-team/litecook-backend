from recipes.models.recipe import Difficulty, MealTime, Diet, DishType, Cuisine, UnitChoice

# Формат даних для рецептів
RECIPES_DATA_7 = [
    {
        "title": "Вершкова паста з креветками та беконом",
        "title_en": "Creamy pasta with shrimp and bacon",
        "title_pl": "Kremowy makaron z krewetkami i boczkiem",
        "description": "Швидка паста з креветками, беконом, маскарпоне, руколою та Пармезаном. Ситна страва для обіду або вечері.",
        "description_en": "Quick pasta with shrimp, bacon, mascarpone, arugula, and Parmesan. A hearty dish for lunch or dinner.",
        "description_pl": "Szybki makaron z krewetkami, boczkiem, mascarpone, rukolą i parmezanem. Sycące danie na obiad lub kolację.",
        "source": "Джеймі Олівер",
        "source_en": "Jamie Oliver",
        "source_pl": "Jamiego Olivera",
        "cooking_time": 20,
        "portions": 2,
        "calories": 550,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.ITALIAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET],
        "dish_types": [DishType.MAIN, DishType.PASTA, DishType.SEAFOOD],
        "ingredients": [
            ("Паста", 150, UnitChoice.G),
            ("Часник", 2, UnitChoice.CLOVE),
            ("Креветки очищені", 160, UnitChoice.G),
            ("Бекон", 80, UnitChoice.G),
            ("Маскарпоне", 40, UnitChoice.G),
            ("Рукола", 50, UnitChoice.G),
            ("Пармезан", 10, UnitChoice.G),
            ("Оливкова олія", 15, UnitChoice.ML),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Відваріть пасту в підсоленій воді, збережіть трохи води від варіння.",
             "en": "Boil the pasta in salted water, keeping a little of the cooking water.",
             "pl": "Ugotuj makaron w osolonej wodzie, zachowaj trochę wody z gotowania."
            },
            {
             "uk": "Бекон дрібно наріжте та обсмажте з оливковою олією до легкої хрусткості.",
             "en": "Finely chop the bacon and fry with olive oil until slightly crispy.",
             "pl": "Boczek drobno posiekaj i usmaż na oliwie z oliwek, aż będzie lekko chrupiący."
            },
            {
             "uk": "Додайте нарізаний часник і очищені креветки. Готуйте 2–3 хвилини.",
             "en": "Add the sliced garlic and peeled shrimp. Cook for 2-3 minutes.",
             "pl": "Dodaj posiekany czosnek i obrane krewetki. Gotuj przez 2-3 minuty."
            },
            {
             "uk": "Додайте маскарпоне і трохи води від пасти, щоб утворився кремовий соус.",
             "en": "Add the mascarpone and a little pasta water to create a creamy sauce.",
             "pl": "Dodaj mascarpone i trochę wody z makaronu, aby powstał kremowy sos."
            },
            {
             "uk": "Змішайте соус із пастою та руколою. Подавайте з Пармезаном і чорним перцем.",
             "en": "Toss the sauce with the pasta and arugula. Serve with Parmesan and black pepper.",
             "pl": "Wymieszaj sos z makaronem i rukolą. Podawaj z parmezanem i czarnym pieprzem."
            }
        ]
    },
    {
        "title": "Паста з креветками, в'яленими томатами та руколою",
        "title_en": "Pasta with shrimp, sun-dried tomatoes, and arugula",
        "title_pl": "Makaron z krewetkami, suszonymi pomidorami i rukolą",
        "description": "Легка паста з креветками, часником, чилі, в’яленими томатами, лимоном і руколою.",
        "description_en": "A light pasta with shrimp, garlic, chili, sun-dried tomatoes, lemon, and arugula.",
        "description_pl": "Lekki makaron z krewetkami, czosnkiem, chili, suszonymi pomidorami, cytryną i rukolą.",
        "source": "Джеймі Олівер",
        "source_en": "Jamie Oliver",
        "source_pl": "Jamiego Olivera",
        "cooking_time": 20,
        "portions": 4,
        "calories": 420,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.ITALIAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET],
        "dish_types": [DishType.MAIN, DishType.PASTA, DishType.SEAFOOD],
        "ingredients": [
            ("Паста", 455, UnitChoice.G),
            ("Часник", 2, UnitChoice.CLOVE),
            ("Креветки очищені", 400, UnitChoice.G),
            ("Оливкова олія", 40, UnitChoice.ML),
            ("Перець чилі", 5, UnitChoice.G),
            ("В'ялені томати", 30, UnitChoice.G),
            ("Лимон", 1, UnitChoice.PCS),
            ("Рукола", 60, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Відваріть пасту у підсоленій воді до стану al dente, збережіть трохи води.",
             "en": "Boil the pasta in salted water until al dente, reserving a little water.",
             "pl": "Ugotuj makaron w osolonej wodzie al dente, zachowując trochę wody."
            },
            {
             "uk": "Часник і чилі дрібно наріжте, руколу грубо подрібніть, з лимона зніміть цедру та вичавіть сік.",
             "en": "Finely chop the garlic and chili, roughly chop the arugula, zest the lemon, and squeeze the juice.",
             "pl": "Drobno posiekaj czosnek i chili, grubo posiekaj rukolę, zetrzyj skórkę z cytryny i wyciśnij sok."
            },
            {
             "uk": "На оливковій олії швидко обсмажте часник і чилі, не допускаючи підгоряння.",
             "en": "Quickly sauté the garlic and chili in olive oil, taking care not to burn them.",
             "pl": "Szybko podsmaż czosnek i chili na oliwie z oliwek, nie dopuszczając do przypalenia."
            },
            {
             "uk": "Додайте креветки та в’ялені томати, готуйте кілька хвилин до готовності креветок.",
             "en": "Add the shrimp and sun-dried tomatoes, cook for a few minutes until the shrimp are done.",
             "pl": "Dodaj krewetki i suszone pomidory, gotuj kilka minut, aż krewetki będą gotowe."
            },
            {
             "uk": "Змішайте соус із пастою, лимонним соком, цедрою, руколою та невеликою кількістю води від пасти.",
             "en": "Toss the sauce with the pasta, lemon juice, zest, arugula, and a splash of the pasta water.",
             "pl": "Wymieszaj sos z makaronem, sokiem z cytryny, skórką, rukolą i niewielką ilością wody z makaronu."
            }
        ]
    },
    {
        "title": "Паста з морепродуктами в томатному соусі",
        "title_en": "Seafood pasta in tomato sauce",
        "title_pl": "Makaron z owocami morza w sosie pomidorowym",
        "description": "Паста з мідіями, креветками, кальмаром, томатною основою, часником і чилі. Швидка вечеря з морепродуктами.",
        "description_en": "Pasta with mussels, shrimp, squid, tomato base, garlic, and chili. A quick seafood dinner.",
        "description_pl": "Makaron z małżami, krewetkami, kalmarami, bazą pomidorową, czosnkiem i chili. Szybka kolacja z owocami morza.",
        "source": "Євген Клопотенко",
        "source_en": "Yevhen Klopotenko",
        "source_pl": "Jewhen Klopotenko",
        "cooking_time": 25,
        "portions": 2,
        "calories": 510,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.ITALIAN, Cuisine.AUTHOR],
        "meal_times": [MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET],
        "dish_types": [DishType.MAIN, DishType.PASTA, DishType.SEAFOOD],
        "ingredients": [
            ("Мідії", 100, UnitChoice.G),
            ("Креветки", 100, UnitChoice.G),
            ("Кальмар", 100, UnitChoice.G),
            ("Паста", 150, UnitChoice.G),
            ("Цибуля ріпчаста", 50, UnitChoice.G),
            ("Перець чилі", 5, UnitChoice.G),
            ("Часник", 2, UnitChoice.CLOVE),
            ("Томатна паста", 30, UnitChoice.G),
            ("Вода", 150, UnitChoice.ML),
            ("Вершкове масло", 50, UnitChoice.G),
            ("Оливкова олія", 15, UnitChoice.ML),
            ("Пармезан", 50, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Відваріть пасту у підсоленій воді на 1 хвилину менше, ніж зазначено на упаковці.",
             "en": "Boil the pasta in salted water for 1 minute less than indicated on the package.",
             "pl": "Gotuj makaron w osolonej wodzie o 1 minutę krócej niż podano na opakowaniu."
            },
            {
             "uk": "Цибулю, часник і чилі дрібно наріжте. Обсмажте їх на суміші оливкової олії та вершкового масла.",
             "en": "Finely chop the onion, garlic, and chili. Fry them in a mixture of olive oil and butter.",
             "pl": "Drobno posiekaj cebulę, czosnek i chili. Usmaż je na mieszance oliwy z oliwek i masła."
            },
            {
             "uk": "Додайте мідії, креветки та кальмар, швидко обсмажте приблизно 1 хвилину.",
             "en": "Add the mussels, shrimp, and squid, and quickly fry for about 1 minute.",
             "pl": "Dodaj małże, krewetki i kalmary, szybko podsmaż przez około 1 minutę."
            },
            {
             "uk": "Додайте томатну пасту і воду, перемішайте та тушкуйте 3 хвилини.",
             "en": "Add the tomato paste and water, stir, and simmer for 3 minutes.",
             "pl": "Dodaj koncentrat pomidorowy i wodę, wymieszaj i duś przez 3 minuty."
            },
            {
             "uk": "Перекладіть пасту в соус, прогрійте 1 хвилину та подавайте з Пармезаном і чорним перцем.",
             "en": "Transfer the pasta to the sauce, heat for 1 minute, and serve with Parmesan and black pepper.",
             "pl": "Przełóż makaron do sosu, podgrzewaj przez 1 minutę i podawaj z parmezanem i czarnym pieprzem."
            }
        ]
    },
    {
        "title": "Мідії у вершковому соусі зі смаженим арахісом",
        "title_en": "Mussels in cream sauce with roasted peanuts",
        "title_pl": "Małże w sosie śmietanowym z prażonymi orzeszkami ziemnymi",
        "description": "Мідії готуються у вершковому соусі з часником, чебрецем, чилі та смаженим арахісом.",
        "description_en": "Mussels are cooked in a cream sauce with garlic, thyme, chili, and roasted peanuts.",
        "description_pl": "Małże przygotowywane w sosie śmietanowym z czosnkiem, tymiankiem, chili i prażonymi orzeszkami ziemnymi.",
        "source": "Євген Клопотенко",
        "source_en": "Yevhen Klopotenko",
        "source_pl": "Jewhen Klopotenko",
        "cooking_time": 15,
        "portions": 2,
        "calories": 380,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.EUROPEAN, Cuisine.AUTHOR],
        "meal_times": [MealTime.LUNCH, MealTime.SNACK],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET],
        "dish_types": [DishType.HOT_SNACK, DishType.SEAFOOD],
        "ingredients": [
            ("Мідії", 200, UnitChoice.G),
            ("Чебрець", 2, UnitChoice.G),
            ("Часник", 2, UnitChoice.CLOVE),
            ("Арахіс", 30, UnitChoice.G),
            ("Вершки", 150, UnitChoice.ML),
            ("Рослинна олія", 15, UnitChoice.ML),
            ("Перець чилі", 1, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Часник наріжте тонкими слайсами, арахіс за потреби грубо подрібніть.",
             "en": "Slice the garlic thinly, and roughly chop the peanuts if necessary.",
             "pl": "Czosnek pokrój w cienkie plasterki, a w razie potrzeby grubo posiekaj orzeszki ziemne."
            },
            {
             "uk": "Розігрійте рослинну олію, додайте часник, чебрець і чилі, прогрійте до появи аромату.",
             "en": "Heat the vegetable oil, add garlic, thyme, and chili, and heat until fragrant.",
             "pl": "Rozgrzej olej roślinny, dodaj czosnek, tymianek i chili, podgrzewaj do uwolnienia aromatu."
            },
            {
             "uk": "Додайте мідії та обсмажуйте 2 хвилини.",
             "en": "Add the mussels and fry for 2 minutes.",
             "pl": "Dodaj małże i smaż przez 2 minuty."
            },
            {
             "uk": "Влийте вершки, зменшіть вогонь і готуйте 2–3 хвилини до легкого загущення соусу.",
             "en": "Pour in the cream, reduce the heat, and cook for 2-3 minutes until the sauce slightly thickens.",
             "pl": "Wlej śmietankę, zmniejsz ogień i gotuj 2-3 minuty do lekkiego zgęstnienia sosu."
            },
            {
             "uk": "Приправте сіллю і перцем, додайте арахіс і подавайте гарячими.",
             "en": "Season with salt and pepper, add peanuts, and serve hot.",
             "pl": "Dopraw solą i pieprzem, dodaj orzeszki ziemne i podawaj na gorąco."
            }
        ]
    },
    {
        "title": "Мідії Провансаль з томатами та травами",
        "title_en": "Mussels Provencal with tomatoes and herbs",
        "title_pl": "Małże Prowansalskie z pomidorami i ziołami",
        "description": "Мідії готуються у томатному соусі з цибулею, часником, чебрецем, розмарином і петрушкою.",
        "description_en": "Mussels are cooked in a tomato sauce with onions, garlic, thyme, rosemary, and parsley.",
        "description_pl": "Małże są przygotowywane w sosie pomidorowym z cebulą, czosnkiem, tymiankiem, rozmarynem i pietruszką.",
        "source": "Diane Kochilas",
        "source_en": "Diane Kochilas",
        "source_pl": "Diane Kochilas",
        "cooking_time": 30,
        "portions": 4,
        "calories": 350,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.FRENCH, Cuisine.MEDITERRANEAN],
        "meal_times": [MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET, Diet.LACTOSE_FREE],
        "dish_types": [DishType.MAIN, DishType.SEAFOOD],
        "ingredients": [
            ("Мідії", 1800, UnitChoice.G),
            ("Оливкова олія", 60, UnitChoice.ML),
            ("Цибуля ріпчаста", 100, UnitChoice.G),
            ("Часник", 6, UnitChoice.CLOVE),
            ("Помідор", 500, UnitChoice.G),
            ("Томатна паста", 20, UnitChoice.G),
            ("Вода", 200, UnitChoice.ML),
            ("Перець чилі", 2, UnitChoice.G),
            ("Чебрець", 3, UnitChoice.G),
            ("Розмарин", 3, UnitChoice.G),
            ("Лавровий лист", 1, UnitChoice.PCS),
            ("Петрушка", 15, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Мідії ретельно промийте та відкиньте пошкоджені або ті, що не закриваються.",
             "en": "Wash the mussels thoroughly and discard any damaged or unclosed ones.",
             "pl": "Małże dokładnie opłucz i wyrzuć te, które są uszkodzone lub się nie zamykają."
            },
            {
             "uk": "У великій каструлі розігрійте оливкову олію, обсмажте цибулю 3–4 хвилини, додайте часник.",
             "en": "Heat olive oil in a large pot, sauté the onion for 3-4 minutes, then add the garlic.",
             "pl": "W dużym garnku rozgrzej oliwę z oliwek, podsmaż cebulę przez 3-4 minuty, dodaj czosnek."
            },
            {
             "uk": "Додайте помідор, томатну пасту, воду, чилі, чебрець, розмарин і лавровий лист. Проваріть 5 хвилин.",
             "en": "Add tomato, tomato paste, water, chili, thyme, rosemary, and bay leaf. Boil for 5 minutes.",
             "pl": "Dodaj pomidora, koncentrat pomidorowy, wodę, chili, tymianek, rozmaryn i liść laurowy. Gotuj przez 5 minut."
            },
            {
             "uk": "Викладіть мідії у киплячий соус, накрийте кришкою і готуйте 5–7 хвилин, доки раковини відкриються.",
             "en": "Place the mussels in the boiling sauce, cover, and cook for 5-7 minutes until the shells open.",
             "pl": "Przełóż małże do gotującego się sosu, przykryj i gotuj przez 5-7 minut, aż muszle się otworzą."
            },
            {
             "uk": "Викиньте нерозкриті мідії, посипте петрушкою та подавайте гарячими.",
             "en": "Discard unopened mussels, sprinkle with parsley, and serve hot.",
             "pl": "Wyrzuć nieotwarte małże, posyp pietruszką i podawaj na gorąco."
            }
        ]
    },
    {
        "title": "Овочевий стір-фрай з кіноа та імбиром",
        "title_en": "Vegetable stir-fry with quinoa and ginger",
        "title_pl": "Warzywne stir-fry z komosą ryżową i imbirem",
        "description": "Швидкий стір-фрай з кіноа, сезонними овочами, шпинатом, імбиром, соєвим соусом і кунжутною олією.",
        "description_en": "A quick stir-fry with quinoa, seasonal vegetables, spinach, ginger, soy sauce, and sesame oil.",
        "description_pl": "Szybkie stir-fry z komosą ryżową, warzywami sezonowymi, szpinakiem, imbirem, sosem sojowym i olejem sezamowym.",
        "source": "Володимир Ярославський",
        "source_en": "Volodymyr Yaroslavskyi",
        "source_pl": "Wołodymyr Jarosławski",
        "cooking_time": 20,
        "portions": 2,
        "calories": 320,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.ASIAN, Cuisine.AUTHOR],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.VEGAN, Diet.LACTOSE_FREE],
        "dish_types": [DishType.MAIN, DishType.GARNISH],
        "ingredients": [
            ("Кіноа", 150, UnitChoice.G),
            ("Корінь селери", 40, UnitChoice.G),
            ("Гарбуз", 45, UnitChoice.G),
            ("Пастернак", 30, UnitChoice.G),
            ("Листя салату", 40, UnitChoice.G),
            ("Цибуля червона", 15, UnitChoice.G),
            ("Перець болгарський", 40, UnitChoice.G),
            ("Шпинат", 40, UnitChoice.G),
            ("Імбир", 10, UnitChoice.G),
            ("Соєвий соус", 60, UnitChoice.ML),
            ("Кунжутна олія", 20, UnitChoice.ML),
            ("Апельсин", 1, UnitChoice.PCS),
            ("Перець чилі", 2, UnitChoice.G),
        ],
        "steps": [
            {
             "uk": "Відваріть кіноа заздалегідь. Корінь селери, гарбуз, пастернак, цибулю та перець наріжте тонкою соломкою.",
             "en": "Boil the quinoa in advance. Cut celery root, pumpkin, parsnip, onion, and pepper into thin strips.",
             "pl": "Wcześniej ugotuj komosę ryżową. Korzeń selera, dynię, pasternak, cebulę i paprykę pokrój w cienkie paski."
            },
            {
             "uk": "Імбир натріть, з апельсина вичавіть сік, чилі дрібно наріжте.",
             "en": "Grate the ginger, squeeze juice from the orange, finely chop the chili.",
             "pl": "Zetrzyj imbir, wyciśnij sok z pomarańczy, drobno posiekaj chili."
            },
            {
             "uk": "Змішайте соєвий соус, кунжутну олію, апельсиновий сік, імбир і чилі.",
             "en": "Mix soy sauce, sesame oil, orange juice, ginger, and chili.",
             "pl": "Wymieszaj sos sojowy, olej sezamowy, sok z pomarańczy, imbir i chili."
            },
            {
             "uk": "На дуже гарячій сковороді швидко обсмажте нарізані овочі 1–2 хвилини.",
             "en": "In a very hot pan, quickly fry the sliced vegetables for 1-2 minutes.",
             "pl": "Na bardzo gorącej patelni szybko podsmaż pokrojone warzywa przez 1-2 minuty."
            },
            {
             "uk": "Додайте кіноа, листя салату, шпинат і соус. Перемішайте, прогрійте 30–60 секунд і подавайте.",
             "en": "Add quinoa, lettuce leaves, spinach, and sauce. Mix, heat for 30-60 seconds, and serve.",
             "pl": "Dodaj komosę ryżową, liście sałaty, szpinak i sos. Wymieszaj, podgrzewaj przez 30-60 sekund i podawaj."
            }
        ]
    },
    {
        "title": "Салат-гриль з кабачком, персиками та фетою",
        "title_en": "Grilled zucchini, peach, and feta salad",
        "title_pl": "Sałatka z grillowaną cukinią, brzoskwiniami i fetą",
        "description": "Літній теплий салат із кабачком, персиками, зеленню, томатами і фетою. Добре підходить як легкий обід або закуска.",
        "description_en": "A warm summer salad with zucchini, peaches, herbs, tomatoes, and feta. Perfect as a light lunch or appetizer.",
        "description_pl": "Ciepła letnia sałatka z cukinią, brzoskwiniami, zieleniną, pomidorami i fetą. Dobra na lekki obiad lub przekąskę.",
        "source": "Джеймі Олівер",
        "source_en": "Jamie Oliver",
        "source_pl": "Jamiego Olivera",
        "cooking_time": 25,
        "portions": 4,
        "calories": 260,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.MEDITERRANEAN],
        "meal_times": [MealTime.LUNCH, MealTime.SNACK],
        "dietary_tags": [Diet.VEGETARIAN, Diet.GLUTEN_FREE],
        "dish_types": [DishType.SALAD, DishType.COLD_SNACK],
        "ingredients": [
            ("Кабачок", 500, UnitChoice.G),
            ("Цибуля зелена", 40, UnitChoice.G),
            ("Персик", 2, UnitChoice.PCS),
            ("Базилік", 30, UnitChoice.G),
            ("Листя салату", 100, UnitChoice.G),
            ("Помідори чері", 250, UnitChoice.G),
            ("Фета", 100, UnitChoice.G),
            ("Лимонний сік", 15, UnitChoice.ML),
            ("Оливкова олія", 30, UnitChoice.ML),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Кабачок наріжте товстими скибками, зелену цибулю залиште цілою або розріжте навпіл.",
             "en": "Cut the zucchini into thick slices, leave the green onions whole or cut in half.",
             "pl": "Cukinię pokrój w grube plastry, zieloną cebulkę zostaw w całości lub przekrój na pół."
            },
            {
             "uk": "Обсмажте кабачок і зелену цибулю на сковороді-гриль до смужок і легкого розм’якшення.",
             "en": "Grill the zucchini and green onions on a grill pan until striped and slightly softened.",
             "pl": "Smaż cukinię i zieloną cebulkę na patelni grillowej, aż powstaną paski i lekko zmiękną."
            },
            {
             "uk": "Персики розріжте, видаліть кісточки та коротко підрум’яньте на грилі з боку зрізу.",
             "en": "Cut peaches, remove pits, and briefly brown them on the grill cut side down.",
             "pl": "Przekrój brzoskwinie, usuń pestki i krótko zrumień na grillu od strony cięcia."
            },
            {
             "uk": "Листя салату порвіть, помідори чері розріжте навпіл, базилік залиште листочками.",
             "en": "Tear the lettuce leaves, cut cherry tomatoes in half, and leave basil leaves whole.",
             "pl": "Porwij liście sałaty, pomidorki cherry przekrój na pół, pozostaw listki bazylii w całości."
            },
            {
             "uk": "Змішайте всі інгредієнти, додайте лимонний сік, оливкову олію, сіль і перець. Зверху розкришіть Фету.",
             "en": "Mix all ingredients, add lemon juice, olive oil, salt, and pepper. Crumble Feta on top.",
             "pl": "Wymieszaj wszystkie składniki, dodaj sok z cytryny, oliwę z oliwek, sól i pieprz. Na wierzchu pokrusz Fetę."
            }
        ]
    },
    {
        "title": "Салат з броколі, беконом та томатами",
        "title_en": "Broccoli, bacon and tomato salad",
        "title_pl": "Sałatka z brokułami, boczkiem i pomidorami",
        "description": "Холодний салат із бланшованої броколі, бекону, томатів, зеленої цибулі та гірчичної заправки.",
        "description_en": "Cold salad of blanched broccoli, bacon, tomatoes, green onions, and mustard dressing.",
        "description_pl": "Zimna sałatka z blanszowanych brokułów, boczku, pomidorów, zielonej cebulki i sosu musztardowego.",
        "source": "Джеймі Олівер",
        "source_en": "Jamie Oliver",
        "source_pl": "Jamiego Olivera",
        "cooking_time": 25,
        "portions": 6,
        "calories": 195,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.AMERICAN],
        "meal_times": [MealTime.LUNCH, MealTime.SNACK],
        "dietary_tags": [Diet.TRADITIONAL, Diet.GLUTEN_FREE, Diet.LACTOSE_FREE],
        "dish_types": [DishType.SALAD, DishType.COLD_SNACK, DishType.GARNISH],
        "ingredients": [
            ("Броколі", 600, UnitChoice.G),
            ("Бекон", 120, UnitChoice.G),
            ("Оливкова олія", 60, UnitChoice.ML),
            ("Помідор", 300, UnitChoice.G),
            ("Цибуля зелена", 15, UnitChoice.G),
            ("Часник", 1, UnitChoice.CLOVE),
            ("Гірчиця", 10, UnitChoice.G),
            ("Лимонний сік", 30, UnitChoice.ML),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Броколі розділіть на дрібні суцвіття, стебло очистіть і наріжте тонко.",
             "en": "Divide the broccoli into small florets, peel the stem and slice thinly.",
             "pl": "Podziel brokuły na małe różyczki, łodygę obierz i cienko pokrój."
            },
            {
             "uk": "Бланшуйте броколі 1–2 хвилини, охолодіть у холодній воді та добре обсушіть.",
             "en": "Blanch the broccoli for 1-2 minutes, cool in cold water, and dry well.",
             "pl": "Blanszuj brokuły przez 1-2 minuty, ostudź w zimnej wodzie i dobrze osusz."
            },
            {
             "uk": "Бекон наріжте і обсмажте до хрускоту, потім викладіть на паперовий рушник.",
             "en": "Chop the bacon and fry until crispy, then place on a paper towel.",
             "pl": "Boczek pokrój i usmaż na chrupko, następnie przełóż na ręcznik papierowy."
            },
            {
             "uk": "Помідор наріжте шматками, зелену цибулю подрібніть. Для заправки змішайте оливкову олію, лимонний сік, гірчицю, часник, сіль і перець.",
             "en": "Cut the tomato into pieces, chop the green onion. For the dressing, mix olive oil, lemon juice, mustard, garlic, salt, and pepper.",
             "pl": "Pomidora pokrój na kawałki, posiekaj zieloną cebulkę. Do sosu wymieszaj oliwę z oliwek, sok z cytryny, musztardę, czosnek, sól i pieprz."
            },
            {
             "uk": "Змішайте броколі, помідор, бекон і заправку. Перед подачею посипте зеленою цибулею.",
             "en": "Toss the broccoli, tomato, bacon, and dressing. Sprinkle with green onions before serving.",
             "pl": "Wymieszaj brokuły, pomidora, boczek i sos. Przed podaniem posyp zieloną cebulką."
            }
        ]
    },
    {
        "title": "Гаряча закуска з броколі, часником та мигдалем",
        "title_en": "Hot appetizer with broccoli, garlic and almonds",
        "title_pl": "Gorąca przekąska z brokułami, czosnkiem i migdałami",
        "description": "Броколі швидко обсмажується з часником, мигдалем, лимонним соком і оливковою олією.",
        "description_en": "Broccoli is quickly fried with garlic, almonds, lemon juice, and olive oil.",
        "description_pl": "Brokuły są szybko smażone z czosnkiem, migdałami, sokiem z cytryny i oliwą z oliwek.",
        "source": "K33 Kitchen",
        "source_en": "K33 Kitchen",
        "source_pl": "K33 Kitchen",
        "cooking_time": 15,
        "portions": 2,
        "calories": 160,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.EUROPEAN],
        "meal_times": [MealTime.LUNCH, MealTime.SNACK],
        "dietary_tags": [Diet.VEGAN, Diet.GLUTEN_FREE, Diet.LACTOSE_FREE],
        "dish_types": [DishType.HOT_SNACK, DishType.GARNISH],
        "ingredients": [
            ("Броколі", 200, UnitChoice.G),
            ("Мигдаль", 15, UnitChoice.G),
            ("Часник", 1, UnitChoice.CLOVE),
            ("Лимонний сік", 5, UnitChoice.ML),
            ("Оливкова олія", 30, UnitChoice.ML),
            ("Сіль", 1, UnitChoice.G),
            ("Перець чорний", 1, UnitChoice.G),
        ],
        "steps": [
            {
             "uk": "Броколі промийте, розділіть на невеликі суцвіття, стебла наріжте тонко.",
             "en": "Wash the broccoli, divide into small florets, slice the stems thinly.",
             "pl": "Brokuły umyj, podziel na małe różyczki, łodygi pokrój w cienkie plasterki."
            },
            {
             "uk": "Відваріть броколі 2–3 хвилини у підсоленій воді, охолодіть і добре відцідіть.",
             "en": "Boil the broccoli for 2-3 minutes in salted water, cool, and drain well.",
             "pl": "Gotuj brokuły 2-3 minuty w osolonej wodzie, ostudź i dobrze odcedź."
            },
            {
             "uk": "На сковороді розігрійте оливкову олію, додайте тонко нарізаний часник і готуйте до легкого аромату.",
             "en": "Heat olive oil in a pan, add thinly sliced garlic, and cook until slightly fragrant.",
             "pl": "Na patelni rozgrzej oliwę z oliwek, dodaj cienko pokrojony czosnek i gotuj do uzyskania delikatnego aromatu."
            },
            {
             "uk": "Додайте броколі та мигдаль, обсмажуйте 3–4 хвилини, постійно перемішуючи.",
             "en": "Add broccoli and almonds, fry for 3-4 minutes, stirring constantly.",
             "pl": "Dodaj brokuły i migdały, smaż 3-4 minuty, ciągle mieszając."
            },
            {
             "uk": "Приправте лимонним соком, сіллю та чорним перцем. Подавайте гарячою.",
             "en": "Season with lemon juice, salt, and black pepper. Serve hot.",
             "pl": "Dopraw sokiem z cytryny, solą i czarnym pieprzem. Podawaj na gorąco."
            }
        ]
    },
    {
        "title": "Марокканський омлет з лісовими грибами",
        "title_en": "Moroccan omelet with wild mushrooms",
        "title_pl": "Marokański omlet z leśnymi grzybami",
        "description": "Ніжний омлет із лісовими грибами, вершковим маслом і плавким сиром. Підходить для ситного сніданку.",
        "description_en": "A delicate omelet with wild mushrooms, butter, and melting cheese. Perfect for a hearty breakfast.",
        "description_pl": "Delikatny omlet z grzybami leśnymi, masłem i topiącym się serem. Odpowiedni na sycące śniadanie.",
        "source": "Гордон Рамзі",
        "source_en": "Gordon Ramsay",
        "source_pl": "Gordona Ramsaya",
        "cooking_time": 15,
        "portions": 1,
        "calories": 410,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.FRENCH, Cuisine.AUTHOR],
        "meal_times": [MealTime.BREAKFAST],
        "dietary_tags": [Diet.VEGETARIAN, Diet.GLUTEN_FREE],
        "dish_types": [DishType.OMELET],
        "ingredients": [
            ("Яйця", 3, UnitChoice.PCS),
            ("Вершкове масло", 15, UnitChoice.G),
            ("Білі гриби", 50, UnitChoice.G),
            ("Гауда", 30, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
            ("Оливкова олія", 15, UnitChoice.ML),
        ],
        "steps": [
            {
             "uk": "Білі гриби очистіть, наріжте та швидко обсмажте на оливковій олії до рум’яності.",
             "en": "Clean and slice the porcini mushrooms, then quickly sauté in olive oil until golden brown.",
             "pl": "Oczyść prawdziwki, pokrój je i szybko usmaż na oliwie z oliwek, aż się zarumienią."
            },
            {
             "uk": "Яйця збийте з сіллю та чорним перцем до однорідності.",
             "en": "Beat the eggs with salt and black pepper until smooth.",
             "pl": "Ubij jajka z solą i czarnym pieprzem do gładkości."
            },
            {
             "uk": "На чистій сковороді розтопіть вершкове масло на середньому вогні.",
             "en": "Melt butter in a clean pan over medium heat.",
             "pl": "Na czystej patelni roztop masło na średnim ogniu."
            },
            {
             "uk": "Влийте яйця і постійно зсувайте масу від країв до центру, щоб омлет залишався ніжним.",
             "en": "Pour in the eggs and constantly push the mixture from the edges to the center so the omelet remains tender.",
             "pl": "Wlej jajka i ciągle przesuwaj masę od brzegów do środka, aby omlet pozostał delikatny."
            },
            {
             "uk": "Коли верх ще трохи вологий, додайте гриби та Гауду, згорніть омлет і подавайте.",
             "en": "When the top is still slightly wet, add mushrooms and Gouda, fold the omelet, and serve.",
             "pl": "Kiedy góra jest jeszcze lekko wilgotna, dodaj grzyby i Goudę, złóż omlet i podawaj."
            }
        ]
    }
]