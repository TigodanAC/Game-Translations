label bnb_livingroom_morning_A_3:

    scene bnb_livingroom_morning_a_1_1 with tstmgr

    a "Good morning."



    player "Morning, Vera."



    a "Breakfast will be good in a minute, you can wait at the table."



    player "Can I get a morning kiss?"



    scene bnb_livingroom_morning_a_3_1 with tstmgr

    a "... ... ... ..."



    player "Come on, there is no other people around."



    a "Fine... ..."



    scene bnb_livingroom_morning_a_3_2 with tstmgr

    a "(Kissing) Wummmm... ... ... ..."



    scene bnb_livingroom_morning_a_3_3 with tstmgr

    a "Alright, now stop interrupting me, go to the table."



    scene void with tstmgr

    "... ... ... ..."



    $ add(A, A.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
