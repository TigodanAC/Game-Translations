label mansion_livingroom_forenoon_E_1:

    scene void with tstmgr

    "I came to Aunt Elisa's mansion in the morning."



    scene e_mansion_inside_smile with tstmgr

    e "Hi, [P]. What brings you here?"



    player "Eh, hi, Aunt Elisa. Do you have any news of my dad?"



    player "I am a little worried, you know."



    scene e_mansion_inside_frown with tstmgr

    e "Oh, [P]. I understand how you feel."



    e "I'm sorry that I don't have any good news to tell you right now."



    scene e_mansion_inside_smile with tstmgr

    e "But trust me, you dad is fine. He will be granted bail very soon."



    e "And now, since you are here, maybe you would like to join the breakfast with me?"



    player "I'd love to, Aunt Elisa."



    scene void with tstmgr

    "... ... ... ..."



    $ add(E, E.love, 1)

    jump playlet_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
