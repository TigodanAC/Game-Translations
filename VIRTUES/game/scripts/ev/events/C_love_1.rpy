label C_love_1:

    scene void with tstmgr
    play music happy

    c "... ... ... ..."



    player "... ... ... ... ... ..."



    c "... ... ... ..."



    player "... ... ... ... ... ..."



    scene c_love_1_1 with dissolve

    c "... ... ... ..."



    player "... ... ... ... ... ..."



    "Let me explain what's going on here."



    "Sometime earlier, I was sent to deliver a document to the other floor. And then I ran into Теодора at an elevator."



    "Being with Теодора alone is the least thing I want to do at this moment. I have known this girl since I was 5, and now she is my supervisor. This is so... embarrassing."



    "And you know what is even more embarrassing?"



    "The freaking elevator was broken! We are stuck together! Unbelievable!"



    "To be fair, being stuck in an elevator is not a big deal. I don't have claustrophobia, and I am pretty sure this situation will be fixed in at most 30 minutes. But God, why do I have to be stuck with Теодора!"



    c "... ... ... ..."



    player "... ... ... ... ... ..."



    "The breathtaking silence."



    c "Why are you acting like I am a serial killer or something?"



    player "Ah? Am I?"



    c "Yeah, is it torture to you to stay with me alone?"



    player "No... ..."



    player "It’s just... ... I don’t really know how to get along with my supervisor. I mean, I never had a supervisor before."



    scene c_love_1_2 with tstmgr

    c "Huh... ... ... ..."



    c "Honestly, I don’t know how to get along with you now, either."



    scene c_love_1_3 with tstmgr

    c "(Murmuring) I never knew... how to get along with you... ..."



    player "What did you say?"



    scene c_love_1_4 with tstmgr

    c "Nothing... Forget it..."



    scene c_love_1_5 with tstmgr

    c "I miss the old you. The old you was a jerk, but at least a funny jerk. You would talk a lot in this situation and keep me from getting bored."



    c "And now... ... you are just boring."



    player "Now you are my superior, so... ... I can’t act like before. I don’t want to offend you."



    scene c_love_1_5 with tstmgr

    c "Sigh... ... nevermind..."



    scene c_love_1_4 with tstmgr

    player "You know, I never got a chance to ask... ..."



    player "We used to be close back in highschool, but why you never contacted me again after you went to college? What happened?"



    c "... ... ... ..."



    c "I was busy."



    player "I wrote you, but you never replied. Do you hate me or something?"



    scene c_love_1_5 with tstmgr

    c "... ... No, I just didn't want to waste my time on a playboy."



    player "That's not fair. I'm a better person than you think."



    scene c_love_1_4 with tstmgr

    c "... ... ... ..."



    scene c_love_1_6 with tstmgr

    c "Well, great, now you work for me and you have the chance to prove yourself~"



    player "I definitely will."



    scene c_love_1_7 with tstmgr

    c "... ... ... ..."



    c "Let’s do a test on your honesty then~"



    scene c_love_1_8 with tstmgr

    "She suddenly came closer to me and put a hand on my chest."



    c "Say you don’t love me."



    player "What are you talking about?"



    c "Your heartbeat will be dramatically faster when you are lying. I knew that since you were 13. Now say it~ Let me see how honesty you are~"



    label C_love_1_choice_1:

    menu:
        "I don’t love you":


            scene c_love_1_9 with tstmgr

            c "Hmmmmm hum... ... ... ..."

            c "You are really a bad liar~"

            player "Wait, that was not fair. My heartbeat got fast only because you were too close to me."

            scene c_love_1_8 with tstmgr

            c "Whatever. I got the answer I want anyway~ playboy~"

            player "... ... ... ..."
        "I love you":




            scene c_love_1_11 with tstmgr

            c "What?... ..."

            scene c_love_1_10 with tstmgr

            c "I... ... ... ..."

            "Did I see it wrong or did she really just flush?"

            c "That was tricky... ... You almost got me."

            c "... ... ... ..."



    scene void with tstmgr

    "The elevator started moving again at the time when we were talking. We soon reached our floor and left the room..."



    "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
