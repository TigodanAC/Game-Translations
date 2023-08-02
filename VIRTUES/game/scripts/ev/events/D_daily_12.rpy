label D_daily_12:

    scene void with tstmgr

    play music happy

    if _in_replay:
        "In order to replay this plot, I need to know this first."
        menu:
            "Теодора has moved into your house":
                jump D_daily_12.line_a
            "Теодора hasn't moved into your house":
                jump D_daily_12.line_b
    else:
        if seen("C_daily_12"):
            jump D_daily_12.line_a
        else:
            jump D_daily_12.line_b

    jump event_post

label D_daily_12.end:

    stop music fadeout 1.0

    jump event_post

label D_daily_12.line_a:

    "*Door bell sound* Ding-dong~ Ding-dong~"

    d "Hello! Anybody home? Уно? Let’s go to a movie!"

    scene d_daily12_24 with dissolve

    c "*Opened the door* Ahhh... ... I really don’t want to open this door... ..."

    scene d_daily12_25 with tstmgr

    d "Теодора? What are you doing here?"

    c "I live here now. Didn’t mom tell you that?"

    scene d_daily12_26 with tstmgr

    d "What? You and [P] live together now? That’s so not fair!"

    c "Hah, and we will get married next month."

    scene d_daily12_27 with tstmgr

    d "What the hell?!"

    scene void with tstmgr

    $ flashlight()

    "???" "Uhhhhhhhhhh!!!!! What?!!!!"

    scene d_daily12_28 with dissolve

    c "Hmmmm?"

    scene d_daily12_29 with tstmgr

    d "*Hiding behind Теодора* Awwwww... ..."

    scene d_daily12_32 with tstmgr

    b "Mamamamama... married?"

    "It seems like Айрин didn’t close the door and Сеннин just happened to get in after her."

    scene d_daily12_30 with tstmgr

    c "Ah, you must be Сеннин. [P] has told me about you."

    c "My name is Теодора, a... tenant. What I said was just a joke, don’t take it seriously."

    scene d_daily12_31 with tstmgr

    c "And this is my sister, Айрин."

    scene d_daily12_33 with tstmgr

    b "It’s a pleasure to meet you. I... I’m sorry. I was overreacting... ..."

    scene d_daily12_34 with tstmgr

    d "Yeah, you’d better be sorry, young lady! You just freaked me out!"

    scene d_daily12_35 with tstmgr

    $ flashlight()

    b "Yaaaaaaaahhh!!!"

    scene d_daily12_29 with tstmgr

    d "*Hiding behind Теодора again* Awwwwww... ... what’s her problem?"

    b "*Murmuring* So cute... ..."

    c "Pardon?"

    b "*Murmuring* Айрин... ... so cute... ..."

    scene d_daily12_36 with tstmgr

    d "Oh, thank you for saying that. You are cute, too~"

    scene d_daily12_37 with tstmgr

    d "Wait, no, strange lady! You freaked me out again! You are not cute at all!"

    b "*Swallowing hard* ... ... ... ..."

    c "You don’t look so well. Are you okay, Сеннин?"

    b "I... I’m fine. I’m totally fine, I just... ..."

    scene d_daily12_38 with tstmgr

    b "I have never seen... anyone... so cute like that... ..."

    b "I need to... ... ... ..."

    c "Сеннин?"

    scene d_daily12_39 with tstmgr

    "Сеннин suddenly lost balance and fell forward."

    c "Сеннин!"

    d "Oh my God! What happens to her?"

    c "... ... ... ..."

    c "Typical low-blood-sugar issue. She fainted because she got too excited. Let’s put her on the ground."

    d "Oh no! Does she need an ambulance? How can we help her?"

    c "I think she will be back to normal in minutes. It is not really a big issue."

    d "Is it my fault that caused her to faint?"

    scene d_daily12_40 with tstmgr

    c "I don’t know, maybe... ..."

    c "She fainted because of your... cuteness? That sounds... strange... ..."

    scene d_daily12_41 with tstmgr

    d "Awwwwww... ... I feel so sorry though I don’t know what was really going on here."

    c "Don’t worry, let’s just get her to the livingroom and she will recover soon."

    b "So... cute... ... Kawaii... ..."

    scene void with tstmgr

    "... ... ... ..."

    "*Сеннин has become friends with Теодора and Айрин.*"

    "... ... ... ..."

    jump D_daily_12.end

label D_daily_12.line_b:

    "*Door bell sound* Ding-dong~ Ding-dong~"



    d "Hello! Anybody home?"



    a "Coming~"



    scene d_daily12_1 with tstmgr

    a "*Opened the door* Oh, hi, Айрин. What brings you here?"



    scene d_daily12_2 with tstmgr

    d "I’m here to visit you and Уно! Am I welcome here?~"



    scene d_daily12_3 with tstmgr

    a "Oh, of course, come on in~ But unfortunately Уно and [P] are not at home right now."



    b "*Flushed* ... ... ... ..."



    scene d_daily12_4 with tstmgr

    a "Hmm? Oh, sorry, I forgot to do the introduction."



    scene d_daily12_5 with tstmgr

    a "Сеннин, this is Айрин, [P] is her private tutor."



    a "And Айрин, this is Сеннин, [P]’s college friend~"



    scene d_daily12_6 with tstmgr

    d "Nice to meet you, Сеннин."



    b "*Flushed* ... ... ... ..."



    scene d_daily12_7 with tstmgr

    a "Sen?"



    scene d_daily12_8 with tstmgr

    b "Hi... ... Nice to... meet you... ..."



    scene d_daily12_9 with tstmgr

    d "Are you alright? You look terrible."



    b "*Murmuring* So cute... ..."



    d "Pardon?"



    scene d_daily12_11 with tstmgr

    b "*Murmuring* You look... ... so cute... ..."



    scene d_daily12_10 with tstmgr

    d "Thank you for saying that. You are cute, too~"



    b "*Swallowing hard* ... ... ... ..."



    b "Can I... have a little hug with you, please, Miss Айрин?"



    d "Hug? Okay~"



    scene d_daily12_12 with tstmgr

    "... ... ... ..."



    b "Awwwwwwww... ..."



    scene d_daily12_13 with tstmgr

    d "Wow... Your heart beats so fast. Are you sure you are alright?"



    scene d_daily12_14 with tstmgr

    b "I... I’m fine. I’m totally fine, I just... ..."



    scene d_daily12_15 with tstmgr

    b "I have never seen... someone... cute like you... ..."



    scene d_daily12_16 with tstmgr

    b "I need to... ... ... ..."



    a "Sen?"



    scene d_daily12_17 with tstmgr

    "Сеннин suddenly lost balance and fell backward."



    scene d_daily12_18 with tstmgr

    a "Sen!"



    "Вера caught Сеннин on time before she fell on the ground."



    scene d_daily12_19 with tstmgr

    d "Oh my God! What happens to her?"



    a "[P] once told me that she has this low-blood-sugar issue. She may faint when she gets super excited in a very short time."



    scene d_daily12_20 with tstmgr

    d "Oh no! Does she need an ambulance? How can we help her?"



    a "I... think she will be back to normal in minutes. It is not really a big issue... ..."



    d "Is it my fault that caused her to faint?"



    scene d_daily12_21 with tstmgr

    a "Eh... Maybe, I... I don’t know... ..."



    a "She fainted because of your... cuteness? That sounds... strange... ..."



    scene d_daily12_22 with tstmgr

    d "Awwwwww... ... I feel so sorry though I don’t know what was really going on here."



    a "Don’t worry, let’s get her to the livingroom and she will wake up just in minutes."



    a "You two will be good friends, I’m pretty sure of that~"



    scene d_daily12_23 with tstmgr

    d "I want to be friends with her too. She looks like a super interesting girl!~"



    b "So... cute... ... Kawaii... ..."



    scene void with tstmgr

    "... ... ... ..."



    "*Айрин and Сеннин have become friends.*"



    "... ... ... ..."

    jump D_daily_12.end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
