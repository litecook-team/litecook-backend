from recipes.models.recipe import Difficulty, MealTime, Diet, DishType, Cuisine, UnitChoice

# Формат даних для рецептів
RECIPES_DATA_6 = [
    {
        "title": "Пудинг з насіння чіа та свіжими ягодами",
        "title_en": "Chia seed pudding with fresh berries",
        "title_pl": "Pudding z nasion chia ze świeżymi jagodami",
        "description": "Легкий десерт на основі мигдального молока та насіння чіа, підсолоджений медом і прикрашений свіжими ягодами. Відмінно підходить для корисного сніданку або легкого перекусу.",
        "description_en": "A light dessert based on almond milk and chia seeds, sweetened with honey and decorated with fresh berries. Great for a healthy breakfast or a light snack.",
        "description_pl": "Lekki deser na bazie mleka migdałowego i nasion chia, słodzony miodem i udekorowany świeżymi owocami. Doskonały na zdrowe śniadanie lub lekką przekąskę.",
        "source": "Jeanine Donofrio, Phoebe Moore",
        "source_en": "Jeanine Donofrio, Phoebe Moore",
        "source_pl": "Jeanine Donofrio, Phoebe Moore",
        "cooking_time": 15,
        "portions": 2,
        "calories": 210,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.AUTHOR, Cuisine.INTERNATIONAL],
        "meal_times": [MealTime.BREAKFAST, MealTime.SNACK],
        "dietary_tags": [Diet.GLUTEN_FREE, Diet.LACTOSE_FREE],
        "dish_types": [DishType.DESSERT],
        "ingredients": [
            ("Насіння чіа", 50, UnitChoice.G),
            ("Мигдальне молоко", 240, UnitChoice.ML),
            ("Мед", 30, UnitChoice.G),
            ("Чорниця", 50, UnitChoice.G),
            ("Полуниця", 50, UnitChoice.G),
        ],
        "steps": [
            {"uk": "У скляній банці або глибокій мисці змішайте насіння чіа, мигдальне молоко та мед.",
             "en": "In a glass jar or deep bowl, mix the chia seeds, almond milk, and honey.",
             "pl": "W szklanym słoiku lub głębokiej misce wymieszaj nasiona chia, mleko migdałowe i miód."},
            {"uk": "Добре перемішайте ложкою, щоб насіння не злипалося в грудочки.",
             "en": "Mix well with a spoon so the seeds do not stick together in clumps.",
             "pl": "Dobrze wymieszaj łyżką, aby nasiona nie sklejały się w grudki."},
            {"uk": "Залиште постояти 10 хвилин, а потім ще раз ретельно перемішайте.",
             "en": "Let it sit for 10 minutes, then mix thoroughly again.",
             "pl": "Odstaw na 10 minut, a następnie jeszcze raz dokładnie wymieszaj."},
            {"uk": "Накрийте банку кришкою і поставте в холодильник мінімум на 2 години, щоб маса загусла.",
             "en": "Cover the jar with a lid and place in the refrigerator for at least 2 hours so the mixture thickens.",
             "pl": "Przykryj słoik pokrywką i wstaw do lodówki na co najmniej 2 godziny, aby masa zgęstniała."},
            {"uk": "Перед подачею прикрасьте пудинг свіжими ягодами полуниці та чорниці.",
             "en": "Before serving, garnish the pudding with fresh strawberries and blueberries.",
             "pl": "Przed podaniem udekoruj pudding świeżymi truskawkami i jagodami."}
        ]
    },
    {
        "title": "Желе зі свіжої малини",
        "title_en": "Fresh raspberry jelly",
        "title_pl": "Galaretka ze świeżych malin",
        "description": "Прозорий і легкий ягідний десерт із свіжої малини та лимонного соку на основі желатину. Освіжаючий варіант для літнього перекусу або післяобіднього десерту.",
        "description_en": "A clear and light berry dessert made from fresh raspberries and lemon juice based on gelatin. A refreshing option for a summer snack or afternoon dessert.",
        "description_pl": "Przezroczysty i lekki deser jagodowy ze świeżych malin i soku z cytryny na bazie żelatyny. Orzeźwiająca opcja na letnią przekąskę lub popołudniowy deser.",
        "source": "Miriam Nice",
        "source_en": "Miriam Nice",
        "source_pl": "Miriam Nice",
        "cooking_time": 20,
        "portions": 4,
        "calories": 140,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.BRITISH, Cuisine.EUROPEAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER, MealTime.SNACK],
        "dietary_tags": [Diet.TRADITIONAL, Diet.LACTOSE_FREE, Diet.GLUTEN_FREE],
        "dish_types": [DishType.DESSERT],
        "ingredients": [
            ("Малина", 500, UnitChoice.G),
            ("Цукор", 140, UnitChoice.G),
            ("Желатин", 12, UnitChoice.G),
            ("Вода", 300, UnitChoice.ML),
            ("Лимонний сік", 15, UnitChoice.ML),
            ("Рослинна олія", 2, UnitChoice.ML),
        ],
        "steps": [
            {
                "uk": "Замочіть 12 г порошкового желатину у 50–60 мл холодної води на 10–15 хвилин, щоб він набух. Злегка змастіть форму для желе олією.",
                "en": "Soak 12 g of powdered gelatin in 50-60 ml of cold water for 10-15 minutes so it swells. Lightly grease a jelly mold with oil.",
                "pl": "Namocz 12 g żelatyny w proszku w 50-60 ml zimnej wody przez 10-15 minut, aby napęczniała. Lekko nasmaruj formę do galaretki olejem."},
            {"uk": "У каструлю налийте 300 мл води, додайте цукор і нагрійте до його розчинення.",
             "en": "Pour 300 ml of water into a saucepan, add sugar, and heat until dissolved.",
             "pl": "Wlej 300 ml wody do rondla, dodaj cukier i podgrzewaj do jego rozpuszczenia."},
            {"uk": "Додайте малину, доведіть до кипіння і поваріть 5 хвилин на слабкому вогні.",
             "en": "Add raspberries, bring to a boil, and simmer for 5 minutes over low heat.",
             "pl": "Dodaj maliny, doprowadź do wrzenia i gotuj na małym ogniu przez 5 minut."},
            {"uk": "Протріть ягідну масу через сито, щоб позбутися кісточок. Влийте лимонний сік.",
             "en": "Push the berry mixture through a sieve to remove the seeds. Stir in the lemon juice.",
             "pl": "Przetrzyj masę jagodową przez sito, aby pozbyć się pestek. Wlej sok z cytryny."},
            {
                "uk": "Додайте набухлий желатин у гарячий малиновий сироп, але не кип’ятіть. Перемішайте до повного розчинення, розлийте у форми і поставте в холодильник на ніч.",
                "en": "Add the swollen gelatin to the hot raspberry syrup, but do not boil. Stir until completely dissolved, pour into molds, and refrigerate overnight.",
                "pl": "Dodaj napęczniałą żelatynę do gorącego syropu malinowego, ale nie gotuj. Wymieszaj do całkowitego rozpuszczenia, rozlej do foremek i wstaw do lodówki na noc."}
        ]
    },
    {
        "title": "Лосось аль форно з картоплею та фенхелем",
        "title_en": "Salmon al forno with potatoes and fennel",
        "title_pl": "Łosoś al forno z ziemniakami i koprem włoskim",
        "description": "Запечений лосось з картоплею, фенхелем, зеленню та лимоном. Ситна і збалансована страва для обіду або вечері.",
        "description_en": "Baked salmon with potatoes, fennel, greens, and lemon. A hearty and balanced dish for lunch or dinner.",
        "description_pl": "Pieczony łosoś z ziemniakami, koprem włoskim, zieleniną i cytryną. Sycące i zbilansowane danie na obiad lub kolację.",
        "source": "Джеймі Олівер",
        "source_en": "Jamie Oliver",
        "source_pl": "Jamiego Olivera",
        "cooking_time": 70,
        "portions": 4,
        "calories": 480,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.ITALIAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET, Diet.GLUTEN_FREE],
        "dish_types": [DishType.MAIN, DishType.FISH],
        "ingredients": [
            ("Картопля", 600, UnitChoice.G),
            ("Фенхель", 250, UnitChoice.G),
            ("Філе лосося", 480, UnitChoice.G),
            ("Петрушка", 15, UnitChoice.G),
            ("Часник", 2, UnitChoice.CLOVE),
            ("Вершкове масло", 15, UnitChoice.G),
            ("М'ята", 5, UnitChoice.G),
            ("Пармезан", 30, UnitChoice.G),
            ("Лимон", 1, UnitChoice.PCS),
            ("Оливкова олія", 30, UnitChoice.ML),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Розігрійте духовку до 220°C. Картоплю розріжте навпіл, фенхель наріжте великими сегментами.",
             "en": "Preheat the oven to 220°C. Cut the potatoes in half, and slice the fennel into large segments.",
             "pl": "Rozgrzej piekarnik do 220°C. Ziemniaki przekrój na pół, a koper włoski pokrój na duże kawałki."
            },
            {
             "uk": "Проваріть картоплю та фенхель у підсоленій воді 6 хвилин, відкиньте на друшляк і дайте волозі випаруватися.",
             "en": "Boil the potatoes and fennel in salted water for 6 minutes, drain in a colander, and let the moisture evaporate.",
             "pl": "Gotuj ziemniaki i koper włoski w osolonej wodzie przez 6 minut, odcedź na durszlaku i pozwól wilgoci odparować."
            },
            {
             "uk": "Викладіть овочі на деко, додайте олію, масло, сіль, перець, часник і частину петрушки. Запікайте 30 хвилин.",
             "en": "Place the vegetables on a baking sheet, add oil, butter, salt, pepper, garlic, and some of the parsley. Bake for 30 minutes.",
             "pl": "Wyłóż warzywa na blachę do pieczenia, dodaj olej, masło, sól, pieprz, czosnek i część pietruszki. Piecz przez 30 minut."
            },
            {
             "uk": "Філе лосося натріть сіллю і перцем, додайте м'яту та петрушку. Викладіть рибу на овочі, посипте Пармезаном і цедрою лимона.",
             "en": "Rub the salmon fillet with salt and pepper, add mint and parsley. Place the fish on top of the vegetables, sprinkle with Parmesan and lemon zest.",
             "pl": "Natrzyj filet z łososia solą i pieprzem, dodaj miętę i pietruszkę. Ułóż rybę na warzywach, posyp parmezanem i skórką z cytryny."
            },
            {
             "uk": "Запікайте ще 15 хвилин до готовності риби. Перед подачею збризніть лимонним соком.",
             "en": "Bake for another 15 minutes until the fish is cooked. Drizzle with lemon juice before serving.",
             "pl": "Piecz jeszcze przez 15 minut, aż ryba będzie gotowa. Przed podaniem skrop sokiem z cytryny."
            }
        ]
    },
    {
        "title": "Запечений лосось з фенхелем та перепелиними яйцями",
        "title_en": "Baked salmon with fennel and quail eggs",
        "title_pl": "Pieczony łosoś z koprem włoskim i jajkami przepiórczymi",
        "description": "Запечений лосось із м’яким вершковим соусом, хроном, кропом і перепелиними яйцями. Добре підходить для святкової вечері.",
        "description_en": "Baked salmon with a soft cream sauce, horseradish, dill, and quail eggs. Well suited for a festive dinner.",
        "description_pl": "Pieczony łosoś z łagodnym sosem śmietanowym, chrzanem, koperkiem i jajkami przepiórczymi. Świetnie nadaje się na uroczystą kolację.",
        "source": "Джеймі Олівер",
        "source_en": "Jamie Oliver",
        "source_pl": "Jamiego Olivera",
        "cooking_time": 45,
        "portions": 8,
        "calories": 420,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.BRITISH, Cuisine.EUROPEAN],
        "meal_times": [MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET, Diet.GLUTEN_FREE],
        "dish_types": [DishType.MAIN, DishType.FISH, DishType.FESTIVE],
        "ingredients": [
            ("Фенхель (насіння)", 10, UnitChoice.G),
            ("Філе лосося", 1000, UnitChoice.G),
            ("Лимон", 1, UnitChoice.PCS),
            ("Сметана", 120, UnitChoice.G),
            ("Хрін", 45, UnitChoice.G),
            ("Оливкова олія", 30, UnitChoice.ML),
            ("Перепелині яйця", 16, UnitChoice.PCS),
            ("Крес-салат", 60, UnitChoice.G),
            ("Кріп", 10, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Розігрійте духовку до 180°C. Розітріть фенхель (насіння) із сіллю та чорним перцем.",
             "en": "Preheat the oven to 180°C. Crush the fennel seeds with salt and black pepper.",
             "pl": "Rozgrzej piekarnik do 180°C. Rozgnieć nasiona kopru włoskiego z solą i czarnym pieprzem."
            },
            {
             "uk": "Покладіть філе лосося шкіркою донизу у форму та рівномірно посипте пряною сумішшю.",
             "en": "Place the salmon fillet skin-side down in a dish and sprinkle evenly with the spice mixture.",
             "pl": "Połóż filet z łososia skórą do dołu w naczyniu i równomiernie posyp mieszanką przypraw."
            },
            {
             "uk": "Запікайте 15–20 хвилин, поки риба стане готовою, але залишиться соковитою.",
             "en": "Bake for 15-20 minutes until the fish is cooked but remains juicy.",
             "pl": "Piecz 15-20 minut, aż ryba będzie gotowa, ale pozostanie soczysta."
            },
            {
             "uk": "Перепелині яйця відваріть 2 хвилини, охолодіть і очистіть. Для соусу змішайте сметану, хрін, лимонний сік, оливкову олію, сіль і перець.",
             "en": "Boil quail eggs for 2 minutes, cool, and peel. For the sauce, mix sour cream, horseradish, lemon juice, olive oil, salt, and pepper.",
             "pl": "Gotuj jajka przepiórcze przez 2 minuty, ostudź i obierz. Do sosu wymieszaj śmietanę, chrzan, sok z cytryny, oliwę z oliwek, sól i pieprz."
            },
            {
             "uk": "Подавайте лосось шматками з крес-салатом, яйцями, кропом і соусом.",
             "en": "Serve the salmon in pieces with watercress, eggs, dill, and sauce.",
             "pl": "Podawaj łososia w kawałkach z rzeżuchą, jajkami, koperkiem i sosem."
            }
        ]
    },
    {
        "title": "Смажений лосось з часниковим маслом та чебрецем",
        "title_en": "Pan-fried salmon with garlic butter and thyme",
        "title_pl": "Smażony łosoś z masłem czosnkowym i tymiankiem",
        "description": "Філе лосося швидко обсмажується на сковороді з вершковим маслом, часником, чебрецем і лимоном.",
        "description_en": "Salmon fillet is quickly pan-fried with butter, garlic, thyme, and lemon.",
        "description_pl": "Filet z łososia jest szybko smażony na patelni z masłem, czosnkiem, tymiankiem i cytryną.",
        "source": "Гордон Рамзі",
        "source_en": "Gordon Ramsay",
        "source_pl": "Gordona Ramsaya",
        "cooking_time": 15,
        "portions": 2,
        "calories": 430,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.FRENCH, Cuisine.AMERICAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET, Diet.GLUTEN_FREE],
        "dish_types": [DishType.MAIN, DishType.FISH],
        "ingredients": [
            ("Філе лосося", 300, UnitChoice.G),
            ("Вершкове масло", 45, UnitChoice.G),
            ("Часник", 4, UnitChoice.CLOVE),
            ("Чебрець", 5, UnitChoice.G),
            ("Лимон", 1, UnitChoice.PCS),
            ("Оливкова олія", 15, UnitChoice.ML),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
            ("Петрушка", 10, UnitChoice.G),
        ],
        "steps": [
            {
             "uk": "Філе лосося обсушіть, посоліть і поперчіть з обох боків.",
             "en": "Pat the salmon fillet dry, season with salt and pepper on both sides.",
             "pl": "Osusz filet z łososia, dopraw solą i pieprzem z obu stron."
            },
            {
             "uk": "Розігрійте оливкову олію на сковороді. Викладіть лосось шкіркою донизу та смажте 2 хвилини.",
             "en": "Heat olive oil in a pan. Place the salmon skin-side down and fry for 2 minutes.",
             "pl": "Rozgrzej oliwę na patelni. Połóż łososia skórą do dołu i smaż przez 2 minuty."
            },
            {
             "uk": "Переверніть рибу, швидко підрум’яньте другий бік і знову поверніть шкіркою донизу.",
             "en": "Flip the fish, quickly brown the other side, and turn it skin-side down again.",
             "pl": "Odwróć rybę, szybko zrumień drugą stronę i ponownie połóż skórą do dołu."
            },
            {
             "uk": "Додайте вершкове масло, часник і чебрець. Готуйте 4–5 хвилин, поливаючи рибу ароматним маслом.",
             "en": "Add butter, garlic, and thyme. Cook for 4-5 minutes, basting the fish with the aromatic butter.",
             "pl": "Dodaj masło, czosnek i tymianek. Gotuj przez 4-5 minut, polewając rybę aromatycznym masłem."
            },
            {
             "uk": "Додайте лимонний сік, зніміть з вогню та подавайте з петрушкою.",
             "en": "Add lemon juice, remove from heat, and serve with parsley.",
             "pl": "Dodaj sok z cytryny, zdejmij z ognia i podawaj z pietruszką."
            }
        ]
    },
    {
        "title": "Запечений лосось у фользі з лимоном та травами",
        "title_en": "Baked salmon in foil with lemon and herbs",
        "title_pl": "Pieczony łosoś w folii z cytryną i ziołami",
        "description": "Цілий лосось запікається у фользі з лимоном, часником, лавровим листом і свіжими травами. Страва підходить для великої компанії.",
        "description_en": "A whole salmon is baked in foil with lemon, garlic, bay leaf, and fresh herbs. The dish is suitable for a large group.",
        "description_pl": "Cały łosoś pieczony jest w folii z cytryną, czosnkiem, liściem laurowym i świeżymi ziołami. Danie idealne dla większej grupy.",
        "source": "Гордон Рамзі",
        "source_en": "Gordon Ramsay",
        "source_pl": "Gordona Ramsaya",
        "cooking_time": 60,
        "portions": 8,
        "calories": 520,
        "difficulty": Difficulty.HARD,
        "cuisine": [Cuisine.EUROPEAN],
        "meal_times": [MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET, Diet.GLUTEN_FREE],
        "dish_types": [DishType.MAIN, DishType.FISH, DishType.FESTIVE],
        "ingredients": [
            ("Лосось", 1600, UnitChoice.G),
            ("Оливкова олія", 40, UnitChoice.ML),
            ("Лимон", 3, UnitChoice.PCS),
            ("Лавровий лист", 2, UnitChoice.PCS),
            ("Розмарин", 5, UnitChoice.G),
            ("Чебрець", 5, UnitChoice.G),
            ("Базилік", 5, UnitChoice.G),
            ("Петрушка", 5, UnitChoice.G),
            ("Часник", 40, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Розігрійте духовку до 200°C. Цілого лосося промийте, обсушіть і натріть сіллю та перцем.",
             "en": "Preheat the oven to 200°C. Wash the whole salmon, pat dry, and rub with salt and pepper.",
             "pl": "Rozgrzej piekarnik do 200°C. Umyj całego łososia, osusz i natrzyj solą oraz pieprzem."
            },
            {
             "uk": "Лимони наріжте кружальцями і коротко підрум’яньте на сковороді з невеликою кількістю оливкової олії.",
             "en": "Slice the lemons into rounds and quickly brown them in a pan with a little olive oil.",
             "pl": "Cytryny pokrój w plasterki i krótko zrumień na patelni z odrobiną oliwy z oliwek."
            },
            {
             "uk": "На фольгу викладіть частину трав, часник і лавровий лист. Зверху покладіть рибу.",
             "en": "Place some of the herbs, garlic, and bay leaf on the foil. Place the fish on top.",
             "pl": "Rozłóż część ziół, czosnek i liść laurowy na folii. Na wierzchu połóż rybę."
            },
            {
             "uk": "У черевце лосося покладіть лимони та решту трав. Полийте олією і щільно загорніть у фольгу.",
             "en": "Stuff the salmon belly with lemons and the remaining herbs. Drizzle with oil and wrap tightly in foil.",
             "pl": "Do brzucha łososia włóż cytryny i resztę ziół. Skrop oliwą i szczelnie zawiń w folię."
            },
            {
             "uk": "Запікайте 35–40 хвилин. Обережно розгорніть фольгу і подавайте рибу з соками, що утворилися.",
             "en": "Bake for 35-40 minutes. Carefully unwrap the foil and serve the fish with its juices.",
             "pl": "Piecz 35-40 minut. Ostrożnie rozwiń folię i podawaj rybę z powstałymi sokami."
            }
        ]
    },
    {
        "title": "Липка лимонна курка",
        "title_en": "Sticky lemon chicken",
        "title_pl": "Lepki kurczak cytrynowy",
        "description": "Курячі ніжки готуються у густій глазурі з меду, соєвого соусу, часнику та лимона. Швидка страва з яскравим смаком.",
        "description_en": "Chicken legs are cooked in a thick glaze of honey, soy sauce, garlic, and lemon. A quick dish with a bright flavor.",
        "description_pl": "Udka z kurczaka przygotowywane są w gęstej glazurze z miodu, sosu sojowego, czosnku i cytryny. Szybkie danie o wyrazistym smaku.",
        "source": "Гордон Рамзі",
        "source_en": "Gordon Ramsay",
        "source_pl": "Gordona Ramsaya",
        "cooking_time": 30,
        "portions": 4,
        "calories": 480,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.ASIAN, Cuisine.BRITISH],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.LACTOSE_FREE],
        "dish_types": [DishType.MAIN, DishType.MEAT],
        "ingredients": [
            ("Курячі ніжки", 800, UnitChoice.G),
            ("Оливкова олія", 45, UnitChoice.ML),
            ("Соєвий соус", 30, UnitChoice.ML),
            ("Мед", 60, UnitChoice.G),
            ("Часник", 40, UnitChoice.G),
            ("Лимон", 1, UnitChoice.PCS),
            ("Вода", 80, UnitChoice.ML),
            ("Чебрець", 5, UnitChoice.G),
            ("Петрушка", 30, UnitChoice.G),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Курячі ніжки посоліть, поперчіть і обсмажте на оливковій олії до золотистої скоринки.",
             "en": "Season the chicken legs with salt and pepper, and fry in olive oil until a golden crust forms.",
             "pl": "Udka z kurczaka posól, popieprz i usmaż na oliwie z oliwek, aż powstanie złocista skórka."
            },
            {
             "uk": "Додайте часник, соєвий соус і мед. Перемішайте, щоб курка покрилася глазур’ю.",
             "en": "Add garlic, soy sauce, and honey. Stir so the chicken is coated in the glaze.",
             "pl": "Dodaj czosnek, sos sojowy i miód. Wymieszaj, aby kurczak pokrył się glazurą."
            },
            {
             "uk": "Влийте воду, додайте скибочки лимона, накрийте кришкою і тушкуйте 10–15 хвилин.",
             "en": "Pour in water, add lemon slices, cover with a lid, and simmer for 10-15 minutes.",
             "pl": "Wlej wodę, dodaj plasterki cytryny, przykryj pokrywką i duś przez 10-15 minut."
            },
            {
             "uk": "Зніміть кришку та уваріть соус до густої липкої консистенції, перевертаючи курку.",
             "en": "Remove the lid and reduce the sauce until it has a thick, sticky consistency, turning the chicken.",
             "pl": "Zdejmij pokrywkę i zredukuj sos, aż uzyskasz gęstą, lepką konsystencję, obracając kurczaka."
            },
            {
             "uk": "Додайте чебрець і петрушку. Подавайте курку гарячою з соусом зі сковороди.",
             "en": "Add thyme and parsley. Serve the chicken hot with the pan sauce.",
             "pl": "Dodaj tymianek i pietruszkę. Podawaj kurczaka na gorąco z sosem z patelni."
            }
        ]
    },
    {
        "title": "Курячі стегна з беконом у лимонному бульйоні",
        "title_en": "Chicken thighs with bacon in lemon broth",
        "title_pl": "Udka z kurczaka z boczkiem w bulionie cytrynowym",
        "description": "Курячі стегна запікаються з беконом, цибулею, часником, лимоном і травами. Страва виходить ситною та ароматною.",
        "description_en": "Chicken thighs are baked with bacon, onions, garlic, lemon, and herbs. The dish turns out hearty and aromatic.",
        "description_pl": "Udka z kurczaka pieczone z boczkiem, cebulą, czosnkiem, cytryną i ziołami. Danie jest sycące i aromatyczne.",
        "source": "Гордон Рамзі",
        "source_en": "Gordon Ramsay",
        "source_pl": "Gordona Ramsaya",
        "cooking_time": 40,
        "portions": 4,
        "calories": 560,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.BRITISH, Cuisine.AMERICAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.LACTOSE_FREE],
        "dish_types": [DishType.MAIN, DishType.MEAT],
        "ingredients": [
            ("Курячі стегна", 800, UnitChoice.G),
            ("Бекон", 100, UnitChoice.G),
            ("Цибуля ріпчаста", 100, UnitChoice.G),
            ("Часник", 3, UnitChoice.CLOVE),
            ("Лимон", 1, UnitChoice.PCS),
            ("Чебрець", 5, UnitChoice.G),
            ("Розмарин", 5, UnitChoice.G),
            ("Бульйон", 250, UnitChoice.ML),
            ("Лимонний сік", 30, UnitChoice.ML),
            ("Перець чилі", 2, UnitChoice.G),
            ("Оливкова олія", 15, UnitChoice.ML),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Бекон наріжте і обсмажте до хрускоту. Вийміть його, залишивши жир у сковороді.",
             "en": "Chop the bacon and fry until crispy. Remove it, leaving the fat in the pan.",
             "pl": "Pokrój boczek i usmaż na chrupko. Wyjmij go, zostawiając tłuszcz na patelni."
            },
            {
             "uk": "Курячі стегна посоліть, поперчіть і обсмажте шкіркою донизу до золотистої скоринки.",
             "en": "Season the chicken thighs with salt and pepper and fry skin-side down until golden brown.",
             "pl": "Posól i popieprz udka z kurczaka i smaż skórą do dołu, aż uzyskają złocistą skórkę."
            },
            {
             "uk": "Додайте цибулю, часник, лимон, чебрець і розмарин. Готуйте 2–3 хвилини.",
             "en": "Add the onion, garlic, lemon, thyme, and rosemary. Cook for 2-3 minutes.",
             "pl": "Dodaj cebulę, czosnek, cytrynę, tymianek i rozmaryn. Gotuj przez 2-3 minuty."
            },
            {
             "uk": "Влийте бульйон і лимонний сік, поверніть бекон, викладіть курку шкіркою догори та додайте чилі.",
             "en": "Pour in the broth and lemon juice, return the bacon, place the chicken skin-side up, and add chili.",
             "pl": "Wlej bulion i sok z cytryny, dodaj z powrotem boczek, ułóż kurczaka skórą do góry i dodaj chili."
            },
            {
             "uk": "Запікайте при 190°C близько 20 хвилин, поки курка буде готовою, а соус стане насиченим.",
             "en": "Bake at 190°C for about 20 minutes until the chicken is done and the sauce becomes rich.",
             "pl": "Piecz w 190°C przez około 20 minut, aż kurczak będzie gotowy, a sos stanie się gęsty."
            }
        ]
    },
    {
        "title": "Запечена курка з нутовою начинкою та салатом",
        "title_en": "Roast chicken with chickpea stuffing and salad",
        "title_pl": "Pieczony kurczak z nadzieniem z ciecierzycy i sałatką",
        "description": "Ціла курка запікається з начинкою з нуту, лимона, чилі та чебрецю. Подається із зеленим салатом і часниковою заправкою.",
        "description_en": "A whole chicken is roasted with a stuffing of chickpeas, lemon, chili, and thyme. Served with a green salad and garlic dressing.",
        "description_pl": "Cały kurczak pieczony z nadzieniem z ciecierzycy, cytryny, chili i tymianku. Podawany z zieloną sałatą i sosem czosnkowym.",
        "source": "Гордон Рамзі",
        "source_en": "Gordon Ramsay",
        "source_pl": "Gordona Ramsaya",
        "cooking_time": 90,
        "portions": 5,
        "calories": 650,
        "difficulty": Difficulty.HARD,
        "cuisine": [Cuisine.BRITISH],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.GLUTEN_FREE],
        "dish_types": [DishType.MAIN, DishType.MEAT, DishType.FESTIVE],
        "ingredients": [
            ("Курка ціла", 1500, UnitChoice.G),
            ("Нут", 400, UnitChoice.G),
            ("Перець чилі", 10, UnitChoice.G),
            ("Лимон", 1, UnitChoice.PCS),
            ("Чебрець", 10, UnitChoice.G),
            ("Оливкова олія", 40, UnitChoice.ML),
            ("Часник", 80, UnitChoice.G),
            ("Листя салату", 150, UnitChoice.G),
            ("Гірчиця", 10, UnitChoice.G),
            ("Лимонний сік", 15, UnitChoice.ML),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Розігрійте духовку до 200°C. Змішайте нут, подрібнений чилі, цедру лимона, чебрець, оливкову олію, сіль і перець.",
             "en": "Preheat the oven to 200°C. Mix the chickpeas, chopped chili, lemon zest, thyme, olive oil, salt, and pepper.",
             "pl": "Rozgrzej piekarnik do 200°C. Wymieszaj ciecierzycę, posiekane chili, skórkę z cytryny, tymianek, oliwę z oliwek, sól i pieprz."
            },
            {
             "uk": "Нафаршируйте курку нутовою сумішшю, а лимон покладіть біля отвору, щоб утримати начинку всередині.",
             "en": "Stuff the chicken with the chickpea mixture and place the lemon near the opening to keep the stuffing inside.",
             "pl": "Nafaszeruj kurczaka mieszanką z ciecierzycy, a cytrynę połóż w otworze, aby utrzymać farsz w środku."
            },
            {
             "uk": "Викладіть курку у форму, поруч покладіть розрізані головки часнику. Запікайте 60–75 хвилин.",
             "en": "Place the chicken in a roasting tin and put the halved garlic heads alongside. Roast for 60-75 minutes.",
             "pl": "Połóż kurczaka w brytfannie, obok połóż przecięte główki czosnku. Piecz 60-75 minut."
            },
            {
             "uk": "Вичавіть м’якоть запеченого часнику, змішайте її з лимонним соком, гірчицею та оливковою олією.",
             "en": "Squeeze out the flesh of the roasted garlic and mix it with lemon juice, mustard, and olive oil.",
             "pl": "Wyciśnij miąższ z upieczonego czosnku i wymieszaj go z sokiem z cytryny, musztardą i oliwą z oliwek."
            },
            {
             "uk": "Подавайте курку з нутовою начинкою і листям салату, заправленим часниково-лимонним соусом.",
             "en": "Serve the chicken with the chickpea stuffing and lettuce leaves dressed with the garlic-lemon sauce.",
             "pl": "Podawaj kurczaka z nadzieniem z ciecierzycy oraz liśćmi sałaty polanymi sosem czosnkowo-cytrynowym."
            }
        ]
    },
    {
        "title": "Паста з креветками, фенхелем та томатами",
        "title_en": "Pasta with shrimp, fennel, and tomatoes",
        "title_pl": "Makaron z krewetkami, koprem włoskim i pomidorami",
        "description": "Паста з креветками, фенхелем, томатами, руколою та лимоном. Легка основна страва з морським смаком.",
        "description_en": "Pasta with shrimp, fennel, tomatoes, arugula, and lemon. A light main dish with a seafood flavor.",
        "description_pl": "Makaron z krewetkami, koprem włoskim, pomidorami, rukolą i cytryną. Lekkie danie główne o smaku owoców morza.",
        "source": "Джеймі Олівер",
        "source_en": "Jamie Oliver",
        "source_pl": "Jamiego Olivera",
        "cooking_time": 40,
        "portions": 4,
        "calories": 450,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.ITALIAN, Cuisine.AUTHOR],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET],
        "dish_types": [DishType.MAIN, DishType.PASTA, DishType.SEAFOOD],
        "ingredients": [
            ("Креветки", 400, UnitChoice.G),
            ("Паста", 320, UnitChoice.G),
            ("Цибуля ріпчаста", 100, UnitChoice.G),
            ("Часник", 2, UnitChoice.CLOVE),
            ("Помідори чері", 200, UnitChoice.G),
            ("Томатна паста", 30, UnitChoice.G),
            ("Перець чилі", 10, UnitChoice.G),
            ("Фенхель", 150, UnitChoice.G),
            ("Рукола", 50, UnitChoice.G),
            ("Лимон", 1, UnitChoice.PCS),
            ("Оливкова олія", 30, UnitChoice.ML),
            ("Сіль", None, UnitChoice.TASTE),
            ("Перець чорний", None, UnitChoice.TASTE),
        ],
        "steps": [
            {
             "uk": "Відваріть пасту у підсоленій воді до стану al dente, збережіть трохи води від варіння.",
             "en": "Boil the pasta in salted water until al dente, saving some of the cooking water.",
             "pl": "Ugotuj makaron w osolonej wodzie al dente, zachowując trochę wody z gotowania."
            },
            {
             "uk": "Цибулю, часник, чилі та фенхель дрібно наріжте. Помідори чері розріжте навпіл.",
             "en": "Finely chop the onion, garlic, chili, and fennel. Halve the cherry tomatoes.",
             "pl": "Drobno posiekaj cebulę, czosnek, chili i koper włoski. Pomidorki cherry przekrój na pół."
            },
            {
             "uk": "На оливковій олії обсмажте цибулю, часник, чилі та фенхель до м’якості.",
             "en": "Sauté the onion, garlic, chili, and fennel in olive oil until soft.",
             "pl": "Na oliwie z oliwek podsmaż cebulę, czosnek, chili i koper włoski do miękkości."
            },
            {
             "uk": "Додайте креветки, помідори чері та томатну пасту. Готуйте кілька хвилин, доки креветки стануть готовими.",
             "en": "Add the shrimp, cherry tomatoes, and tomato paste. Cook for a few minutes until the shrimp are done.",
             "pl": "Dodaj krewetki, pomidorki cherry i koncentrat pomidorowy. Gotuj kilka minut, aż krewetki będą gotowe."
            },
            {
             "uk": "Змішайте соус із пастою, додайте трохи води від варіння, руколу та лимонний сік.",
             "en": "Mix the sauce with the pasta, add a splash of the cooking water, arugula, and lemon juice.",
             "pl": "Wymieszaj sos z makaronem, dodaj odrobinę wody z gotowania, rukolę i sok z cytryny."
            }
        ]
    },
]