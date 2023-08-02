default cLabel = None

label run_label():

    $ set_scene("Action")

    jump expression cLabel

label label_post:

    if _in_replay:
        $ renpy.end_replay()
        return

    $ cLabel = None

    $ show_map()

    $ queue_auto_event()
    $ auto_event()

    jump pauser
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
