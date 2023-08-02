label downtown_evening_E_1:

    scene downtown_evening_e_1_1 with tstmgr

    e "Thank you for coming with me, [P]. It has been so long since the last time I went shopping with a male."



    scene downtown_evening_e_1_2 with tstmgr

    e "If you find anything you like on this street, just buy it. I’ll pay."



    player "That’s... very generous of you..."



    scene downtown_evening_e_1_1 with tstmgr

    e "So what is on your mind? A suit? A watch? A pair of shoes maybe?"



    player "Eh... I... ..."



    player "We haven’t eaten anything tonight so... how about I buy you a dinner?"



    scene downtown_evening_e_1_3 with tstmgr

    e "[P]... ... ... ..."



    scene downtown_evening_e_1_4 with tstmgr

    e "You are such a thoughtful kid! Auntie loves you!~~"



    scene void with tstmgr

    "... ... ... ..."



    $ add(E, E.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
