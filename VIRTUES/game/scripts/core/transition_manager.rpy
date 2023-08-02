init -1 python:



    tstmgr = Dissolve(0.15)
    flashback = pixellate 
    flashlight = Dissolve(1.5) 
    fadehold = Fade(0.5, 1.0, 0.5)
    longdissolve = Dissolve(1.0)

    def closeeyes(pause=True):
        _window_hide()
        renpy.show("closeeyes")
        if pause:
            renpy.pause()

    def openeyes(image):
        _window_hide()
        renpy.hide("closeeyes")
        renpy.show(image)
        renpy.show("openeyes")
        renpy.pause()
        renpy.hide("openeyes")

    def flashlight():
        _window_hide()
        renpy.show("flashlight")
        renpy.pause()
        renpy.hide("flashlight")

image closeeyes:
    contains:
        "void"
        pos (0, -1080)
        easeout 0.8 pos (0, -540)
    contains:
        "void"
        pos (0, 1080)
        easeout 0.8 pos (0, 540)

image openeyes:
    contains:
        "void"
        pos (0, -540)
        easeout 0.8 pos (0, -1080)
    contains:
        "void"
        pos (0, 540)
        easeout 0.8 pos (0, 1080)

image flashlight:
    Solid("#FFF")
    alpha 0.0
    easeout 0.3 alpha 1.0
    easeout 0.3 alpha 0.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
