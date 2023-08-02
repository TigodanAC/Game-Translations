label basic_room:
    jump action_post

default first_clean = True
default clean_count = 0
label clean:
    if first_clean:
        "In order to attract guests, we didn't charge them for any cleaning fee. But if I can clean their bedrooms with permission, maybe they will tip me some."
        $ first_clean = False

    if is_day():
        scene home_livingroom_day_background with tstmgr
    else:
        scene home_livingroom_night_background with tstmgr
    narrator "I cleaned the house for a little bit, and earned some tip from the guests."

    $ time_proceed(1)
    $ P.earn (50.0, "Tip")
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
    "I checked around, everything seems fine."
    jump action_post

label livingroom:
    if is_day():
        scene home_livingroom_day_background with tstmgr
    else:
        scene home_livingroom_night_background with tstmgr
    "I checked around, everything seems fine."
    jump action_post

label free_money:
    "... ... ... ..."
    "Why is there a bag on the couch."
    "And what inside it is..."
    "A stack of cash?"
    "And there is a note..."
    "A little help from devs. Good luck on your life (*^▽^*)"
    "... ... ... ..."
    "What are devs? This is so weird."
    "But... I think I'm going to take this money anyway."
    "... ... ... ..."
    $ P.cash.add(2000)
    $ free_money = True
    jump action_post

label kitchen:
    scene home_kitchen_day_background with tstmgr
    "I checked around, everything seems fine."
    jump action_post

label bathroom:
    scene home_shower_day_background with tstmgr
    "I checked around, everything seems fine."
    jump action_post

label toilet:

    "I checked around, everything seems fine."
    jump action_post

default build_pool_count = 0
label build_pool:
    scene void with tstmgr
    "I spent some hours on building the pool... ..."
    $ build_pool_count += 1
    $ time_proceed(1)
    jump action_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
