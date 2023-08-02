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
        posia "Hi there, the chosen one~ {fast}"
        "Buy her service [shop_buy_service_badge]":


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
                "Fortunetelling ($200) [shop_fortune_badge]" if not fortunetelling_today:
                    if not P.buy(200, _("Fortunetelling")):
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

                "{color=#aaaaaa}Fortunetelling (come tomorrow){/color} [shop_fortune_badge]" if fortunetelling_today:
                    jump shop.shop_buy_serive

                "Cleansing ($500) [shop_cleanse_badge]" if seen("store_1_cl_firstime") and not cleansing_today:
                    if not P.buy(500, _("Cleansing")):
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

                "{color=#aaaaaa}Cleansing (come tomorrow){/color} [shop_fortune_badge]" if seen("store_1_cl_firstime") and cleansing_today:
                    jump shop.shop_buy_serive

                "Blessing ($800)" if seen("store_1_bl_firstime") and not blessing_today:
                    if not P.buy(800, _("Blessing")):
                        jump shop.shop_menu

                    $ set_default_ui()
                    $ blessing_today = True
                    $ blessing_count += 1

                    $ run_event('store_1_bl_playlet1')

                "{color=#aaaaaa}Blessing (come tomorrow){/color}" if seen("store_1_bl_firstime") and blessing_today:
                    jump shop.shop_buy_serive
                "Back":

                    jump shop.shop_menu
        "Buy something from her":

            label shop.buy_wallpaper:
            $ set_shop_ui_wide()
            menu:
                "Vera's Astrologer Suit Wallpaper ($500)" if not BackgroundSystem.data["a_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["a_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Senning's Astrologer Suit Wallpaper ($500)" if not BackgroundSystem.data["b_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["b_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Теодора's Astrologer Suit Wallpaper ($500)" if not BackgroundSystem.data["c_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["c_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Irene's Astrologer Suit Wallpaper ($500)" if not BackgroundSystem.data["d_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["d_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Elisa's Astrologer Suit Wallpaper ($500)" if not BackgroundSystem.data["e_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["e_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Rachel's Astrologer Suit Wallpaper ($500)" if not BackgroundSystem.data["f_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["f_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Uno's Astrologer Suit Wallpaper ($500)" if not BackgroundSystem.data["g_store_1"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["g_store_1"].unlock_from_shop()
                    jump shop.buy_wallpaper
                "Back":
                    jump shop.shop_menu
        "Back":

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
        minna "Ah, it's my future son-in-law~{fast}"
        "Interact with her [hotel_interact_with_badge]":


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
                "Talk with her [hotel_shop_chat_badge]" if not hotel_shop_chat_today:
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

                "{color=#aaaaaa}Talk with her (come tomorrow){/color} [hotel_shop_chat_badge]" if hotel_shop_chat_today:
                    jump hotel_shop.interact_with

                "Satisfy her need [satisfy_her_need_badge]" if what_about_me and not satisfy_her_need_today:
                    $ set_default_ui()
                    $ satisfy_her_need_count += 1
                    $ satisfy_her_need_today = True

                    $ rdc = RandomChoice(2)
                    if rdc(1):
                        $ run_event('store_2_more_playlet1')
                    else:
                        $ run_event('store_2_more_playlet2')

                "{color=#aaaaaa}Satisfy her need (come tomorrow){/color} [satisfy_her_need_badge]" if what_about_me and satisfy_her_need_today:
                    jump hotel_shop.interact_with
                "Back":

                    jump hotel_shop.shop_menu
        "Buy something from her":

            label hotel_shop.buy_wallpaper:
            $ set_hotel_shop_ui_wide()
            menu:
                "Vera in Cheongsam Wallpaper ($500)" if not BackgroundSystem.data["a_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["a_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Senning in Cheongsam Wallpaper ($500)" if not BackgroundSystem.data["b_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["b_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Теодора in Cheongsam Wallpaper ($500)" if not BackgroundSystem.data["c_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["c_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Irene in Cheongsam Suit Wallpaper ($500)" if not BackgroundSystem.data["d_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["d_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Elisa in Cheongsam Wallpaper ($500)" if not BackgroundSystem.data["e_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["e_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Rachel in Cheongsam Wallpaper ($500)" if not BackgroundSystem.data["f_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["f_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Uno in Cheongsam Wallpaper ($500)" if not BackgroundSystem.data["g_store_2"].is_shop_unlocked:
                    if P.buy(500, _("Wallpaper")):
                        $ BackgroundSystem.data["g_store_2"].unlock_from_shop()
                    jump hotel_shop.buy_wallpaper
                "Back":
                    jump hotel_shop.shop_menu
        "Back":

            pass

    $ set_default_ui()
    jump action_post

label bungalow:
    if is_day():
        scene e_love_8_8 with tstmgr
    else:
        scene e_train_inti_1_4 with tstmgr
    "Aunt Elisa isn't in the bungalow right now, I'm definitely not going to walk cross that forest..."
    jump action_post

label my_room_in_hotel:
    menu:
        "Go to bed":
            if t.period < LateNight:
                "It's too early to go to bed."
            else:
                if t.period < LateNight:
                    "It's too early to go to bed."
                else:
                    $ new_day()
        "Back":
            pass
    jump action_post

label my_room:
    hide screen bnb
    $ show_home()
    jump action_post



label course:

    if not seen('B_love_1'):
        scene class_background with tstmgr
        "I went to a class and spent some time on studying."
        "I tried to talk with Senning, but she was still angry at me."
        "... ... ... ..."
    else:
        scene go_to_class with tstmgr
        $ rdc = RandomChoice(3)
        if rdc(1):
            b "There will be a quiz at the end of this class, remember not to leave early."
        elif rdc(2):
            b "The professor said that the next exam won’t cover today’s lecture, so... ..."
        else:
            b "Hi, [P]. Let’s sit together."
        "I spent some time in the class with Senning."
        "... ... ... ..."

    $ add(B, B.love, 1)
    $ time_proceed(1)
    jump action_post



default days_worked = 0
label work:

    scene go_to_work with tstmgr
    $ rdc = RandomChoice(3)
    if rdc(1):
        c "Keep working like this and you will get a promotion very soon."
    elif rdc(2):
        c "If you have any question, feel free to reach me in my office."
    else:
        c "Did you go to my mom’s house recently? How are she and Irene doing?"

    "I spent some time working in the company."
    "... ... ... ..."

    $ add(C, C.love, 1)
    $ days_worked += 1

    if renpy.random.random() <= 0.5 and not E.love.is_locked:
        call E_inspect_work

    $ time_proceed(1)

    jump action_post

label find_C_company:

    scene expression find_bg(C) with Dissolve(0.5)

    "I don't have much time. What's the matter?"

    $ show_find_fix(C)

    jump action_post



default B_gift = False
default D_gift = False
label street:

    if is_day():
        scene downtown_day_background
    else:
        scene downtown_night_background
    "I wish I could bring someone here with me… …"

    if not B_gift or not D_gift:

        label downtown_menu:
        menu:
            "Buy a gift for Senning ($2000)" if not B_gift:
                $ P.buy(2000, _("Gift"))
                $ B_gift = True
                jump downtown_menu
            "Buy a gift for Irene ($5000)" if not D_gift:
                $ P.buy(5000, _("Gift"))
                $ D_gift = True
                jump downtown_menu
            "Return":
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

    b "Hello, [P.name], it's nice to see you."

    $ show_find_fix(B)

    jump action_post

label C_room:
    if is_day():
        scene croom_day_background with tstmgr
    else:
        scene croom_night_background with tstmgr

    "This is Теодора's old room. Nobody lives here after she moved out from this mansion. But Aunt Elisa still keeps this room nice and clean."
    jump action_post

label D_room:
    if not seen("D_dqsj"):
        scene void with tstmgr
        narrator "Irene is still mad at me. I should go buy a gift for her, and then come back to her."
        $ show_map()
        jump pauser

    scene expression find_bg(D) with Dissolve(0.5)

    d "[P.name]!"

    $ show_find_fix(D)

    jump action_post

label E_room:
    scene expression find_bg(E) with Dissolve(0.5)

    e "It's good to see you, [P]!"

    $ show_find_fix(E)

    jump action_post

label F_room:
    scene expression find_bg(F) with Dissolve(0.5)

    if F.love >= 25 and not seen("A_love_5"):
        $ Push("More of her story will be unlocked after you improve relationship with Vera")

    d "[P.name]!"

    $ show_find_fix(F)

    jump action_post

label tutor:

    scene ddqsj_d5 with tstmgr
    "I spent some time on tutoring Irene."

    $ add(D, D.love, 1)
    $ P.earn(50, _("Tutorship"), t)
    $ time_proceed(1)

    if renpy.random.random() <= 0.5 and not E.love.is_locked:
        call E_inspect_tutor
    jump action_post



label booking:
    jump action_post




label bookstore:



    scene g_bookstore_smile with tstmgr

    g "Hi, [P]."

    g "Are you looking for a book?"

    player "Nope, just here to check you out."

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
            f "Hi there, my friend. I’m going for a jog. Are you with me?"
        elif rdc(2):
            f "Don’t be lazy. Let’s sweat together."
        else:
            f "Why are you staring at me? Come on, let’s go for a run!"

        "I spent some time with Rachel in the park."
        "... ... ... ..."
        $ add(F, F.love, 1)
        $ time_proceed(1)
    else:
        "I'm too tired today."



    jump action_post

label alley:
    scene alley_background with tstmgr
    "A dark, creepy, dangerous alley. Why would I come here alone?"
    jump action_post

label beach:
    scene beach_background with tstmgr
    "This beach is a famous scenic spot of this city. But it's kinda pathetic to come here alone."
    jump action_post




label G_room:

    scene expression find_bg(G) with Dissolve(0.5)

    g "... ... ... ... Hi..."

    $ show_find_fix(G)

    jump action_post

default first_A_room = True
label A_room:

    if first_A_room:
        "Now Vera and I are living next door to each other. I can meet with her every day."
        "But remember, she will be in her room only in the morning and late night every day except Sunday. "
        "Well, she is at home now, I think it may be a good time to have a chat with her."
        "(Knock, knock, knock.)"
        a "Who is this?"
        player "It's me, [P]."
        a "Oh, wait a moment, I'm changing clothes now."
        "Changing clothes? So she is now talking to me half-nakedly? That... really captures my imagination..."
        "(Door opened)"
        $ first_A_room = False

    if seen("A_love_4") and not seen("A_love_5"):
        "She is not in the mood right now."
        $ show_map()
        jump action_post

    scene expression find_bg(A) with Dissolve(0.5)

    $ show_find_fix(A)

    jump action_post

label C_room_2:
    if is_day():
        scene bnb_croom_background with tstmgr
        "Теодора is not in her room."
        "... ... ... ..."
    else:
        scene void with tstmgr
        "Теодора has locked her door. Maybe she doesn't want others to know what she is doing."
        "... ... ... ..."
    jump action_post



label find_A_cafe:

    if seen("A_love_4") and not seen("A_love_5"):
        scene a_cafe_weird with tstmgr
        a "... ... ... ..."
        "She is not in the mood right now."
        $ add(A, A.love, 1)
        $ time_proceed(1)
        jump action_post

    scene cafe_background with tstmgr
    player "Hi, Vera"
    scene a_cafe_normal1 with tstmgr
    a "[P.name]?"
    a "What would you like to eat today?"
    scene cafe_background with tstmgr
    "... ... ... ..."

    $ add(A, A.love, 1)


    $ time_proceed(1)
    jump action_post


label find_A_clothing:

    if seen("A_love_4") and not seen("A_love_5"):
        scene a_dressstore_frown with tstmgr
        a "... ... ... ..."
        "She is not in the mood right now."
        $ add(A, A.love, 1)
        $ time_proceed(1)
        jump action_post

    if A.relation == "general":
        scene a_dressstore_weird with tstmgr
        a "... ... ... ..."
        a "You came again..."
        scene dressstore_background with tstmgr
        "... ... ... ..."
        $ add(A, A.love, 1)
        $ time_proceed(1)
    else:


























        scene a_dressstore_smile3

        a "Hello, [P]."

        a "Thanks for coming to see me. I'm bored to death right now."

        a "… … … …"

        $ add(A, A.love, 1)

        $ time_proceed(1)




    jump action_post


label find_A_restaurant:

    if seen("A_love_4") and not seen("A_love_5"):
        scene bar_background with tstmgr
        "... ... ... ..."
        "Vera is not in the mood right now."
        $ add(A, A.love, 1)
        $ time_proceed(1)
        jump action_post

    scene a_restaurant_smile with tstmgr
    a "[P.name]?"
    player "Hi, Vera."
    a "What can I get for you?"
    player "Nothing but a cup of beer, please. I'm just waiting for you getting off work."
    scene a_restaurant_slight_surprise with tstmgr
    a "Oh, okay..."
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
    "I took a walk at the park. Nothing special."

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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
