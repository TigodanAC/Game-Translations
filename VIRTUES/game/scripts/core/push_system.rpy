init -2 python:

    class Message(object):
        def __init__(self, content, created_order=0):
            self.content = content
            self.created_order = created_order
            self.dying = False
            
            def __cmp__(self, other):
                return cmp(self.created_order, other.created_order)
        
        def __str__(self):
            return self.content
        
        def __repr__(self):
            return ("Message({}, {}, {})".format(self.content, self.created_order, self.dying))

    class Push(object):
        ui = [Message("")] * 8
        count = 0
        
        def __new__(cls, content):
            
            ui = cls.ui
            
            message = Message(content, cls.count)
            cls.count += 1
            
            try:
                for i, msg in enumerate(ui):
                    if msg.content is "":
                        idx = i
                        break
                else:
                    raise ValueError("no empty string")
            except ValueError:
                idx = cls.ui.index(min(cls.ui))
            except ValueError:
                idx = 0
            
            cls.ui[idx] = message
            
            
            
            renpy.invoke_in_thread (cls.pop, message=message)
        
        @classmethod
        def pop(cls, message):
            
            time.sleep(3)
            message.dying = True
            renpy.restart_interaction()
            
            
            time.sleep(0.5)
            try:
                cls.ui[cls.ui.index(message)] = store.Message("")
            except ValueError:
                pass




screen push():
    zorder 110
    style_prefix "push"

    vbox:
        for m in Push.ui:
            frame:
                text m.content
                if m.content is "":
                    at message_hide
                elif not m.dying:
                    at message_emerge
                else:
                    at message_disappear

transform message_emerge:
    alpha 0
    linear .5 alpha 1.0

transform message_disappear:
    linear .5 alpha 0.0

transform message_hide:
    alpha 0.0

style push_vbox:
    xpos 20
    ypos 390

style push_frame:
    ymargin gui.frame_margin +5
    ypadding gui.frame_padding -2

style push_text:
    size gui.regular

style push_text:
    variant "small"
    size 35
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
