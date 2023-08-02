screen bigclock():
    style_prefix "bigclock"

    zorder 100
    button action Return()
    frame:
        at bigclock
        background Solid("#2e2e2c7F")
        xfill True ysize 250 yalign 0.45
        has vbox:
            xalign 0.2 yalign 0.5
        text _("{}").format(DAY_PERIOD_NAME[t.period])
        text _("Week {}, {}").format(t.week, str(t.day))

style bigclock_text:
    size 40

transform bigclock:
    on show:
        alpha 0.0
        linear 1.0 alpha 1.0
    on hide:
        linear 1.0 alpha 0.0


style clock_button is default:
    properties gui.button_properties("clock")

style clock_button_text is default:
    properties gui.button_text_properties("clock")

transform clock_atl:
    on hover:
        alpha 1.0
        linear 0.2 alpha 0.7
    on idle:

        alpha 0.7
        linear 0.2 alpha 1.0

screen clock_glow():
    zorder 87
    add Image("gui/clock/clock_glow.png", xpos=clock.xpos, ypos=clock.ypos, xoffset=clock.xoffset-10, yoffset=clock.yoffset-10)
    text "Click to skip a time period":
        size 16
        xalign 1.0 xoffset -56
        ypos 15
        font gui.clock_font
        color "#F0EEE9"
        outlines gui.clock_timeext_outlines
    fixed:
        xpos clock.xpos
        ypos clock.ypos
        xsize clock.xsize
        ysize clock.ysize
        use body

screen clock_pressed():
    zorder 87
    timer 0.05 action Hide("clock_pressed")
    add Image("gui/clock/clock_pressed.png", xpos=clock.xpos, ypos=clock.ypos)
    fixed:
        xpos clock.xpos
        ypos clock.ypos
        xsize clock.xsize
        ysize clock.ysize
        use body

define gui.clock_timeext_outlines = [(3, "#F0EEE906"), (2.5, "#F0EEE90c"), (2, "#F0EEE912"), (1.5, "#F0EEE918"), (1, "#F0EEE91e"), (0.5, "#F0EEE924")]

screen body():
    if t.period == Morning:
        fixed at tsfm_morning

    elif t.period == Forenoon:
        fixed at tsfm_forenoon

    elif t.period == Afternoon:
        fixed at tsfm_afternoon

    elif t.period == Evening:
        fixed at tsfm_evening

    elif t.period == LateNight:
        fixed at tsfm_latenight

    elif t.period == TimeToSleep:
        fixed at tsfm_tts





transform tsfm_morning:
    contains:
        clock.sun
        xalign 0.5 yalign 0.3 alpha 0.0
        linear 0.5 alpha 1.0
    contains:
        clock.moon
        xalign 0.5 yalign 0.3 alpha 1.0
        linear 0.5 alpha 0.0

transform tsfm_forenoon:
    clock.sun
    xalign 0.5 yalign 0.3

transform tsfm_afternoon:
    clock.sun
    xalign 0.5 yalign 0.3

transform tsfm_evening:
    contains:
        clock.moon
        xalign 0.5 yalign 0.3 alpha 0.0
        linear 0.5 alpha 1.0
    contains:
        clock.sun
        xalign 0.5 yalign 0.3 alpha 1.0
        linear 0.5 alpha 0.0

transform tsfm_latenight:
    clock.moon
    xalign 0.5 yalign 0.3

transform tsfm_tts:
    clock.moon
    xalign 0.5 yalign 0.3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
