screen home():

    style_prefix "find"

    default sub = None

    showif is_scene("Home"):

        add ImageReference("myroom_day_background") at normal_t(0.5)

        fixed:
            at slide_from_bot(0.5)

            xysize (1920, 190)
            yalign 1.0

            add Solid("#00000080")

            hbox:
                xalign 1.0 xoffset -30
                ypos 915-890
                spacing 20

                style_prefix "find_bar"

                imagebutton:
                    idle "gui/find/subplot.png"
                    insensitive insensitive("gui/find/subplot.png")
                    action ToggleScreenVariable("sub", true_value="subplot", false_value=None)
                    sensitive get_all_subplots()

                imagebutton:
                    idle "gui/find/endings.png"
                    insensitive insensitive("gui/find/endings.png")
                    action ToggleScreenVariable("sub", true_value="endings", false_value=None)
                    sensitive get_all_endings()

                imagebutton:
                    idle "gui/find/sleep_with.png"
                    insensitive insensitive("gui/find/sleep_with.png")
                    action ToggleScreenVariable("sub", true_value="sleep_with", false_value=None)
                    sensitive sleepers

                imagebutton:
                    idle "gui/find/sleep.png"
                    action [Hide("home"), Function(run_label, name="sleep_event")]

                if t.period != TimeToSleep:
                    button:
                        add "gui/find/return.png"
                        action Function(show_map, at=True, time=0.3)


        showif sub == "subplot":
            frame:
                style "find_submenu"
                at slide_from_bot(0.3)
                has vbox
                for subplot, name in get_all_subplots().items():
                    textbutton "[name]" action [Hide("home"), Function(run_replay, event=subplot, source="home")]

        showif sub == "endings":
            frame:
                style "find_submenu"
                at slide_from_bot(0.3)
                has vbox
                for ending, name in get_all_endings().items():
                    textbutton "[name]" action [Hide("home"), Function(run_replay, event=ending, source="home")]

        elif sub == "sleep_with":
            frame:
                style "find_submenu"
                at slide_from_bot(0.3)
                has vbox
                for nz in sleepers:
                    button:
                        text "%s" % get_nz(nz)
                        action [Hide("home"), Function(run_label, name="sleep_%s" % nz)]
                if seen("ACG_duo_5"):
                    button:
                        text "Your housemates"
                        action [Hide("home"), Function(run_label, name="sleep_ACG")]

    use top(True)
    use clock3(True)

label go_to_bed:
    if t.period < LateNight:
        "It's too early to go to bed."
    else:
        call sleep_event
    return

init python:
    def get_nz(code):
        for nz in [A, B, C, D, E, F, G]:
            if nz.code == code:
                return nz
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
