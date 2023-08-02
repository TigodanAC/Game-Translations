define guide_text = '''You don’t need a walkthrough to play this game. 

All the plots & events in this game can be easily triggered. We don’t want to add any puzzles, or complicated trigger conditions that may turn you off. 

The most important way to advance the story is to raise girls’ love points. You can achieve that in two ways: 
1. Meet the girls at certain locations. For example, on weekdays Senning can be found at class. You can just click on the “go to class” button in the university panel, meet her there, and then her love points will be raised.

2. Trigger girls’ short events which would automatically show on the map with a badge of girls’ mini avatars. Those events will only show up after the prologue.

Whenever there is a new triggerable plot & event, it will show on the map with a badge (red/orange/mini avatars)
---------------------------------------------------------------
{size=-4}If you're stuck in a place that you're unable to proceed the game, use the Escape button in the right-click menu to go back to the map. (or press E to open escape menu.){/size}'''

screen guide():
    zorder 91

    button:
        action Hide("guide", transition=Dissolve(0.3))

    frame:
        if renpy.variant("small"):
            xfill True yfill True
        else:
            xsize 1200 ysize 900

        xalign .5 yalign .5
        background Solid("#000000e6")
        padding (gui.frame_padding-11, gui.frame_padding-11)

        if not renpy.variant("small"):
            add xbtn(action=Hide("guide", transition=Dissolve(0.3)), xpos=1211, ypos=-9)

        vbox:
            xalign .5 yalign .5
            spacing 10

            if renpy.variant("small"):
                xsize 1600 ysize 900

            else:
                xsize 1000 ysize 670 yoffset 20

            text "{size=+10}{color=#e8888a}Tutorial{/color}{/size}"

            text guide_text:
                size 27
                if renpy.variant("small"):
                    size 32
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
