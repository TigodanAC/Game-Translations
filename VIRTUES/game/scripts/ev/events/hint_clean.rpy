label hint_clean:

    scene void with tstmgr
    play music happy

    "Morning, while I was cleaning the house with Vera..."



    scene hint_clean_1 with dissolve

    a "You know, there is something strange about this house..."



    player "What do you mean?"



    scene hint_clean_2 with tstmgr

    a "Don't you think the livingroom and the kitchen are a little bit... too small for such a big house?"



    player "... ... ... ..."



    "I think she has a point. I have never seen a big house with such a small livingroom and kitchen before. It's like... someone built a wall and cut them in the middle."



    player "I don't know... I will see if I can get a layout map of this house."



    scene void with tstmgr

    "... ... ... ..."

    call screen hint("You will have to do the cleaning for a few more times to discover what is hidden in your house.")

    call screen hint("There will always be a red dot on the button of 'cleaning'. It will be gone after you discover something.")

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
