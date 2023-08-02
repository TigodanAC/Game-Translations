





define skipping = False
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:
        if is_scene("Map"):
            frame:

                background None
                xalign 1.0
                yalign 1.0

                has hbox
                button action Skip() alternate Skip(fast=True, confirm=True):
                    add "gui/phone/skip_button.png"
                button action Rollback():
                    add "gui/phone/back_button.png"
                button action ShowMenu():
                    add "gui/phone/menu_button.png"




        else:
            hbox:
                style_prefix "quick"

                xalign 0.5
                yalign 1.0

                textbutton _("Back") action Rollback()
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Hide") action HideInterface()
                if _in_replay:
                    textbutton _("End Replay") action EndReplay(confirm=False)
                else:
                    textbutton _("Menu") action ShowMenu()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
