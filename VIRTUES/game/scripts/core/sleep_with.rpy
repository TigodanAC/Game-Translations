default sleepers = set()
init python:
    def update_sleepers():
        old_sleepers = sleepers.copy()
        if seen("A_love_5"):
            sleepers.add(A.code)
        if seen("C_daily_12"):
            sleepers.add(C.code)
        if seen("G_love_6"):
            sleepers.add(G.code)
        for nz in (sleepers - old_sleepers):
            Push('Теперь вы можете спать с {} по ночам.'.format(get(nz)))

default sleep_A_count = 0
label sleep_A:

    $ sleep_A_count += 1

    $ rdc = RandomChoice(3)

    if rdc(1):
        scene sleep_a_1 with tstmgr
        player "Оууу... Вера... ты так хороша в этом..."
        narrator "... ... ... ..."
    elif rdc(2):
        scene sleep_a_2 with tstmgr
        a "У меня завтра есть дела, [P.name]. Не... делай это слишком долго."
    else:
        scene sleep_a_3 with tstmgr
        a "Стоп... Я хочу спать..."
        "... ... ... ..."

    $ new_day()

    jump label_post

default sleep_C_count = 0
label sleep_C:

    $ sleep_C_count += 1

    $ rdc = RandomChoice(3)

    if rdc(1):
        scene sleep_c_1 with tstmgr
        c "(Говорит во сне) Айрин... Я не делаю за тебя домашку... ..."
        "... ... ... ..."
    elif rdc(2):
        scene sleep_c_2 with tstmgr
        c "Подожди~~ Не играйся с моим соском!~~~"
        "... ... ... ..."
    else:
        scene sleep_c_3 with tstmgr
        c "Спокойной ночи, мой маленький девственник~"
        "... ... ... ..."

    $ new_day()

    jump label_post

default sleep_G_count = 0
label sleep_G:

    $ sleep_G_count += 1

    $ rdc = RandomChoice(3)

    if rdc(1):
        scene sleep_g_1 with tstmgr
        g "Подожди, подожди, ещё рано спать~ Ночь ещё только начинается~"
        "... ... ... ..."
    elif rdc(2):
        scene sleep_g_2 with tstmgr
        g "Оооооооу~~~~~ Да, ДАА, продолжай трахать меня в том же духе~~"
        "... ... ... ..."
    else:
        scene sleep_g_3 with tstmgr
        g "(Говорит во сне) Курица... ... жареная курица... ..."
        "... ... ... ..."

    $ new_day()

    jump label_post

label sleep_ACG:

    $ rdc = RandomChoice(3)

    if rdc(1):
        scene sleep_acg_1 with tstmgr
        player "Хрррррр~~ Хрррррр~ Хрррррр~~~"
        "... ... ... ..."
    elif rdc(2):
        scene sleep_acg_2 with tstmgr
        player "Оууу~ Как хорошо иметь гарем~"
        "... ... ... ..."
    else:
        scene sleep_acg_3 with tstmgr
        c "На этот раз... Я продержусь дольше, чем Вера~"
        "... ... ... ..."

    $ new_day()

    jump label_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
