image bubble_triangle:
    "gui/bubble/bubble_triangle.png"
    ease 0.3 yoffset -4
    ease 0.3 yoffset 0
    repeat


screen bubble(who=None, what, triangle=True, color=None):
    zorder 99
    style_prefix "bubble"

    frame:
        at bubble_t
        background Frame("gui/bubble/bubble_bot.png", left=15, top=15, right=15, bottom=15+48)
        has vbox:
            spacing 10
        text what id "what":
            outlines []
            yoffset 0
            pos (0, 0)
            font font.regular
        if triangle:
            add "bubble_triangle" xalign 1.0 yoffset 5


    frame:
        at bubble_t
        if color:
            background Frame(dark_colorize("gui/bubble/bubble_solid.png", color), left=15, top=15, right=15, bottom=15+48)
        else:
            background Frame("gui/bubble/bubble_solid.png", left=15, top=15, right=15, bottom=15+48)

        vbox:
            spacing 10
            text what id "what":
                outlines []
                yoffset 0
                pos (0, 0)
                font font.regular
            if triangle:
                add "bubble_triangle" xalign 1.0 yoffset 5

define _bubble_what = ""
define _bubble_color = "#FFF"
screen bubble_find():
    zorder 99
    showif not cInteraction:
        use bubble(what=_bubble_what, triangle=False, color=_bubble_color)

style bubble_frame:
    anchor (0.2, 0.3)
    padding (15+30, 15+20, 15+30, 15+48+20)
    xmaximum 800
    pos (1145, 240)








transform bubble_t:
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.25 alpha 0.0



transform slide_from_bot(t):
    on show:
        crop_relative True
        crop (0, 0, 1.0, 0.0)
        easein t crop (0, 0, 1.0, 1.0)
    on hide:
        crop_relative True
        crop (0, 0, 1.0, 1.0)
        easein t crop (0, 0, 1.0, 0.0)
    on replace:
        crop_relative True
        crop (0, 0, 1.0, 0.0)
        easein t crop (0, 0, 1.0, 1.0)
    on replaced:
        crop_relative True
        crop (0, 0, 1.0, 1.0)
        easein t crop (0, 0, 1.0, 0.0)


default findee = None
screen find():

    style_prefix "find"

    default sub = None

    if findee:

        showif is_scene("Find") and not cInteraction:

            add find_bg(findee) at normal_t(0.5)

            fixed:
                at slide_from_bot(0.5)

                xysize (1920, 190)
                yalign 1.0

                add "gui/find/find_bg.png"

                fixed pos (220, 947-890) xysize (123, 89) xoffset -10:
                    fixed:
                        xysize (103, 89) xoffset 10
                        add "gui/find/find_love.png"
                    text "Love {}".format(format(findee.love.value)) align (0.5, 0.5):
                        outlines [(1, "#9a1ec7")]
                fixed pos (340, 926-890) xysize (100, 112):
                    add "gui/find/find_lust.png"
                    text "H.A. {}".format(format(findee.harem.value)) align (0.5, 0.69):
                        outlines [(1, "#c7491e")]

                vbox pos (470, 948-890):
                    text "Relationship:" size 33 font font.bold
                    add "gui/find/{}.png".format(findee.relation)

                hbox:
                    align 1.0, 1.0
                    offset -20, -24
                    spacing 20

                    style_prefix "find_bar"

                    imagebutton:
                        idle "gui/find/general_interact.png"
                        insensitive insensitive("gui/find/general_interact.png")
                        action ToggleScreenVariable("sub", true_value="general", false_value=None)
                        sensitive get_available_interactions(findee.code, "general")

                    imagebutton:
                        idle "gui/find/shame.png"
                        insensitive insensitive("gui/find/shame.png")
                        action ToggleScreenVariable("sub", true_value="shame", false_value=None)
                        sensitive get_available_interactions(findee.code, "shame")

                    imagebutton:
                        idle "gui/find/sub.png"
                        insensitive insensitive("gui/find/sub.png")
                        action ToggleScreenVariable("sub", true_value="sub", false_value=None)
                        sensitive get_available_interactions(findee.code, "sub")

                    imagebutton:
                        idle "gui/find/skill.png"
                        insensitive insensitive("gui/find/skill.png")
                        action ToggleScreenVariable("sub", true_value="skill", false_value=None)
                        sensitive get_available_interactions(findee.code, "skill")

                    imagebutton:
                        idle "gui/find/inti.png"
                        insensitive insensitive("gui/find/inti.png")
                        action ToggleScreenVariable("sub", true_value="inti", false_value=None)
                        sensitive get_available_interactions(findee.code, "inti")

                    imagebutton:
                        idle "gui/find/take_her_to.png"
                        insensitive insensitive("gui/find/take_her_to.png")
                        action ToggleScreenVariable("sub", true_value="take", false_value=None)
                        sensitive get_findee_take_to_locs()

                    button:
                        add "gui/find/return.png"
                        action Function(show_map, at=True, time=0.3)

                fixed pos (14, 905-890) xysize (150, 170):
                    add "gui/icons/{}_icon.png".format(findee.code) align (0.5, 0.5) size (160, 160)
                    fixed xysize (150, 43) align (0.0, 1.0):
                        add Solid("#0000004D")
                        text "[findee.name]" align (0.5, 0.5)
                    add AlphaMask(Solid("#677377", xysize=(150, 170)), "gui/find/find_icon_mask.png")


            showif sub == "subplot":
                frame:
                    style "find_submenu"
                    at slide_from_bot(0.3)
                    has vbox
                    for subplot, name in get_findee_subplots().items():
                        textbutton "[name]" action [SetScreenVariable("sub", None), Function(run_replay, event=subplot, source=findee)]

            elif sub == "general":
                frame:
                    style "find_submenu"
                    at slide_from_bot(0.3)
                    has vbox
                    for interaction in get_available_interactions(findee.code, "general"):
                        button:
                            text interaction.name
                            action Function(interaction.run)

            showif sub == "inti":
                frame:
                    style "find_submenu"
                    at slide_from_bot(0.3)
                    has vbox
                    for interaction in get_available_interactions(findee.code, "inti"):
                        button:
                            text interaction.name
                            action Function(interaction.run)

            showif sub == "skill":
                frame:
                    style "find_submenu"
                    at slide_from_bot(0.3)
                    has vbox
                    for interaction in get_available_interactions(findee.code, "skill"):
                        button:
                            text interaction.name
                            action Function(interaction.run)

            showif sub == "sub":
                frame:
                    style "find_submenu"
                    at slide_from_bot(0.3)
                    has vbox
                    for interaction in get_available_interactions(findee.code, "sub"):
                        button:
                            text interaction.name
                            action Function(interaction.run)

            showif sub == "shame":
                frame:
                    style "find_submenu"
                    at slide_from_bot(0.3)
                    has vbox
                    for interaction in get_available_interactions(findee.code, "shame"):
                        button:
                            text interaction.name
                            action Function(interaction.run)

            showif sub == "take":
                frame:
                    style "find_submenu"
                    at slide_from_bot(0.3)
                    has vbox
                    for loc_tuple in get_findee_take_to_locs():
                        button:
                            text loc_tuple[0]
                            action Function(run_label, name=loc_tuple[1])










            if get_trainning_active():
                vbox:
                    pos 100, 180
                    for type in TrainingStatus.types:
                        $ action = get_trainning_action(type)
                        button:
                            background gui.bi70_frame
                            xysize 400, 60
                            margin (-30, -10)
                            padding (40, 30)
                            action action
                            text "%s" % TrainingStatus.type_names.get(type) align .0, .5
                            text "Lv. %s" % get_findee_training_level(type) align 1.0, .5
                            if action:
                                add "badge_red" xoffset 376 yoffset -36
            button:
                pos 1735, 30
                add "gui/change_background.png"
                action Show("bg_selection", transition=Dissolve(0.3))

            use bubble_find


style find_button:
    padding (0, 0)

style find_bar_button:
    padding (0, 0)
    background "gui/find/find_button_bg.png"

style find_bar_imagebutton:
    align (0.5, 0.5)

style find_text:
    size 28

style find_submenu:
    background Solid("#00000080")
    padding (30, 30)
    xanchor 0.5
    align (0.82, 1.0) yoffset -190

style find_vbox:
    spacing 24

style find_submenu_button_text:
    size 38
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
