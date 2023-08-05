style top is default
style top_frame:
    padding (0, 0) margin (0, 0)
    background None
style top_button is button:
    padding (0, 0)
    align (0.5, 0.5)
style top_button_text is text:
    size 25
define top_value_frame = Frame("gui/top/frame.png", left=5, top=5)

screen top(force=False):
    style_prefix "top"
    showif is_scene("Map") or force:

        imagebutton auto "gui/top/guide_%s.png":
            align 0.0, 0.0
            xpos -22 ypos 136
            action Show('guide', transition=Dissolve(0.3))

        add "gui/top/bg.png"

        frame pos (148, 13) xysize (195, 140):
            xpadding 7
            has vbox:
                spacing 7
            frame ysize 42:
                xpadding 10
                background top_value_frame
                textbutton "[P.name]":
                    action Show("name_input", prompt="Пожалуйста, введите ваше имя:", prefix="Я ", suffix=".", rt=False)
                    hovered ShowTransient("player_panel_hover", content="Нажмите, чтобы изменить свое имя.")
                    unhovered Hide("player_panel_hover")










            frame ysize 42:
                xpadding 10
                background top_value_frame
                has hbox spacing 8 yoffset 6
                add "gui/top/cash.png" align (0.5, 0.5)
                textbutton "$[P.cash]":

                    unhovered Hide("player_panel_hover")
                    action NullAction()
                    hover_sound None


screen clock3(force=False):
    default glowing = False
    zorder 86

    showif is_scene("Map") or force:

        hbox pos (1577, 23):
            add "gui/clock/{}.png".format(t.period)
            fixed xysize (140, 120):
                vbox align (0.0, 0.5) offset (20, -1):
                    spacing -1
                    text ("Неделя {}").format(str(t.week)):
                        at normal_t_update(0.3)
                        size 28
                        font gui.clock_font
                        color "#28b4b5"


                    text ("{}").format(str(t.day)):
                        at normal_t_update(0.3)
                        size 25
                        font gui.clock_font
                        color "#28b4b5"

                    add DynamicDisplayable(period_func)

        button:
            pos (1580, 20)
            xysize (340, 150)
            background None

            action Function(pass_time)
            sensitive t.period < TimeToSleep

            hovered SetScreenVariable("glowing", True)
            unhovered SetScreenVariable("glowing", False)

        showif glowing:
            fixed at normal_t(0.2):
                pos (1562, 0) xysize (358, 158)
                frame:
                    align (0.5, 0.9)


                    text ">>> Нажмите, чтобы пропустить время." size 18

    else:
        $ glowing = False


init python:
    def period_func(screen_time, at, *args, **kwargs):
        txt = _("{}").format(str(t.period))
        kwargs = {
            "size": 28,
            "font": gui.clock_font,
            "color": clock_color,
            
        }
        return Text(txt, **kwargs), 0.01

