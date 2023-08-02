screen player_panel_hover(content=None):
    style_prefix "room_hover"
    default pos = list(renpy.get_mouse_pos())
    if pos[0] < 100:
        $ pos[0] += 100
    zorder 86
    frame:
        at normal_t(0.3)
        style_prefix "player_panel_hover"
        pos pos anchor (0, 0)
        text content




style player_panel_text

style player_panel_button_text is player_panel_text

style player_panel_frame:
    margin (-30, -30)
    padding (40, 40)
    background gui.bi70_frame

style player_panel_hover_text is player_panel_text:
    size gui.small






























































































style progress_text:
    size gui.semi
    xalign .5

define color.progress = {
    "study": "#508ac9",
    "work":"#d49331",
    "sport":"#208553"
}
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
