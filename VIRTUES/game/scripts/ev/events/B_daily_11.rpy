label B_daily_11:

    scene void with tstmgr
    play music happy

    "Another day at school, heading to class right now, normal as usual, nothing special."



    "Except that..."



    scene b_daily11_1 with tstmgr

    b "Can you... slow down for a little bit?"



    "Except that I’m holding Сеннин’s hand for the first time in my life."



    scene b_daily11_2 with tstmgr

    b "We still have time, no need to rush."



    player "Oh... sorry."



    scene b_daily11_3 with tstmgr

    b "And is it necessary to hold my hand all the way?"



    b "I feel... a little embarrassed."



    player "I think you will have to get used to this, since now we are together."



    b "... ... ... ..."



    scene b_daily11_4 with tstmgr

    b "Okay... ..."



    if B.relation == "girlfriend":

        player "I want every people to see that you are my girlfriend now."

    if B.relation == "sexpartner":

        player "I want every people to see that you are mine now."



    b "Is that a showing off?"



    player "Hmm... yep."



    player "You don’t like it?"



    b "I... ... ... ..."



    b "Just... do whatever you want..."



    scene void with tstmgr

    "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
