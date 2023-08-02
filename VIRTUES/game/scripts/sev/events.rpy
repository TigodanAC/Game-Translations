label weekend_plan_tutorial:
    $ show_map()
    $ UI.show()
    $ weekend_button_displaying = True
    call screen tutorial(5, 5) with Dissolve(0.5)
    jump event_post

label reset_days_worked:
    $ days_worked = 0
    jump event_post

label pay_room:
    $ P.pay(P.expanses[0].value, P.expanses[0].name)
    jump event_post




default bLine = True

label post_d1_1:
    $ show_map()
    call screen hint("Now the game formally begins. Enjoy your life!")
    call screen tutorial(2, 4) with Dissolve(0.5)
    jump post_event_post

label post_jjsj:


    $ P.ie_suffix = _("/Week")
    $ P.ie_short_suffix = ("/Wk")



    $ P.cash._value = 0.0

    $ show_map()
    call screen bigclock

    jump post_event_post

default G_MoveIn_Room_Change = False
label post_G_MoveIn:
    if seen("G_MoveIn") and not G_MoveIn_Room_Change:
        $ G_MoveIn_Room_Change = True
        $ store.player_rooms["basic_room"] -= 1
    jump post_event_post

label post_F_daily_1:
    $ exercise.add_count_of_day()
    jump post_event_post
label post_F_daily_2:
    $ exercise.add_count_of_day()
    jump post_event_post
label post_F_love_2:
    $ exercise.add_count_of_day()
    jump post_event_post

label post_C_daily_13:
    call screen hint("Now you can build the basement pool in your house. You will have to do that for several times to finish it. Each time will cost you $200.")
    jump post_event_post

label post_A_daily_5:
    call screen hint("Now you can do the cleaning in you house. You will earn some tips by doing that and you may find some... secrets of the house as well.")
    jump post_event_post




label auto_sleep_prologue:
    scene void with Dissolve(0.5)
    window show wipeup(.2)
    "It's late, I should go to bed."
    window hide wipedown(.2)
    menu:
        "Go to bed":

            pass
    jump event_post

label auto_sleep:
    scene void with Dissolve(0.3)
    window show wipeup(.2)
    "It's late, I should go to bed."
    window hide wipedown(.2)

    $ show_home()
    jump event_post

label sleep_event:
    if t.period < LateNight:
        "It's too early to go to bed."
    else:

        $ new_day()
    jump label_post


label pay_bill:



    $ P.cash._value -= 1500

    if P.cash._value < 0:
        $ P.cash._value = 0

    $ Push("You paid $1500 for Land Tax & Maintenance Cost")

    jump event_post

label wage:
    $ temp_wage = days_worked * 50 * (0.85 + 0.15*C.love.stage)
    if temp_wage > 0:
        "I just received my wage."
        $ P.earn( temp_wage, "Wage", t )
    jump event_post

label earn:
    $ P.earn(get_bnb_revenue(), "B&B Business")
    jump event_post


label w2_d6_1_hint:
    call screen hint("Right now there is nothing much to do in the weekend since you haven't built a close relationship with any girl. You can just click the top right corner and skip this weekend.")
    jump event_post





label first_company:
    "This company is owned by Теодора's family. I don't know why I'm here."
    return

label E_inspect_work:
    scene void with tstmgr
    narrator "... ... ... ..."
    narrator "At the time when I was at work, Aunt Elisa came in the company and observed me in a distance."
    scene e_office_smile with tstmgr
    e "(He works really hard...)"
    e "(And I can see how his girl colleagues adore him. Such a charming young man he is.)"
    $ add(E, E.love, 1)
    return

label E_inspect_tutor:
    scene void with tstmgr
    narrator "... ... ... ..."
    narrator "At the time when I was tutoring Irene, Aunt Elisa opened the door with a crack quietly and looked inside."
    scene e_droom_smile with tstmgr
    e "([P] is doing quite a good job at teaching Irene.)"
    e "(He is patient and gentle, just like what his father used to be.)"
    $ add(E, E.love, 1)
    return

label first_lose_credit_sj:

    "... ... ... ..."

    narrator "Now I have encountered a serious issue..."

    narrator "I don't have enough money to pay this week's bills."

    narrator "It is not a big problem for now, because I can just go borrow some money from my rich friends. And I don't even need to repay them. It's just a small money to them, no big deal."

    narrator "But I can't keep doing it that way. If I rely on my friends' help too much, my credit and reputation will all be reduced. People will think that I am a total loser without my dad's wealth."

    narrator "That's not what I want."

    narrator "I have to work harder to solve this financial issue by myself. Let's see how things will go next week."

    jump event_post

label lose_credit_sj:

    "... ... ... ..."

    "I don't have enough money to pay this week's bills."

    "It is not a big problem for now, because I can just go borrow some money from my rich friends. And I don't even need to repay them. It's just a small money to them, no big deal."

    "But I can't keep doing it that way. If I rely on my friends' help too much, my credit and reputation will all be reduced. People will think that I am a total loser without my dad's wealth."

    "That's not what I want."

    "I have to work harder to solve this financial issue by myself. Let's see how things will go next week."

    jump event_post



label reset_shop:
    $ fortunetelling_today = False
    $ cleansing_today = False
    $ blessing_today = False
    $ hotel_shop_chat_today = False
    $ satisfy_her_need_today = False
    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
