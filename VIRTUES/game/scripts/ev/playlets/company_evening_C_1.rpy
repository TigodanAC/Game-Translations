label company_evening_C_1:

    scene company_evening_c_1_1 with tstmgr

    c "... ... ... ..."



    "Теодора is still working while everyone else had gone home."



    scene company_evening_c_1_2 with tstmgr

    c "Hmm? Why are you still here?"



    player "I... ... ... ..."



    c "Nevermind, since you are here, why don't you join me and do some extra works?"



    player "Will I get extra paid?"



    scene company_evening_c_1_3 with tstmgr

    c "No."



    player "... ... ... ..."



    player "Fine... ..."



    $ add(C, C.love, 1)



    $ P.cash.add(500)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
