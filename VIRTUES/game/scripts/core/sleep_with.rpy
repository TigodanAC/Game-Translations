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
            Push('You can now sleep with {} at night.'.format(get(nz)))

default sleep_A_count = 0
label sleep_A:

    $ sleep_A_count += 1

    $ rdc = RandomChoice(3)

    if rdc(1):
        scene sleep_a_1 with tstmgr
        player "Oww... Vera... you are so good at this..."
        narrator "... ... ... ..."
    elif rdc(2):
        scene sleep_a_2 with tstmgr
        a "I have work to do tomorrow, [P.name]. Don't... make it too long."
    else:
        scene sleep_a_3 with tstmgr
        a "Stop... I want to sleep..."
        "... ... ... ..."

    $ new_day()

    jump label_post

default sleep_C_count = 0
label sleep_C:

    $ sleep_C_count += 1

    $ rdc = RandomChoice(3)

    if rdc(1):
        scene sleep_c_1 with tstmgr
        c "(Talking in the dream) Irene... I'm not doing your homework for you... ..."
        "... ... ... ..."
    elif rdc(2):
        scene sleep_c_2 with tstmgr
        c "Wait~~ Don't play with my nipple!~~~"
        "... ... ... ..."
    else:
        scene sleep_c_3 with tstmgr
        c "Have a good night, my little virgin~"
        "... ... ... ..."

    $ new_day()

    jump label_post

default sleep_G_count = 0
label sleep_G:

    $ sleep_G_count += 1

    $ rdc = RandomChoice(3)

    if rdc(1):
        scene sleep_g_1 with tstmgr
        g "Wait, wait, don't sleep yet~ The night is still young~"
        "... ... ... ..."
    elif rdc(2):
        scene sleep_g_2 with tstmgr
        g "Awwwwwwww~~~~~ yes, yes, keep fucking me like that~~"
        "... ... ... ..."
    else:
        scene sleep_g_3 with tstmgr
        g "(Talking in the dream) chicken... ... fried chicken... ..."
        "... ... ... ..."

    $ new_day()

    jump label_post

label sleep_ACG:

    $ rdc = RandomChoice(3)

    if rdc(1):
        scene sleep_acg_1 with tstmgr
        player "Zzzzzzzz~~ Zzzzzzz~ Zzzzzzz~~~"
        "... ... ... ..."
    elif rdc(2):
        scene sleep_acg_2 with tstmgr
        player "Awww~ It's so good to have a harem~"
        "... ... ... ..."
    else:
        scene sleep_acg_3 with tstmgr
        c "This time... I will hold longer than Vera~"
        "... ... ... ..."

    $ new_day()

    jump label_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
