label TouchHead_D_girlfriend:

    if D.clothes == 1:

        scene d_gf_1_smile with tstmgr

    if D.clothes == 2:

        scene d_gf_2_smile with tstmgr

    if D.clothes == 3:

        scene d_gf_3_smile with tstmgr

    bubble_d "Yeah, yeah! That sounds great!"



    if D.clothes == 1:

        scene d_gf_1_touchead_1 with tstmgr

    if D.clothes == 2:

        scene d_gf_2_touchead_1 with tstmgr

    if D.clothes == 3:

        scene d_gf_3_touchead_1 with tstmgr

    if D.clothes in (1, 2):

        d "Come on, come on. pat me with your hand... ..."

        d "Don't keep me waiting, or I will bite you."

    if D.clothes == 3:

        d "Come on, come on. pat me with your hand... ..."

        d "Don't keep the kitty waiting, or the kitty will bite you..."

    if D.clothes == 1:

        scene d_gf_1_touchead_2 with tstmgr

    if D.clothes == 2:

        scene d_gf_2_touchead_2 with tstmgr

    if D.clothes == 3:

        scene d_gf_3_touchead_2 with tstmgr

    if D.clothes == 1:

        d "Wuuuuuuuu... ... ... ..."

        d "Yes, yes, reward me for being a good little sister~~"

    if D.clothes == 2:

        d "Wuuuuuuuu... ... ... ..."

        d "Yes, yes, reward me for being your good student~~"

    if D.clothes == 3:

        d "Ohhh... ... sorry, I said the wrong words. Cough~ cough~"

        d "Please... forgive me... master... ..."

    if D.clothes == 1:

        scene d_gf_1_touchead_3 with tstmgr

    if D.clothes == 2:

        scene d_gf_2_touchead_3 with tstmgr

    if D.clothes == 3:

        scene d_gf_3_touchead_3 with tstmgr

    if D.clothes == 1:

        d "Now can you give your little sister a kiss?"

        d "Onii sama~~~~"

    if D.clothes == 2:

        d "Now can you give your student a kiss?"

        d "Mr. [P]~~~~"

    if D.clothes == 3:

        d "Yes, yes... ... Punish me~~ Play with my body as you want, master~~"

        d "This is what the naughty kitty deserves~~~"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
