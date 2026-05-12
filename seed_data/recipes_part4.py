from recipes.models.recipe import Difficulty, MealTime, Diet, DishType, Cuisine, UnitChoice

# Формат даних для рецептів
RECIPES_DATA_4 = [
    {
        "title": "Вершкова паста з лососем",
        "title_en": "Creamy salmon pasta",
        "title_pl": "Kremowy makaron z łososiem",
        "description": "Ніжна паста з лососем, вершковим соусом, кропом і лимонним соком. Ситна страва для обіду або вечері.",
        "description_en": "Tender pasta with salmon, cream sauce, dill, and lemon juice. A hearty dish for lunch or dinner.",
        "description_pl": "Delikatny makaron z łososiem, sosem śmietanowym, koperkiem i sokiem z cytryny. Sycące danie na obiad lub kolację.",
        "source": "Anna Glover",
        "source_en": "Anna Glover",
        "source_pl": "Anna Glover",
        "cooking_time": 30,
        "portions": 2,
        "calories": 580,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.ITALIAN, Cuisine.EUROPEAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET],
        "dish_types": [DishType.MAIN, DishType.FISH, DishType.PASTA],
        "ingredients": [
            ("Філе лосося", 300, UnitChoice.G),
            ("Паста", 175, UnitChoice.G),
            ("Вершки", 200, UnitChoice.ML),
            ("Цибуля ріпчаста", 50, UnitChoice.G),
            ("Часник", 5, UnitChoice.G),
            ("Лимонний сік", 15, UnitChoice.ML),
            ("Кріп", 10, UnitChoice.G),
            ("Оливкова олія", 15, UnitChoice.ML),
            ("Сіль", 2, UnitChoice.G),
        ],
        "steps": [
            {
                "uk": "Відваріть пасту в киплячій підсоленій воді. Злийте воду, обов'язково зберігши близько 50 мл крохмалистої рідини для соусу.",
                "en": "Boil the pasta in boiling salted water. Drain the water, being sure to save about 50 ml of starchy liquid for the sauce.",
                "pl": "Ugotuj makaron we wrzącej, osolonej wodzie. Odcedź, koniecznie zachowując około 50 ml płynu z gotowania do sosu."},
            {"uk": "Нагрійте оливкову олію у сковороді. Дрібно нарізану цибулю та часник пасеруйте до розм'якшення.",
             "en": "Heat olive oil in a pan. Sauté finely chopped onion and garlic until softened.",
             "pl": "Rozgrzej oliwę na patelni. Drobno posiekaną cebulę i czosnek smaż, aż zmiękną."},
            {"uk": "Залийте ароматичну базу вершками і доведіть до легкого кипіння.",
             "en": "Pour cream over the aromatic base and bring to a light simmer.",
             "pl": "Zalej aromatyczną bazę śmietanką i doprowadź do lekkiego wrzenia."},
            {"uk": "Занурте філе у киплячий соус. Готуйте 4-5 хвилин до зміни кольору риби на непрозорий рожевий.",
             "en": "Submerge the fillet into the boiling sauce. Cook 4-5 minutes until the fish turns opaque pink.",
             "pl": "Zanurz filet w gotującym się sosie. Gotuj 4-5 minut, aż ryba zmieni kolor na nieprzezroczysty różowy."},
            {
                "uk": "Вмішайте лимонний сік, подрібнений кріп та відварену пасту разом із водою з-під неї. Інтенсивно перемішайте для створення густої емульсії.",
                "en": "Stir in lemon juice, chopped dill, and the cooked pasta along with the reserved pasta water. Mix vigorously to create a thick emulsion.",
                "pl": "Wymieszaj sok z cytryny, posiekany koperek i ugotowany makaron wraz z zachowaną wodą z gotowania. Intensywnie wymieszaj, aby uzyskać gęstą emulsję."}
        ]
    },
    {
        "title": "Запечений хек з буряком та імбиром",
        "title_en": "Baked hake with beetroot and ginger",
        "title_pl": "Pieczony morszczuk z burakami i imbirem",
        "description": "Запечений хек у сметанному соусі з буряком, цибулею та імбиром. Страва виходить ніжною, поживною і добре підходить для вечері.",
        "description_en": "Baked hake in sour cream sauce with beetroot, onion, and ginger. The dish turns out tender, nutritious, and great for dinner.",
        "description_pl": "Pieczony morszczuk w sosie śmietanowym z burakami, cebulą i imbirem. Danie jest delikatne, pożywne i świetnie nadaje się na kolację.",
        "source": "Євген Клопотенко",
        "source_en": "Yevhen Klopotenko",
        "source_pl": "Jewhen Klopotenko",
        "cooking_time": 120,
        "portions": 4,
        "calories": 260,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.UKRAINIAN, Cuisine.AUTHOR],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.DIETARY, Diet.SEAFOOD_DIET],
        "dish_types": [DishType.MAIN, DishType.FISH],
        "ingredients": [
            ("Хек", 800, UnitChoice.G),
            ("Буряк", 300, UnitChoice.G),
            ("Сметана", 300, UnitChoice.G),
            ("Цибуля ріпчаста", 80, UnitChoice.G),
            ("Вода", 250, UnitChoice.ML),
            ("Імбир", 3, UnitChoice.G),
            ("Кріп", 5, UnitChoice.G),
            ("Сіль", 5, UnitChoice.G),
            ("Рослинна олія", 15, UnitChoice.ML),
        ],
        "steps": [
            {
                "uk": "Буряк герметично запечіть у фользі до м'якості (60-90 хв при 180°C). Охолодіть та наріжте кружальцями товщиною 3-5 мм.",
                "en": "Bake the beets tightly in foil until soft (60-90 min at 180°C). Cool and cut into 3-5 mm thick rounds.",
                "pl": "Upiecz buraki szczelnie zawinięte w folii do miękkości (60-90 minut w 180°C). Ostudź i pokrój w plastry o grubości 3-5 mm."},
            {
                "uk": "Філе хека наріжте на порції. Зробіть на шкірці 2-3 неглибокі надрізи, щоб уникнути деформації під час теплової обробки.",
                "en": "Cut the hake fillet into portions. Make 2-3 shallow cuts on the skin to prevent deformation during cooking.",
                "pl": "Filet z morszczuka pokrój na porcje. Zrób 2-3 płytkie nacięcia na skórze, aby zapobiec deformacji podczas gotowania."},
            {"uk": "Для соусу змішайте сметану з водою, натертим імбиром, кропом, сіллю та півкільцями цибулі.",
             "en": "For the sauce, mix sour cream with water, grated ginger, dill, salt, and half-rings of onion.",
             "pl": "Do sosu wymieszaj śmietanę z wodą, startym imbirem, koperkiem, solą i pokrojoną w piórka cebulą."},
            {
                "uk": "Форму для запікання змастіть олією. Викладіть рибу шкіркою донизу, зверху розмістіть нарізаний буряк. Залийте все сметанково-імбирним соусом.",
                "en": "Grease a baking dish with oil. Place the fish skin-side down, place sliced beets on top. Pour the sour cream and ginger sauce over everything.",
                "pl": "Naczynie do pieczenia posmaruj olejem. Ułóż rybę skórą do dołu, na wierzchu rozłóż pokrojone buraki. Całość zalej sosem śmietanowo-imbirowym."},
            {"uk": "Запікайте у духовці при 180°C протягом 35-45 хвилин до готовності риби.",
             "en": "Bake in the oven at 180°C for 35-45 minutes until the fish is cooked.",
             "pl": "Piecz w piekarniku w temperaturze 180°C przez 35-45 minut do ugotowania ryby."}
        ]
    },
    {
        "title": "Запечена дорадо з фенхелем та картоплею",
        "title_en": "Baked dorado with fennel and potatoes",
        "title_pl": "Pieczona dorado z koprem włoskim i ziemniakami",
        "description": "Дорадо запікається на подушці з картоплі та фенхелю з ароматною глазур’ю. Це легка рибна страва для вечері або святкової подачі.",
        "description_en": "Dorado is baked on a bed of potatoes and fennel with an aromatic glaze. This is a light fish dish for dinner or holiday serving.",
        "description_pl": "Dorada zapiekana na łóżku z ziemniaków i kopru włoskiego z aromatyczną glazurą. To lekkie danie rybne na kolację lub uroczyste podanie.",
        "source": "Helena Busiakiewicz",
        "source_en": "Helena Busiakiewicz",
        "source_pl": "Helena Busiakiewicz",
        "cooking_time": 50,
        "portions": 2,
        "calories": 410,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.MEDITERRANEAN],
        "meal_times": [MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.GLUTEN_FREE, Diet.SEAFOOD_DIET],
        "dish_types": [DishType.MAIN, DishType.FISH],
        "ingredients": [
            ("Дорадо", 600, UnitChoice.G),
            ("Картопля", 300, UnitChoice.G),
            ("Фенхель", 150, UnitChoice.G),
            ("Часник", 10, UnitChoice.G),
            ("Лимонний сік", 30, UnitChoice.ML),
            ("Соєвий соус", 30, UnitChoice.ML),
            ("Мед", 10, UnitChoice.G),
            ("Кінза", 15, UnitChoice.G),
            ("Рослинна олія", 30, UnitChoice.ML),
            ("Сіль", 3, UnitChoice.G),
        ],
        "steps": [
            {"uk": "Розігрійте духовку до 200°C. Картоплю та фенхель наріжте дуже тонкими слайсами.",
             "en": "Preheat the oven to 200°C. Slice the potatoes and fennel very thinly.",
             "pl": "Rozgrzej piekarnik do 200°C. Ziemniaki i koper włoski pokrój w bardzo cienkie plasterki."},
            {
                "uk": "Викладіть овочі шарами (як луска) на застелене пергаментом деко. Збризніть олією, посоліть і запікайте 15 хвилин для розм'якшення.",
                "en": "Layer the vegetables (like scales) on a parchment-lined baking sheet. Drizzle with oil, salt, and bake for 15 minutes to soften.",
                "pl": "Ułóż warzywa warstwami (jak łuski) na blasze wyłożonej papierem do pieczenia. Skrop olejem, posól i piecz 15 minut do zmięknięcia."},
            {
                "uk": "Тим часом приготуйте глазур: змішайте подрібнений часник, соєвий соус, мед, лимонний сік та дрібно нарізані стебла кінзи.",
                "en": "Meanwhile, prepare the glaze: mix minced garlic, soy sauce, honey, lemon juice, and finely chopped cilantro stems.",
                "pl": "W międzyczasie przygotuj glazurę: wymieszaj posiekany czosnek, sos sojowy, miód, sok z cytryny i drobno posiekane łodygi kolendry."},
            {
                "uk": "Дістаньте овочі з духовки. Зробіть на шкірці підготовленої цілої риби кілька глибоких надрізів. Покладіть рибу поверх овочів.",
                "en": "Remove vegetables from the oven. Make several deep cuts on the skin of the prepared whole fish. Place the fish on top of the vegetables.",
                "pl": "Wyjmij warzywa z piekarnika. Zrób kilka głębokich nacięć na skórze przygotowanej całej ryby. Połóż rybę na warzywach."},
            {
                "uk": "Залийте рибу та овочі підготовленим соусом-глазур'ю. Накрийте фольгою і запікайте ще 15 хвилин. За бажанням, зніміть фольгу в кінці, щоб скоринка підрум'янилася.",
                "en": "Pour the prepared glaze sauce over the fish and vegetables. Cover with foil and bake another 15 minutes. Optionally, remove the foil at the end so the crust browns.",
                "pl": "Zalej rybę i warzywa przygotowanym sosem z glazurą. Przykryj folią aluminiową i piecz kolejne 15 minut. Opcjonalnie na koniec zdejmij folię, aby skórka się zarumieniła."}
        ]
    },
    {
        "title": "Курячий боул з кіноа та лохиною",
        "title_en": "Chicken and quinoa bowl with blueberries",
        "title_pl": "Miska з kurczakiem, komosą ryżową i borówkami",
        "description": "Поживний боул із куркою, кіноа, лохиною, зеленим горошком і фетою. Поєднує білок, крупу та свіжий ягідний смак.",
        "description_en": "A nutritious bowl with chicken, quinoa, blueberries, green peas, and feta. Combines protein, grains, and a fresh berry taste.",
        "description_pl": "Pożywna miska z kurczakiem, komosą ryżową, borówkami, zielonym groszkiem i fetą. Łączy białko, kaszę i świeży jagodowy smak.",
        "source": "Джеймі Олівер",
        "source_en": "Jamie Oliver",
        "source_pl": "Jamiego Olivera",
        "cooking_time": 25,
        "portions": 2,
        "calories": 595,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.BRITISH, Cuisine.AUTHOR],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.HIGH_PROTEIN, Diet.DIETARY],
        "dish_types": [DishType.SALAD, DishType.MEAT, DishType.MAIN],
        "ingredients": [
            ("Куряче філе", 300, UnitChoice.G),
            ("Кіноа", 250, UnitChoice.G),
            ("Горошок зелений", 150, UnitChoice.G),
            ("Лохина", 160, UnitChoice.G),
            ("Фета", 30, UnitChoice.G),
            ("Часник", 10, UnitChoice.G),
            ("Лимон", 1, UnitChoice.PCS),
            ("М'ята", 15, UnitChoice.G),
            ("Оливкова олія", 15, UnitChoice.ML),
            ("Сіль", 2, UnitChoice.G),
            ("Перець чорний", 1, UnitChoice.G),
        ],
        "steps": [
            {
                "uk": "Попередньо відваріть кіноа. Піддайте куряче філе швидкому обсмажуванню на оливковій олії до золотистого кольору (близько 5 хвилин), попередньо приправивши сіллю та перцем.",
                "en": "Pre-boil the quinoa. Quickly fry the chicken fillet in olive oil until golden brown (about 5 minutes), seasoning with salt and pepper beforehand.",
                "pl": "Wcześniej ugotuj komosę ryżową. Szybko podsmaż filet z kurczaka na oliwie z oliwek na złoty kolor (około 5 minut), wcześniej doprawiając solą i pieprzem."
            },
            {
                "uk": "Додайте нарізаний часник та цедру лимона до курки для ароматизації олії.",
                "en": "Add chopped garlic and lemon zest to the chicken to flavor the oil.",
                "pl": "Dodaj posiekany czosnek i skórkę z cytryny do kurczaka, aby nadać oliwie aromat."
            },
            {
                "uk": "Додайте лохину у сковороду. Готуйте, поки ягоди не почнуть лопатися і виділяти сік, формуючи натуральний соус. Зніміть м'ясо з вогню та наріжте.",
                "en": "Add the blueberries to the pan. Cook until the berries start to burst and release their juice, forming a natural sauce. Remove the meat from the heat and slice.",
                "pl": "Dodaj borówki na patelnię. Gotuj, aż jagody zaczną pękać i puszczać sok, tworząc naturalny sos. Zdejmij mięso z ognia i pokrój."
            },
            {
                "uk": "У ту ж сковороду додайте відварену кіноа та зелений горошок. Прогрійте до випаровування зайвої вологи. Додайте лимонний сік.",
                "en": "In the same pan, add the cooked quinoa and green peas. Heat until excess moisture evaporates. Add lemon juice.",
                "pl": "Na tę samą patelnię dodaj ugotowaną komosę ryżową i zielony groszek. Podgrzewaj, aż nadmiar wilgoci wyparuje. Dodaj sok z cytryny."
            },
            {
                "uk": "Викладіть теплу базу у тарілку, зверху розмістіть курку, посипте м'ятою та розкришеною Фетою.",
                "en": "Place the warm base on a plate, top with chicken, sprinkle with mint and crumbled feta.",
                "pl": "Wyłóż ciepłą bazę na talerz, na wierzchu połóż kurczaka, posyp miętą i pokruszoną fetą."
            }
        ]
    },
    {
        "title": "Ароматний плов з білим рисом та мідіями",
        "title_en": "Fragrant pilaf with white rice and mussels",
        "title_pl": "Aromatyczny pilaw z białym ryżem i małżami",
        "description": "Плов із білим рисом, мідіями, морквою, цибулею та паприкою. Ситна страва з морепродуктами для обіду або вечері.",
        "description_en": "Pilaf with white rice, mussels, carrots, onions, and paprika. A hearty seafood dish for lunch or dinner.",
        "description_pl": "Pilaw z białym ryżem, małżami, marchewką, cebulą i papryką. Sycące danie z owocami morza na obiad lub kolację.",
        "source": "Євген Клопотенко",
        "source_en": "Yevhen Klopotenko",
        "source_pl": "Jewhen Klopotenko",
        "cooking_time": 90,
        "portions": 6,
        "calories": 390,
        "difficulty": Difficulty.MEDIUM,
        "cuisine": [Cuisine.AUTHOR, Cuisine.INTERNATIONAL],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET],
        "dish_types": [DishType.MAIN, DishType.SEAFOOD],
        "ingredients": [
            ("Рис білий", 400, UnitChoice.G),
            ("Мідії", 500, UnitChoice.G),
            ("Морква", 150, UnitChoice.G),
            ("Цибуля ріпчаста", 100, UnitChoice.G),
            ("Часник", 40, UnitChoice.G),
            ("Рослинна олія", 50, UnitChoice.ML),
            ("Паприка", 5, UnitChoice.G),
            ("Сіль", 5, UnitChoice.G),
            ("Вода", 500, UnitChoice.ML),
        ],
        "steps": [
            {
                "uk": "Промийте рис у холодній воді 3-5 разів (до прозорої води) та замочіть на 10 хвилин.",
                "en": "Wash the rice in cold water 3-5 times (until the water is clear) and soak for 10 minutes.",
                "pl": "Opłucz ryż w zimnej wodzie 3-5 razy (aż woda będzie czysta) i namocz na 10 minut."
            },
            {
                "uk": "У казані розігрійте олію. Обсмажте нарізану кубиками цибулю та соломкою моркву (близько 10 хвилин).",
                "en": "Heat the oil in a cauldron. Fry diced onions and julienned carrots (about 10 minutes).",
                "pl": "Rozgrzej olej w kociołku. Podsmaż pokrojoną w kostkę cebulę i marchewkę w paski (około 10 minut)."
            },
            {
                "uk": "Додайте очищені мідії і смажте не більше 2 хвилин, щоб білок не стал жорстким.",
                "en": "Add peeled mussels and fry for no more than 2 minutes so the protein does not become tough.",
                "pl": "Dodaj oczyszczone małże i smaż nie dłużej niż 2 minuty, aby białko nie stwardniało."
            },
            {
                "uk": "Всипте солодку паприку та рис, ретельно перемішайте для обволікання зерен ліпідами.",
                "en": "Pour in sweet paprika and rice, mix thoroughly to coat the grains with lipids.",
                "pl": "Wsyp słodką paprykę i ryż, dokładnie wymieszaj, aby ziarna pokryły się lipidami."
            },
            {
                "uk": "Залийте гарячою водою, в центр занурте цілу нечищену головку часнику. Посоліть, накрийте кришкою і варіть на мінімальному вогні 30 хвилин. Дайте настоятися ще 15 хвилин без вогню.",
                "en": "Pour hot water, submerge a whole unpeeled head of garlic in the center. Add salt, cover, and cook on minimum heat for 30 minutes. Let it brew for another 15 minutes off the heat.",
                "pl": "Zalej gorącą wodą, zanurz w środku całą, nieobraną główkę czosnku. Posól, przykryj i gotuj na minimalnym ogniu przez 30 minut. Pozostaw do naciągnięcia na kolejne 15 minut bez ognia."
            }
        ]
    },
    {
        "title": "Омлет зі шпинатом та фетою",
        "title_en": "Spinach and feta omelet",
        "title_pl": "Omlet ze szpinakiem i fetą",
        "description": "Ніжний омлет зі шпинатом, фетою та зеленою цибулею. Добрий варіант для швидкого сніданку або легкого перекусу.",
        "description_en": "A delicate omelet with spinach, feta, and green onions. A great option for a quick breakfast or a light snack.",
        "description_pl": "Delikatny omlet ze szpinakiem, fetą i zieloną cebulką. Dobra opcja na szybkie śniadanie lub lekką przekąskę.",
        "source": "Katie Workman",
        "source_en": "Katie Workman",
        "source_pl": "Katie Workman",
        "cooking_time": 15,
        "portions": 1,
        "calories": 320,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.INTERNATIONAL],
        "meal_times": [MealTime.BREAKFAST, MealTime.SNACK],
        "dietary_tags": [Diet.TRADITIONAL, Diet.VEGETARIAN, Diet.GLUTEN_FREE],
        "dish_types": [DishType.OMELET],
        "ingredients": [
            ("Яйця", 3, UnitChoice.PCS),
            ("Шпинат", 50, UnitChoice.G),
            ("Фета", 30, UnitChoice.G),
            ("Вершкове масло", 10, UnitChoice.G),
            ("Цибуля зелена", 5, UnitChoice.G),
            ("Сіль", 1, UnitChoice.G),
            ("Перець чорний", 1, UnitChoice.G),
        ],
        "steps": [
            {
                "uk": "На гарячій сковороді з краплею масла швидко спасеруйте шпинат до м'якості (близько 1 хвилини). Перекладіть його на тарілку, щоб зупинити приготування, і злийте зайву рідину.",
                "en": "On a hot pan with a drop of butter, quickly sauté the spinach until soft (about 1 minute). Transfer it to a plate to stop the cooking, and drain excess liquid.",
                "pl": "Na gorącej patelni z odrobiną masła szybko podsmaż szpinak do miękkości (około 1 minuty). Przełóż na talerz, aby zatrzymać gotowanie, i odcedź nadmiar płynu."
            },
            {
                "uk": "Збийте яйця у мисці з сіллю та чорним перцем до однорідності.",
                "en": "Beat the eggs in a bowl with salt and black pepper until smooth.",
                "pl": "Ubij jajka w misce z solą i czarnym pieprzem na gładką masę."
            },
            {
                "uk": "Розтопіть вершкове масло на сковороді на середньому вогні. Вилийте яєчну масу. Коли краї почнуть хапатися, злегка підіймайте їх лопаткою, щоб рідка маса стікала вниз.",
                "en": "Melt butter in a pan over medium heat. Pour in the egg mixture. When the edges start to set, lift them slightly with a spatula so the liquid mass flows underneath.",
                "pl": "Roztop masło na patelni na średnim ogniu. Wlej masę jajeczną. Gdy brzegi zaczną się ścinać, lekko unoś je szpatułką, aby płynna masa spłynęła na dół."
            },
            {
                "uk": "Коли омлет буде майже готовий, але ще злегка вологий зверху, викладіть на одну половину підготовлений шпинат та покришіть сир Фета.",
                "en": "When the omelet is almost done but still slightly moist on top, place the prepared spinach on one half and crumble the Feta cheese.",
                "pl": "Gdy omlet będzie prawie gotowy, ale wciąż lekko wilgotny na wierzchu, wyłóż przygotowany szpinak na jedną połowę i pokrusz ser Feta."
            },
            {
                "uk": "Обережно складіть омлет навпіл за допомогою лопатки, потримайте на вогні ще 30 секунд для розплавлення сиру. Подавайте, посипавши зеленою цибулею.",
                "en": "Carefully fold the omelet in half using a spatula, keep on the heat for another 30 seconds to melt the cheese. Serve sprinkled with green onions.",
                "pl": "Ostrożnie złóż omlet na pół za pomocą szpatułki, potrzymaj na ogniu przez kolejne 30 sekund, aby ser się roztopił. Podawaj posypany zieloną cebulką."
            }
        ]
    },
    {
        "title": "Запечена курка з картоплею та лимоном",
        "title_en": "Baked chicken with potatoes and lemon",
        "title_pl": "Pieczony kurczak z ziemniakami i cytryną",
        "description": "Курячі стегна запікаються разом із картоплею, лимоном, часником і розмарином. Це проста ситна страва для сімейного обіду або вечері.",
        "description_en": "Chicken thighs baked with potatoes, lemon, garlic, and rosemary. This is a simple hearty dish for a family lunch or dinner.",
        "description_pl": "Udka z kurczaka pieczone z ziemniakami, cytryną, czosnkiem i rozmarynem. To proste, sycące danie na rodzinny obiad lub kolację.",
        "source": "Good Food team",
        "source_en": "Good Food team",
        "source_pl": "Good Food team",
        "cooking_time": 75,
        "portions": 4,
        "calories": 520,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.BRITISH, Cuisine.INTERNATIONAL],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.GLUTEN_FREE],
        "dish_types": [DishType.MAIN, DishType.MEAT, DishType.GARNISH],
        "ingredients": [
            ("Курячі стегна", 800, UnitChoice.G),
            ("Картопля", 500, UnitChoice.G),
            ("Лимон", 1, UnitChoice.PCS),
            ("Розмарин", 5, UnitChoice.G),
            ("Часник", 40, UnitChoice.G),
            ("Цибуля ріпчаста", 100, UnitChoice.G),
            ("Оливкова олія", 30, UnitChoice.ML),
            ("Сіль", 4, UnitChoice.G),
            ("Перець чорний", 2, UnitChoice.G),
        ],
        "steps": [
            {
                "uk": "Розігрійте духовку до 190°C.",
                "en": "Preheat the oven to 190°C.",
                "pl": "Rozgrzej piekarnik do 190°C."
            },
            {
                "uk": "Змішайте в мисці кілька подрібнених зубчиків часнику, оливкову олію та сіль/перець. Натріть цією сумішшю курячі стегна і викладіть їх у велику форму для запікання.",
                "en": "Mix a few minced cloves of garlic, olive oil, and salt/pepper in a bowl. Rub the chicken thighs with this mixture and place them in a large baking dish.",
                "pl": "W misce wymieszaj kilka posiekanych ząbków czosnku, oliwę z oliwek i sól/pieprz. Natrzyj tą mieszanką udka z kurczaka i umieść je w dużym naczyniu do pieczenia."
            },
            {
                "uk": "Наріжте картоплю на половинки або чверті, цибулю — товстими скибками. Лимон розріжте на 4 частини.",
                "en": "Cut the potatoes into halves or quarters, and the onion into thick slices. Cut the lemon into 4 pieces.",
                "pl": "Ziemniaki przekrój na połówki lub ćwiartki, a cebulę w grube plastry. Cytrynę pokrój na 4 części."
            },
            {
                "uk": "Розкладіть картоплю, лимон, цибулю, цілі (неочищені) зубчики часнику та гілочки розмарину навколо курки.",
                "en": "Arrange the potatoes, lemon, onion, whole (unpeeled) garlic cloves, and rosemary sprigs around the chicken.",
                "pl": "Ułóż ziemniaki, cytrynę, cebulę, całe (nieobrane) ząbki czosnku i gałązki rozmarynu wokół kurczaka."
            },
            {
                "uk": "Запікайте 45-55 хвилин, періодично перевертаючи овочі в соках, що виділилися, доки курка не стане золотистою, а картопля м'якою всередині та хрусткою зовні.",
                "en": "Bake for 45-55 minutes, occasionally turning the vegetables in the released juices, until the chicken is golden and the potatoes are soft inside and crispy outside.",
                "pl": "Piecz 45-55 minut, od czasu do czasu obracając warzywa w wydzielonych sokach, aż kurczak będzie złocisty, a ziemniaki miękkie w środku i chrupiące na zewnątrz."
            }
        ]
    },
    {
        "title": "Запечене філе лосося на овочевій подушці",
        "title_en": "Baked salmon fillet on a bed of vegetables",
        "title_pl": "Pieczony filet z łososia na łóżku warzywnym",
        "description": "Філе лосося запікається з кабачком, бататом, чері, печерицями та червоною цибулею. Страва виходить легкою, яскравою і збалансованою.",
        "description_en": "Salmon fillet is baked with zucchini, sweet potato, cherry tomatoes, mushrooms, and red onion. The dish turns out light, bright, and balanced.",
        "description_pl": "Filet z łososia pieczony jest z cukinią, batatem, pomidorkami cherry, pieczarkami i czerwoną cebulą. Danie jest lekkie, kolorowe i zbilansowane.",
        "source": "Євген Клопотенко",
        "source_en": "Yevhen Klopotenko",
        "source_pl": "Jewhen Klopotenko",
        "cooking_time": 25,
        "portions": 2,
        "calories": 380,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.EUROPEAN, Cuisine.INTERNATIONAL],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.SEAFOOD_DIET, Diet.HIGH_PROTEIN],
        "dish_types": [DishType.MAIN, DishType.FISH],
        "ingredients": [
            ("Філе лосося", 250, UnitChoice.G),
            ("Цибуля червона", 100, UnitChoice.G),
            ("Помідор", 100, UnitChoice.G),  # чері
            ("Кабачок", 150, UnitChoice.G),
            ("Батат", 150, UnitChoice.G),
            ("Печериці", 100, UnitChoice.G),
            ("Тим'ян", 2, UnitChoice.G),
            ("Оливкова олія", 15, UnitChoice.ML),
            ("Гірчиця", 10, UnitChoice.G),
            ("Часник", 5, UnitChoice.G),
            ("Сіль", 2, UnitChoice.G),
            ("Перець чорний", 1, UnitChoice.G),
            ("Орегано", 1, UnitChoice.G),
            ("Лимон", 0.5, UnitChoice.PCS),
        ],
        "steps": [
            {
                "uk": "Кабачок, батат, помідори чері, печериці та червону цибулю помийте й наріжте великими шматками.",
                "en": "Wash the zucchini, sweet potato, cherry tomatoes, mushrooms, and red onion, and cut them into large pieces.",
                "pl": "Umyj cukinię, batata, pomidorki cherry, pieczarki i czerwoną cebulę i pokrój na duże kawałki."
            },
            {
                "uk": "Перекладіть овочі та гриби в миску. Додайте сіль, перець чорний, орегано й оливкову олію. Перемішайте, щоб овочі рівномірно вкрилися спеціями та олією.",
                "en": "Transfer the vegetables and mushrooms to a bowl. Add salt, black pepper, oregano, and olive oil. Mix so that the vegetables are evenly coated with spices and oil.",
                "pl": "Przełóż warzywa i grzyby do miski. Dodaj sól, czarny pieprz, oregano i oliwę z oliwek. Wymieszaj, aby warzywa były równomiernie pokryte przyprawami i oliwą."
            },
            {
                "uk": "Філе лосося злегка посоліть. Змастіть його гірчицею та додайте подрібнений часник.",
                "en": "Lightly salt the salmon fillet. Brush it with mustard and add minced garlic.",
                "pl": "Lekko posól filet z łososia. Posmaruj go musztardą i dodaj posiekany czosnek."
            },
            {
                "uk": "Зробіть із пергаменту два імпровізовані «кораблики». На дно кожного викладіть овочеву подушку з кабачка, батату, чері, печериць і червоної цибулі.",
                "en": "Make two makeshift 'boats' out of parchment paper. At the bottom of each, place a vegetable bed of zucchini, sweet potato, cherry tomatoes, mushrooms, and red onion.",
                "pl": "Zrób dwie zaimprowizowane 'łódeczki' z papieru do pieczenia. Na dnie każdej z nich ułóż łóżko warzywne z cukinii, batata, pomidorków cherry, pieczarek i czerwonej cebuli."
            },
            {
                "uk": "Поверх овочів покладіть філе лосося. Додайте кілька гілочок тим’яну.",
                "en": "Place the salmon fillet on top of the vegetables. Add a few sprigs of thyme.",
                "pl": "Na warzywach połóż filet z łososia. Dodaj kilka gałązek tymianku."
            },
            {
                "uk": "Запікайте в духовці при температурі 180°C протягом 25 хвилин.",
                "en": "Bake in the oven at 180°C for 25 minutes.",
                "pl": "Piecz w piekarniku w temperaturze 180°C przez 25 minut."
            },
            {
                "uk": "Перед подачею полийте страву соком лимона.",
                "en": "Squeeze lemon juice over the dish before serving.",
                "pl": "Przed podaniem skrop danie sokiem z cytryny."
            }
        ]
    },
    {
        "title": "Медова курка з броколі та рисом",
        "title_en": "Honey soy chicken with broccoli and rice",
        "title_pl": "Miodowy kurczak z brokułami i ryżem",
        "description": "Курячі стегна запікаються в медово-соєвому маринаді та подаються з броколі й рисом. Це ситна страва з легким азійським смаком.",
        "description_en": "Chicken thighs are baked in a honey-soy marinade and served with broccoli and rice. This is a hearty dish with a light Asian flavor.",
        "description_pl": "Udka z kurczaka pieczone w marynacie miodowo-sojowej i podawane z brokułami i ryżem. To sycące danie o lekkim azjatyckim smaku.",
        "source": "Sophie Godwin – Cookery writer",
        "source_en": "Sophie Godwin – Cookery writer",
        "source_pl": "Sophie Godwin – Cookery writer",
        "cooking_time": 50,
        "portions": 4,
        "calories": 450,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.ASIAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.TRADITIONAL, Diet.LACTOSE_FREE],
        "dish_types": [DishType.MAIN, DishType.MEAT],
        "ingredients": [
            ("Курячі стегна", 800, UnitChoice.G),
            ("Броколі", 300, UnitChoice.G),
            ("Рис білий", 200, UnitChoice.G),
            ("Соєвий соус", 45, UnitChoice.ML),
            ("Мед", 45, UnitChoice.G),
            ("Рослинна олія", 30, UnitChoice.ML),
            ("Імбир", 10, UnitChoice.G),
            ("Часник", 10, UnitChoice.G),
            ("Кунжутна олія", 5, UnitChoice.ML),
        ],
        "steps": [
            {
                "uk": "Розігрійте духовку до 200°C. Змішайте соєвий соус, мед, 1 ст.л. рослинної олії, натертий імбир та розчавлений часник.",
                "en": "Preheat the oven to 200°C. Mix the soy sauce, honey, 1 tbsp vegetable oil, grated ginger, and crushed garlic.",
                "pl": "Rozgrzej piekarnik do 200°C. Wymieszaj sos sojowy, miód, 1 łyżkę oleju roślinnego, starty imbir i zgnieciony czosnek."
            },
            {
                "uk": "Залийте цим маринадом курячі стегна. Якщо є час, залиште на 30 хвилин.",
                "en": "Pour this marinade over the chicken thighs. If you have time, leave for 30 minutes.",
                "pl": "Zalej udka z kurczaka tą marynatą. Jeśli masz czas, zostaw na 30 minut."
            },
            {
                "uk": "Викладіть курку разом з усім маринадом у форму для запікання шкіркою догори. Запікайте 30-35 хвилин до рум'яної скоринки і повної готовності.",
                "en": "Place the chicken along with all the marinade in a baking dish, skin-side up. Bake for 30-35 minutes until browned and fully cooked.",
                "pl": "Umieść kurczaka wraz z całą marynatą w naczyniu do pieczenia skórą do góry. Piecz przez 30-35 minut do zrumienienia i całkowitego ugotowania."
            },
            {
                "uk": "Паралельно відваріть рис та розберіть броколі на суцвіття. Броколі відваріть на пару або бланшуйте в окропі 3 хвилини.",
                "en": "Meanwhile, boil the rice and break the broccoli into florets. Steam the broccoli or blanch it in boiling water for 3 minutes.",
                "pl": "W międzyczasie ugotuj ryż i podziel brokuły na różyczki. Gotuj brokuły na parze lub blanszuj we wrzątku przez 3 minuty."
            },
            {
                "uk": "Подавайте готову курку з рисом і броколі, поливши страву соками з дека та краплею кунжутної олії для аромату.",
                "en": "Serve the cooked chicken with rice and broccoli, drizzling the dish with the pan juices and a drop of sesame oil for flavor.",
                "pl": "Podawaj gotowego kurczaka z ryżem i brokułami, polewając danie sokami z blachy i kroplą oleju sezamowego dla smaku."
            }
        ]
    },
    {
        "title": "Запечена картопля по-селянськи з паприкою",
        "title_en": "Baked potato wedges with paprika",
        "title_pl": "Pieczone łódeczki ziemniaczane z papryką",
        "description": "Запечена картопля з паприкою, часником і хрусткою скоринкою. Підходить як гарнір або проста гаряча закуска.",
        "description_en": "Baked potatoes with paprika, garlic, and a crispy crust. Suitable as a side dish or a simple hot snack.",
        "description_pl": "Pieczone ziemniaki z papryką, czosnkiem i chrupiącą skórką. Nadaje się jako dodatek do dania głównego lub prosta gorąca przekąska.",
        "source": "Євген Клопотенко",
        "source_en": "Yevhen Klopotenko",
        "source_pl": "Jewhen Klopotenko",
        "cooking_time": 45,
        "portions": 4,
        "calories": 260,
        "difficulty": Difficulty.EASY,
        "cuisine": [Cuisine.UKRAINIAN],
        "meal_times": [MealTime.LUNCH, MealTime.DINNER],
        "dietary_tags": [Diet.VEGAN, Diet.VEGETARIAN, Diet.GLUTEN_FREE, Diet.LACTOSE_FREE],
        "dish_types": [DishType.GARNISH],
        "ingredients": [
            ("Картопля", 500, UnitChoice.G),
            ("Паприка", 10, UnitChoice.G),
            ("Рослинна олія", 45, UnitChoice.ML),
            ("Сіль", 5, UnitChoice.G),
            ("Перець чорний", 2, UnitChoice.G),
            ("Часник", 10, UnitChoice.G),
        ],
        "steps": [
            {
                "uk": "Бульби ретельно вимийте жорсткою щіткою (шкірку не зрізати) та наріжте рівномірними часточками.",
                "en": "Thoroughly wash the tubers with a stiff brush (do not peel) and cut into even wedges.",
                "pl": "Dokładnie umyj bulwy sztywną szczotką (nie obieraj) i pokrój w równe łódeczki."
            },
            {
                "uk": "Змішайте часточки з олією, паприкою, сіллю, перцем та розчавленим часником, переконавшись у повному покритті кожної картоплини плівкою зі спецій.",
                "en": "Mix the wedges with oil, paprika, salt, pepper, and crushed garlic, making sure each potato is fully coated with a film of spices.",
                "pl": "Wymieszaj łódeczki z olejem, papryką, solą, pieprzem i rozgniecionym czosnkiem, upewniając się, że każdy ziemniak jest w pełni pokryty warstwą przypraw."
            },
            {
                "uk": "Викладіть на деко з пергаментом шкіркою донизу, залишаючи простір між шматочками для конвекції гарячого повітря.",
                "en": "Place skin-side down on a baking sheet lined with parchment, leaving space between pieces for hot air convection.",
                "pl": "Ułóż skórką do dołu na blasze wyłożonej papierem do pieczenia, zostawiając przestrzeń między kawałkami dla konwekcji gorącego powietrza."
            },
            {
                "uk": "Запікайте у попередньо розігрітій до 200°C духовці протягом 30-35 хвилин до хрусткої золотистої скоринки.",
                "en": "Bake in a preheated 200°C oven for 30-35 minutes until a crispy golden crust forms.",
                "pl": "Piecz w nagrzanym do 200°C piekarniku przez 30-35 minut, aż utworzy się chrupiąca, złocista skórka."
            },
            {
                "uk": "Подавайте гарячою як самостійну закуску або гарнір до м'яса чи риби.",
                "en": "Serve hot as a standalone snack or as a side dish to meat or fish.",
                "pl": "Podawaj na gorąco jako samodzielną przekąskę lub jako dodatek do mięsa lub ryb."
            }
        ]
    }
]