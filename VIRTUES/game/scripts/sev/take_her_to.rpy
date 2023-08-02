init python:
    def get_findee_take_to_locs():
        r = []
        
        if seen("found_pool") and get_findee_training_level("inti") >= 2:
            r.append(("Basement Pool", "pool"))
        if seen("found_dungeon") and get_findee_training_level("sub") >= 2:
            r.append(("Dungeon", "dungeon"))        
        if seen("found_outdoors") and get_findee_training_level("shame") >= 2 and findee != D:
            r.append(("Outdoors", "outdoors"))
        
        return r

define take_her_to_button_colors = {
    "A": "#A33B3B",
    "B": "#888888",
    "C": "#00C2CE",
    "D": "#A9E88E",
    "E": "#efe51f",
    "F": "",
    "G": "#FE2E74",
}


label pool:
    scene expression "%s_pool_0" % findee.code.lower() with tstmgr
    $ gui.choice_align = (1.0, 0.35)
    $ gui.choice_button_background = colorize("gui/button/take_her_to_button.png", take_her_to_button_colors[findee.code])
    $ gui.choice_xoffset = 0
    $ gui.choice_text_yoffset = -27
    $ gui.choice_text_outlines = []

    $ unlock_from_gallery("pool_%s.%s_pool_1" % (findee.code, findee.code.lower()))
    $ unlock_from_gallery("pool_%s.%s_pool_2" % (findee.code, findee.code.lower()))

    jump expression "pool_%s" % findee.code
    label pool.end:

    $ time_proceed(1)

    $ set_default_ui()
    jump label_post

label dungeon:
    scene expression "%s_dungeon_0" % findee.code.lower() with tstmgr
    $ gui.choice_align = (1.0, 0.35)
    $ gui.choice_button_background = colorize("gui/button/take_her_to_button.png", take_her_to_button_colors[findee.code])
    $ gui.choice_spacing = 90
    $ gui.choice_xoffset = 0
    $ gui.choice_text_yoffset = -27

    $ unlock_from_gallery("dungeon_%s.%s_dungeon_1" % (findee.code, findee.code.lower()))
    $ unlock_from_gallery("dungeon_%s.%s_dungeon_2" % (findee.code, findee.code.lower()))

    jump expression "dungeon_%s" % findee.code
    label dungeon.end:

    $ time_proceed(1)

    $ set_default_ui()
    jump label_post

label outdoors:
    scene expression "%s_outdoors_0" % findee.code.lower() with tstmgr
    $ gui.choice_align = (1.0, 0.35)
    $ gui.choice_button_background = colorize("gui/button/take_her_to_button.png", take_her_to_button_colors[findee.code])
    $ gui.choice_spacing = 90
    $ gui.choice_xoffset = 0
    $ gui.choice_text_yoffset = -27

    $ unlock_from_gallery("outdoors_%s.%s_outdoors_1" % (findee.code, findee.code.lower()))
    $ unlock_from_gallery("outdoors_%s.%s_outdoors_2" % (findee.code, findee.code.lower()))

    jump expression "outdoors_%s" % findee.code
    label outdoors.end:

    $ time_proceed(1)

    $ set_default_ui()
    jump label_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
