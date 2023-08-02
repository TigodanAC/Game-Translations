label TV_D_general:

    if D.clothes == 1:

        scene d_general_1_default with tstmgr

    if D.clothes == 2:

        scene d_general_2_default with tstmgr







    bubble_d "Great! It’s time for a break."

    bubble_d "You are the best, [P]!"



    if D.clothes == 1:

        scene d_general_1_watchtv_1 with tstmgr

    if D.clothes == 2:

        scene d_general_2_watchtv_1 with tstmgr







    d "... ... ... ..."

    d "It’s like I’m sitting on a sofa monster."



    if D.clothes == 1:

        scene d_general_1_watchtv_2 with tstmgr

    if D.clothes == 2:

        scene d_general_2_watchtv_2 with tstmgr







    d "Oww... itchy... ..."

    d "Bad sofa, bad sofa..."



    if D.clothes == 1:

        scene d_general_1_watchtv_3 with tstmgr

    if D.clothes == 2:

        scene d_general_2_watchtv_3 with tstmgr







    d "But nevermind. I like the way you kissing my face."

    d "My skin is softer than Theo, don’t you think?"

    jump interaction_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
