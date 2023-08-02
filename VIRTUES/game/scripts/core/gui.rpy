init offset = -2









init python:
    gui.init(1920, 1080)












define color.xpf = "#b79c9d"
define color.nxpf = "#9e8687"
define color.gnxpf = "#8f797a"
define color.cream = "#f0eee9"
define color.grey0 = "#aaaaaa"
define color.grey1 = "#6f6f6f"
define color.rpf0 = "#e066a3"
define color.powerder = "#f2e6dd"
define color.mh = "#cc0066"
define color.blackish = "#2e2e2c"
define color.some_pink = "#E08E8E"
define color.important = "#ffcd5c"


define gui.main_accent_color = "#ef869f"


define gui.selected_color = "#f0a6b2"

define confirm_overlay = Solid("#00000060")

define gui.bi70_solid = Solid("#2e2e2cb3")
define gui.bi70_frame = Frame("/gui/frame2020.png", 15, 15)
define gui.frame_margin = -15
define gui.frame_padding = 20

define gui.not_implemented_color = color.grey1
define gui.hovered_color = gui.main_accent_color


define gui.frame_borders = Borders(5, 5, 5, 5, -5, -5, -5,- 5)
define gui.frame_tile = True

define gui.dialogue_color = "#E6E6E6"


define gui.ultra = 48
define gui.huge = 34
define gui.big = 30
define gui.semi = 28
define gui.regular = 24
define gui.small = 22

init -1 python in font:
    pass

define font.light = "fonts/Monorale-Light.otf"
define font.regular = "fonts/Monorale-Regular.otf"
define font.medium = "fonts/Monorale-Medium.otf"
define font.semibold = "fonts/Monorale-SemiBold.otf"
define font.bold = "fonts/Monorale-Bold.otf"
define font.black = None
define font.thin = "fonts/Monorale-Thin.otf"

define gui.dialogue_outlines = [(3, "#514546")]

define gui.regular_outlines = [ (0, "#00000059", 1, 1), (1, "#51454659") ]
define gui.large_outlines = [ (0, "#00000059", 1, 1), (2, "#51454659") ]

define gui.regular_light_default_outlines = [(1, "#635556")]

define gui.interface_text_size = 32


define gui.accent_color = gui.main_accent_color
define gui.accent_outlines = [(2, "#514546")]


define gui.text_size = gui.semi
define gui.text_color = gui.dialogue_color
define gui.text_outlines = gui.regular_outlines


define gui.name_text_size = 45
define gui.protagonist_name_size = 45


define gui.idle_color = "#E6E6E6"



define gui.idle_small_color = gui.main_accent_color


define gui.hover_color = gui.main_accent_color


define gui.insensitive_color = '#aaaaaa7f'



define gui.muted_color = gui.main_accent_color
define gui.hover_muted_color = "#f0eee9"


define gui.name_text_color = "#f0eee9"
define gui.name_text_outlines = [ (1, "#00000059", 1, 1), (1, "#514546")]
define gui.namebox_background = None



define gui.interface_text_color = "#E6E6E6"
define gui.interface_text_outlines = gui.large_outlines



define gui.label_text_font = font.medium
define gui.label_text_size = gui.huge
define gui.label_text_color = "#f0a6b2"
define gui.label_text_outlines = [ (0, "#00000059", 1, 1), (1, "#514546") ]

define gui.frame_text_outlines = gui.large_outlines




define gui.clock_font = font.light


define gui.text_font = font.regular

define gui.dialogue_text_font = "fonts/SourceHanSansJP-medium.ttf"


define gui.name_text_font = "fonts/SourceHanSansJP-medium.ttf"


define gui.interface_text_font = font.regular


define gui.notify_text_size = 24


define gui.title_text_size = 75
define gui.title_text_outlines = [(6, "#514546")]





define gui.game_menu_background = "gui/game_menu.png"








define gui.textbox_height = 278



define gui.textbox_yalign = 1.0




define gui.name_xpos = 360
define gui.name_ypos = 0



define gui.name_xalign = 0.0



define gui.namebox_width = None
define gui.namebox_height = None



define gui.namebox_borders = Borders(5, 5, 5, 5)



define gui.namebox_tile = False





define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75


define gui.dialogue_width = 1116



define gui.dialogue_text_xalign = 0.0








define gui.button_width = None
define gui.button_height = None

define gui.button_padding = (0, 0)


define gui.button_borders = Borders(6, 6, 6, 6)



define gui.button_tile = False


define gui.button_text_font = gui.interface_text_font


define gui.button_text_size = gui.interface_text_size


define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color



define gui.button_text_xalign = 0.0








define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color















define gui.navigation_xpos = 60


define gui.skip_ypos = 15


define gui.notify_ypos = 68


define gui.navigation_spacing = 12


define gui.pref_spacing = 15


define gui.pref_button_spacing = 0


define gui.main_menu_text_xalign = 1.0
define gui.main_menu_text_outlines = gui.frame_text_outlines











define gui.confirm_frame_borders = Borders(60, 60, 60, 60)


define gui.skip_frame_borders = Borders(24, 8, 75, 8)


define gui.notify_frame_borders = Borders(24, 8, 60, 8)














define gui.bar_size = 38
define gui.scrollbar_size = 10
define gui.slider_size = 38


define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False


define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)


define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)



define gui.unscrollable = "hide"







define config.history_length = 250



define gui.history_height = None



define gui.history_name_xpos = 160
define gui.history_name_ypos = 0
define gui.history_name_width = 160
define gui.history_name_xalign = 1.0


define gui.history_text_xpos = 182
define gui.history_text_ypos = 3
define gui.history_text_width = 1040
define gui.history_text_xalign = 0.0







define gui.nvl_borders = Borders(0, 15, 0, 30)



define gui.nvl_list_length = 6



define gui.nvl_height = 173



define gui.nvl_spacing = 15



define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0


define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0



define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0


define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0







define gui.language = "unicode"






init python:



    if renpy.variant("touch"):
        
        gui.quick_button_borders = Borders(60, 21, 60, 0)



    if renpy.variant("small"):
        
        gui.scrollbar_size = 54
        
        
        gui.text_size = 38
        gui.name_text_size = 52
        gui.notify_text_size = 34
        gui.interface_text_size = 36
        gui.button_text_size = 36
        gui.label_text_size = 36
        
        
        gui.textbox_height = 390
        gui.name_xpos = 220
        gui.dialogue_xpos = 240
        gui.dialogue_ypos = 85
        gui.dialogue_width = 1440
        
        
        gui.slider_size = 50
        
        gui.navigation_spacing = 26 
        gui.pref_button_spacing = 15
        
        gui.history_height = 285
        gui.history_text_width = 1035
        
        gui.quick_button_text_size = 34
        
        
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        
        
        gui.nvl_height = 255
        
        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488
        
        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8
        
        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30
        
        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
