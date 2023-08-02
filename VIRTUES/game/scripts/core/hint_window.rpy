style hint_label:
    properties gui.text_properties("label")

style hint_button:
    xalign 0.5
    properties gui.text_properties("input_prompt")

style hint_button_text:
    xalign 0.5
    properties gui.text_properties("input_prompt")
    outlines gui.dialogue_outlines
    color "#CCCCCC"
    size 28
    hover_color gui.accent_color

style hint:
    xalign 0.5
    properties gui.text_properties("input_prompt")
    xmaximum gui.dialogue_width

screen hint(message, mode=None, who=None, xysize=None):

    if mode == "hint":
        $ who = "Hint"
        $ xysize = (800, 600)
    elif mode == "notice":
        $ xysize = (640,100)

    zorder 151
    modal True

    button action Return():
        add confirm_overlay
        at normal_t(0.5)

    frame at normal_t(0.4):
        if xysize:
            xysize xysize
        align (0.5, 0.5)
        padding (80, 120)
        vbox:
            spacing 20
            align (0.5, 0.5)
            if who is not None:
                text who:
                    style "say_dialogue"
                    align (.0, .0)

                    color gui.main_accent_color
                    size 64

            text message:
                style "say_dialogue"
                align (.0, .0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
