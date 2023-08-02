screen tutorial_overlay():
    zorder 10
    add confirm_overlay at normal_t(0.5)

screen tutorial(beg, end):
    modal True

    zorder 150

    button:












        add "tutorial_{}".format(beg)

        if beg >= end:
            action Return()
        else:
            action Show("tutorial", beg=beg+1, end=end)

        activate_sound None
        hover_sound None
        at transform:
            on show:
                alpha 0.0
                linear 0.5 alpha 1.0
            on hide:
                linear 0.5 alpha 0.0
            on replace:
                alpha 0.0
                linear 0.3 alpha 1.0
            on replaced:
                linear 0.3 alpha 0.0
    on "show" action Show("tutorial_overlay")
    on "hide" action Hide("tutorial_overlay")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
