default cInteraction = None

label run_interaction:

    $ set_scene("Action")

    call expression cInteraction.nz_code + "_PreInteraction"

    jump expression cInteraction.label + "_" + cInteraction.nz.relation

label interaction_post:






    $ persistent.seens.append(cInteraction.label)

    $ cInteraction.state.count += 1

    $ show_find()

    $ _cInteraction_nz = cInteraction.nz

    $ cInteraction = None

    $ print('Interaction Clear')

    jump pauser
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
