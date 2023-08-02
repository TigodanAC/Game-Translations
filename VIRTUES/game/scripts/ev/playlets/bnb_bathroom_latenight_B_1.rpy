label bnb_bathroom_latenight_B_1:

    scene bnb_bathroom_latenight_b_1_1 with tstmgr

    b "Thanks for letting me use your bathroom."



    player "You are always welcome."



    player "It's late, you can stay here for a night if you want."



    scene bnb_bathroom_latenight_b_1_2 with tstmgr

    b "... ... ... ..."



    b "But... ... ... ..."



    player "You can sleep in my... ..."



    a "Cough, cough."



    scene bnb_bathroom_latenight_b_1_3 with tstmgr

    a "Сеннин can sleep with me."



    scene bnb_bathroom_latenight_b_1_4 with tstmgr

    b "Yeah, I'd love to."



    scene bnb_bathroom_latenight_b_1_5 with tstmgr

    a "Come with me, I'll show you the room. We can have girl's talk all night."



    scene void with tstmgr

    player "... ... ... ..."



    player "Okay then... ..."



    $ add(B, B.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
