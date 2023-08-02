image gallery_hover_border:
    Null()
    size (460, 258)
    on idle:
        contains:
            Null()
            size (460, 258)
        contains:
            "gui/gallery_hover.png"
            size (460, 258)
            alpha 1.0
            ease 0.4 alpha 0.0
    on hover:
        contains:
            Null()
            size (460, 258)
        contains:
            "gui/gallery_hover.png"
            size (460, 258)
            alpha 0.0
            ease 0.4 alpha 1.0


init python:

    CGSETS = defaultdict(list) 

    class CGSet:
        pass

    class ComplexCGSet:
        pass

    class CGList:
        pass

    class EventCGSet(object):
        
        def __init__(self, label, thumbnail, images=[]):
            self.label =label
            self.thumbnail = thumbnail
            self.images = images
            
            prefix = label.split("_")[0]
            if prefix.isupper():
                for code in prefix:    
                    nz = globals()[code].name
                    CGSETS[nz].append(self)
            else:
                CGSETS["Other"].append(self)
            
            self.action = [Function(late_replay, label=label)]
        
        def __repr__(self):
            return "EventCGSet(%s)" % self.label

    def get_cgset(label):
        try:
            return CGSETS[label]
        except:
            print("CGSet %s not found." % label)

    def unlock_from_gallery(name):
        if not name in persistent.seens:
            persistent.seens.append(name)

default persistent.seens = []
default persistent.replay_notify = True
screen gallery():
    tag menu




    default notified = False

    default tab = "Вера"

    use game_menu("Gallery")

    vbox:
        ypos 240 ysize 730
        xsize 1920 xalign 0.5
        xoffset 240

        hbox spacing 12:
            for k in ["Вера", "Айрин", "Рэйчел", "Теодора", "Уно", "Элиза", "Сеннин", "Other"]:
                textbutton k action SetScreenVariable("tab", k)

        vpgrid:
            cols 3
            mousewheel True
            arrowkeys True
            draggable True
            scrollbars "vertical"
            spacing 30

            for cgset in CGSETS[tab]:
                fixed:
                    xysize (460, 258)
                    add (cgset.thumbnail+"_thumbnail" if cgset.label in persistent.seens else "locked") size (460, 258)

                    button:
                        padding (0, 0)
                        add "gallery_hover_border"
                        if cgset.label in persistent.seens:
                            action ShowTransient("gallery_viewer", cgset=cgset, transition=Pixellate(0.5, 8))
                            alternate cgset.action
                        if renpy.variant("pc"):
                            hovered MenuNotify("{color=#e8888a}Right click{/color} to replay the memory.")
                            unhovered HideMenuNotify()

    if not notified:
        on "show" action If(renpy.variant("touch"), true=MenuNotify("{color=#e8888a}Long press{/color} to replay the memory."))

    if renpy.variant("touch"):
        use game_menu_notify("{color=#e8888a}Long Press{/color} to replay the memory.", size=32)
    else:
        use game_menu_notify

    showif persistent.replay_notify and renpy.variant("pc"):
        frame:
            padding (28, 28)
            at normal_t(0.5)
            align (0.5, 0.5)
            has vbox
            text "{color=#e8888a}Right click{/color} to replay the memory.{color=#e8888a}" size 32
            textbutton "OK" action SetVariable("persistent.replay_notify", False) xalign 0.5 yoffset 10

screen gallery_viewer(cgset):
    predict False

    default i = 0

    add cgset.images[i-1 if i>0 else 0]
    add cgset.images[i] at gallery_switch(0.2)
    button:
        if i < len(cgset.images)-1:
            action SetScreenVariable("i", i+1)
        else:
            action Hide("gallery_viewer", transition=Pixellate(0.5, 6))
        alternate Hide("gallery_viewer", transition=Pixellate(0.5, 6))

    key "game_menu" action Hide("gallery_viewer", transition=Pixellate(0.5, 6))




screen gallery_navigation():
    hbox:
        spacing 20

        style_group "gallery"
        align (.98, .98)

        textbutton _("prev")
        textbutton _("next")
        textbutton _("return") action Return()

python:
    style.gallery = Style(style.default)
    style.gallery_button.background = None
    style.gallery_button_text.color = "#666"
    style.gallery_button_text.hover_color = "#fff"
    style.gallery_button_text.selected_color = "#fff"
    style.gallery_button_text.size = 16
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
