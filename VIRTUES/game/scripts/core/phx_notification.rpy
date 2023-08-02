init 1 python:
    pass

transform phx_transform():
    on show:
        alpha 0.0 xalign 1.04
        pause 0.8
        parallel:
            linear 0.5 xalign 1.0
        parallel:
            easeout_circ 0.5 alpha 1.0
    on hide:
        parallel:
            easeout_circ 0.5 xalign 1.04
        parallel:
            linear 0.5 alpha 0.0

screen phx_notification():
    zorder -5
    button at phx_transform:
        background "gui/noti_bg.png"
        xysize (448, 288)
        xalign 1.0 yalign 1.0
        xoffset -12 yoffset -12
        padding (0.0, 0.0)

        if not renpy.variant("touch"):
            action OpenURL("https://www.patreon.com/NoMeme")

            default hovered = False
            hovered SetLocalVariable("hovered", True)
            unhovered SetLocalVariable("hovered", False)

            showif hovered:
                fixed at normal_t(0.15):

                    button:
                        padding (0.0, 0.0)
                        action Hide("phx_notification")
                        hovered SetLocalVariable("hovered", True)
                        align (1.0, 0.0) xysize (60, 36)
                        add "gui/x_hover.png"
        else:
            action [OpenURL("https://www.patreon.com/NoMeme"), Hide("phx_notification")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
