from recipes.models.recipe import Difficulty, MealTime, Diet, DishType, Cuisine, UnitChoice

# Формат даних для рецептів
RECIPES_DATA_8 = [
    {
        "title": "Сирний омлет з раками та грибами",
        "title_en": "Cheese omelet with crawfish and mushrooms",
        "title_pl": "Serowy omlet z rakami i grzybami",
        "description": "Омлет із раками, грибами, шалотом, зеленою цибулею та сиром Гауда. Ситний варіант для бранчу.",
        "description_en": "Omelet with crawfish, mushrooms, shallots, green onions, and Gouda cheese. A hearty option for brunch.",
        "description_pl": "Omlet z rakami, grzybami, szalotką, zieloną cebulką i serem Gouda. Sycąca opcja na brunch.",
        "source": "Гордон Рамзі",
        "source_en": "Gordon Ramsay",
        "source_pl": "Gordona Ramsaya",
        "cooking_time": 20,
        "portions": 2,
        "calories": 520,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.AMERICAN],
        "meal_times": [MealTime.BREAKFAST, MealTime.SNACK],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET, Diet.GLUTEN_FREE],
        "dish_types": [DishType.OMELET, DishType.SEAFOOD],
        "ingredients": [
            ("Яйця", 4, UnitChoice.PCS),
            ("Цибуля шалот", 30, UnitChoice.G),
            ("Часник", 1, UnitChoice.CLOVE),
            ("Печериці", 60, UnitChoice.G),
            ("Раки", 150, UnitChoice.G),
            ("Перець чилі", 1, UnitChoice.G),
            ("Вершкове масло", 20, UnitChoice.G),
            ("Цибуля зелена", 20, UnitChoice.G),
            ("Гауда", 50, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Шалот наріжте тонко, часник подрібніть, печериці наріжте скибками.",
             "en": "Thinly slice the shallot, mince the garlic, and slice the mushrooms.",
             "pl": "Szalotkę pokrój w cienkie plasterki, posiekaj czosnek, a pieczarki pokrój w plastry."
            },
            {
             "uk": "На частині вершкового масла обсмажте печериці, шалот і часник до м’якості.",
             "en": "In some of the butter, sauté the mushrooms, shallot, and garlic until soft.",
             "pl": "Na części masła podsmaż pieczarki, szalotkę i czosnek do miękkości."
            },
            {
             "uk": "Додайте раки, чилі та зелену цибулю, коротко прогрійте і зніміть начинку з вогню.",
             "en": "Add the crawfish, chili, and green onions, heat briefly, and remove the filling from the heat.",
             "pl": "Dodaj raki, chili i zieloną cebulkę, krótko podgrzej i zdejmij farsz z ognia."
            },
            {
             "uk": "Яйця збийте з сіллю і перцем, вилийте на сковороду з рештою масла та готуйте до майже готового стану.",
             "en": "Beat the eggs with salt and pepper, pour into the pan with the remaining butter, and cook until almost set.",
             "pl": "Jajka ubij z solą i pieprzem, wylej na patelnię z resztą masła i smaż, aż będą prawie gotowe."
            },
            {
             "uk": "Викладіть начинку і Гауду на омлет, складіть його навпіл і подавайте гарячим.",
             "en": "Place the filling and Gouda on the omelet, fold it in half, and serve hot.",
             "pl": "Nałóż farsz i Goudę na omlet, złóż na pół i podawaj na gorąco."
            }
        ]
    },
    {
        "title": "Паста з запеченим камамбером та шпинатом",
        "title_en": "Pasta with baked camembert and spinach",
        "title_pl": "Makaron z pieczonym camembertem i szpinakiem",
        "description": "Паста змішується з розплавленим камамбером, часником, розмарином, шпинатом і Пармезаном. Проста вершкова вечеря.",
        "description_en": "Pasta is mixed with melted Camembert, garlic, rosemary, spinach, and Parmesan. A simple creamy dinner.",
        "description_pl": "Makaron miesza się z roztopionym camembertem, czosnkiem, rozmarynem, szpinakiem i parmezanem. Prosta kremowa kolacja.",
        "source": "Джеймі Олівер",
        "source_en": "Jamie Oliver",
        "source_pl": "Jamiego Olivera",
        "cooking_time": 30,
        "portions": 4,
        "calories": 680,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.EUROPEAN, Cuisine.ITALIAN],
        "meal_times": [MealTime.DINNER],
        "dietary_tags": [Diet.VEGETARIAN],
        "dish_types": [DishType.MAIN, DishType.PASTA],
        "ingredients": [
            ("Камамбер", 250, UnitChoice.G),
            ("Часник", 2, UnitChoice.CLOVE),
            ("Розмарин", 3, UnitChoice.G),
            ("Оливкова олія", 15, UnitChoice.ML),
            ("Паста", 450, UnitChoice.G),
            ("Шпинат", 150, UnitChoice.G),
            ("Пармезан", 100, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Розігрійте духовку до 180°C. Камамбер покладіть у дерев’яну коробочку або жароміцну форму.",
             "en": "Preheat the oven to 180°C. Place the Camembert in a wooden box or heatproof dish.",
             "pl": "Rozgrzej piekarnik do 180°C. Umieść camembert w drewnianym pudełku lub naczyniu żaroodpornym."
            },
            {
             "uk": "Зріжте верхню скоринку сиру, додайте часник, розмарин, чорний перець і оливкову олію.",
             "en": "Cut off the top rind of the cheese, add garlic, rosemary, black pepper, and olive oil.",
             "pl": "Odetnij górną skórkę sera, dodaj czosnek, rozmaryn, czarny pieprz i oliwę z oliwek."
            },
            {
             "uk": "Запікайте камамбер 20–25 хвилин, доки він повністю розплавиться.",
             "en": "Bake the Camembert for 20-25 minutes until it is completely melted.",
             "pl": "Piecz camembert przez 20-25 minut, aż całkowicie się rozpuści."
            },
            {
             "uk": "Паралельно відваріть пасту у підсоленій воді. За 10 секунд до готовності додайте шпинат, потім злийте воду, залишивши трохи рідини.",
             "en": "Meanwhile, boil the pasta in salted water. 10 seconds before it's done, add the spinach, then drain the water, reserving a little liquid.",
             "pl": "W międzyczasie ugotuj makaron w osolonej wodzie. Na 10 sekund przed gotowością dodaj szpinak, a następnie odcedź wodę, zostawiając odrobinę płynu."
            },
            {
             "uk": "Змішайте пасту і шпинат із розплавленим камамбером, Пармезаном і невеликою кількістю води від пасти.",
             "en": "Toss the pasta and spinach with the melted Camembert, Parmesan, and a splash of pasta water.",
             "pl": "Wymieszaj makaron i szpinak z roztopionym camembertem, parmezanem i odrobiną wody z makaronu."
            }
        ]
    }
]