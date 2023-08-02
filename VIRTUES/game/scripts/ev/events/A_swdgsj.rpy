label A_swdgsj:

    scene void with tstmgr

    narrator "According to Jake, Вера works at a cafe every morning. Perhaps I could encounter her there and try and get to know her better."

    narrator "... ... ... ..."

    scene cafe_background with tstmgr

    narrator "I found the cafe Jake mentioned and made my way inside.."

    narrator "The place is smaller than I imagined and quite...quaint. I don't know how a place can be so dark when the sun is beaming outside. Whose idea was this?"

    narrator "Luckily, Вера is really here. It was not difficult to find her at all because she was the only server here."

    scene a_cafe_smile2 with tstmgr

    a "Welcome."

    scene a_cafe_weird with tstmgr

    a "Ah..."

    player "Oh? Hi, Вера. I didn't expect to see you here."

    a "Hello..."

    player "Do you work here?"

    narrator "... ... ... ..."

    narrator "She was a little bit shocked at my appearance. It took her a while to return to normal."

    scene a_cafe_normal1 with tstmgr

    a "Yes, I work here every day in the morning, as a waitress."

    scene a_cafe_weird with tstmgr

    a "Why are you here?"

    player "I was just... walking down the street and happened to see you from outside, so I decided to come in and say hi. That's all."

    a "... ... ... ..."

    scene a_cafe_normal1 with tstmgr

    a "Alright...... What can I get for you today?"

    player "Do you have any recommendations?"

    scene a_cafe_weird with tstmgr

    a "Emm... I don't know."

    scene a_cafe_smile2 with tstmgr

    a "You can try the bacon sandwich meal. The bacon is fresh, I'm sure of that."

    player "Sounds good. I'll have one bacon sandwich meal then. Thank you."

    a " I'll be right back."

    scene cafe_background with tstmgr

    narrator "... ... ... ..."

    narrator "Sometime later, I finished my breakfast and checked out."

    scene a_cafe_normal1 with tstmgr

    a "Did you enjoy the meal?"

    player "... ... ... ..."

    narrator "(Well, no. The bacon was overcooked. It tasted like firewood. I wonder if I should tell her the truth.)"

    a "... ... ... ..."

    scene a_cafe_weird with tstmgr

    a "Nevermind, you don't need to tell, I knew the bacon was overcooked. It must taste like firewood."

    player "??? How did you know?"

    a "... ... ... ..."

    a "I am actually quite good at cooking, but the chief doesn't listen to any of my advice."

    player "Why is that?"

    a "He wouldn't hear from a server."

    player "Ha, now I see why this place has so few guests."

    menu:
        "Tip her regularly":

            scene cafe_background with tstmgr

            narrator "We had a brief conversation after that. She didn't talk much, but it was a good start."

            narrator "... ... ... ..."
        "Tip her generously":


            scene a_cafe_weird with tstmgr

            a "Eh, why do you tip me so much?"

            player "Because I am satisfied with your service. Just take it."

            a "But 30%%... That's too much."

            player "People always tip more for a server they know. It's a sign of goodwill, nothing else."

            scene a_cafe_smile2 with tstmgr

            a "Is that so..."

            a "... ... ... ..."

            scene a_cafe_smile2 with tstmgr

            a "Fine, thank you."

            scene cafe_background with tstmgr

            narrator "We had a brief conversation after that. She didn't talk much, but it was a good start."

            narrator "... ... ... ..."

            $ add(A, A.love, 1)

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
