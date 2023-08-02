label bnb_frontyard_forenoon_B_1:

    scene bnb_frontyard_forenoon_b_1_1 with tstmgr

    b "These flowers in your yard are really beautiful! Did you plant them yourself?"



    player "Ehh... ... I didn't do anything about it. Вера did all this."



    b "Miss Вера is such a great person!"



    b "Do you have more places in your yard? Can I plant something else?"



    player "Eh... sure, what do you want to plant?"



    player "(This could be a good chance to know what flowers she likes~)"



    scene bnb_frontyard_forenoon_b_1_2 with tstmgr

    b "Chives, onions, cabbages, tomatos... ... I have a list of them!~"



    player "What the... ... ... ..."



    scene void with tstmgr

    "... ... ... ..."




    $ add(B, B.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
