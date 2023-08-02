label cafe_forenoon_A_1:

    scene a_cafe_normal1 with tstmgr

    player "Hi, Вера."



    a "Hi... ..."



    a "What would you like to eat today?"



    player "Nothing but two large hot chocolate. One is for you."



    a "... ... ... ..."



    scene a_cafe_smile2 with tstmgr

    a "Thanks..."



    a "Just go have a seat and I will be there soon."



    scene void with tstmgr

    "... ... ... ..."



    $ add(A, A.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
