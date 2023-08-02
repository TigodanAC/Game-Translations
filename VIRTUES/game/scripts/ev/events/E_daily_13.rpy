label E_daily_13:

    scene void with tstmgr
    play music happy

    "It seems like Vera is talking with someone in the hallway. I should probably go take a look..."



    scene e_daily13_1 with dissolve

    player "Elis... ... Aunt Elisa?"



    scene e_daily13_2 with tstmgr

    e "Hi, [P]. This is the first time I visit your house. What a nice place~"



    e "And you got a really nice roommate here... ..."



    scene e_daily13_3 with tstmgr

    a "You are too kind, Mrs. Shinyrost~"



    a "I’m going to prepare for lunch now, see you later~"



    e "See you, honey~"



    scene e_daily13_4 with tstmgr

    "... ... ... ..."



    player "So... what brings you here, Aunt Elisa?"



    scene e_daily13_5 with tstmgr

    e "... ... ... ..."



    e "I still can’t believe I’m doing this, but... ..."



    scene e_daily13_6 with tstmgr

    e "Here... ..."



    "She handed me a key."



    e "It is... the key to that bungalow. I think you should have it..."



    scene e_daily13_7 with tstmgr

    e "*Murmuring* So... when you want to spend some time with me... alone... again, we can... ... meet there... ..."



    "Elisa’s face was red like a teenage girl who finally mustered up the courage to talk with her first crush. I have never seen this strong lady being so shy like this before."



    player "Thanks, Auntie, I’ll take it."



    scene e_daily13_8 with tstmgr

    e "And... don’t tell others about that place. That is... a secret between us."



    player "I’m sure I won’t... ..."



    scene e_daily13_9 with tstmgr

    e "*Relieved smiling* ... ... ... ..."



    e "Okay, that’s it. I should go now..."



    player "Don’t you want to stay here for the lunch? Vera is really good at cooking..."



    e "I need to go to meet with Теодора now. So... ..."



    player "Oh, okay... ..."



    e "Bye, honey~"



    scene void with tstmgr

    "... ... ... ..."

    $ add(E, E.love, 1)

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
