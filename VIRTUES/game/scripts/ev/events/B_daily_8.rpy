label B_daily_8:

    scene void with tstmgr
    play music happy

    "There is something about Senning that bothers me these days."



    "Does this girl really like me or not?"



    "We go to class every day, study together, and always hang out with each other."



    "And... ..."



    scene b_date1_13 with tstmgr

    pause

    scene b_love3_6 with tstmgr

    pause

    scene b_love4_14 with tstmgr

    pause



    scene void with tstmgr

    "Our relationship is kind of ambiguous right now, but I still cannot be sure about how she thinks of me."



    "Am I a potential lover, or only a best friend?"



    scene b_daily8_1 with dissolve

    player "... ... ... ..."



    player "(It’s so hard to guess a girl’s mind.)"



    player "(Hmmm... what should I do?)"



    scene b_daily8_2 with tstmgr

    "*Patting sound*..."



    scene b_daily8_3 with tstmgr

    player "Uh?"



    scene b_daily8_4 with tstmgr

    "I turned my head a little. And at the next second, my face was lightly poked by a soft finger."



    scene b_daily8_5 with tstmgr

    b "Got you."



    player "Senning?"



    b "Oh. Did I just interrupt your meditation?"



    player "Meditation?"



    player "Eh... Why do you think I was meditating?"



    b "You stood in front of the pool, steady like a sculpture. If it was not a meditation, then you must be thinking about something troubling."



    player "... ... ... ..."



    player "Yeah... you are right. There is indeed something that troubles me."



    scene b_daily8_6 with tstmgr

    b "Do you want to share?"



    player "... ... ... ..."



    b "... ... It’s okay if you don’t want to talk. But if there is anything I can do, please let me know."



    player "... ... ... ..."



    scene b_daily8_7 with tstmgr

    player "Oh, Sen..."



    "I could not help embracing her in my arms. This girl is an angel."



    b "Wait... ..."



    "Her body is light and small. I feel like I am holding a vulnerable china doll."



    label B_daily_8_choice_1:

    menu:
        "Kiss her forehead":


            scene b_daily8_8 with tstmgr

            player "*Kissing*... ..."

            b "(Surprised moaning) Yah!... ..."

            player "... ... ... ..."

            scene b_daily8_7 with tstmgr

            b "Why did you kiss me?"

            player "Eh... I don’t know. It just naturally happened."

            scene b_daily8_9 with tstmgr

            b "(Seems a little angry) Wmmm... ... ..."

            b "You can’t just kiss a girl without a reason. That’s rude!"

            player "Sorry... ..."

            scene b_daily8_10 with tstmgr

            b "... ... ... ..."

            scene b_daily8_11 with tstmgr

            b "(Whispering) The next time... be sure to have a good reason..."

            player "Sen... ... ... ..."

            scene b_daily8_12 with tstmgr

            b "*Sniffing, sniffing*... ..."

            scene b_daily8_11 with tstmgr

            b "Are you using a new perfume?"

            b "It smells... really good."

            player "Yeah, I’m glad you like it."

            b "... ... ... ..."

            b "Anyway. Now I need to see a professor in his office. See you later."

            player "See you then."

            scene void with tstmgr

            "... ... ... ..."
        "Pat her head":




            scene b_daily8_13 with tstmgr

            player "*Patting*... ..."

            b "(Surprised moaning) Yah!... ..."

            player "... ... ... ..."

            scene b_daily8_7 with tstmgr

            b "Why are you doing this?"

            player "Eh... I don’t know. You look too adorable, I can’t help."

            scene b_daily8_11 with tstmgr

            b "(Seems a little happy) Hmmm... ... ..."

            b "You really think... that I am adorable?"

            player "Yep, definitely, without a doubt."

            b "... ... ... ..."

            b "(Whispering) Thank you... ..."

            scene b_daily8_12 with tstmgr

            b "*Sniffing, sniffing*... ..."

            b "Are you using a new perfume?"

            scene b_daily8_11 with tstmgr

            b "It smells... really good."

            player "Yeah, I’m glad you like it."

            b "... ... ... ..."

            b "Anyway. Now I need to see a professor in his office. See you later."

            player "See you then."

            scene void with tstmgr

            "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
