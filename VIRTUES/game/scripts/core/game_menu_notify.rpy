screen game_menu_notify(text=None, size=None):
    zorder 100







    add gmn.text pos (50, 1034)
    if text:
        text text pos (50, 1034):
            if size:
                size size








transform game_menu_show_t:
    alpha 0.0
    ease 0.3 alpha 1.0

transform game_menu_hide_t:
    alpha 1.0
    ease 0.3 alpha 0.0

transform alpha(alpha):
    alpha alpha

init python in game_menu_notify:

    from store import renpy, At, Text, DynamicDisplayable, alpha

    show = False
    message = ""
    state = "hidden"
    showing_timer = 0.0
    hiding_timer = 0.0
    waiting_timer = 0.0

    show_duration = 0.3
    wait_duration = 0.3
    hide_duration = 0.3
    step = 0.01



    import time, threading

    def holder():
        
        while(True):
            
            global state, waiting_timer, showing_timer, hiding_timer, step
            global show_duration, wait_duration, hide_duration
            
            try:
                time.sleep(step)
                
                if state == "showing":
                    if showing_timer >= show_duration:
                        state = "holding"
                        showing_timer = 0.0
                    showing_timer += step
                else:
                    showing_timer = 0.0
                
                if state == "wait_hiding":
                    if waiting_timer >= wait_duration:
                        state = "hiding"
                        waiting_timer = 0.0
                    waiting_timer += step
                else:
                    waiting_timer = 0.0
                
                if state == "hiding":
                    if hiding_timer >= hide_duration:
                        state = "hidden"
                        hiding_timer = 0.0
                    hiding_timer += step
                else:
                    hiding_timer = 0.0
            
            except NameError:
                pass

    renpy.invoke_in_thread(holder)


    def hover(msg=None):
        
        if msg:
            global message
            message = msg
        
        global state, waiting_timer
        
        if state == "hidden":
            state = "showing"
            showing_timer = 0.0
        if state == "hiding":
            state = "holding"
            return
        elif state == "wait_hiding":
            state = "holding"
            holding_timer = 0.0
            return


    def unhover():
        global state, waiting_timer, thread_alive
        
        
        
        
        
        
        if state == "showing":
            state = "hiding"
            hiding_timer = 0.0
            return
        elif state == "holding":
            state = "wait_hiding"
            return

    def state1(st, at):
        return Text(state), None

    def state2(st, at):
        return Text(str(waiting_timer)), None

    d = DynamicDisplayable(state1)
    d1 = DynamicDisplayable(state2)

    def get_alpha(ratio):
        return hex(ratio)[2:].rjust(2, str("0"))

    def func(st, at):
        global state, showing_timer, hiding_timer, step
        global show_duration, wait_duration, hide_duration
        
        cream = u"#f0eee9"
        
        
        if state in ("holding", "wait_hiding"):
            
            return Text(message), step
        
        elif state == "showing":
            
            ratio = showing_timer/show_duration
            
            return At(Text(message), alpha(ratio)), step
        
        elif state =="hiding":
            
            ratio = 1 - hiding_timer/hide_duration
            
            return At(Text(message), alpha(ratio)), step
        
        elif state == "hidden":
            
            return Text(""), step


    text = DynamicDisplayable(func)

init python:

    gmn = game_menu_notify

    def MenuNotify(message=None):
        return Function(game_menu_notify.hover, msg=message)

    def HideMenuNotify():
        return Function(game_menu_notify.unhover)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
