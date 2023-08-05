init python:
    Action.current_parent = None
    none_action = Action("none", "")

    Action.current_parent = None
    map_action = Action("map", _("Карта"), has_children=True)

    Action.current_parent = "map"
    hotel = Action("hotel", _("Отель"), has_children=True, pos=(1480, 230), displaying="not seen('pcsj') or seen('B_daily_18')")
    my_room_in_hotel = Action("my_room_in_hotel", _("Моя комната"), "not seen('pcsj')")
    hotel_shop = Action("hotel_shop", _("Магазин"), "seen('B_daily_18')")

    Action.current_parent = "map"
    park = Action("park", _("Парк"), has_children=True, pos=(1614, 713-60))
    hang_park = Action("hang_park", _("Пойти на прогулку"), "seen('d8_1')")
    exercise = Action("exercise", _("Упражняться"), "seen('gysj_4') and is_day()")




    Action.current_parent = None
    college = Action("college", _("Колледж"), has_children=True)

    Action.current_parent = "college"
    college_facilities = Action("college_facilities", _("Оборудование колледжа"), has_children=True, pos=(522, 432))  
    campus = Action("campus", _("Кампус"), "is_day()")
    library = Action("library", _("Библиотека"))

    Action.current_parent = "college"
    apartment = Action("apartment", _("Студенческое общежитие"), has_children=True, pos=(522, 432))  
    B_room = Action("B_room", _("Найти Сеннин"), "t.period in (Forenoon, Afternoon)", displaying="seen('B_love_1')", to_map=False, training_nz="B")
    F_room = Action("F_room", _("Найти Рэйчел"), "is_day()", displaying="seen('F_love_2')", to_map=False, training_nz="F")
    college_bathroom = Action("college_bathroom", _("Общественная ванная комната"))

    Action.current_parent = "college"
    college_action = Action("college_action", "", has_children=True)
    course = Action("course", _("Иди в класс"), "t.period in (Forenoon, Afternoon) and t.day not in (Saturday, Sunday)")




    Action.current_parent = None
    mansion = Action("mansion", _("Особняк"), has_children=True)

    Action.current_parent = "mansion"
    mansion_rooms = Action("mansion_rooms", _("Особняк Элизы"), displaying="seen('d7_1')", has_children=True, rename=[("Особняк Элизы", "seen('D_dqsj')")], pos=(950, 485))
    C_room = Action("C_room", _("Комната Теодоры"), "t.period in (Forenoon, Afternoon, Evening, LateNight)", displaying="seen('pcsj')")
    D_room = Action("D_room", _("Найти Айрин"), "t.period in (Afternoon, Evening)", to_map=False, training_nz="D")
    E_room = Action("E_room", _("Найти Элизу"), "t.period in (Forenoon, Afternoon, Evening)", displaying="seen('pcsj', 'D_dqsj')", to_map=False, training_nz="E")
    mansion_pool = Action("mansion_pool", _("Бассейн"))
    mansion_bathroom = Action("mansion_bathroom", _("Ванная комната"))
    mansion_toilet = Action("mansion_toilet", _("Туалет"), xysize=(135, 124))
    mansion_livingroom = Action("mansion_livingroom", _("Гостиная"))
    mansion_guestroom = Action("mansion_guestroom", _("Гостевая комната"))

    Action.current_parent = "mansion"
    mansion_action = Action("mansion_action", "", has_children=True)
    tutor = Action("tutor", _("Репетиторство"), "t.period in (Afternoon, Evening) and tutor.count_of_day < 1", displaying="seen('pcsj')")




    Action.current_parent = "map"
    company = Action("company", _("Здание ШайниРост"), has_children=True, pos=(676, 378-60))
    work = Action("work", _("Работа"), "seen('pcsj') and t.period in (Forenoon, Afternoon) and Monday <= t.day <= Friday"),
    find_C_company = Action("find_C_company", _("Найти Теодору"), "seen('pcsj') and t.period in (Forenoon, Afternoon) and Monday <= t.day <= Friday", to_map=False, training_nz="C")

    Action.current_parent = "map"
    find_A_restaurant = Action("find_A_restaurant", _("Ресторан"), "t.period is Evening and Monday<=t.day<=Saturday and seen('A_wsdgsj')", pos=(500, 713-60))

    Action.current_parent = "map"
    find_A_cafe = Action("find_A_cafe", _("Кафе"), "t.period is Forenoon and Monday <= t.day <= Saturday and seen('d6_1')", pos=(1436, 500-60))


    Action.current_parent = "map"
    bookstore = Action("bookstore", _("Книжный магазин"), "seen('G_MoveIn') and t.period is Afternoon", pos=(698, 604-60))


    Action.current_parent = "map"
    downtown = Action("downtown", _("Центр города"), pos=(1569, 387-60), has_children=True)
    Action("street", _("Улица"), "seen('d8_1')")
    Action("shop", _("Магазин Позии"), displaying="seen('store_1_cj')")

    Action.current_parent = "map"
    find_A_clothing = Action("find_A_clothing", _("Магазин одежды"), "t.period is Afternoon and Monday <= t.day <= Saturday and seen('d8_1')", pos=(257, 811-60))

    alley = Action("alley", _("Темный переулок"), "t.period in (Evening, LateNight)", pos=(257, 600-60))

    Action('beach', _('Пляж'), "t.period in (Forenoon, Afternoon)", pos=(590, 187))

    Action('bungalow', _('Бунгало'), displaying="seen('E_daily_13')", pos=(196, 325-60))


    Action.current_parent = None
    bnb = Action("bnb", _("B&B"), has_children=True, pos=(522, 432))

    Action.current_parent = "bnb"
    bnb_action = Action("bnb_action", "", has_children=True)
    clean = Action("clean", _("Уборка"), "(t.period is not LateNight) and clean.count_of_day < 1", displaying="seen('A_daily_5') and clean_count < 5")
    build_pool = Action("build_pool", _("Построить бассейн"), "build_pool.count_of_day < 1", displaying="seen('C_daily_13') and build_pool_count < 7")

    Action.current_parent = "bnb"
    bnb_rooms = Action("bnb_rooms", _("Комнаты B&B"), has_children=True)
    basic_room = Action("basic_room", _("Спальня"))
    couple_room = Action("couple_room", _("Комната для пары"))
    my_room = Action("my_room", _("Моя комната"), to_map=False)
    frontyard = Action("frontyard", _("Передний двор"))
    livingroom = Action("livingroom", _("Гостиная"))
    kitchen = Action("kitchen", _("Кухня"))
    bathroom = Action("bathroom", _("Ванная комната"))
    toilet = Action("toilet", _("Туалет"))

    def G_room_hover():
        if t.period == Morning:
            return "Уно спит."
        if is_weekday() and t.period < Evening:
            return "Уно нет дома."

    def A_room_hover():
        if not is_A_home():
            return "Ее нет дома."

    def is_G_home():
        if is_weekday() and t.period in (Evening, LateNight):
            return True
        elif is_weekend() and t.period in periods_except(Morning, Afternoon):
            return True
        return False

    def is_A_home():
        if is_weekday() and t.period in (Morning, LateNight):
            return True
        elif is_weekend() and t.period in (Morning, Evening, LateNight):
            return True
        return False

    G_room = Action("G_room", _("Найти один"), "is_G_home()", hover_message=G_room_hover, to_map=False, training_nz="G")
    A_room = Action("A_room", _("Найти Веру"), "is_A_home()", hover_message=A_room_hover, to_map=False, training_nz="A")
    C_room_2 = Action("C_room_2", ("Комната Теодоры"))

    Action.current_parent = None

