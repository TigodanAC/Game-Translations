init python:
    Action.current_parent = None
    none_action = Action("none", "")

    Action.current_parent = None
    map_action = Action("map", _("Map"), has_children=True)

    Action.current_parent = "map"
    hotel = Action("hotel", _("Hotel"), has_children=True, pos=(1480, 230), displaying="not seen('pcsj') or seen('B_daily_18')")
    my_room_in_hotel = Action("my_room_in_hotel", _("My Room"), "not seen('pcsj')")
    hotel_shop = Action("hotel_shop", _("Store"), "seen('B_daily_18')")

    Action.current_parent = "map"
    park = Action("park", _("Park"), has_children=True, pos=(1614, 713-60))
    hang_park = Action("hang_park", _("Take a Stroll"), "seen('d8_1')")
    exercise = Action("exercise", _("Exercise"), "seen('gysj_4') and is_day()")




    Action.current_parent = None
    college = Action("college", _("College"), has_children=True)

    Action.current_parent = "college"
    college_facilities = Action("college_facilities", _("College Facilities"), has_children=True, pos=(522, 432))  
    campus = Action("campus", _("Campus"), "is_day()")
    library = Action("library", _("Library"))

    Action.current_parent = "college"
    apartment = Action("apartment", _("Student Apartment"), has_children=True, pos=(522, 432))  
    B_room = Action("B_room", _("Find Senning"), "t.period in (Forenoon, Afternoon)", displaying="seen('B_love_1')", to_map=False, training_nz="B")
    F_room = Action("F_room", _("Find Rachel"), "is_day()", displaying="seen('F_love_2')", to_map=False, training_nz="F")
    college_bathroom = Action("college_bathroom", _("Public Bathroom"))

    Action.current_parent = "college"
    college_action = Action("college_action", "", has_children=True)
    course = Action("course", _("Go to Class"), "t.period in (Forenoon, Afternoon) and t.day not in (Saturday, Sunday)")




    Action.current_parent = None
    mansion = Action("mansion", _("Mansion"), has_children=True)

    Action.current_parent = "mansion"
    mansion_rooms = Action("mansion_rooms", _("Elisa's Mansion"), displaying="seen('d7_1')", has_children=True, rename=[("Elisa's Mansion", "seen('D_dqsj')")], pos=(950, 485))
    C_room = Action("C_room", _("Theodora's Room"), "t.period in (Forenoon, Afternoon, Evening, LateNight)", displaying="seen('pcsj')")
    D_room = Action("D_room", _("Find Irene"), "t.period in (Afternoon, Evening)", to_map=False, training_nz="D")
    E_room = Action("E_room", _("Find Elisa"), "t.period in (Forenoon, Afternoon, Evening)", displaying="seen('pcsj', 'D_dqsj')", to_map=False, training_nz="E")
    mansion_pool = Action("mansion_pool", _("Swimming Pool"))
    mansion_bathroom = Action("mansion_bathroom", _("Bathroom"))
    mansion_toilet = Action("mansion_toilet", _("Toilet"), xysize=(135, 124))
    mansion_livingroom = Action("mansion_livingroom", _("Living Room"))
    mansion_guestroom = Action("mansion_guestroom", _("Guest Room"))

    Action.current_parent = "mansion"
    mansion_action = Action("mansion_action", "", has_children=True)
    tutor = Action("tutor", _("Tutoring"), "t.period in (Afternoon, Evening) and tutor.count_of_day < 1", displaying="seen('pcsj')")




    Action.current_parent = "map"
    company = Action("company", _("ShinyRost Building"), has_children=True, pos=(676, 378-60))
    work = Action("work", _("Work"), "seen('pcsj') and t.period in (Forenoon, Afternoon) and Monday <= t.day <= Friday"),
    find_C_company = Action("find_C_company", _("Find Theodora"), "seen('pcsj') and t.period in (Forenoon, Afternoon) and Monday <= t.day <= Friday", to_map=False, training_nz="C")

    Action.current_parent = "map"
    find_A_restaurant = Action("find_A_restaurant", _("Restaurant"), "t.period is Evening and Monday<=t.day<=Saturday and seen('A_wsdgsj')", pos=(500, 713-60))

    Action.current_parent = "map"
    find_A_cafe = Action("find_A_cafe", _("Cafe"), "t.period is Forenoon and Monday <= t.day <= Saturday and seen('d6_1')", pos=(1436, 500-60))


    Action.current_parent = "map"
    bookstore = Action("bookstore", _("Bookstore"), "seen('G_MoveIn') and t.period is Afternoon", pos=(698, 604-60))


    Action.current_parent = "map"
    downtown = Action("downtown", _("Downtown"), pos=(1569, 387-60), has_children=True)
    Action("street", _("Street"), "seen('d8_1')")
    Action("shop", _("Posia's shop"), displaying="seen('store_1_cj')")

    Action.current_parent = "map"
    find_A_clothing = Action("find_A_clothing", _("Clothing Store"), "t.period is Afternoon and Monday <= t.day <= Saturday and seen('d8_1')", pos=(257, 811-60))

    alley = Action("alley", _("Dark Alley"), "t.period in (Evening, LateNight)", pos=(257, 600-60))

    Action('beach', _('Beach'), "t.period in (Forenoon, Afternoon)", pos=(590, 187))

    Action('bungalow', _('Bungalow'), displaying="seen('E_daily_13')", pos=(196, 325-60))


    Action.current_parent = None
    bnb = Action("bnb", _("B&B"), has_children=True, pos=(522, 432))

    Action.current_parent = "bnb"
    bnb_action = Action("bnb_action", "", has_children=True)
    clean = Action("clean", _("Cleaning"), "(t.period is not LateNight) and clean.count_of_day < 1", displaying="seen('A_daily_5') and clean_count < 5")
    build_pool = Action("build_pool", _("Build the Pool"), "build_pool.count_of_day < 1", displaying="seen('C_daily_13') and build_pool_count < 7")

    Action.current_parent = "bnb"
    bnb_rooms = Action("bnb_rooms", _("B&B Rooms"), has_children=True)
    basic_room = Action("basic_room", _("Bedroom"))
    couple_room = Action("couple_room", _("Couple Room"))
    my_room = Action("my_room", _("My room"), to_map=False)
    frontyard = Action("frontyard", _("Front Yard"))
    livingroom = Action("livingroom", _("Living Room"))
    kitchen = Action("kitchen", _("Kitchen"))
    bathroom = Action("bathroom", _("Bathroom"))
    toilet = Action("toilet", _("Toilet"))

    def G_room_hover():
        if t.period == Morning:
            return "Uno is sleeping."
        if is_weekday() and t.period < Evening:
            return "Uno is not home."

    def A_room_hover():
        if not is_A_home():
            return "She's not at home."

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

    G_room = Action("G_room", _("Find Uno"), "is_G_home()", hover_message=G_room_hover, to_map=False, training_nz="G")
    A_room = Action("A_room", _("Find Vera"), "is_A_home()", hover_message=A_room_hover, to_map=False, training_nz="A")
    C_room_2 = Action("C_room_2", ("Theodora's room"))

    Action.current_parent = None
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
