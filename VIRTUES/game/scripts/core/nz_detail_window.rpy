transform nz_detail_overlay_swipe:
    on hide:
        xalign 0.0
        crop (0, 0, 1920, 1080)
        easein 0.5 crop (0, 0, 0, 1080)
    on show:

        xalign 1.0
        crop (1920, 0, 0, 1080)
        easein 0.5 crop (0, 0, 1920, 1080)
    on replaced:
        pause 0.03
        xalign 0.0
        crop (0, 0, 1920, 1080)
        easein 0.5 crop (0, 0, 0, 1080)
    on replace:

        xalign 1.0
        crop (1920, 0, 0, 1080)
        easein 0.5 crop (0, 0, 1920, 1080)

transform nz_detail_content_swipe:
    on hide:
        parallel:
            size (1920, 1080)
            easein 0.5 size (0, 1080)
        parallel:
            crop (0, 0, 1920, 1080)
            easein 0.5 crop (1920, 0, 0, 1080)
        parallel:
            xpos 960
            easein 0.5 xpos 2560
        size (1920, 1080)
        crop (0, 0, 1920, 1080)
        xpos 0
    on show:
        parallel:
            size (0, 1080)
            easein 0.6 size (1920, 1080)
        parallel:
            crop (1920, 0, 0, 1080)
            easein 0.6 crop (0, 0, 1920, 1080)
        parallel:
            align (0.0, 0.0)
            easein 0.6 align (1.0, 0.0)
    on replaced:
        parallel:
            size (1920, 1080)
            easein 0.5 size (0, 1080)
        parallel:
            crop (0, 0, 1920, 1080)
            easein 0.5 crop (1920, 0, 0, 1080)
        parallel:
            xpos 960
            easein 0.5 xpos 2560
        size (1920, 1080)
        crop (0, 0, 1920, 1080)
        xpos 0
    on replace:
        parallel:
            size (0, 1080)
            easein 0.6 size (1920, 1080)
        parallel:
            crop (1920, 0, 0, 1080)
            easein 0.6 crop (0, 0, 1920, 1080)
        parallel:
            align (0.0, 0.0)
            easein 0.6 align (1.0, 0.0)

init python in nz_detail:
    import store
    separator = store.Solid("#e6e6e659", xsize=1040, ysize=1, xalign=0.5)
    separator_short = store.Fixed(store.Solid("#e6e6e659", xsize=660, ysize=1, align=(0.5, 0.5)), xsize=660, ysize=21)



style nz_detail_label_text:
    font font.medium
    size gui.huge
    color gui.accent_color
    outlines gui.accent_outlines
    yalign 0.5

style nz_detail_name is label
style nz_detail_name_text is label_text:
    font font.semibold
    size 56
    xoffset -4

style nzd_content is vbox
style nzd_content_text:
    size 26

style nzd_content_label is label
style nzd_content_label_text:
    size gui.semi

transform nz_detail_transform:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

init python:
    _nz_detail = False

screen nz_detail(idx):
    predict False

    on "show" action SetVariable("_nz_detail", True)
    on "hide" action SetVariable("_nz_detail", False)

    zorder 86

    style_prefix "nz_detail"

    $ nz = nz_display_list[idx]


    add Image("gui/nzd/nzd_overlay_{}.png".format(nz.code), pos=(0, 0)):
        at nz_detail_overlay_swipe

    fixed:

        at nz_detail_content_swipe

        button:
            action Hide("nz_detail")
            alternate Play("sound", "sfx/button_click.ogg"), Hide("nz_detail")





        frame at nz_detail_transform:
            background None
            padding (0, 0)
            align (0.5, 0.5)
            xsize 1200 ysize 800 yoffset 120

            has hbox:

                spacing 40

            vbox:
                xsize 720 yfill 

                spacing 10
                label "[nz.name]" style "nz_detail_name"
                vbox:
                    style_prefix "nzd_content"
                    add nz_detail.separator_short

                    label "Age: "
                    text _("[nz.age]")
                    add nz_detail.separator_short

                    label "Favorites: "
                    text _(", ".join(nz.like))
                    add nz_detail.separator_short

                    label "About [nz.name]: "
                    text _(nz.intro() if callable(nz.intro) else nz.intro)

                    add nz_detail.separator_short
                    label "Erogenous Zones: "
                    text _(", ".join(nz.zone))

                    add nz_detail.separator_short
                    text nz.hint:
                        color color.important
                        font font.medium

            add nz.code.lower() + "_id" yoffset -40


    textbutton _("Return"):
        style "return_button"
        action Hide("nz_detail")

    hbox:
        xpos gui.navigation_xpos+140 yalign 1.0 yoffset -60
        if len(nz_display_list) == 1:
            pass
        else:
            textbutton ("<") action Show("nz_detail", idx=(len(nz_display_list)-1 if idx==0 else idx-1))
            textbutton (">") action Show("nz_detail", idx=(0 if idx==len(nz_display_list)-1 else idx+1))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
