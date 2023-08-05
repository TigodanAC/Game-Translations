default fortunetelling_today = False
default cleansing_today = False
default blessing_today = False
default fortunetelling_count = 0
default cleansing_count = 0
default blessing_count = 0

label shop:
    $ set_scene("Action")
    scene shop with tstmgr

    label shop.shop_menu:
    $ set_shop_ui()

    if seen('store_1_ft_firstime', 'store_1_bl_firstime'):
        $ shop_buy_service_badge = ""
    else:
        $ shop_buy_service_badge = "{image=badge2}"


    menu:
        posia "Привет, избранный~ {fast}"
        "Купить ее услугу [shop_buy_service_badge]":


            label shop.shop_buy_serive:

            if not seen('store_1_cl_firstime'):
                $ shop_fortune_badge = "{image=badge2}"
            else:
                $ shop_fortune_badge = ""

            if not seen('store_1_bl_firstime'):
                $ shop_cleanse_badge = "{image=badge2}"
            else:
                $ shop_cleanse_badge = ""

            menu:
                "Гадание ($200) [shop_fortune_badge]" if not fortunetelling_today:
                    if not P.buy(200, _("Гадание")):
                        jump shop.shop_menu

                    $ set_default_ui()
                    $ fortunetelling_today = True
                    $ fortunetelling_count += 1

                    if not seen('store_1_ft_firstime'):
                        $ run_event('store_1_ft_firstime')

                    elif fortunetelling_count == 4:
                        $ run_event('store_1_cl_firstime')
                    else:

                        $ rdc = RandomChoice(3)
                        if rdc(1):
                            $ run_event('store_1_ft_playlet1')
                        elif rdc(2):
                            $ run_event('store_1_ft_playlet2')
                        else:
                            $ run_event('store_1_ft_playlet3')

                "{color=#aaaaaa}Гадание (приходите завтра){/color} [shop_fortune_badge]" if fortunetelling_today:
                    jump shop.shop_buy_serive

                "Очищение ($500) [shop_cleanse_badge]" if seen("store_1_cl_firstime") and not cleansing_today:
                    if not P.buy(500, _("Очищение")):
                        jump shop.shop_menu

                    $ set_default_ui()
                    $ cleansing_today = True
                    $ cleansing_count += 1

                    if cleansing_count == 4:
                        $ run_event('store_1_bl_firstime')
                    else:

                        $ rdc = RandomChoice(2)
                        if rdc(1):
                            $ run_event('store_1_cl_playlet1')
                        elif rdc(2):
                            $ run_event('store_1_cl_playlet2')

                "{color=#aaaaaa}Очищение (приходите завтра){/color} [shop_fortune_badge]" if seen("store_1_cl_firstime") and cleansing_today:
                    jump shop.shop_buy_serive

                "Благословение ($800)" if seen("store_1_bl_firstime") and not blessing_today:
                    if not P.buy(800, _("Благословение")):
                        jump shop.shop_menu

                    $ set_default_ui()
                    $ blessing_today = True
                    $ blessing_count += 1

                    $ run_event('store_1_bl_playlet1')

                "{color=#aaaaaa}Благословение (приходите завтра){/color}" if seen("store_1_bl_firstime") and blessing_today:
                    jump shop.shop_buy_serive
                "Назад":

                    jump shop.shop_menu
        "Купите что-нибудь у нее":

            label shop.buy_wallpaper:
            $ set_shop_ui_wide()
            menu:
                "Костюм астролога Веры (Обои) ($500)" if not BackgroundSystem.data["a_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Обои")):
                        $ BackgroundSystem.data["a_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Костюм астролога Сеннин (Обои) ($500)" if not BackgroundSystem.data["b_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Обои")):
                        $ BackgroundSystem.data["b_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Костюм астролога Теодоры (Обои) ($500)" if not BackgroundSystem.data["c_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Обои")):
                        $ BackgroundSystem.data["c_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Костюм астролога Айрин (Обои) ($500)" if not BackgroundSystem.data["d_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Обои")):
                        $ BackgroundSystem.data["d_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Костюм астролога Элизы (Обои) ($500)" if not BackgroundSystem.data["e_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Обои")):
                        $ BackgroundSystem.data["e_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Костюм астролога Рэйчел (Обои) ($500)" if not BackgroundSystem.data["f_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Обои")):
                        $ BackgroundSystem.data["f_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Костюм астролога Уно (Обои) ($500)" if not BackgroundSystem.data["g_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Обои")):
                        $ BackgroundSystem.data["g_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Назад":
                    jump shop.shop_menu
        "Назад":

            pass

    $ set_default_ui()
    jump action_post

default hotel_shop_chat_count = 0
default hotel_shop_chat_today = False
default satisfy_her_need_count = 0
default satisfy_her_need_today = False
label hotel_shop:
    $ set_scene("Action")
    scene hotel_shop with tstmgr

    label hotel_shop.shop_menu:
    $ set_hotel_shop_ui()

    if seen('store_2_more_firstime', 'store_2_sex_firstime'):
        $ hotel_interact_with_badge = ""
    else:
        $ hotel_interact_with_badge = "{image=badge2}"

    menu:
        minna "Ах, это мой будущий зять~{fast}"
        "Взаимодействовать с ней [hotel_interact_with_badge]":


            label hotel_shop.interact_with:

            if not seen('store_2_more_firstime'):
                $ hotel_shop_chat_badge = "{image=badge2}"
            else:
                $ hotel_shop_chat_badge = ""

            if not seen('store_2_sex_firstime'):
                $ satisfy_her_need_badge = "{image=badge2}"
            else:
                $ satisfy_her_need_badge = ""

            menu:
                "Поговорите с ней [hotel_shop_chat_badge]" if not hotel_shop_chat_today:
                    $ set_default_ui()
                    $ hotel_shop_chat_count += 1
                    $ hotel_shop_chat_today = True

                    $ rdc = RandomChoice(3)
                    if rdc(1):
                        $ run_event('store_2_chat_1')
                    elif rdc(2):
                        $ run_event('store_2_chat_2')
                    else:
                        $ run_event('store_2_chat_3')

                "{color=#aaaaaa}Поговорите с ней (приходите завтра){/color} [hotel_shop_chat_badge]" if hotel_shop_chat_today:
                    jump hotel_shop.interact_with

                "Удовлетворите её потребность [satisfy_her_need_badge]" if what_about_me and not satisfy_her_need_today:
                    $ set_default_ui()
                    $ satisfy_her_need_count += 1
                    $ satisfy_her_need_today = True

                    $ rdc = RandomChoice(2)
                    if rdc(1):
                        $ run_event('store_2_more_playlet1')
                    else:
                        $ run_event('store_2_more_playlet2')

                "{color=#aaaaaa}Удовлетворите её потребность (приходите завтра){/color} [satisfy_her_need_badge]" if what_about_me and satisfy_her_need_today:
                    jump hotel_shop.interact_with
                "Назад":

                    jump hotel_shop.shop_menu
        "Купите что-нибудь у нее":

            label hotel_shop.buy_wallpaper:
            $ set_hotel_shop_ui_wide()
            menu:
                "Вера в Ципао (Обои) ($500)" if not BackgroundSystem.data["a_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["a_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Сеннин в Ципао (Обои) ($500)" if not BackgroundSystem.data["b_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["b_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Теодора в Ципао (Обои) ($500)" if not BackgroundSystem.data["c_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["c_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Айрин в Ципао Suit (Обои) ($500)" if not BackgroundSystem.data["d_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["d_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Элиза в Ципао (Обои) ($500)" if not BackgroundSystem.data["e_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["e_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Рэйчел в Ципао (Обои) ($500)" if not BackgroundSystem.data["f_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["f_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Уно в Ципао Wallpaper ($500)" if not BackgroundSystem.data["g_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["g_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Назад":
                    jump hotel_shop.shop_menu
        "Назад":

            pass

    $ set_default_ui()
    jump action_post

label bungalow:
    if is_day():
        scene e_love_8_8 with tstmgr
    else:
        scene e_train_inti_1_4 with tstmgr
    "Тети Элизы сейчас нет в бунгало, я точно не пойду через этот лес...."
    jump action_post

label my_room_in_hotel:
    menu:
        "Ложиться спать":
            if t.period < LateNight:
                "Слишком рано ложиться спать."
            else:
                if t.period < LateNight:
                    "Слишком рано ложиться спать."
                else:
                    $ new_day()
        "Назад":
            pass
    jump action_post

label my_room:
    hide screen bnb
    $ show_home()
    jump action_post



label course:

    if not seen('B_love_1'):
        scene class_background with tstmgr
        "Я пошел в класс и потратил некоторое время на учёбу."
        "Я пытался поговорить с Сеннин, но она все еще злилась на меня.."
        "... ... ... ..."
    else:
        scene go_to_class with tstmgr
        $ rdc = RandomChoice(3)
        if rdc(1):
            b "В конце этого урока будет викторина, не забывайте оставаться до её начала."
        elif rdc(2):
            b "Профессор сказал, что следующий экзамен не будет охватывать сегодняшнюю лекцию, так что... ..."
        else:
            b "Привет, [P]. Давай сядем вместе."
        "Я провел некоторое время в классе с Сеннин."
        "... ... ... ..."

    $ add(B, B.love, 1)
    $ time_proceed(1)
    jump action_post



default days_worked = 0
label work:

    scene go_to_work with tstmgr
    $ rdc = RandomChoice(3)
    if rdc(1):
        c "Продолжай в том же духе и очень скоро вы получите повышение."
    elif rdc(2):
        c "Если у тебя есть какие-либо вопросы, не стесняйтесь спрашивать меня в моем офисе."
    else:
        c "Ты недавно был у моей мамы? Как они с Айрин поживают?"

    "Я провел некоторое время, работая в компании."
    "... ... ... ..."

    $ add(C, C.love, 1)
    $ days_worked += 1

    if renpy.random.random() <= 0.5 and not E.love.is_locked:
        call E_inspect_work

    $ time_proceed(1)

    jump action_post

label find_C_company:

    scene expression find_bg(C) with Dissolve(0.5)

    "У меня мало времени. В чем дело?"

    $ show_find_fix(C)

    jump action_post



default B_gift = False
default D_gift = False
label street:

    if is_day():
        scene downtown_day_background
    else:
        scene downtown_night_background
    "Хотел бы я привести кого-нибудь сюда с собой… …"

    if not B_gift or not D_gift:

        label downtown_menu:
        menu:
            "Купить подарок для Сеннин ($2000)" if not B_gift:
                $ P.buy(2000, _("Gift"))
                $ B_gift = True
                jump downtown_menu
            "Купить подарок для Айрин ($5000)" if not D_gift:
                $ P.buy(5000, _("Gift"))
                $ D_gift = True
                jump downtown_menu
            "Вернуться":
                $ time_proceed(1)
                jump action_post

    jump action_post




label B_room:
    if seen("d5_2") and not seen("B_love_1"):
        scene b_school_day_unhappy with tstmgr




        b "... ... ... ..."
        $ show_map()
        jump action_post

    scene expression find_bg(B) with Dissolve(0.5)

    b "Привет, [P.name], рада видеть тебя."

    $ show_find_fix(B)

    jump action_post

label C_room:
    if is_day():
        scene croom_day_background with tstmgr
    else:
        scene croom_night_background with tstmgr

    "Это старая комната Теодоры. Здесь никто не живет после того, как она уехала из этого особняка. Но тетя Элиза по-прежнему содержит эту комнату в чистоте и порядке."
    jump action_post

label D_room:
    if not seen("D_dqsj"):
        scene void with tstmgr
        narrator "Айрин все еще злится на меня. Я должен пойти купить ей подарок, а потом вернуться к ней."
        $ show_map()
        jump pauser

    scene expression find_bg(D) with Dissolve(0.5)

    d "[P.name]!"

    $ show_find_fix(D)

    jump action_post

label E_room:
    scene expression find_bg(E) with Dissolve(0.5)

    e "Рада видеть тебя, [P]!"

    $ show_find_fix(E)

    jump action_post

label F_room:
    scene expression find_bg(F) with Dissolve(0.5)

    if F.love >= 25 and not seen("A_love_5"):
        $ Push("Больше ее истории будет разблокировано после того, как вы улучшите отношения с Верой.")

    d "[P.name]!"

    $ show_find_fix(F)

    jump action_post

label tutor:

    scene ddqsj_d5 with tstmgr
    "Я потратил некоторое время на обучение Айрин."

    $ add(D, D.love, 1)
    $ P.earn(50, _("Репетиторство"), t)
    $ time_proceed(1)

    if renpy.random.random() <= 0.5 and not E.love.is_locked:
        call E_inspect_tutor
    jump action_post



label booking:
    jump action_post




label bookstore:



    scene g_bookstore_smile with tstmgr

    g "Привет, [P]."

    g "Ты ищешь книгу?"

    player "Нет, просто зашёл проведать тебя."

    scene g_bookstore_normal with tstmgr

    g "... ... ... ..."

    $ add(G, G.love, 1)

    $ time_proceed(1)

    jump action_post

label supermarket:
    jump action_post




label exercise:

    if exercise.count_of_day == 0:
        scene go_to_sports with tstmgr
        $ rdc = RandomChoice(3)
        if rdc(1):
            f "Привет, мой друг. Я иду на пробежку. Ты со мной?"
        elif rdc(2):
            f "Не ленись. Давай пропотеем вместе."
        else:
            f "Почему ты смотришь на меня? Давай, побежали!"

        "Я провел некоторое время с Рэйчел в парке."
        "... ... ... ..."
        $ add(F, F.love, 1)
        $ time_proceed(1)
    else:
        "я слишком устал сегодня."



    jump action_post

label alley:
    scene alley_background with tstmgr
    "Темный, жуткий, опасный переулок. Зачем мне приходить сюда одному?"
    jump action_post

label beach:
    scene beach_background with tstmgr
    "Этот пляж является известным живописным местом этого города. Но как-то жалко приходить сюда одному."
    jump action_post




label G_room:

    scene expression find_bg(G) with Dissolve(0.5)

    g "... ... ... ... Привет..."

    $ show_find_fix(G)

    jump action_post

default first_A_room = True
label A_room:

    if first_A_room:
        "Сейчас мы с Верой живем по соседству. Я могу встречаться с ней каждый день."
        "Но помните, она будет в своей комнате только утром и поздно вечером каждый день, кроме воскресенья."
        "Ну, она сейчас дома, думаю, самое время с ней поболтать.."
        "(Тук, тук, тук)"
        a "Кто это?"
        player "Это я,  [P]."
        a "Ой, подожди минутку, я сейчас переоденусь."
        "Переоденусь? Так она сейчас разговаривает со мной полуголая? Это... действительно захватывает моё воображение..."
        "(Дверь открылась)"
        $ first_A_room = False

    if seen("A_love_4") and not seen("A_love_5"):
        "Она сейчас не в настроении."
        $ show_map()
        jump action_post

    scene expression find_bg(A) with Dissolve(0.5)

    $ show_find_fix(A)

    jump action_post

label C_room_2:
    if is_day():
        scene bnb_croom_background with tstmgr
        "Теодоры нет в ее комнате."
        "... ... ... ..."
    else:
        scene void with tstmgr
        "Теодора заперла дверь. Может быть, она не хочет, чтобы другие знали, что она делает."
        "... ... ... ..."
    jump action_post



label find_A_cafe:

    if seen("A_love_4") and not seen("A_love_5"):
        scene a_cafe_weird with tstmgr
        a "... ... ... ..."
        "Она сейчас не в настроении."
        $ add(A, A.love, 1)
        $ time_proceed(1)
        jump action_post

    scene cafe_background with tstmgr
    player "Привет, Вера"
    scene a_cafe_normal1 with tstmgr
    a "[P.name]?"
    a "Что бы ты хотела съесть сегодня?"
    scene cafe_background with tstmgr
    "... ... ... ..."

    $ add(A, A.love, 1)


    $ time_proceed(1)
    jump action_post


label find_A_clothing:

    if seen("A_love_4") and not seen("A_love_5"):
        scene a_dressstore_frown with tstmgr
        a "... ... ... ..."
        "Она сейчас не в настроении."
        $ add(A, A.love, 1)
        $ time_proceed(1)
        jump action_post

    if A.relation == "general":
        scene a_dressstore_weird with tstmgr
        a "... ... ... ..."
        a "Ты снова пришел..."
        scene dressstore_background with tstmgr
        "... ... ... ..."
        $ add(A, A.love, 1)
        $ time_proceed(1)
    else:


























        scene a_dressstore_smile3

        a "Привет, [P]."

        a "Спасибо, что пришёл ко мне. мне сейчас до смерти скучно."

        a "… … … …"

        $ add(A, A.love, 1)

        $ time_proceed(1)




    jump action_post


label find_A_restaurant:

    if seen("A_love_4") and not seen("A_love_5"):
        scene bar_background with tstmgr
        "... ... ... ..."
        "Вера сейчас не в настроении."
        $ add(A, A.love, 1)
        $ time_proceed(1)
        jump action_post

    scene a_restaurant_smile with tstmgr
    a "[P.name]?"
    player "Привет, Вера."
    a "Что я могу сделать для вас?"
    player "Только кружечку пива, пожалуйста. Я просто жду, когда ты закончишь работу."
    scene a_restaurant_slight_surprise with tstmgr
    a "Ох, ладно..."
    scene bar_background with tstmgr
    "... ... ... ..."

    $ add(A, A.love, 1)
    $ time_proceed(1)




    jump action_post




label hang_park:
    if is_day():
        scene park_day_background with tstmgr
    else:
        scene park_night_background with tstmgr
    "Я прогулялся по парку. Ничего особенного."

    $ time_proceed(1)
    jump action_post



label map:
    jump action_post
label hotel:
    jump action_post
label my_house:
    jump action_post
label park:
    jump action_post
label college:
    jump action_post
label mansion:
    jump action_post
label cafe:
    jump action_post
label bar:
    jump action_post
label mall:
    jump action_post
label clothing:
    jump action_post
label company:
    jump action_post

