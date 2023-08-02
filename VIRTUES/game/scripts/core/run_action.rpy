default cAction = None

label run_action(action, hide_map=True):

    $ cAction = action
    $ set_scene("Action")
    $ ini_time = t.copy()

    jump expression action.label

label action_post:

    $ cAction.state.add_count_of_day()


    if cAction.post:
        $ cAction.post()

    $ auto_event()

    if cAction.to_map:
        $ show_map()

    $ cAction = None

    jump pauser
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
