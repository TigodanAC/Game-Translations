default persistent.update_note_dontshowagain = False
screen update_note():
    zorder 142

    button:
        action Hide("update_note")

    drag:
        drag_handle (0,0,1000,800)
        if renpy.variant("small"):
            drag_handle (0,0,1400,1000)

        xalign .5 yalign .5
        drag_offscreen True

        fixed:
            if renpy.variant("small"):
                xsize 1400 ysize 1000
            else:
                xsize 1000 ysize 800
            xalign .5 yalign .5

            frame:
                background Solid("#000000e6")
                padding (gui.frame_padding-11, gui.frame_padding-11)
                xalign .5 yalign .5

                if renpy.variant("small"):
                    pass





                else:
                    xsize 1000 ysize 800

                    add Solid("#3e678150", ysize=42)
                    add xbtn(action=Hide("update_note", transition=Dissolve(0.3)), xpos=999, ypos=3)

                vbox:
                    if renpy.variant("small"):
                        xsize 1300 ysize 870
                    else:
                        xsize 900 ysize 670
                        xalign .5 yalign 1.0 yoffset -10

                    xalign .5 yalign 1.0
                    spacing 10

                    if renpy.variant("small"):
                        text "{size=+10}{color=#e8888a}Примечания к обновлению:{/color}{/size}"
                    else:
                        text "{size=+10}{color=#5a96bd}Примечания к обновлению:{/color}{/size}"

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        has text "[update_note_text]":
                            size 24
                            if renpy.variant("small"):
                                size 32
                            hyperlink_functions (update_note_screen_past_notes_style, update_note_screen_past_notes_action, None)

                    hbox:
                        imagebutton:
                            align (.5, .5) yoffset 3
                            auto "gui/checkbox_%s.png"
                            action ToggleVariable("persistent.update_note_dontshowagain")
                        button:
                            action ToggleVariable("persistent.update_note_dontshowagain")
                            has text "Больше не показывать":
                                size 24
                            if renpy.variant("small"):
                                size 32

                if renpy.variant("small"):
                    button:
                        align (1.0, 1.0) offset (-40, 0)
                        text "Закрыть" size 32
                        action Hide("update_note", transition=Dissolve(0.3))

init python:
    def update_note_screen_past_notes_style(url):
        return style.hyperlink_text

    def update_note_screen_past_notes_action(url):
        store.update_note_text = store.update_note_text.replace(store.past_note_link_text, "")
        store.update_note_text += past_update_note_text
        renpy.restart_interaction()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
