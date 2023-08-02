screen building_pane(pos, img, screen, action):
    button padding 0, 0:
        xysize (225, 160)
        pos pos
        action Show(screen)
        add img
        hbox:
            offset (0, 10)
            for badge in get_children_badge(action):
                fixed xysize (55, 55):
                    add badge align (0.5, 0.5)

default weekend_button_displaying = False
screen right_panel():
    zorder 81

    if is_scene("Map"):

        if seen('pcsj'):
            use building_pane((1222, 191), "gui/map/bnb.png", "bnb", Action.get("bnb"))

        if seen("d7_1"):
            use building_pane((934, 340), "gui/map/mansion.png", "mansion", Action.get("mansion"))

        use building_pane((446, 361), "gui/map/college.png", "college", Action.get("college"))


image weekend_button:
    "gui/weekend_button_insensitive.png"
    on idle:
        "gui/weekend_button_idle.png" with Dissolve(0.2)
    on hover:
        "gui/weekend_button_hover.png" with Dissolve(0.2)
    on insensitive:
        "gui/weekend_button_insensitive.png"

image bnb_button:
    "gui/bnb_button_insensitive.png"
    on idle:
        "gui/bnb_button_idle.png" with Dissolve(0.2)
    on hover:
        "gui/bnb_button_hover.png" with Dissolve(0.2)
    on insensitive:
        "gui/bnb_button_insensitive.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
