image fileslot_hover_border:
    Null()
    size (460, 258)
    on idle:
        contains:
            Null()
            size (4, 258)
        contains:
            "gui/fileslot_hover.png"
            alpha 1.0
            ease 0.4 alpha 0.0
    on hover:
        contains:
            Null()
            size (4, 258)
        contains:
            "gui/fileslot_hover.png"
            alpha 0.0
            ease 0.4 alpha 1.0

image fileslot_hover_border2:
    "gui/fileslot_hover.png"
    alpha 0.0
    ease 0.4 alpha 1.0









define gui.slot_button_width = 460
define gui.slot_button_height = 258
define gui.slot_button_borders = None
define gui.slot_button_text_size = 23
define gui.slot_button_text_xalign = 0.0
define gui.slot_button_text_color = color.cream





define config.thumbnail_width = 460
define config.thumbnail_height = 258


define gui.file_slot_cols = 3
define gui.file_slot_rows = 3


define gui.page_spacing = 0


define gui.slot_spacing = 30

init python:
    def generate_save_time():
        global save_name
        save_name = "{{color=#e5ca6e}}{}{{/color}} {}|".format(P.name, t)

    def parse_save_time(slot):
        try:
            return FileSaveName(slot).split("|")[1]
        except IndexError:
            return ""

screen file_slots(title):

    default desc = False

    on "show" action Function(generate_save_time)
    on "replace" action Function(generate_save_time)

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title)

    vpgrid:
        cols gui.file_slot_cols
        mousewheel True
        arrowkeys True
        draggable True
        scrollbars "vertical"



        ypos 240 ysize 730
        xsize 1920 xalign 0.5
        style_prefix "slot"
        spacing gui.slot_spacing

        for slot in trange(1, 21):

            fixed:
                xysize 460, 258
                add Solid("#adadad77", xysize=(460,258))

                button:
                    xysize 460, 258
                    background FileScreenshot(slot)
                    padding (0, 0)
                    if renpy.variant("touch"):
                        action FileAction(slot, confirm=True)
                    else:
                        action FileAction(slot)
                    if title == "Save":
                        alternate Show("save_input", slot=slot)
                        hovered SetLocalVariable("desc", True), MenuNotify("{color=#e8888a}Right Click{/color} to save with description.")
                    else:
                        alternate FileDelete(slot)
                        hovered SetLocalVariable("desc", True), MenuNotify("{color=#e8888a}Right Click{/color} to delete the save.")
                    unhovered HideMenuNotify(), SetLocalVariable("desc", False)
                    add "fileslot_hover_border"

                vbox:
                    yalign 0.0 xoffset 6
                    text FileSaveName(slot).split("|")[0]:
                        style "slot_name_text"

                    showif desc:
                        text parse_save_time(slot):
                            at normal_t(0.3)
                            style "slot_name_text"

                text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("Empty Slot")):
                    style "slot_time_text"
                    yalign 1.0 xoffset 6

                if FileJson(slot):
                    text "v%s" % FileJson(slot)["_version"]:
                        style "slot_time_text"
                        xalign 1.0 yalign 1.0 xoffset -4



    hbox:
        style_prefix "page"

        xalign 0.5
        yalign 1.0

        ysize 40 yoffset -60

        spacing gui.page_spacing

        textbutton _("<") action FilePagePrevious()

        if config.has_autosave:
            textbutton _("{#auto_page}A") action FilePage("auto")

        if config.has_quicksave:
            textbutton _("{#quick_page}Q") action FilePage("quick")


        hbox:
            for page in range(1, 21):
                textbutton "[page]" action FilePage(page)

        textbutton _(">") action FilePageNext()


    if renpy.variant("touch") and title == "Load":
        if title == "Load":
            use game_menu_notify("{color=#e8888a}Long Press{/color} to delete the save.", size=32)
    else:
        use game_menu_notify

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


screen save_input(slot):
    style_prefix "name_input"

    modal True

    key "mousedown_3" action Hide("save_input")

    default desc = ""

    frame at normal_t(0.4):
        xsize 800
        ysize 200
        xalign 0.5
        yalign 0.5
        has vbox:
            xalign 0.5
            yalign 0.5
        text "{color=#f0eee9}Save Description: {/color}":
            style "name_input_input"
        input:
            style "name_input_input"
            pixel_width 760
            copypaste True
            value ScreenVariableInputValue("desc", default=True, returnable=True)

        hbox:
            xalign 0.5
            button:
                style "name_input_button"
                text _("Confirm") style "name_input_button_text"
                action SetVariable("save_name", save_name+desc), FileAction(slot), Hide("save_input")

            button:
                style "name_input_button"
                text _("Cancel") style "name_input_button_text"
                action Hide("save_input")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
