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
    call screen hint("Теперь игра формально начинается. Наслаждайся жизнью!")
    call screen tutorial(2, 4) with Dissolve(0.5)
    jump post_event_post

label post_jjsj:


    $ P.ie_suffix = _("/Неделя")
    $ P.ie_short_suffix = ("/Нед")



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
    call screen hint("Теперь Вы можете построить подвальный бассейн в своем доме. Вам придется заплатить несколько раз, чтобы его закончить. Каждый раз будет стоить Вам 200$.")
    jump post_event_post

label post_A_daily_5:
    call screen hint("Теперь вы можете сделать уборку в вашем доме. За это вы получите несколько советов и, возможно, найдете некоторые... секреты дома.")
    jump post_event_post




label auto_sleep_prologue:
    scene void with Dissolve(0.5)
    window show wipeup(.2)
    "Уже поздно, мне пора спать."
    window hide wipedown(.2)
    menu:
        "Ложиться спать":

            pass
    jump event_post

label auto_sleep:
    scene void with Dissolve(0.3)
    window show wipeup(.2)
    "Уже поздно, мне пора спать."
    window hide wipedown(.2)

    $ show_home()
    jump event_post

label sleep_event:
    if t.period < LateNight:
        "Слишком рано ложиться спать."
    else:

        $ new_day()
    jump label_post


label pay_bill:



    $ P.cash._value -= 1500

    if P.cash._value < 0:
        $ P.cash._value = 0

    $ Push("Вы заплатили 1500$ по счетам")

    jump event_post

label wage:
    $ temp_wage = days_worked * 50 * (0.85 + 0.15*C.love.stage)
    if temp_wage > 0:
        "Я только что получил свою зарплату."
        $ P.earn( temp_wage, "Зарплата", t )
    jump event_post

label earn:
    $ P.earn(get_bnb_revenue(), "B&B Бизнес")
    jump event_post


label w2_d6_1_hint:
    call screen hint("Прямо сейчас нечего делать на выходных, так как вы не построили близких отношений ни с одной из девушек. Вы можете просто нажать на верхний правый угол и пропустить эти выходные.")
    jump event_post





label first_company:
    "Эта компания принадлежит семье Теодоры. Я не знаю, почему я здесь."
    return

label E_inspect_work:
    scene void with tstmgr
    narrator "... ... ... ..."
    narrator "В то время, когда я был на работе, в компанию вошла тетя Элиза и издалека наблюдала за мной."
    scene e_office_smile with tstmgr
    e "(Он очень усердно работает...)"
    e "(И я вижу, как его обожают коллеги-девушки. Такой обаятельный молодой человек.)"
    $ add(E, E.love, 1)
    return

label E_inspect_tutor:
    scene void with tstmgr
    narrator "... ... ... ..."
    narrator "В то время, когда я занимался с Айрин, тетя Элиза тихонько открыла дверь и заглянула внутрь."
    scene e_droom_smile with tstmgr
    e "([P] делает довольно хорошую работу по обучению Айрин.)"
    e "(Он терпелив и нежен, как и его отец.)"
    $ add(E, E.love, 1)
    return

label first_lose_credit_sj:

    "... ... ... ..."

    narrator "Теперь я столкнулся с серьезной проблемой ..."

    narrator "У меня нет достаточно денег, чтобы оплатить счета на этой неделе."

    narrator "Пока это не большая проблема, потому что я могу просто занять немного денег у своих богатых друзей. И мне даже не нужно возвращать их. Для них это небольшие деньги, ничего страшного."

    narrator "Но я не могу продолжать в том же духе. Если я буду слишком полагаться на помощь своих друзей, мой кредит доверия и репутация будут снижены. Люди будут думать, что я полный неудачник без богатства моего отца."

    narrator "Это не то, чего я хочу."

    narrator "Я должен работать усерднее, чтобы решить этот финансовый вопрос самостоятельно. Посмотрим, как пойдут дела на следующей неделе."

    jump event_post

label lose_credit_sj:

    "... ... ... ..."

    "У меня недостаточно денег, чтобы оплатить счета на этой неделе."

    "Пока это не большая проблема, потому что я могу просто занять немного денег у своих богатых друзей. И мне даже не нужно возвращать их. Для них это небольшие деньги, ничего страшного."

    "Но я не могу продолжать в том же духе. Если я буду слишком полагаться на помощь своих друзей, мой кредит доверия и репутация будут снижены. Люди будут думать, что я полный неудачник без богатства моего отца."

    "Это не то, чего я хочу."

    "Я должен работать усерднее, чтобы решить этот финансовый вопрос самостоятельно. Посмотрим, как пойдут дела на следующей неделе."

    jump event_post



label reset_shop:
    $ fortunetelling_today = False
    $ cleansing_today = False
    $ blessing_today = False
    $ hotel_shop_chat_today = False
    $ satisfy_her_need_today = False
    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
