define location_right = Frame("gui/map/location_right.png", right=30, ysize=60)
screen map_panel():
    default selected_location = none_action
    default launched = False
    style_prefix "map"
    zorder 80
    default tip = None

    if is_scene("Map"):


        for location in map_action.displaying_children:

            $ runnable = location.get_runnable()
            $ clickable = location.is_clickable

            button:
                add location.get_icon()

                if runnable:
                    action runnable
                else:
                    action ToggleScreenVariable("selected_location", true_value=location, false_value=none_action)

                sensitive location.is_clickable

                pos location.pos
                background "gui/map/location_left.png"

                xysize (60, 60)

                showif location is not selected_location:
                    for i, badge in enumerate(get_location_badge(location)):
                        add badge offset (-30+i*20, -15) at normal_t(0.3)


            showif location is not selected_location:

                button:
                    if runnable:
                        action runnable
                    else:
                        action ToggleScreenVariable("selected_location", true_value=location, false_value=none_action)

                    sensitive location.is_clickable

                    if launched:
                        at map_submenu
                    else:
                        at normal_t(0.3)
                        $ launched = True

                    pos (location.pos[0]+60, location.pos[1])
                    background location_right

                    text "[location.display_name]  ":
                        insensitive_color "#888888"


            else:
                $ children = location.displaying_children
                fixed at map_submenu:
                    pos (location.pos[0]+60, location.pos[1]-20)
                    xysize (len(children)*70 + 11), 80
                    frame ypos 20:

                        background location_right

                        has hbox
                        add Solid("#f0eee9bb", xysize=(1, 60))
                        for action in children:
                            null width 10
                            button:
                                xsize 60
                                add action.get_icon()
                                sensitive action.is_clickable
                                action action.run
                                hovered ShowTransient("tooltip", content=action.display_name)
                                unhovered Hide("tooltip")

                                add get_action_badge(action) align (0.0, 0.0) offset (-20, -15)

                        null width 10

    else:
        $ launched = False

screen tooltip(content):
    style_prefix "tooltip"
    default pos = renpy.get_mouse_pos()
    zorder 86

    frame:
        pos pos anchor (-6, -20)
        text content


style map_button:
    padding (0, 0)
    ysize 60

style tooltip_text:
    size 24

style map_text:
    size 24
    yalign 0.5

style map_frame:
    margin (0, 0)
    padding (0, 0)
    background None
    xpadding 0
    ypadding 0

transform map_submenu:
    on show:
        crop_relative True
        crop (0, 0, 0.0, 1.0)
        pause 0.2
        linear 0.2 crop (0, 0, 1.0, 1.0)
    on hide:
        crop (0, 0, 1.0, 1.0)
        linear 0.2 crop (0, 0, 0.0, 1.0)

transform map_submenu2:
    on show:
        crop_relative False
        crop (0, 0, 60, 60)
        pause 0.2
        crop_relative True
        linear 0.2 crop (0, 0, 1.0, 1.0)
    on hide:
        crop_relative True
        crop (0, 0, 1.0, 1.0)
        crop_relative False
        linear 0.2 crop (0, 0, 60, 60)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
