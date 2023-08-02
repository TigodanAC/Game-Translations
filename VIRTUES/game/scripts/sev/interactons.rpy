label A_PreInteraction:



    return True

label B_PreInteraction:
    return True

label C_PreInteraction:
    return True

label D_PreInteraction:
    return True

label E_PreInteraction:
    return True

label F_PreInteraction:
    return True

label G_PreInteraction:
    return True

label TouchHead_A_general:

    scene a_general_1_frown with tstmgr

    bubble_a "Why do you want to do that?"

    bubble_b "But fine... ..."

    scene a_touchead_night_1 with tstmgr

    a "... ... ... ..."

    a "Eh... It feels... itchy..."

    scene a_touchead_night_2 with tstmgr

    a "Wait... You are too close to me."

    a "This is getting weird..."

    scene a_touchead_night_3 with tstmgr

    a "Stop..."

    a "(Slightly groaning)Ah... no..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label TouchHead_A_girlfriend:

    scene a_gf_1_default with tstmgr

    bubble_a "Touching my head?"

    bubble_a "Of course... love."

    scene a_gf_1_touchead_1 with tstmgr

    a "No one has been this nice to me before."

    a "I am so happy... ..."

    scene a_gf_1_touchead_2 with tstmgr

    a "Thanks... for being here with me."

    a "... ... ... ..."

    scene a_gf_1_touchead_3 with tstmgr

    a "You know... you can do something more if you want."

    a "I'm yours..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label TouchHead_A_sexpartner:

    scene a_gf_1_default with tstmgr

    bubble_a "Touching my head?"

    bubble_a "Of course, [P]."

    scene a_gf_1_touchead_1 with tstmgr

    a "We are like lovers... ..."

    a "I'm just saying... don't think too much..."

    scene a_gf_1_touchead_2 with tstmgr

    a "Thanks... for being here with me."

    a "... ... ... ..."

    scene a_gf_1_touchead_3 with tstmgr

    a "You know... you can do something more if you want."

    a "I won't run..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label Hug_A_general:

    scene a_general_1_frown with tstmgr

    bubble_a "Do you really think it's necessary?"

    bubble_a "... ... ... ..."

    scene a_general_1_hug_1 with tstmgr

    a "I know you are doing this to comfort me."

    a "Thank you... ..."

    scene a_general_1_hug_2 with tstmgr

    a "Your shoulder... it makes me feel safety."

    a "So warm..."

    scene a_general_1_hug_3 with tstmgr

    a "... ... ... ..."

    a "Why are you being so nice to me?"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label Hug_A_girlfriend:

    scene a_gf_1_default with tstmgr

    bubble_a "Let's do this."

    bubble_a "I want to be in your arms again..."

    scene a_gf_1_hug_1 with tstmgr

    a "Don't smile like that..."

    a "It's a little... embarrassing."

    scene a_gf_1_hug_2 with tstmgr

    a "(Moaning with pleasure) Ah... ... [P]... ..."

    a "Try not to... leave any hickey on my neck."

    scene a_gf_1_hug_3 with tstmgr

    a "I love you being aggressive to me..."

    a "(Moaning with pleasure) Ahhh... ..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label Hug_A_sexpartner:

    scene a_gf_1_default with tstmgr

    bubble_a "If you say so..."

    bubble_a "I'm happy to do that."

    scene a_gf_1_hug_1 with tstmgr

    a "Don't smile like that..."

    a "It's a little... embarrassing."

    scene a_gf_1_hug_2 with tstmgr

    a "(Moaning with pleasure) Ah... ... [P]... ..."

    a "Yes... I want more..."

    scene a_gf_1_hug_3 with tstmgr

    a "Do you like touching my butt..."

    a "(Moaning with pleasure) Ahhh... ..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label Doggie_A_girlfriend:

    scene a_gf_1_default with tstmgr

    bubble_a "Yes... I want to taste that... too."

    bubble_a "Love... ..."

    scene void with tstmgr

    "... ... ... ..."

    window hide

    scene a_love_5_26 with tstmgr

    pause

    scene a_love_5_28 with tstmgr

    pause

    scene a_love_5_27 with tstmgr

    pause

    scene a_love_5_30 with tstmgr

    a "I'm cuming~~~~~~"

    $ flashlight()

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label Doggie_A_sexpartner:

    scene a_gf_1_frown with tstmgr

    bubble_a "Okay... ..."

    bubble_a "If that is what you want."

    scene void with tstmgr

    "... ... ... ..."

    window hide

    scene a_love_5_25 with tstmgr

    pause

    scene a_love_5_28 with tstmgr

    pause

    scene a_love_5_27 with tstmgr

    pause

    scene a_love_5_30 with tstmgr

    a "I'm cuming~~~~~~"

    $ flashlight()

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label TouchHead_B_general:

    if B.clothes == 1:
        scene b_general_1_frown with tstmgr
    elif B.clothes == 2:
        scene b_general_2_frown with tstmgr

    bubble_b "Touching... my head?"
    bubble_b "Hmm... ... fine..."

    if B.clothes == 1:
        scene b_touchead_day_1 with tstmgr
    elif B.clothes == 2:
        scene b_general_2_touchead_1 with tstmgr
    b "... ... ... ..."
    b "Do you like doing this?"

    if B.clothes == 1:
        scene b_touchead_day_2 with tstmgr
    elif B.clothes == 2:
        scene b_general_2_touchead_2 with tstmgr
    b "Your hand is so big..."
    b "... ... ... ..."

    if B.clothes == 1:
        scene b_touchead_day_3 with tstmgr
    elif B.clothes == 2:
        scene b_general_2_touchead_3 with tstmgr
    b "And it feels so warm..."
    b "I actually start to like this..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label ShouderRub_C_general:

    scene c_general_1_smile with tstmgr

    bubble_c "... ... ... ..."
    bubble_c "That's... nice of you."
    bubble_c "Are you trying to please me? I won't raise your wage for this, just let you know."
    bubble_c "I'll wait you at the couch."

    scene c_sdmassage_1 with tstmgr

    c "... ... ... ..."

    c "... ... ... ... ... ..."

    scene c_sdmassage_2 with tstmgr

    c "Hmm... ..."

    scene c_sdmassage_3 with tstmgr

    c "?... ..."

    c "(He is doing it again... I should have realized it.)"

    c "... ... ... ..."

    scene c_sdmassage_2 with tstmgr

    c "(Whatever... as long as he doesn't go too far...)"

    c "... ... ... ..."

    scene void with tstmgr

    "... ... ... ..."
    jump interaction_post


label TouchHead_D_general:

    if D.clothes == 1:
        scene d_general_1_default with tstmgr
    elif D.clothes == 2:
        scene d_general_2_default with tstmgr
    bubble_d "Ha? Head touching?"
    bubble_d "Great! Let's do this."

    if D.clothes == 1:
        scene d_touchead_1 with tstmgr
    elif D.clothes == 2:
        scene d_general_2_touchead_1 with tstmgr
    d "... ... ... ..."
    d "It feels good..."

    if D.clothes == 1:
        scene d_touchead_2 with tstmgr
    elif D.clothes == 2:
        scene d_general_2_touchead_2 with tstmgr
    d "It's like... I am being petted."
    d "So relieved..."

    if D.clothes == 1:
        scene d_touchead_3 with tstmgr
    elif D.clothes == 2:
        scene d_general_2_touchead_3 with tstmgr
    d "Meow, Meow!"
    d "Do you like hearing me saying that?"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label LapPillow_E_general:

    if E.clothes == 1:
        scene e_general_1_frown with tstmgr
    elif E.clothes == 2:
        scene e_general_2_frown with tstmgr
    bubble_e "You want to... do that again?"
    bubble_e "(This poor kid is seeking for mother's love. I should help him.)"
    bubble_e "... ... ... ..."
    bubble_e "Alright, son, come here."

    if E.clothes == 1:
        scene e_lapillow_1 with tstmgr
    elif E.clothes == 2:
        scene e_general_2_lapillow_1 with tstmgr
    e "Sleep, sleep, little child..."
    e "I got you here..."

    if E.clothes == 1:
        scene e_lapillow_2 with tstmgr
    elif E.clothes == 2:
        scene e_general_2_lapillow_2 with tstmgr
    e "(Oh, his sleeping face is so lovely.)"
    e "(I always want to have my own son...)"

    if E.clothes == 1:
        scene e_lapillow_3 with tstmgr
    elif E.clothes == 2:
        scene e_general_2_lapillow_3 with tstmgr
    e "(He must be in a nice dream right now...)"
    e "(I wish to know what he is dreaming about...)"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label TouchBreasts_G_general:

    if G.clothes == 1:
        scene g_general_1_smile with tstmgr
    elif G.clothes == 2:
        scene g_general_2_smile with tstmgr

    bubble_g "Take your time, 30 seconds."

    if G.clothes == 1:

        scene g_general_1_breastouch_1 with tstmgr

        g "Just remember not to do anything... weird."

        g "... ... ... ..."

        scene g_general_1_breastouch_2 with tstmgr

        g "Be... gentle, please."

        g "Don't leave any bruise. I have a cosplay activity next week."

        scene g_general_1_breastouch_3 with tstmgr

        g "Hmm?... ..."

        g "Do you really have to take off my bra?"

        scene g_general_1_breastouch_4 with tstmgr

        g "... ... ... ..."

        g "They are... ugly, right? Ptosed like this... I wish they can be smaller."

        scene g_general_1_breastouch_5 with tstmgr

        g "Really? You like them?"

        g "Well... then... you can have, 5 more seconds, today."

        scene void with tstmgr

        "... ... ... ..."

    elif G.clothes == 2:

        scene g_general_2_breastouch_1 with tstmgr

        g "Just remember not to do anything... weird."

        g "... ... ... ..."

        scene g_general_2_breastouch_2 with tstmgr

        g "Be... gentle, please."

        g "Don't leave any bruise. I have a cosplay activity next week."

        scene g_general_2_breastouch_3 with tstmgr

        g "Why are you... holding them like holding your toys."

        g "They are heavy, aren't they?"

        scene g_general_2_breastouch_4 with tstmgr

        g "(Groaning with pleasure) Aww... ... ... ..."

        g "Nipple..."

        scene g_general_2_breastouch_5 with tstmgr

        g "(Groaning) It feels... strange..."

        g "(Groaning) Time... is... up..."

        g "Release me now..."

        scene void with tstmgr

        "... ... ... ..."

    jump interaction_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
