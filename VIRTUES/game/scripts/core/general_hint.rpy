default general_hint_seen = False
define general_hint_text = '''{size=+10}{color=#e8888a}General Hints{/color}{/size}
1. Most events in school happen at daytime. '''
screen general_hint_window():
    zorder 87

    drag at zoom_emerge:
        drag_handle (0,0,1000,600)
        xalign .5 yalign .5
        drag_offscreen True

        has fixed:
            xsize 1000 ysize 600
            xalign .5 yalign .5
        frame:
            padding (gui.frame_padding-11, gui.frame_padding-11)
            add Solid("#00000010", xsize=1000, ysize=42)
            add xbtn(action=Hide("general_hint_window"), xpos=990, ypos=4)
            xsize 1000 ysize 600
            xalign .5 yalign .5
            frame:
                background None
                xpadding 30 ypadding 30
                xsize 900 ysize 500
                xalign .5 yalign .5

                text general_hint_text

image general_hint:
    "general_hint_idle"
    on idle:
        "general_hint_idle" with Dissolve(0.2)
    on hover:
        "general_hint_hover" with Dissolve(0.2)

image general_hint_hover_layer_blink:
    "gui/general_hint_hover_layer.png"
    align (0.5, 0.5)
    ease 0.8 alpha 0.0
    ease 0.8 alpha 1.0
    repeat

image general_hint_idle = Fixed(Image("gui/general_hint_idle.png", align=(0.5, 0.5)), xysize=(70, 50))

image general_hint_blink = Fixed(Image("gui/general_hint_idle.png", align=(0.5, 0.5)), "general_hint_hover_layer_blink", xysize=(70, 50))

image general_hint_hover = Fixed(Image("gui/general_hint_idle.png", align=(0.5, 0.5)), Image("gui/general_hint_hover_layer.png", align=(0.5, 0.5)), xysize=(70, 50))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
