screen mansion():

    zorder 90

    if is_scene("Map"):

        button:
            padding (0,0)
            action Hide("mansion")
            alternate Hide("mansion")

        button at normal_t(0.2):
            background gui.bi70_frame
            alternate Hide("mansion")
            xysize (1400, 900)
            align (0.5, 0.5)
            padding (60, 60)

            vbox:
                yalign 0.3
                style_prefix "bnbwvb"
                align (1.0, 0.0)
                spacing 10
                use sub_action_panel(mansion_action)

            frame:
                xsize 1000 ysize 800
                padding (30, 30)

                has vbox:
                    yalign 0.5

                hbox:
                    box_wrap True
                    box_wrap_spacing 20
                    spacing 20
                    for room in mansion_rooms.displaying_children:
                        vbox spacing 10:

                            button:
                                alternate Hide("mansion")

                                xysize room.xysize

                                if room.is_clickable:
                                    add "gui/action/{}.png".format(room.label)
                                    action room.run
                                else:
                                    add im.Grayscale("gui/action/{}.png".format(room.label))
                                    action NullAction()

                                add get_action_badge(room) align (0.0, 0.0) offset (-20, -25)





                            text room.name align (0.5, 1.0) size 24

                null height 36
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
