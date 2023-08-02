label bookstore_afternoon_B_1:

    scene g_daily2_9 with tstmgr

    b "Good afternoon, [P]."



    player "Hello, Sen, how's your work here?"



    b "Not bad. People are all friendly here. I can feel that my English speaking skill is improving fast."



    player "I'm happy to hear that, Sen."



    b "So... ... do you want to buy a book?"



    b "Comics, Mangas, Novels... ... Everything you want."



    player "Why don't you give me a tour?"



    scene void with tstmgr

    "... ... ... ..."



    $ add(B, B.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
