label company_forenoon_E_1:

    scene company_forenoon_e_1_1 with tstmgr

    c "Mom? Why are you here?"



    e "Just to check you and [P] out."



    "Wow, they look like sisters rather than mother and daughter."



    scene company_forenoon_e_1_2 with tstmgr

    e "How's your work, [P]?"



    player "Eh, I'm doing fine. Thanks for asking, Aunt Elisa."



    e "That's good to know."



    scene void with tstmgr

    "... ... ... ..."



    $ add(E, E.love, 1)



    $ P.cash.add(500)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
