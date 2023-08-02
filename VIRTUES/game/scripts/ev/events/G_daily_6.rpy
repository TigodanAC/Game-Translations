label G_daily_6:

    scene g_daily7_1 with tstmgr
    play music happy

    a "Уно, you got a new package."



    scene g_daily7_2 with tstmgr

    g "Thanks, Вера. It must be another cosplay costume I ordered online."



    scene g_daily7_1 with tstmgr

    a "Oh, really?"



    scene g_daily7_3 with tstmgr

    a "I wonder what it is like... It must be beautiful."



    scene g_daily7_2 with tstmgr

    g "... ... ... ..."



    g "I can put it on now so you can have a look~"



    scene g_daily7_4 with tstmgr

    a "Really? That would be great! Thanks, Уно~"



    a "Owww~ I've never seen a professional coser dressed up in person before! I'm so excited!"



    a "I once dressed like Wonder Woman for Halloween, but this is different, right?"

    scene void with tstmgr

    "... ... ... ..."



    "Sometime later..."



    scene g_daily7_5 with tstmgr

    g "How do you like it?"



    scene g_daily7_6 with tstmgr

    a "Wow! You look so pretty!"



    scene g_daily7_7 with tstmgr

    a "But is it too revealing to dress like this in the public?"



    scene g_daily7_8 with tstmgr

    g "It's just a bikini. If we can wear bikinis on the beach, why can’t we do that at a comic-con?"



    scene g_daily7_9 with tstmgr

    a "That’s... a good point."



    scene g_daily7_10 with tstmgr

    g "... ... ... ..."



    g "Would you like to try the suit on? I have another suit just like it in a different color."



    scene g_daily7_6 with tstmgr

    a "Oh! Can I?"



    scene g_daily7_8 with tstmgr

    g "Of course, you are welcome."



    g "We have similar body types so... I think it will fit you well."



    scene void with tstmgr

    "... ... ... ..."



    "... ... ... ... ... ..."



    "Later tonight..."



    player "Ahh... ... that was a great shower. Time to go to bed now."



    "*Opening the door* ... ... ... ..."



    player "Emmmmm???"



    scene g_daily7_11 with dissolve

    a "Ah, he is back!"



    g "The evil lord has returned to this world!"



    player "Eh... hello?"



    scene g_daily7_12 with tstmgr

    g "Take this!"



    scene g_daily7_12 with tstmgr

    $ flashlight()

    player "Oh, ouch~"



    player "Hey, stop! What are you two doing?"



    scene g_daily7_14 with tstmgr

    a "We are bikini fighters, the mightiest heroes in the world!"



    g "Now you should get prepared, evil lord sir. We're going to beat you so you can't harass innocent women anymore!"



    player "This world is definitely fucked if its mightiest heroes are two girls in bikinis"



    player "But, eh... ... okay, I get it. A role play game, ha..."



    player "So... I am supposed to be the bad guy?"



    scene g_daily7_13 with tstmgr

    $ flashlight()

    a "Yeah!~~ Take this!"



    player "Wait, wait, ouch! Stop, it is dangerous, okay?"



    scene g_daily7_11 with tstmgr

    player "Fine, girls, you successfully got me irritated. Now I’m going to let you know what the evil lord is capable of!"



    scene g_daily7_15 with tstmgr

    $ flashlight()

    a "Ahhhh~~~"



    g "That’s not how the plot goes... ..."



    a "Yeah, the evil lord never wins~"



    player "Well, guess today is my lucky day then."



    player "Submit to me, ladies, or I’ll show you no mercy."



    scene g_daily7_16 with tstmgr

    g "Never~ Bikini fighters forever!"



    player "Well, Then prepare to feel my wrath!~"



    scene g_daily7_17 with tstmgr

    $ flashlight()

    "Girls" "Ahhhhhhhhh!!!~~~~~~~~"



    "I threw them on my bed like throwing two bean bags. They are just too light compared to me."



    player "Now you all have become my captives."



    scene g_daily7_18 with tstmgr

    a "You may capture us, but you will never make us surrender!"



    g "What are you going to do with us?"



    player "Ha, you are about to find out."



    scene g_daily7_20 with tstmgr

    $ flashlight()

    "Girls" "HAHAHAAAAAHAA! HAHAAAAA!!~~~~~"



    "I put my hands on their bellies and tickled them like two puppies."



    a "Stop! Stop!~~"



    g "Haahahaa! It’s so itchy!~"



    player "... ... ... ..."



    scene g_daily7_21 with tstmgr

    "The feeling of their flat quivering bellies is amazing. Damn, my dick is getting hard right now."



    "And they seemed to enjoy my touching, what should I do next?"



    label G_daily_6_choice_1:

    menu:
        "Ask them to submit":


            player "Last chance, ladies, submit to me!"

            scene g_daily7_19 with tstmgr

            g "Okay, okay, just stop tickling us, please."

            a "We submit, we submit~~"

            player "Alright then, now kneel down to me and say that you are sorry."

            scene g_daily7_25 with tstmgr

            g "Kneel... down?"

            a "It sounds a little creepy..."

            scene g_daily7_20 with tstmgr

            "Girls" "*Being tickled* Ahhaaaaahahahahah!! Haahahahahahha!~~~"

            a "Stop! We’ll do what you say!~"

            scene void with tstmgr

            "... ... ... ..."

            scene g_daily7_22 with dissolve

            g "Sorry, evil lord sir."

            a "We will never disobey you again..."

            player "*Swallowing hard* ... ... ... ..."

            "Will they... really obey whatever I say?"

            scene g_daily7_23 with tstmgr

            player "I... ..."

            scene g_daily7_24 with tstmgr

            a "Alright, game is over. Do you want to have some ice cream, Уно?"

            g "Yeah, I’d love to~"

            scene g_daily7_26 with tstmgr

            "The two girls then got up and left the room like I wasn’t there."

            player "Ehhhh... ... ... ..."

            scene g_daily7_27 with tstmgr

            "Ha... What was I thinking... Of course it was only a game."

            player "*Shouting* Can I get some ice cream, too?"

            a "*Shouting* No~ only for girls~"

            player "But... ... ... ..."

            player "*Murmuring* But I’m the evil lord, damn it... ... ... ..."

            scene void with tstmgr

            "... ... ... ..."
        "Punish them":




            if A.harem < 10 or G.harem < 10:

                "The further plot will be unlocked after Вера and Уно's harem acceptance levels reach 10."

                "You can always replay this event in the ‘subplot replay’ button located in your bedroom."

                jump G_daily_6_choice_1
            else:


                player "Last chance, ladies, submit to me!"

                scene g_daily7_19 with tstmgr

                g "Okay, okay, just stop tickling us, please."

                a "We submit, we submit~~"

                player "Alright then, now kneel down to me and say that you are sorry."

                scene g_daily7_25 with tstmgr

                g "Kneel... down?"

                a "It sounds a little creepy..."

                scene g_daily7_20 with tstmgr

                "Girls" "*Being tickled* Ahhaaaaahahahahah!! Haahahahahahha!~~~"

                a "Stop! We’ll do what you said!~"

                scene void with tstmgr

                "... ... ... ..."

                scene g_daily7_22 with dissolve

                g "Sorry, evil lord sir."

                a "We will never challenge you again..."

                player "Alright, I’ll forgive you after you get your punishment."

                a "The punishment?"

                player "Yes! You will pay for your disobedience!"

                scene g_daily7_28 with tstmgr

                $ flashlight()

                "Girls" "Yaaaaahhhhhhh!!~~~~~~"

                player "Seriously, what do you think you can do with these bikini armors?"

                g "According to the anime, these are the best armors in the world. Even a nuclear bomb can’t harm us!"

                player "Hah, but can they protect you from this?"

                scene g_daily7_29 with tstmgr

                "I put my hands on their pussies and started to rub them roughly."

                "Girls" "Owwwwwww~~~~~~~"

                scene g_daily7_30 with tstmgr

                a "What are you doing? This is... too much... for a prank... ..."

                scene g_daily7_31 with tstmgr

                g "Yes, yes, keep doing... ... No, I mean, stop doing this!"

                a "I... I’m going to get angry~~"

                scene g_daily7_32 with tstmgr

                a "Wait, Ohhh, Awwwww~~~ that spot~~~~"

                g "Вера... ... ... ..."

                scene g_daily7_33 with tstmgr

                g "Ahhhhhhh!~~~~ it feels so comfortable!~"

                g "Please~~~ stop~~~ evil lord sir~~~ You are making us feel strange!~~~"

                player "... ... ... ..."

                "Yeah, I guess this should be enough for now. I'm surprised they were even okay with me fondling their pussies together in the first place. I shouldn't push them any further. They'll probably be really embarrassed if I make them cum in front of each other."

                scene g_daily7_34 with tstmgr

                player "Alright, the punishment is done. Do you have anything to say?"

                g "We are so sorry, evil lord sir~~"

                a "We will never disobey you again... ..."

                player "That’s my good girls... ..."

                scene g_daily7_35 with tstmgr

                "Girls" "Hee hee... ... ... ..."

                scene void with tstmgr

                "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
