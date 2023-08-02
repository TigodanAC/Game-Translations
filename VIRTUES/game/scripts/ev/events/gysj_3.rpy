label gysj_3:

    scene park_night_background with tstmgr

    narrator "I went to the park for a walk after dinner."

    narrator "It was so quiet and dark. To be honest, I started to regret it. This place is creepy at night."

    player "Hmm?... ... ... ..."

    narrator "I heard some voices."

    narrator "... ... ... ..."

    "Woman" "Oh master, I can't crawl no more. I'm so tired."

    "Man" "Shit, you lazy dog, stick your ass up! You need some punishments."

    "Woman" "Ah... Master, punish me, put your big cock inside my dirty pussy, please."

    "Man" "(Slapping woman's butt) You are nothing but a fucking dog. What should a dog suppose to say?"

    "Woman" "(Groaning) Arf, arf, woof... Ah... harder, harder please... Woof, woof..."

    narrator "... ... ... ..."

    player "Eh... ... ... ..."

    player "What the hell is that..."

    player "It sounds like some kind of weird role play game."

    label gysj_3_choices:

    menu:
        "Leave quietly":


            player "I don't wanna see this, it is an invation of privacy..."

            player "And it is just way too creepy. I should probably go home."
        "Take a peek":

            if P.virtue < 30:
                $ not_implemented_message()
                jump gysj_3_choices
            else:
                "(Virtue needs to be less than 30.)"

                narrator "You can expect it in the future updates."

                jump gysj_3_choices

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
