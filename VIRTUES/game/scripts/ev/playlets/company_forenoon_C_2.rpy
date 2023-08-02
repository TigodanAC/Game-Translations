label company_forenoon_C_2:

    scene company_afternoon_c_1_1 with tstmgr

    c "[P], fill up these files and bring them to my office."



    player "Eh, okay, manager, will do it right away."



    c "... ... ... ..."



    player "Eh... ... Anything else?"



    c "No, nothing. Keep working."



    scene void with tstmgr

    player "... ... ... ..."



    $ add(C, C.love, 1)



    $ P.cash.add(500)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
