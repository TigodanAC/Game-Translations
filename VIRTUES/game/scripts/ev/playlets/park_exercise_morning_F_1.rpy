label park_exercise_morning_F_1:

    scene void with tstmgr

    "I encountered with Rachel in the park this morning."



    scene f_wood_smile2 with tstmgr

    f "Hi there, my friend. I’m going for a jog. Are you with me?"



    player "Eh... ... yeah, sure."



    scene f_wood_frown with tstmgr

    f "Why do you sound like you are already tired?"



    f "Are you not happy hanging with me?"



    player "No... absolutely not... ..."



    player "It's just... too early. I'm still half asleep."



    scene f_wood_wink with tstmgr

    f "Oh, okay. Don't worry, you will feel better after a 20-minute jogging."



    scene void with tstmgr

    "... ... ... ..."



    $ add(F, F.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
