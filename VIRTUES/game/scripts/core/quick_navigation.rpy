init python:
    if 'mouseup_3' in config.keymap["game_menu"]:
        config.keymap["game_menu"].remove('mouseup_3')

    def quick_navigation():
        if _menu:
            _invoke_game_menu()
        else:
            ToggleScreen("quick_navigation")()
    config.underlay.append(renpy.Keymap(mousedown_3=quick_navigation))

    def _K_ESCAPE():
        if _in_replay:
            EndReplay(confirm=True)
        elif _replaying_event:
            renpy.jump("event_post")
        elif _nz_detail:
            Hide("nz_detail")()
        else:
            _invoke_game_menu()
    config.underlay.append(renpy.Keymap(K_ESCAPE=_K_ESCAPE))

    def _boss_key():
        renpy.iconify()

    config.underlay.append(renpy.Keymap(b=_boss_key))
    config.underlay.append(renpy.Keymap(B=_boss_key))

    def _boss_quit():
        renpy.quit(relaunch=False, status=0, save=True)

    config.underlay.append(renpy.Keymap(K_BACKQUOTE=_boss_quit))
    config.underlay.append(renpy.Keymap(K_BACKQUOTE=_boss_quit))

    def _quick_save():
        for action in QuickSave():
            action()

    config.underlay.append(renpy.Keymap(q=_quick_save))
    config.underlay.append(renpy.Keymap(Q=_quick_save))












style quick_navigation_button is gui_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    padding (8, 8)

style quick_navigation_button_text is gui_button_text:
    properties gui.button_text_properties("navigation_button")
    size 34

transform qnbtn:
    on idle:
        linear .1 zoom 0.8
    on hover:
        linear .1 zoom 1.0

define _state_before_hide = None
init python:
    def get_qv_pos():
        x, y = renpy.get_mouse_pos()
        
        if y <= 408/2:
            y = 0
        
        elif y <= 1080-408/2:
            y -= 408/2
        
        elif y > 1080-408/2:
            y = 1080-408
        
        if x > 1800: 
            x = 1800
        
        return x, y










label show_save_menu:
    $ ShowMenu("save")
    return

screen show_save_menu():
    timer 0.000001 action [ShowMenu("save"), Hide("show_save_menu")]

screen quick_navigation():

    key "mouseup_1" action Hide("quick_navigation")

    default pos = get_qv_pos()

    zorder 200

    frame at qn_transform:

        pos pos[0], pos[1]
        xsize 120
        has vbox:
            style_prefix "quick_navigation"
            spacing 2

        if not _in_replay and not _replaying_event:

            textbutton _("Gallery") at qnbtn action Hide("quick_navigation"), ShowMenu("gallery")

        textbutton _("History") at qnbtn action Hide("quick_navigation"), ShowMenu("history")

        textbutton _("Setting") at qnbtn action Hide("quick_navigation"), ShowMenu("preferences")

        if not _in_replay and not _replaying_event:

            textbutton _("Load") at qnbtn action Hide("quick_navigation"), ShowMenu("load")

            textbutton _("Save") at qnbtn action Hide("quick_navigation"), Show("show_save_menu")

        if cAction or cEvent or cPlaylets or cInteraction or cLabel:
            textbutton _("Hide") at qnbtn action Hide("quick_navigation"), HideInterface()

        if _in_replay:

            textbutton _("End Replay") at qnbtn action Hide("quick_navigation"), EndReplay(confirm=False)

        if _replaying_event or (config.developer and is_scene("Event")):

            textbutton _("End Replay") at qnbtn action Hide("quick_navigation"), Jump("event_post")








        textbutton _("Escape") at qnbtn action Call("escape")

        if renpy.variant("pc") or renpy.variant("android"):


            textbutton _("Quit Game" if _in_replay else "Quit") at qnbtn action Quit(confirm=not main_menu)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
