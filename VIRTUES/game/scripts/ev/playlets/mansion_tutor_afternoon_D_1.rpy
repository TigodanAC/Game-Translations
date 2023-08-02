label mansion_tutor_afternoon_D_1:

    scene rcsj_d14 with tstmgr

    d "Ahhhhh... ... I hate math!"



    player "Calm down, it is just a simple question."



    player "Be patient, and you will find the right solution."



    scene rcsj_d15 with tstmgr

    d "... ... ... ..."



    d "Okay, but you need to reward me if I solve this question by myself."



    player "What do you want?"



    scene rcsj_d16 with tstmgr

    d "I want to play my cellphone for 10 minutes!"



    player "... ... ... ..."



    $ add(D, D.love, 1)



    $ P.cash.add(100)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
