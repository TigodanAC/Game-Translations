label B_date_1:

    scene map_day with dissolve
    play music happy

    narrator "What a lovely weekend. Think about it, what should I do today?"

    narrator "Stay in my room and play video games? That's too nerdy."

    narrator "Reviewing course materials? Gods, that'll be... pathetic."

    narrator "... ... ... ..."

    narrator "Maybe I should try ask Сеннин out to spend some time together."

    narrator "I made her a call."

    b "Hello, [P.name]."

    player "Hi, Sen. Do you have time today?"

    b "Hmm... I do. What's the matter?"

    player "Do you want to take a ride with me? You haven't seen my new car yet, right? I just bought it two months ago."

    b "Sounds great. When shall we go?"

    player " I'll be at your apartment in half an hour."

    scene void with tstmgr

    narrator "... ... ... ..."

    narrator "Half an hour later..."

    scene b_date1_1 with tstmgr

    player "Hi, Сеннин."

    menu:
        "You look great":

            scene b_date1_2 with tstmgr
            b "Thanks."
            scene b_date1_4 with tstmgr
            b "So this is your new car?"
        "What took you so long?":

            scene b_date1_3 with tstmgr
            b "Sorry, I spent too much time on the makeup."
            player "No big deal, it's worth the wait. You look beautiful."
            scene b_date1_2 with tstmgr
            b "Thanks."
            scene b_date1_4 with tstmgr
            b "So this is your new car?"

    player "Is it a nice one?"

    scene b_date1_3 with tstmgr

    b "It is nice indeed..."

    if not seen('pcsj'):

        b "But is it a little bit too flaunty?"

        menu:
            "That's the reason I bought her":
                pass
            "I agree with you, but she is really nice":

                pass
    else:

        b "But it must need a lot of money for maintenance. Can you afford it now?"

        player "Well, it's indeed a problem. So I rarely drive it now. Today is an exception."

        b "Why don't you just sell it?"

        player "I would never sell my car. She is my friend. Besides, I only bought her for two months."


    b "So that's a \"she\"? ..."

    b "Weird..."

    narrator "She got into my car. Then we drove away from school to Seaside Avenue."

    scene b_date1_5 with tstmgr

    narrator "Which topic should I choose to start a conversation?"

    menu:
        "Talk about car":


            player "Can you feel the speed? Can you hear that engine roaring? Such a fantastic symphony!"
            scene b_date1_6 with tstmgr

            b "Eh... I don't know much about cars."
            b "But are you overspeeding right now? The speed limit is 70."
            player "Oh, ah, shit."
            player "I didn't mean to. I must be carried away."
            scene b_date1_5 with tstmgr

            b "Nothing. I just hope you can be more careful when driving."
            b "You know, one of my favorite movie stars was dead in a car accident."
            player "Thanks for your concern..."
            narrator "The moment is becoming awkward. I should probably change the topic."
            narrator "She just said something about her favorite movie star. How about talking something about the movie?"
            narrator "So... ..."

            menu:
                "Talk about romantic movies":

                    player "You know, our school's theatre will show some classic romantic films next week. Do you want to watch them?"
                    scene b_date1_8 with tstmgr

                    b "What movies will be on showing exactly?"
                    player "Titanic, Ghost, and some others I can't remember."
                    b "I haven't seen Ghost before. Is it good?"
                    player "It's one of the best romantic movies in the world. I can promise you that."
                    player "You know, when it first released in Montreal, every female audience would get an envelope with some tissues inside in case they cried."
                    b "No tissues for males?"
                    player "Yep, only for the ladies."
                    scene b_date1_6 with tstmgr

                    b "That... sounds like sexism in today's view."
                    player "Yeah, I don't think they would do that again anymore."
                    player "But anyway, that movie is really amazing. You should definitely go watch it if you haven't done so."
                    scene b_date1_7 with tstmgr

                    b "Fine. Let's watch it together next week."
                    narrator "Watching a romantic movie with her together? Wow, how can I refuse that?"
                    player "That will be great!"
                "Talk about Chinese movies":



                    player "I am unfamiliar with Chinese movies. Can you tell me something about it?"
                    b "What would you want to know?"
                    player "Like, the movie industry in China, how's it like?"
                    scene b_date1_7 with tstmgr

                    b "Well, I'm not professional, so don't take my words seriously."
                    b "The movie industry in China is extremely huge due to the market size and high purchasing power."
                    b "Sometimes the box office that China contributes to a hollywood movie may be even higher than the rest of the world do."
                    player "That sounds... amazing."
                    b "But sadly, although China produces more than 400 movies every year, only a few of them are good. The rest of them are just rubbish because people realize that they don't really need to make a good movie to make benefit in such a big market."
                    player "Well, that's reasonable."
                    player "So do you have any Chinese movies to recommend?"
                    b "There was a good Chinese sci-fi movie named The Wandering Earth, released only a few months ago. You can watch it now on Netflix."
                    player "Sci-fi, huh. Sounds cool. I'll go check it out."
                    narrator "... ... ... ..."
        "Talk about her":

            player "So, how's your week?"
            b "Nothing special, so far so good."
            player "Me too. I would be bored to death if you didn't accept this date."
            scene b_date1_8 with tstmgr

            b "Wait, this is a date?"
            player "Eh, what's wrong?"
            b "I thought only lovers can have dates."
            player "No, not really."
            narrator "... ... ... ..."

            menu:
                "Talk about her love experiences":

                    player "Have you ever been in a relationship with a boy?"
                    scene b_date1_6 with tstmgr

                    b "I had it once, during high school, in China."
                    narrator "Wow, that's something I didn't know. I thought her love life would be a piece of blank paper."
                    b "But... nothing happened between us."
                    b "In China, high school students are forbidden to be in love with others."
                    b "So... we did not dare to do anything. We never kiss, hug, or even grab each other's hands."
                    player "That's... sad."
                    b "Indeed, it was..."
                    player "So it was only a platonic relationship?"
                    b "Yes... I think so."
                    narrator "Well, it seems like her love life is indeed a piece of blank paper."
                    player "I feel sorry for you, Sen. I truly do."
                    player "And I think... since you have got into college, it may be a good time for you to start a real relationship with someone."
                    scene b_date1_7 with tstmgr

                    b "... ... ... ..."
                    b " I'll think about it."
                "Talk about her current love status":




                    player "Be honest with me. Is there any boy you like in our college?"
                    scene b_date1_6 with tstmgr

                    b "Eh... Why do you ask?"
                    player "We are good friends, aren't we? I ask because I care about you."
                    scene b_date1_7 with tstmgr

                    b "Alright, fine..."
                    b "I like you."
                    player "Oh, I won't judge... Wait, what?"
                    b "You are my best friend in this country. How would I not like you?"
                    player "... ... ... ..."
                    player "I see what you are playing right now."
                    player "Don't try to fool me. You know that was not what I'm asking about. I'm asking if you have a potential boyfriend target."
                    scene b_date1_6 with tstmgr

                    b "Oh..."
                    b "That's, that's a secret..."
                    player "I will take that as a yes. Ah, fuck that lucky dude."
                    scene b_date1_5 with tstmgr

                    b "... ... ... ..."
                    b "(Speaking in a small voice) You silly..."



    narrator "... ... ... ..."

    narrator "We had a good chat along the way. Сеннин looks introverted in public but becomes outgoing when she is with me. We basically talk about everything."

    player "Are you wearing a new dress? I never saw you wear it before."

    b "Yes, how does it look?"

    player "You look fabulous whatever you wear, and this dress makes you look even more fabulous."

    scene b_date1_9 with tstmgr

    b "Thanks. You are really good at saying sweet words."

    player "But, to be honest, I was kinda disappointed."

    scene b_date1_6 with tstmgr

    b "Why is that?"

    player "Well, I was expecting you to wear some less conservative dresses. I mean, you are in wonderful shape, but you always hide it under clothes. That's a pity."

    b "We have discussed this. I don't like to wear those sexy stuff. It is just not my style."

    player "But what if you are on the beach? Won't you wear a bikini?"

    b "That is... different."

    player "So you do wear bikinis on the beach? That's good to hear."

    scene b_date1_5 with tstmgr

    player "... ... ... ..."

    menu:
        "Suggest going to the beach":

            player "How about we go to the beach today? We still have time to do that."
            scene b_date1_6 with tstmgr

            b "What? But I didn't bring my swimsuit..."
            player "It doesn't matter. I will drive you back to pick that up."
            b "... ... ... ..."
            b "Why are you so enthusiastic about it? Do you want to see me in a bikini that bad?"
            player "Yep, indeed."
            narrator "Honesty is a virtue."
            b "... ... ... ..."
            scene b_date1_5 with tstmgr

            b "Fine then. I don't have other things to do anyway."
            player "You agreed? Great!"
            narrator "I turned around and drove her back to her apartment."
            narrator "... ... ... ..."

            scene void with dissolve

            narrator "Two hours later... ..."
            narrator "What happened next was not in our expectation - We encountered a huge traffic jam. At the time when we finally reached the beach, the sun is about to set. Nobody else was on the beach."
            narrator "But... turned out, it was actually a good thing."
            narrator "... ... ... ..."
            b "So, how do I look?"

            $ openeyes("b_date1_10")

            narrator "Сеннин is dressing in her bikini. She walked towards me, like a goddess of dusk."
            narrator "She looks pretty as usual, but a lot sexier. The setting sun is sparkling behind her body, making her demure as a heavenly being."
            narrator "The sunlight shines on her fair skin, her big breasts, and her flat stomach. Now she is just... magnificent..."
            narrator "My eyes gaze at her greedily, like looking at a precious artwork."
            narrator "I'm speechless."
            scene b_date1_11 with tstmgr

            narrator "She sat next to me."
            b "Why are you so quiet?"
            player "... ... ... ..."
            player "You look... amazing."
            b "That's it? Nothing else?"
            player "What else are you expecting me to say? Can't you get it from my face?"
            player "You are like a pin-up girl coming to reality..."
            player "I feel lucky to be the only one who is seeing this now."
            scene b_date1_12 with tstmgr

            b "Hmm, thank you."
            b "... ... ... ..."
            b "I have a question for you, a silly question. You can choose not to answer."
            player "Say it."
            b "Am I the most beautiful girl in a bikini that you have ever seen?"
            narrator "Is she?"
            narrator "Of course she is..."
            narrator "But..."
            narrator "Another girl's face coming into my head after Сеннин asked the question."
            scene day2_c10 with flashback

            narrator "Теодора."
            narrator "Although Теодора and I don't really get along with each other, I still have to admit that she is extremely charming when she wears a swimming suit. I don't think any man can resist her."
            narrator "So who is better? Сеннин, or Theo?"
            narrator "How should I answer her?"

            menu:
                "You are the most beautiful.":
                    scene b_date1_12 with flashback

                    b "Really? Thanks for saying that."
                    b "I don't know if you are telling the truth, but I'm happy anyway."
                    player "Why do you think I may not tell you the truth?"
                    b "Because you are a playboy who knows a lot of girls. There must be someone better than me."
                    player "Well..."
                    player "First, I'm not a playboy. I'm a virtuous man."
                    player "Second, you should be more confident about yourself. What I just said was absolutely true. You are indeed the best bikini girl I have ever seen in my life."
                    b "... ... ... ..."
                    b "Alright..."
                    b "Thank you..."
                    narrator "... ... ... ..."
                "You are one of the most beautiful.":

                    scene b_date1_11 with flashback
                    b " \"One of the best\"?"
                    scene b_date1_12 with tstmgr

                    b "Fine, at least you are being honest."
                    player "Please don't take it wrong. You look amazing, but I..."
                    narrator "She stops my explanation with eye contact."
                    narrator "... ... ... ..."
                    narrator "Indeed, she didn't seem to get angry. Maybe just as she said, that was nothing but a silly question."
                    narrator "... ... ... ..."

            scene b_date1_13 with tstmgr

            b "That sunset is so marvelous."
            player "Yeah, we should definitely come here more often and see this, just two of us."
            b "... ... ... ..."
            b "I agree with that."
            narrator "We sat on the beach, side by side, and left until the sun completely gone under the skyline."
        "Suggest to end this date":


            scene b_date1_5 with tstmgr
            player "I really would like to suggest going to the beach now, but it is about the afternoon rush hour. If we don't head back now, we will definitely encounter the traffic jam."
            scene b_date1_6 with tstmgr

            b "... ... ... ..."
            b "You are right. We should probably go back."
            player "Let's save the beach trip for the next time, okay?"
            scene b_date1_7 with tstmgr

            b "em, okay."

    scene void with tstmgr

    narrator "... ... ... ..."

    narrator "And I went back home at late night."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
