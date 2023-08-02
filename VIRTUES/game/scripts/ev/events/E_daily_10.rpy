label E_daily_10:

    scene void with tstmgr
    play music happy

    "I went to the hospital this morning..."



    scene e_daily10_1 with tstmgr

    player "Doctor Connie, you have to save my life! I think I have brain cancer!"



    "This adorable big lady is Doctor Connie, a great doctor, very professional in her field."



    scene e_daily10_2 with tstmgr

    "Doctor Connie" "Wow... don’t panic, [P]. Describe your problems to me in detail."



    player "Recently I always pass out after dinner time, and sleep till the next morning."



    player "And also, I would be very tired after waking up..."



    "Doctor Connie" "That’s strange. Okay, let’s run some tests and take some graphs of your brain."



    scene void with tstmgr

    "... ... ... ..."



    "Sometime later..."



    scene e_daily10_1 with dissolve

    "Doctor Connie" "Good news for you, [P]. You are perfectly healthy. There is nothing wrong with your brain."



    player "Are you 100%% sure of that?"



    "Doctor Connie" "Yeah. I have done several tests and failed to detect anything abnormal."



    player "That’s weird. Then how do you explain my issue?"



    scene e_daily10_2 with tstmgr

    "Doctor Connie" "I... don’t really think that was caused by a malfunction of your brain."



    "Doctor Connie" "Maybe it was because of some kind of medicine? You know, drowsiness and dizziness can be side effects of many medications."



    "Doctor Connie" "And you did mention that you would only faint out during a specific time period of a day."



    player "But... I didn’t take any medication... ..."



    player "... ... ... ..."



    player "Anyway, it’s good to know that I’m still healthy. Thanks, doctor Connie. I’ll come back if things get worse."



    scene e_daily10_1 with tstmgr

    "Doctor Connie" "Good luck to you, [P]."



    scene void with tstmgr

    "Okay, if it’s not my brain, then it must be something else that causes my problem. I need to find out what it is."



    "Hmmm... ... ... ..."



    "I’ll think up a plan later. As for now, I need to go to Aunt Elisa’s house for tutoring Irene."



    "Wait... wait a sec... Aunt Elisa’s house?"



    "It seems like I would only have that brain problem when I was at Aunt Elisa’s house."



    "Is it because of something I eat there? Or is it some kind of anaphylaxis?"



    player "... ... ... ..."



    "This is so weird..."



    $ add(E, E.love, 1)

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
