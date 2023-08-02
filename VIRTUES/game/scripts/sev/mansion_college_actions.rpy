label mansion_bathroom:
    scene mansion_bathroom_background with tstmgr
    "This is the main bathroom of this house. It is probably even bigger than my room."
    jump action_post

label mansion_toilet:
    scene mansion_toilet_background with tstmgr
    "This is just a toilet."
    jump action_post

label mansion_guestroom:
    scene mansion_guestroom_background with tstmgr
    "I used to live in this room. Ah… full of memories here."
    jump action_post

label mansion_pool:
    if is_day():
        scene mansion_swimpool_day_background with tstmgr
    else:
        scene mansion_swimpool_night_background with tstmgr
    "Why am I here in an empty swimming pool?"
    jump action_post

label mansion_livingroom:
    "I checked around, everything seems fine."
    jump action_post

label college_bathroom:
    "This is a ladies' bathroom. I can't get inside."
    jump action_post

label campus:
    scene school_day_background with tstmgr
    "I spent some time walking around the campus myself."
    jump action_post

label library:
    scene library_background with tstmgr
    "I spent some time studying in the library myself."
    $ time_proceed(1)
    jump action_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
