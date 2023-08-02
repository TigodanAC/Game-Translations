transform uhd:
    zoom .5

transform normal_t_all(t):
    on show:
        alpha 0.0
        linear t alpha 1.0
    on hide:
        linear t alpha 0.0
    on replace:
        alpha 0.0
        linear t alpha 1.0
    on replaced:
        linear t alpha 0.0

transform normal_t(t, t1=None):
    on show:
        alpha 0.0
        linear t alpha 1.0
    on hide:
        linear (t1 if t1 else t) alpha 0.0

transform qn_transform():
    on show:
        alpha 0.0
        linear 0.2 alpha 1.0

transform reverse_normal_t(t):
    on show:
        linear t alpha 0.0
    on hide:
        alpha 0.0
        linear t alpha 1.0

transform normal_t_update(t):
    on show:
        alpha 0.0
        linear t alpha 1.0
    on hide:
        linear t alpha 0.0
    on replace:
        alpha 0.0
        linear t alpha 1.0
    on replaced:
        linear t alpha 0.0
    on update:
        alpha 0.0
        linear t alpha 1.0

transform gallery_switch(t):
    on update:
        alpha 0.0
        linear t alpha 1.0

transform title:
    on show:
        alpha 0.0
        linear 0.3 alpha 1.0

transform pause_emerge(pause):
    on show:
        alpha 0.0
        pause pause
        linear 0.5 alpha 1.0

transform emerge2:
    on show:
        alpha 0.5
        linear .2 alpha 1.0
    on hide:
        linear .2 alpha 0.0
    on replace:
        alpha 0.7
        linear 0.2 alpha 1.0
    on replaced:
        alpha .7
        linear 0.2 alpha 0.0

transform zoom_emerge:
    on show:
        align (0.5, 0.5)
        zoom 0.9
        linear .2 zoom 1.0
    on hide:
        parallel:
            linear .2 zoom 0.9
        parallel:
            linear .2 alpha 0.0


transform nzd_show:
    parallel:
        zoom 0.85
        linear .1 zoom 1.0
    parallel:
        alpha 0.0
        linear .1 alpha 1.0

transform nzd_hide:
    parallel:
        linear .1 zoom 0.85
    parallel:
        linear .1 alpha .0

transform textbox_blur:
    yalign 1.0
    on show:
        crop ((0, 820, 1920, 260))



transform left_slide():
    on show:
        xpos -320
        linear 0.3 xpos 0
    on hide:
        linear 0.3 xpos -320

transform left_slide_resize(xsize, ysize):
    size (xsize, ysize)
    on show:
        xpos -320
        linear 0.3 xpos 0
    on hide:
        linear 0.3 xpos -320

init python in textbox:
    import store

    def show(trans, st, at):
        duration = .4
        
        
        
        
        if st < duration:
            trans.yoffset = 278 * (1 - st/duration)
            return .0
        elif st >= duration:
            trans.yoffset = 0
            return None

    def hide(trans, st, at):
        pass



transform show_t(t):
    alpha 0.0
    ease t alpha 1.0

transform hide_t(t):
    alpha 0.0
    ease t alpha 1.0

transform textbox_transform:
    on show:
        function textbox.show
    on hide:
        yoffset 0
        linear 0.3 yoffset 250
        function textbox.hide

transform text_fade_in:
    alpha 0
    linear 0.5 alpha 1

init python:
    wr3 = CropMove(0.3, "wiperight")
    wl3 = CropMove(0.3, "wipeleft")            

transform wr3:
    on replaced:
        crop_relative True
        crop (0, 0, 1.0, 1.0)
        easein 1 crop (0, 0, 0.0, 1.0)
    on replace:
        pause 1
        crop_relative True
        crop (0, 0, 0.0, 1.0)
        easein 1 crop (0, 0, 1.0, 1.0)

transform wl3:
    on replaced:
        crop_relative True
        crop (1.0, 0, 1.0, 1.0)
        easein 1 crop (0, 0, 0.0, 1.0)
    on replace:
        pause 1
        crop_relative True
        crop (1.0, 0, 0.0, 1.0)
        easein 1 crop (0, 0, 1.0, 1.0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
