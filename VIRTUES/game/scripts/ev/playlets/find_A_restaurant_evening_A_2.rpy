label find_A_restaurant_evening_A_2:

    scene bar_background with tstmgr

    player "Hi, Vera."



    scene a_restaurant_slight_surprise with tstmgr

    a "Sorry, I'm kind of busy right now. I'll talk to you later."



    player "Oh, alright, take your time."



    a "... ... ... ..."



    scene a_restaurant_smile with tstmgr

    a "You know what? Nevermind, what can I get for you today?"



    player "Don't you need to worry about the other guests?"



    a "You are also my guest..."



    a "(Whispering) My favorite guest."



    scene void with tstmgr

    "... ... ... ..."



    $ add(A, A.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
