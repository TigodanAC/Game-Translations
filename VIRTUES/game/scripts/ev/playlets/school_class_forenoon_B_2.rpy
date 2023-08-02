label school_class_forenoon_B_2:

    scene school_class_afternoon_b_1_2 with tstmgr

    b "Seriously, [P], I know you are having a tough time..."



    b "But you can't just sleep at class all the time."



    player "Hmmm... ... ... ..."



    player "You are right. I was just too tired, sorry."



    b "... ... ... ..."



    scene school_class_forenoon_b_1_1 with tstmgr

    b "Don't worry, let's go to my place after class and I will help you review."



    player "But I prefer to do something else with you at your place... ..."



    scene school_class_afternoon_b_1_2 with tstmgr

    b "Huh?... ... ... ..."



    $ add(B, B.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
