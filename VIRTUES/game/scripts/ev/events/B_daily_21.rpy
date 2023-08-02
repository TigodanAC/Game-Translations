label B_daily_21:



    scene void with tstmgr
    play music happy

    "... ... ... ..."



    scene b_daily21_1 with dissolve

    "Lady Minna" "Hmmm? Isn’t this my dearest boy?"



    player "Lady Minna? Good afternoon, and... ..."



    "I noticed there is a head hiding behind Lady Minna."



    player "Sen?"



    b "Hi, [P]~"



    scene b_daily21_2 with tstmgr

    "Lady Minna" "... ... ... ..."



    "Lady Minna" "Why don’t you just go give your man a hug, little lemon?"



    scene b_daily21_3 with tstmgr

    b "No... ... ... ..."



    "It looks like Senning is quite shy when her mother is around."



    "Lady Minna" "Western boys prefer girls to be more outgoing. [P] will get tired of you soon if you keep being so inactive."



    scene b_daily21_4 with tstmgr

    b "No way, [P] won't get tired of me~"



    scene b_daily21_5 with tstmgr

    "Lady Minna" "Ha... you won’t be so confident once you see your opponents."



    scene b_daily21_6 with tstmgr

    b "Opponents?"



    scene b_daily21_7 with tstmgr

    e "Ah-rah, what a coincidence~"



    c "[P]... and Senning?"



    "Lady Minna" "Here we go... ..."



    scene b_daily21_8 with tstmgr

    e "*Noticing Minna* Hmmmmm?"



    scene b_daily21_9 with tstmgr

    e "We have... met before, right, ma’am?"



    "Lady Minna" "Yeah, five years ago on a fashion week. You bought a cheongsam from me, remember now?"



    scene b_daily21_10 with tstmgr

    e "Oh yeah! You are Lady Minna, the Cheongsam Queen!"



    scene b_daily21_11 with tstmgr

    "Lady Minna" "Glad to see you still remember my name, Elisa~"



    "The two ladies hit it off straight away and soon acted like they are best friends..."



    scene void with tstmgr

    "... ... ... ..."



    scene b_daily21_12 with dissolve

    player "I can’t tell if they are really that close or they are just acting to be... ..."



    "Теодора answered with a shrug."



    scene b_daily21_13 with tstmgr

    e "Oh~~ look at you, so young and so beautiful, just like 5 years ago. I’m so jealous~"



    scene b_daily21_14 with tstmgr

    "Lady Minna" "Shut up~ I am somebody’s grandaunt now~"



    scene b_daily21_13 with tstmgr

    e "That doesn’t mean anything. People will mistake you as my daughter if we walk together~"



    scene b_daily21_14 with tstmgr

    "Lady Minna" "Nope, I’m not going to walk with you. You will take all the limelight away from me~"



    player "... ... ... ..."



    scene b_daily21_15 with tstmgr

    player "Wanna go for some ice cream?"



    c "Yeah, why not."



    player "... ... ... ..."



    label B_daily_21_choice_1:

    menu:
        "Take Senning’s hand":


            scene b_daily21_16 with tstmgr

            player "*Taking Senning’s hand* Let’s go then~"

            b "[P]~~~"

            c "Huh... ... ... ..."
        "Take Теодора’s hand":




            scene b_daily21_17 with tstmgr

            player "*Taking Теодора’s hand* Let’s go then~"

            c "*Being slightly surprised* Huh... ..."

            b "*Murmuring* Opp... opponent... ... ... ..."
        "Take their hands at the same time":




            scene b_daily21_18 with tstmgr

            player "Alright, let’s go then~"

            c "*Being slightly surprised* Huh... ..."

            b "O... okay~~"



    scene void with tstmgr

    "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
