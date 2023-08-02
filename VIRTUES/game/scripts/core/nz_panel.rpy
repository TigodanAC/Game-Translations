screen left_sensor():
    zorder 70
    button:
        xpos 0

        xsize 320

        ysize 600
        yalign 0.5
        background Solid("#00000000")
        action [Hide("left_sensor"), Show("nz_panel")]

init python:
    def resizing_shadow(st, at):
        try:
            size = renpy.get_screen("nz_panel").child.child.child.window_size
            xsize = size[0]
            ysize = size[1]
        except AttributeError:
            xsize = 270
            ysize = 1080
        return im.Crop(nz_panel.whole_shadow, (0, 0, 270, ysize), yalign=0.5), 1000

define nz_panel.whole_shadow = Image("gui/nz_panel_shadow_2.png", yalign=0.5)
define nz_panel.shadow = DynamicDisplayable(resizing_shadow)

style nz_panel_text is default:
    size 32
    outlines []
    font font.light
    align (.5, .5)

transform regular:
    zoom 0.6

transform small:
    zoom 0.7

screen nz_panel2():
    zorder 72
    showif is_scene("Map"):
        fixed:
            ypos 150 ysize 930

            frame at regular:
                align (0.0, 0.5)
                background gui.frame2019
                padding (0, 0)

                has vbox:
                    spacing 14
                for i, nz in enumerate(nz_display_list):
                    fixed:
                        xysize (217, 217)
                        button at zoom:
                            align (.5, .5)
                            anchor (.5, .5)
                            padding (.0, .0)
                            style_prefix "nz_panel"
                            action Show("nz_detail", idx=i)
                            has fixed:
                                xsize 200 ysize 200
                                xalign .5 yalign .5

                            add nz.code + "_icon"
                            add "icon_top"

                            fixed:
                                xysize (50, 50)
                                xpos 135
                                ypos 15
                                text format(nz.love.value)

                            fixed:
                                xysize (50, 50)
                                xpos 137
                                ypos 143
                                text format(nz.harem.value)

screen nz_panel():

    zorder 72
    showif is_scene("Map"):
        hbox:
            pos (8, 906)
            spacing 4
            for i, nz in enumerate(nz_display_list):
                fixed xysize (140, 170):
                    button at zoom:
                        padding (0, 0)
                        xysize (140, 170)
                        add "gui/nz/{}.png".format(nz.code)
                        action Show("nz_detail", idx=i)

                        fixed pos (37, 138) xysize (32, 28):
                            text format(nz.love.value) align (0.5, 0.5) size 25

                        fixed pos (103, 138) xysize (32, 28):
                            text format(nz.harem.value) align (0.5, 0.5) size 25

transform zoom:
    transform_anchor True
    rotate_pad True
    on show:
        alpha 0.5
        linear .2 alpha 1.0
    on hide:
        linear .2 alpha 0.0
    on idle:
        rotate None
        parallel:
            linear .1 zoom 1.0
        parallel:
            linear .1 offset (.0, .0)
    on hover:
        parallel:
            linear .1 zoom 1.1
            linear 0.025 rotate 2
            linear 0.025 rotate -2
            repeat
        parallel:
            xalign 0.0 yalign 1.0
            linear 0.1 yalign 1.0
            linear 0.1 xalign 0.5
    on selected_hover:
        rotate None
        linear .1 zoom 1.0

transform icon:
    on show:
        zoom 0.5
        alpha 0.5
        linear .2 alpha 1.0
    on hide:
        zoom 0.5
        linear .2 alpha 0.0
    on idle:
        parallel:
            linear .1 zoom 0.5
        parallel:
            linear .1 offset (.0, .0)
    on hover:
        parallel:
            linear .1 zoom 0.55
        parallel:
            linear .1 offset (8.0, 8.0)


init python:
    mouse_x = 0
    mosue_y = 0
    def _get_mouse_pos(st, at):
        store.mouse_x, store.mosue_y = renpy.get_mouse_pos()
        if mouse_x >= 400:
            renpy.hide_screen("left_bar")
            return Null(), 0.2
        return Null(), 0

    get_mouse_pos_displayable = DynamicDisplayable(_get_mouse_pos)

init python in left_panel:
    hovered = False

init python:
    class XScrollValue0(BarValue, FieldEquality):
        """
         :doc: value

         The value of an adjustment that horizontally scrolls the viewport with the
         given id, on the current screen. The viewport must be defined before a bar
         with this value is.
         """
        
        equality_fields = [ 'viewport' ]
        
        def __init__(self, viewport):
            self.viewport = viewport
        
        def get_adjustment(self):
            w = self.viewport
            if not isinstance(w, Viewport):
                raise Exception("The displayable with id %r is not declared, or not a viewport." % self.viewport)
            
            return w.xadjustment
        
        def get_style(self):
            return "scrollbar", "vscrollbar"

    class YScrollValue0(BarValue, FieldEquality):
        """
         :doc: value

         The value of an adjustment that vertically scrolls the viewport with the
         given id, on the current screen. The viewport must be defined before a bar
         with this value is.
         """
        
        equality_fields = [ 'viewport' ]
        
        def __init__(self, viewport):
            self.viewport = viewport
        
        def get_adjustment(self):
            
            w = self.viewport
            if not isinstance(w, Viewport):
                raise Exception("The displayable with id %r is not declared, or not a viewport." % self.viewport)
            
            return w.yadjustment
        
        def get_style(self):
            return "scrollbar", "vscrollbar"

transform icon2:
    on show:
        zoom 0.5
        alpha 0.8
        linear .2 alpha 1.0
    on hide:
        zoom 0.5
        linear .2 alpha 0.0
    on idle:


        linear 0.15 zoom 0.5
    on hover:




        linear 0.15 zoom 0.65
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
