label company_afternoon_C_2:

    scene void with tstmgr

    player "Here is your milk tea."



    scene rcsj_c3 with tstmgr

    c "Thank you. You can go back to your work now."



    player "Is there anything else you want me to buy for you? A sandwich? An icecream? Or maybe a magazine?"



    scene rcsj_c5 with tstmgr

    c "That's not like you. What happened?"



    player "Eh... you know, I just realized that being your servant is not that bad."



    player "At least I can escape from my job for a little while."



    c "... ... ... ..."



    c "It's not wise to tell that to your manager."



    c "But nevermind. You can buy me some chocolate in the Walmart nearby. I'll give you 20 minutes."



    scene void with tstmgr

    "... ... ... ..."



    $ add(C, C.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
