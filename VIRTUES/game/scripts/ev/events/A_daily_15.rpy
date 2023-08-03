label A_daily_15:


    scene void with tstmgr

    play music happy

    if seen("G_love_1"):
        jump A_daily_15.line_c
    else:
        jump A_daily_15.line_d

    jump event_post

label A_daily_15.end:

    stop music fadeout 1.0

    jump event_post

label A_daily_15.line_c:

    "*The following plot is from Vera’s perspective*"



    scene a_daily15_1 with dissolve

    g "Good morning, Vera... ..."



    scene a_daily15_2 with tstmgr

    a "Oh, hi, Uno~ Why are you up so early today?"



    scene a_daily15_3 with tstmgr

    g "*Yawning* Ah... ... hh... ...hhh... ..."



    scene a_daily15_4 with tstmgr

    g "I just got up to pee... ... Will... go back to my bed right away."



    a "Oh, do you want anything for breakfast?"



    scene a_daily15_5 with tstmgr

    g "No, I’m fine, mommy, thank you for asking~"



    scene a_daily15_6 with tstmgr

    a "Mommy... ... I am not that old!~"



    g "Hee hee~~~"



    g "I’m sure you will be a great mommy after you have a kid~"



    scene a_daily15_7 with tstmgr

    a "A... kid... ..."



    g "How can you get up so early every day and still be full of energy? Life is so not fair~"



    g "See you tonight, have a good day~"



    scene a_daily15_8 with tstmgr

    a "You have a good dream~"



    "Uno left the living room and went to sleep again."



    scene a_daily15_9 with tstmgr

    a "... ... ... ..."



    scene a_daily15_10 with tstmgr

    a "(Hummm~ It’s about time to wake [P] up~)"



    scene a_daily15_11 with tstmgr

    a "... ... ... ..."



    scene a_daily15_12 with tstmgr

    a "(Wait a second... ... I feel... ...)"



    scene a_daily15_13 with tstmgr

    a "(Ewwwwww... ... I... I think I’m going to vomit... ...)"



    scene void with tstmgr

    "Vera ran to the toilet as fast as she could and even forgot to turn off the gas oven..."



    "... ... ... ..."





    "10 minutes later... ..."



    scene a_daily15_14 with dissolve

    a "*Left the toilet* Ah... ... This is strange, it never happened before."



    scene a_daily15_15 with tstmgr

    a "Do I have a stomach problem?"



    a "Or... ... ... ..."



    a "Was that actually a morning sickness?"



    scene a_daily15_16 with tstmgr

    a "I... didn’t have my period this month either."



    a "Am I... pregnant?"



    scene a_daily15_5 with flashback

    g "I’m sure you will be a great mommy after you have a kid~"



    scene a_daily15_16 with flashback

    a "Oh dear... ... ... ..."



    scene a_daily15_17 with tstmgr

    a "Am I going to be a mother?"



    scene void with tstmgr

    "... ... ... ..."

    jump A_daily_15.end

label A_daily_15.line_d:

    "*The following plot is from Vera’s perspective*"



    scene a_daily15_1 with dissolve

    "BnB Guest" "Good morning, Vera... ..."



    scene a_daily15_2 with tstmgr

    a "Oh, hi, Mrs. Smith~ The breakfast is about ready~"



    "BnB Guest" "Ah, I really would like to have it, but I’m going to an interview now, so... ..."



    scene a_daily15_8 with tstmgr

    a "It’s okay~ Good luck with the interview. You can do it!"



    "BnB Guest" "I will, thanks..."



    "BnB Guest" "... ... ... ..."



    "BnB Guest" "I wish I could have a mom like you... ..."



    scene a_daily15_6 with tstmgr

    a "Huh?"



    "BnB Guest" "Oh, I mean... you are such a virtuous woman, I’ve only been here for a few days but you have already given me a feeling of being cared for like a family... ..."



    "BnB Guest" "I’m sure you will be a great mom after you have a kid~"



    scene a_daily15_7 with tstmgr

    a "A... kid... ..."



    "BnB Guest" "Anyway, see you tonight, Vera, have a good day~"



    scene a_daily15_8 with tstmgr

    a "You too, Mrs. Smith~"



    "The lady guest then left the house for the interview... ..."



    scene a_daily15_9 with tstmgr

    a "... ... ... ..."



    scene a_daily15_10 with tstmgr

    a "(Hummm~ It’s about time to wake [P] up~)"



    scene a_daily15_11 with tstmgr

    a "... ... ... ..."



    scene a_daily15_12 with tstmgr

    a "(Wait a second... ... I feel... ...)"



    scene a_daily15_13 with tstmgr

    a "(Ewwwwww... ... I... I think I’m going to vomit... ...)"



    scene void with tstmgr

    "Vera ran to the toilet as fast as she could and even forgot to turn off the gas oven..."



    "... ... ... ..."



    "10 minutes later... ..."



    scene a_daily15_14 with dissolve

    a "*Left the toilet* Ah... ... This is strange, it never happened before."



    scene a_daily15_15 with tstmgr

    a "Do I have a stomach problem?"



    a "Or... ... ... ..."



    a "Was that actually a morning sickness?"



    scene a_daily15_16 with tstmgr

    a "I... didn’t have my period this month either."



    a "Am I... pregnant?"



    scene a_daily15_6 with flashback

    "BnB Guest" "I’m sure you will be a great mom after you have a kid~"



    scene a_daily15_16 with flashback

    a "Oh dear... ... ... ..."



    scene a_daily15_17 with tstmgr

    a "Am I really going to be a mother?"



    scene void with tstmgr

    "... ... ... ..."

    jump A_daily_15.end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
