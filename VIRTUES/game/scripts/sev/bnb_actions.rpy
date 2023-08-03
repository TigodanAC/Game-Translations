label basic_room:
    jump action_post

default first_clean = True
default clean_count = 0
label clean:
    if first_clean:
        "Чтобы привлечь гостей, мы не брали с них никакой платы за уборку. Но если я смогу убраться в спальнях гостей с их разрешения, они, возможно, дадут мне чаевые."
        $ first_clean = False

    if is_day():
        scene home_livingroom_day_background with tstmgr
    else:
        scene home_livingroom_night_background with tstmgr
    narrator "Я немного убрался в доме и получил чаевые от гостей."

    $ time_proceed(1)
    $ P.earn (50.0, "Чаевые")
    $ clean_count += 1
    jump action_post

label decorate:

    jump action_post

label new_room:

    jump action_post

label new_facility:

    jump action_post

label frontyard:
    scene home_frontyard_day_background with tstmgr
    "Я проверил, всё вроде в порядке."
    jump action_post

label livingroom:
    if is_day():
        scene home_livingroom_day_background with tstmgr
    else:
        scene home_livingroom_night_background with tstmgr
    "Я проверил вокруг, кажется всё в порядке."
    jump action_post

label free_money:
    "... ... ... ..."
    "Почему на диване сумка?"
    "А что там внутри?.."
    "Пачка наличных?"
    "Ещё и есть записка..."
    "Небольшая помощь от разработчиков. Удачи в жизни (*^▽^*)"
    "... ... ... ..."
    "Кто такие эти разработчики? Всё это так странно."
    "Но... Думаю, я все равно возьму эти деньги."
    "... ... ... ..."
    $ P.cash.add(2000)
    $ free_money = True
    jump action_post

label kitchen:
    scene home_kitchen_day_background with tstmgr
    "Я проверил вокруг, кажется всё в порядке."
    jump action_post

label bathroom:
    scene home_shower_day_background with tstmgr
    "Я проверил вокруг, кажется всё в порядке."
    jump action_post

label toilet:

    "Я проверил вокруг, кажется всё в порядке."
    jump action_post

default build_pool_count = 0
label build_pool:
    scene void with tstmgr
    "Я потратил несколько часов на строительство бассейна... ..."
    $ build_pool_count += 1
    $ time_proceed(1)
    jump action_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
