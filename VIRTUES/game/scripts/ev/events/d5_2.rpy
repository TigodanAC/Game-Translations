label d5_2:

    scene void with tstmgr

    narrator "The next day, morning."

    scene a_apartment_background_day with tstmgr

    narrator "This place... looks so terrible... And it smells really bad..."

    narrator "I am here again in front of Вера's apartment building."

    narrator "She lives in a slum... God, this place stinks..."

    narrator "She may not like my appearance, so l'd better not to let her know that I'm here."

    narrator "You may wonder why I came here. Well, this is what a man of virtue needs to do when he commits a mistake, he tries to fix the shit up. And this will be my first step."

    scene slum_door_background with tstmgr

    narrator "I went into the apartment and soon found her cell. It's 7 o'clock in the morning. I think she should still be in her room."

    narrator "I put a pill bottle, some name cards, and a letter on the ground in front of her door."

    player "Okay, that will do."

    narrator "Then I left this place in quiet."

    scene void with tstmgr

    narrator "... ... ... ..."

    narrator "Sometime later."

    scene a_door_curious with tstmgr

    a "(Opened door and noticed things on the ground) Hm?"

    scene a_door_letter with tstmgr

    a "(Picked them up) What are...?"

    a "A letter of apology, a bottle of pills, and doctor's name cards?"

    narrator "Вера opened the letter."

    narrator "{i}Hi, Вера. It's me, [P]. I don’t dare to ask for your forgiveness, but I want you to know that I am deeply sorry for everything I have done to you.{/i}"

    narrator "{i}What I did was absolutely despicable. You have every reason to hate me, but I still hope that you could take these things.{/i}"

    narrator "{i}The pills inside that bottle are for emergency contraception. I tried my best to recall what happened that night, and I remembered that I didn't... you know... inside you, but there is still a small possibility for pregnancy. So I think you'll need this.{/i}"

    narrator "{i}And there are some famous doctors' name cards. If you want to do a health check or something, just call them and schedule an appointment. It will be totally free, just tell the doctor my name.{/i}"

    narrator "{i}At last, again, I'm sorry for everything and I really want to make up for you if you could give me a chance. Here is my number: 5XX 2XX 4XXX. Just call me if you need any help.{/i}"

    a "... ... ... ..."

    a "He... ..."

    narrator "... ... ... ... ... ..."

    scene void with tstmgr

    narrator "... ... ... ..."

    jump event_post


label d5_2_bLine:

    scene void with tstmgr

    "The next morning..."



    scene d5_2_1 with dissolve

    "Here I am again, in front of Вера’s apartment building."



    "She lives in a slum. This place... looks so terrible... and it smells really bad..."



    scene d5_2_2 with tstmgr

    a "Hmm? What are you doing here?"



    scene d5_2_4 with tstmgr

    a "Wait, what’s your name again?"



    player "[P]... ..."



    player "I just want to check around, you know, to see if there is anything I can help you with... ..."



    player "I am sorry for what happened that night and... ..."



    scene d5_2_5 with tstmgr

    a "Sigh... It was not your fault. It’s not like you raped me or forced me to do anything. We were drunk, remember?"



    scene d5_2_6 with tstmgr

    a "I think I’m going to regret that day for the rest of my life, but I don’t really blame you for that..."



    player "But... ..."



    scene d5_2_7 with tstmgr

    a "Ehhh... ... My waist... still hurts... ..."



    player "Is it serious? I can drive you to a hospital if you want."



    scene d5_2_8 with tstmgr

    a "Thanks, but I think I’ll be fine..."



    a "Please just... leave me alone. I don’t need you to remind me of what happened that night..."



    scene d5_2_9 with tstmgr

    a "Now I’m going to work. See you, oh no, I mean, farewell... ..."



    scene d5_2_1 with tstmgr

    "She then ignored me and limped off towards the street..."



    player "... ... ... ..."



    "She is really a special girl. Her pride doesn’t allow her to receive my help, but... I think there must be something else I can do for her..."



    "... ... ... ..."

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
