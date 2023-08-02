label school_campus_forenoon_F_1:

    scene void with tstmgr

    "I was wandering in the campus with Рэйчел."



    scene school_day_background with tstmgr

    player "So, what's your favorite movie?"



    scene f_school_day_frown with tstmgr

    f "Hmm? I have never thought of that. Why asking?"



    player "Just want to get to know more about you."



    scene f_school_day_wink with tstmgr

    f "Oh yeah, we are friends."



    scene f_school_day_frown with tstmgr

    f "But... ... I don't think I have a favorite movie. Sorry."



    scene f_school_day_wink with tstmgr

    f "I can tell you my favorite fitness Youtuber if you want."



    player "Oh, eh... ..."



    player "Okay, I guess... ..."



    $ add(F, F.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
