init python:
    def set_shop_ui():
        gui.choice_align = (1.0, 0.3)
        gui.choice_button_background = "shop_button_background"
        gui.choice_spacing = 40

    def set_shop_ui_wide():
        gui.choice_align = (1.0, 0.3)
        gui.choice_button_background = "shop_button_background_long"
        gui.choice_spacing = -20

    def set_hotel_shop_ui():
        gui.choice_align = (1.0, 0.3)
        gui.choice_button_background = "gui/button/hotel_shop_idle_background.png"
        gui.choice_spacing = 40

    def set_hotel_shop_ui_wide():
        gui.choice_align = (1.0, 0.3)
        gui.choice_button_background = "gui/button/hotel_shop_idle_background_long.png"
        gui.choice_spacing = -20

    def set_default_ui():
        gui.choice_button_background = "choice_button_background"
        gui.choice_align = (1.0, 0.9)
        gui.choice_size = (800, 140)
        gui.choice_spacing = 40
        gui.choice_xoffset = -60
        
        gui.choice_size = (800, 140)
        gui.choice_button_text_color = "#ffffff"
        gui.choice_text_yoffset = 0
        gui.choice_text_outlines = [ (0, "#00000059", 1, 1), (1, "#51454659") ]

    set_default_ui()



















define gui.insensitive_choice_color = "#AAAAAA"
define gui.unimplemented_choice_color = "#444444"

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

screen choice(items):
    style_prefix "choice"

    vbox at choice:
        align gui.choice_align
        spacing gui.choice_spacing
        xoffset gui.choice_xoffset

        for i in items:

            fixed:
                xysize gui.choice_size

                button:
                    background None
                    xysize gui.choice_size

                    add gui.choice_button_background align (0.5, 0.5)

                    if "not_implemented" in i.kwargs:
                        action Function(not_implemented_message)
                    elif len(i.args) > 0 and eval(i.args[0]):
                        pass
                    else:
                        action i.action

                text i.caption:
                    align (0.5, 0.5)
                    yoffset gui.choice_text_yoffset
                    outlines gui.choice_text_outlines
                    if len(i.args) > 0 and not eval(i.args[0]):
                        color gui.insensitive_choice_color
                    elif "not_implemented" in i.kwargs:
                        color gui.unimplemented_choice_color





define config.narrator_menu = True

transform choice:
    alpha 0.0
    linear 0.5 alpha 1.0

image choice_button_background:
    "gui/button/choice_idle_background.png"
    on idle:
        "gui/button/choice_idle_background.png" with Dissolve(0.2)
    on hover:
        "gui/button/choice_hover_background.png" with Dissolve(0.2)
    on insensitive:
        "gui/button/choice_idle_background.png"

image shop_button_background:
    "gui/button/shop_idle_background.png"
    on idle:
        "gui/button/shop_idle_background.png" with Dissolve(0.2)
    on hover:
        "gui/button/shop_hover_background.png" with Dissolve(0.2)
    on insensitive:
        "gui/button/shop_idle_background.png"

image shop_button_background_long:
    "gui/button/shop_idle_background_long.png"
    on idle:
        "gui/button/shop_idle_background_long.png" with Dissolve(0.2)
    on hover:
        "gui/button/shop_hover_background_long.png" with Dissolve(0.2)
    on insensitive:
        "gui/button/shop_idle_background_long.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
