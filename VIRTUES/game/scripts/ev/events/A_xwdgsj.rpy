label A_xwdgsj:

    scene void with tstmgr

    narrator "According to Jake, Вера works at a clothing store every afternoon. Perhaps I could encounter her there and see if I can strike up a conversation."

    narrator "... ... ... ..."

    scene dressstore_background with tstmgr

    narrator "I found the store he mentioned and walked in."

    narrator "Hmm... This place looks quite nice. If Вера really works here, she might get a fair wage."

    narrator "I soon found Вера. Her face and body shape make her so conspicuous in this store."

    scene a_dressstore_unhappy with tstmgr

    narrator "Wow, nice uniform."

    player "Вера? What a coincidence. Do you work here?"

    a "... ... ... ..."

    a "Yes, I work at this place every afternoon."

    a "... ... ... ..."

    a "Why are you here? We only sell women's clothing."

    player "Oh... About that..."

    a "Are you stalking me?"

    player "What? No, God, how would you think that way?"

    player "I am just trying to... buy a gift for my...aunt."

    scene a_dressstore_frown with tstmgr

    a "Your aunt?"

    player "Yes, I can show you her picture."

    a "There is no need for that..."

    a "So... What would you like to buy?"

    player "I don't know yet. I'm just looking around."

    a "Oh... Okay..."

    a "... ... ... ..."

    player "... ... ... ..."

    narrator "As a salesperson, she is supposed to talk with the guest all the time...but she is certainly not in the mood to talk with me right now."

    narrator "This is awkward."

    player "Eh... Well..."

    player "It's pretty late in the afternoon so you should be getting off soon, right? Would you like to join me for dinner?"

    scene a_dressstore_weird with tstmgr

    a "Dinner?"

    scene a_dressstore_frown with tstmgr

    a "Thank you, but no."

    a "I prefer to go home directly after work these days."

    player "I understand that."

    a "Sorry."

    player "Then how about letting me drive you home?"

    scene a_dressstore_weird with tstmgr

    a "... ... ... ..."

    a "Why are you... ..."

    scene a_dressstore_smile3 with tstmgr

    a "Alright. Thanks for your kindness."

    player "Great!"

    narrator "... ... ... ..."

    narrator "Later, I drove her home and we had a conversation along the way. I have a feeling that things are getting better between us."


    $ add(A, A.love, 1)

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
