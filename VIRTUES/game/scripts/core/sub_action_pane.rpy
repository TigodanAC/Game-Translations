style bnb_bar_text is default:
    xalign 0.5
    yalign 0.5
    size 20
    color "#fff"

style room_hover_text is default:
    size 20

screen sub_action_panel(action):
    zorder 80
    frame:
        ypadding 26
        has vbox:
            xalign 0.5
            spacing 30
        for child_action in action.children:
            if child_action.displaying:
                fixed xfill  yfill :


                    button:
                        align (0.5, 0.5)

                        background None
                        text ([child_action.display_name]):
                            if child_action.is_not_implemented:
                                style "action_button_text_is_not_implemented"
                            else:
                                style "action_button_text"
                        sensitive child_action.is_clickable
                        action child_action.run

                    if (child_action.label == "build_pool" and build_pool_count < 7) or (child_action.label == "clean" and clean_count < 5):
                        add "badge_red" align (0.0, 0.5) offset (-10, 0)
                    else:
                        add get_action_badge(child_action) align (0.0, 0.5) offset (0, 0)

style bnbwvb_fixed:
    xalign 1.0 ysize 40 xsize 260


style bnbwvb_button_frame:
    xsize 90
    background None

style bnbwvb_text:
    variant "small"
    size 32
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
