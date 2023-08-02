default cPlaylet = None

init python:
    def get_cPlaylet():
        try:
            return get_playlet(store.cPlaylet)
        except:
            print("cPlaylet %s not found" % cPlaylet)


label run_playlet(playlet):

    $ set_scene("Action")

    $ store.cPlaylet = playlet.label

    if renpy.has_label(playlet.label):
        jump expression playlet.label
    else:
        "No label of playlet."

label playlet_post:

    $ get_cPlaylet().run_results()

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

    jump pauser
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
