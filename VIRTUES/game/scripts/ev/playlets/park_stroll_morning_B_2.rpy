label park_stroll_morning_B_2:

    scene park_stroll_morning_b_2_1 with tstmgr

    player "Сеннин? I didn't expect to see you here so early in the morning."



    b "Hello, [P]."



    b "I didn't sleep well last night, so... decide to have a walk in the park."



    player "What happened last night?"



    scene park_stroll_morning_b_2_2 with tstmgr

    b "It's my neighbor, Teresa. Her boyfriend was in her room last night..."



    b "And I could hear her groaning for the entire night."



    b "Sigh... ..."



    scene void with tstmgr

    player "... ... ... ..."



    $ add(B, B.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
