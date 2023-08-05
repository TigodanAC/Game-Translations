label start:
    scene void with Dissolve(0.4)

    window show
    "Как твоё имя, ещё раз?"
    window hide

    $ P_state.name = "Аганг" if renpy.variant("pc") else "Лео"
    call screen name_input(prompt=_(""), prefix="Я ", suffix=".")

    $ hotel_room_rent = Attr(500.0, name=_("Аренда комнаты"))
    $ P.ie_suffix = _("/День")
    $ P.ie_short_suffix = _("/Д")
    $ P.expanses.append(hotel_room_rent)



    menu:
        "Начать с самого начала":
            $ run_event('d1_1')
        "Пропустить пролог":

            $ fake_run('d4_1_bLine', 'd4_4_bLine', 'd5_2_bLine', 'd5_4_bLine')
            $ fake_run('d4_3', 'A_dgsjhx', 'd8_1', 'A_daily_1', 
                    'A_swdgsj', 'd5_3', 'B_love_1', 'd7_1', 'd1_1', 'D_dqsj', 'd3_1', 'A_wsdgsj', 
                    'A_wsdgsjhx', 'd6_1', 'A_love_1', 'A_xwdgsj', 'd2_1', 'd2_5',
                    'pcsj', 'pcsjhx', 'bjsj', 'sbsj', 'jjsj'
                )
            $ bLine = True
            $ B_gift, D_gift = True, True

            $ A.love.meter._value = 5.0
            $ B.love.meter._value = 5.0

            $ P.cash.value = 0
            $ P.virtue.value = 49

            $ set_time(Time(week=8, day=Monday, period=Morning))

            $ _on_event_complete()

    $ set_scene("Map")
    $ show_map()
    jump pauser

