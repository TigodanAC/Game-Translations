label mansion_bathroom:
    scene mansion_bathroom_background with tstmgr
    "Это главная ванная в этом доме. Она, наверное, даже больше, чем моя комната."
    jump action_post

label mansion_toilet:
    scene mansion_toilet_background with tstmgr
    "Это всего лишь туалет."
    jump action_post

label mansion_guestroom:
    scene mansion_guestroom_background with tstmgr
    "Я жил в этой комнате. Ах… здесь полно воспоминаний."
    jump action_post

label mansion_pool:
    if is_day():
        scene mansion_swimpool_day_background with tstmgr
    else:
        scene mansion_swimpool_night_background with tstmgr
    "Почему я здесь, в пустом бассейне?"
    jump action_post

label mansion_livingroom:
    "Я проверил вокруг, всё кажется в порядке."
    jump action_post

label college_bathroom:
    "Это женская ванная. Я не могу попасть внутрь."
    jump action_post

label campus:
    scene school_day_background with tstmgr
    "Я некоторое время гулял по кампусу в одиночестве."
    jump action_post

label library:
    scene library_background with tstmgr
    "Я какое-то время занимался в библиотеке в одиночестве."
    $ time_proceed(1)
    jump action_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
