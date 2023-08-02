style name_input_frame:
    align (0.5, 0.5)
    xminimum 400

style name_input_frame:
    variant "phone"
    align (0.5, 0.1)
    xminimum 400

style name_input_vbox:
    align (0.5, 0.5)

style name_input_text:
    xalign 0.5
    properties gui.text_properties("input_prompt")
    outlines []
    color gui.dialogue_color

style name_input_input:
    xalign 0.5
    properties gui.text_properties("input_prompt")

    color gui.accent_color


style name_input_button:
    xalign 0.5
    properties gui.text_properties("input_prompt")

style name_input_button_text:
    xalign 0.5
    properties gui.text_properties("input_prompt")

    color "#CCCCCC"
    size 28
    hover_color gui.accent_color

screen name_input(prompt, prefix, suffix, rt=True, **kwargs):
    zorder 101

    style_prefix "name_input"

    frame at normal_t(0.4):
        has vbox

        text prompt

        input:
            style "name_input_input"
            pixel_width 760
            copypaste True
            prefix _("{{plain}}{{color=#f0eee9}}{}{{/color}}{{/plain}}".format(prefix))
            suffix _("{{plain}}{{color=#f0eee9}}{}{{/color}}{{/plain}}".format(suffix))

            value FieldInputValue(P_state, "name", default=True, returnable=True)

        button:
            style "name_input_button"
            text _("Confirm") style "name_input_button_text"
            if rt:
                action Return()
            else:
                action Hide("name_input")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
