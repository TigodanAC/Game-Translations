label B_daily_17:

    scene void with tstmgr
    play music sorrow

    "Senning stayed with her mother in the hotel room last night. Now it’s time to pay them a visit."



    scene b_daily17_1 with tstmgr

    b "Ah, [P]! Welcome!~"



    player "Hi, Sen, and..."



    player "Good afternoon, Lady Minna."



    "Lady Minna" "Uh-huh~"



    "Lady Minna" "We have been waiting for you for a long time. Come here, sit with me."



    b "I’ll go make you some tea~"



    scene b_daily17_2 with tstmgr

    "... ... ... ..."



    "I took a seat next to Lady Minna..."



    scene b_daily17_3 with tstmgr

    "Lady Minna" "Senning told me a lot about you last night. Thank you for taking care of her during these years. I mean it."



    player "It’s fine... ..."



    scene b_daily17_4 with tstmgr

    "Man... Senning has told me about her conservative family culture, but her mother doesn’t seem to be a conservative person at all. Look at those legs... ..."



    scene b_daily17_5 with tstmgr

    player "So... Lady Minna, would you like to tell me about how you are going to make Senning stay in this country after her graduation?"



    scene b_daily17_6 with tstmgr

    "Lady Minna" "Coming straight to the point, hah, I like it~"



    "Lady Minna" "Well, it’s not hard at all. I have many ways."



    scene b_daily17_7 with tstmgr

    "Lady Minna" "You see, Senning’s father has many offsprings and Senning is his favorite. He wants her to get back and help him run the family business."



    "Lady Minna" "So what I need to do is just to convince him that she is able to help even if she stays here. For example, I can suggest he expand his business to your country and let Senning take charge of it."



    scene b_daily17_8 with tstmgr

    "Lady Minna" "But that will be quite... I don’t know, irresponsible, right? Throwing millions of dollars into a new market that doesn’t belong to us just to make you two stay together? It’s like a childish romantic novel by a teenage writer. The real world doesn’t work that way."



    player "Yeah... ..."



    scene b_daily17_9 with tstmgr

    "Lady Minna" "So let’s be more realistic. There is an easier and cheaper way~"



    player "Which is?"



    scene b_daily17_10 with tstmgr

    "Lady Minna" "Just go make her pregnant within a year."



    player "What? Are you serious?"



    "Lady Minna" "As I said, senning is her father’s favorite offspring. He won’t be so cruel to break you up and make her child grow up without a father."



    scene b_daily17_11 with tstmgr

    "Lady Minna" "Also, as you know, we are a conservative family. Being a single mother is not acceptable there. Senning will have to stay with you if she gets pregnant."



    player "Conservative... ... hah... ..."



    scene b_daily17_12 with tstmgr

    "Lady Minna" "So what do you say?~"



    player "... ... ... ..."



    label B_daily_17_choice_1:

    menu:
        "I’ll try my best":


            player "I... I didn’t plan to have a child at such a young age, but... ... if it is for Senning, I will try my best."

            "Lady Minna" "Good... ..."

            player "... ... ... ..."
        "... ... ... ...":




            player "... ... ... ..."



    player "Wait, I just noticed one thing..."



    player "You said Senning’s father has many offsprings. It sounds like... you are not the mother of all of them?"



    scene b_daily17_13 with tstmgr

    "Lady Minna" "Of course I’m not. Senning is the only child I have."



    scene b_daily17_11 with tstmgr

    "Lady Minna" "Senning’s father has four wives and I am one of them. He bought a house for each of us so we won’t fight each other."



    player "Wow, for real? Is that even legal?"



    scene b_daily17_10 with tstmgr

    "Lady Minna" "For a man to have four wives? Of course not, but money solves everything."



    player "That’s... ... cool... ..."



    "‘Conservative family’... ... huh, I don’t even know what conservative means anymore."



    scene b_daily17_11 with tstmgr

    "Lady Minna" "I can’t say I like the other three women, but I’m okay with living with them. The four of us play mahjong every day and I always win~"



    scene b_daily17_12 with tstmgr

    "Lady Minna" "So you see, I am not an opposer of polygamy. That’s why I didn’t forbid Senning from being with you even though I have known about your story with other women..."



    scene b_daily17_11 with tstmgr

    "Lady Minna" "Especially your story with the elder daughter of Elisa Shinyrost... ... Humph~"



    scene b_daily17_12 with tstmgr

    "Lady Minna" "You know, I met that blonde gorgeous once during a fashion week many years ago, but I guess she has forgotten who I am."



    player "How did you know about... my relationships?"



    "Lady Minna" "It’s not a secret anyway. Maybe Senning has been aware of that too. Maybe she just doesn’t care, either."



    scene b_daily17_14 with tstmgr

    $ flashlight()

    b "What are you guys talking about? The tea is ready~"



    player "We... ..."



    scene b_daily17_15 with tstmgr

    "Lady Minna" "We were talking about the next test I prepared for [P]."



    scene b_daily17_16 with tstmgr

    b "There are more tests? I thought [P] has passed all of them."



    scene b_daily17_17 with tstmgr

    "Lady Minna" "Well, he has proved that he is good enough to be my little girl’s boyfriend, but is he good enough to be her future husband? We don’t know that yet~"



    scene b_daily17_18 with tstmgr

    b "What’s the difference?"



    scene b_daily17_19 with tstmgr

    "Lady Minna" "Oh girl, there are a lot of differences~"



    "Lady Minna" "Come and find me tomorrow to begin the test, will you, [P]?"



    b "Why don’t you just test him right now?"



    scene b_daily17_20 with tstmgr

    "Lady Minna" "We will need your avoidance to ensure fairness~"



    b "Mama, are you serious?"



    scene b_daily17_21 with tstmgr

    b "Awwwwww... ... it sounds like a tough test. Please go easy on him."



    "Lady Minna" "Relax, I’m not going to eat him~"



    "Lady Minna" "Now where is the tea? I’m thirsty to death~"



    scene void with tstmgr

    "... ... ... ..."



    "I spent the rest of the afternoon with the mother and the daughter."



    stop music fadeout 1.0


    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
