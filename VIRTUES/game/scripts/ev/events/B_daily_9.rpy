label B_daily_9:

    scene void with tstmgr
    play music happy

    "After an exam..."



    scene b_school_day_smile with tstmgr

    b "How do you feel about the exam?"



    player "I don’t know. It felt like an easy one, but I’m not sure about my answers."



    player "... ... ... ..."



    player "Forget about it. Where do you like to spend your afternoon?"



    player "Do you want to go to a movie with me?"



    scene b_school_day_frown with tstmgr

    b "Me? Hmm... ..."



    b "No, I don't think it's a good idea."



    b "I think I will just stay in my room and have some rest."



    player "Oh... fine... ..."



    scene b_school_day_normal with tstmgr

    b "... ... ... ..."



    b "Maybe..."



    scene b_school_day_smile with tstmgr

    b "You know... if you like, maybe we can have afternoon tea together."



    player "Eh, you mean, in your room?"



    b "(Nodding)... ... ... ..."



    player "Yeah, I‘d love to."



    player "What are we waiting for? Let’s go!"



    scene void with tstmgr

    "... ... ... ..."



    "Sometime later, in Сеннин’s apartment."



    scene b_daily9_1 with tstmgr

    b "How do you like the tea?"



    b "I know you are not a fan of bitter taste, so I added some pieces of rock candy in your tea. Do you like it?"



    player "I... Yes, I like it."



    label B_daily_9_choice_1:

    menu:
        "Admire the tea":


            player "What’s the name of this tea? It tastes really good."

            b "I’m so happy you like it."

            b "It’s called Jin Jun Mei, the brows of golden steeds."

            player "That is a gorgeous name..."

            b "It’s my favorite black tea. You can take some with you before you leave."

            player "There is no need for that."

            player "I’ll just come to you every time when I miss this taste."

            scene b_daily9_2 with tstmgr

            b "Oh... ..."

            scene b_daily9_1 with tstmgr

            b "Yeah, you are always welcome here."
        "Admire her":




            player "... ... ... ..."

            scene b_daily9_2 with tstmgr

            b "... Why are you staring at me like that?"

            player "(Smiling)... ... ... ..."

            b "Eh... why are you smiling like that?"

            player "It just... you know, feels unreal."

            player "On a lovely afternoon, having tea with a beautiful lady on a balcony. I feel like I am a British nobility or something."

            scene b_daily9_1 with tstmgr

            player "I think we should have afternoon tea together more often."

            b "Yeah, you are always welcome here."



    scene b_daily9_3 with tstmgr

    "The sunshine passed through the clouds and fell upon her smiling face. Oh... she is just amazing."



    scene b_daily9_2 with tstmgr

    b "Hmmm... ... ... ..."



    b "Your smile becomes weirder."



    player "Sorry."



    b "And you are still staring at me."



    player "(Holding up a cup of tea and pretending to drink) It’s just... ..."



    scene b_daily9_4 with tstmgr

    b "Watch out!"



    "I accidentally spilled some tea on my shirt."



    player "Ah... crap..."



    player "It's okay, not a big deal. The water is not hot at all."



    scene b_daily9_2 with tstmgr

    b "But the tea would make your shirt dirty. It might be hard to clean up since normal detergents don’t have much use on tea stains."



    b "Hmm... ... ... ..."



    scene b_daily9_5 with tstmgr

    b "You can leave your shirt to me if you don’t mind. I will handwash it for you."



    player "Oh, don’t worry about it. I can wash it myself."



    b "No offense, but I don’t think you can handle it well."



    b "You didn’t even know how to use a dishwasher until last month."



    b "Come on, I will wash it for you. Don’t mention it. We are friends."



    player "Hmmm... ... Okay, fine."



    player "Thank you, Sen. You are the best."



    scene b_daily9_6 with tstmgr

    b "I’m happy to do something for you."



    scene void with tstmgr

    "... ... ... ..."



    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
