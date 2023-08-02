label run_OneCG(cg):

    $ set_scene("Action")

    if len(cg.nz) == 1:
        scene expression cg.cg.replace("#", str(get(cg.nz).clothes)) with tstmgr
    else:
        scene expression cg.cg with tstmgr
    python:
        for line in cg.text:
            renpy.say(None, line)

    if t.period < LateNight:
        $ time_proceed(1)
        $ auto_event()
        $ show_map()
    elif t.period == LateNight:
        $ time_proceed(1)
        $ auto_event()
        $ show_home()
    else:
        $ show_home()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
