label mansion_tutor_evening_D_1:

    scene void with tstmgr

    "This evening, I was tutoring Айрин in her room... ..."



    scene rcsj_d13 with tstmgr

    d "It is already late. I think you should stay here for tonight, [P]."



    player "Eh, I'd like to, but I have other things to do."



    d "What things?"



    player "I need to pick up a friend after she gets off work."



    scene rcsj_d14 with tstmgr

    d "A she?"



    player "Don't think too much, now concentrate on your homework."



    scene rcsj_d13 with tstmgr

    d "... ... ... ..."



    d "Fine... ..."



    $ add(D, D.love, 1)



    $ P.cash.add(100)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
