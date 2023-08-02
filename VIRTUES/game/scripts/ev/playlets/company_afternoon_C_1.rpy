label company_afternoon_C_1:

    scene company_afternoon_c_1_1 with tstmgr

    c "[P]."



    c "... ... ... ..."



    scene company_afternoon_c_1_2 with tstmgr

    c "[P]!"



    player "(Suddenly awake) What? What happened?"



    player "Oh... ... ... ..."



    player "Sorry, I know I was not supposed to nap at work. I was too tired."



    scene company_afternoon_c_1_1 with tstmgr

    c "... ... ... ..."



    c "I will spare you for this time. Keep working."



    scene void with tstmgr

    "... ... ... ..."



    $ add(C, C.love, 1)



    $ P.cash.add(500)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
