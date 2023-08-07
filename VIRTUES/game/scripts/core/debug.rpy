default persistent.debug = False

init python in debug:
    import store
    events = store.defaultdict(list)

    def init():
        for name, event in store.EVENTS.items():
            
            prefix = name.split("_")[0]
            if prefix.isupper():
                events[prefix].append(event)
            elif event.repeatable:
                events["Повторяемый"].append(event)
            else:
                events["Другой"].append(event)
        
        for prefix, lst in events.items():
            events[prefix] = sorted(lst, key=store.sort_event)
        
        renpy.restart_interaction()

    def print_history():
        for i, event in enumerate(store.EventHistory):
            print("{}: {}".format(i, event))

    def full_history():
        s = ""
        total = len(store.EventHistory)
        for i, event in enumerate(reversed(store.EventHistory)):
            s += "{}: {}\n".format(total-i, event)
        return s

    def str_history():
        his20 = []
        for i, event in enumerate(store.EventHistory[-7:]):
            his20.append("{} {}".format(i, event))
        return ", ".join(his20)

style debug

style debug_frame:
    xalign 1.0
    yalign 1.0

style debug_button

style debug_button_text:
    size gui.semi

screen debug():
    style_prefix "debug"
    zorder 300

    if config.developer:

        key "m" action ToggleScreen("main_var")
        key "M" action ToggleScreen("main_var")
        key "e" action ToggleScreen("eventer")
        key "E" action ToggleScreen("eventer")
        key "p" action ToggleScreen("playleter")
        key "P" action ToggleScreen("playleter")

        default showing = ""

    else:
        key "e" action Call("escape")
        key "E" action Call("escape")


screen eventer():
    key "e" action ToggleScreen("eventer")
    key "E" action ToggleScreen("eventer")

    predict False

    zorder 1000
    style_prefix "eventer"
    default prefix = "A"

    use event_history

    frame:
        xalign 0.5
        background Solid("#000000")
        xysize 1400,1080
        has vbox
        text "{color=#d6d500}Текущее событие: [cEvent]{/color}"
        text "{{color=#7cd6be}}Очередь автособытий: {}{{/color}}".format(", ".join(auto_event_queue))
        textbutton "{{color=#8080ba}}История событий: {}{{/color}}".format(debug.str_history()):
            action ShowTransient("event_history"), debug.print_history

        hbox spacing 12:
            for k in debug.events.keys():
                textbutton k action SetScreenVariable("prefix", k)

        viewport:
            mousewheel True
            draggable True
            has vbox:
                xalign 0.5
                spacing 2

            for event in debug.events[prefix]:
                python:
                    error = False
                    try:
                        event.triggerable
                    except:
                        error = True
                if error:
                    vbox:
                        text ("{color=#d67c7c}[event.name] has an error!{/color}")
                        text ("{color=#d67c7c}%s" % traceback.format_exc())
                else:
                    hbox:
                        spacing 12
                        fixed:
                            xsize 220
                            if event.seen:
                                textbutton "{s}{color=#aaaaaa}[event.name]{/color}{/s}"
                            elif event.triggerable:
                                textbutton "{color=#7cd6be}[event.name]{/color}"
                            else:
                                textbutton "{color=#d67c7c}[event.name]{/color}"
                        fixed:
                            xsize 160
                            if not event.action:
                                text "AutoEvent"
                            else:
                                text "{color=#d6d500}%s{/color}" % "|".join(event.action_name)

                        textbutton "Run" action Function(event.run)
                        textbutton "FakeRun" action Function(fake_run_alternate, event=event)
                        textbutton "Un-run" action Function(unrun, event=event)

                        text " {color=#7cd6be}|{/color} ".join(event.get_triggerable_detail())

style eventer_frame:
    background Solid("#000000")

style eventer_fixed:
    ysize 32

style eventer_text:
    size 20

style eventer_button:
    padding (0, 0)
    size 20

style eventer_button_text:
    size 20

screen event_history():
    style_prefix "eventer"
    zorder 1001
    frame:
        xysize 240, 1080
        xalign 1.0
        has viewport:
            mousewheel True
            draggable True
        text debug.full_history()

screen main_var():
    zorder 1000

    frame:

        add main_var_dyn


init python:
    def toggle_event_seen(event):
        event.seen = not event.seen


    def sort_event(event):
        try:
            
            
            
            
            
            
            
            
            if not event.seen:
                return "0" + event.name
            else:
                return "1" + event.name
        except:
            pass
        return event.name

    def main_var(st, at):
        vb = VBox(
            Text("config.version=[config.version]"),
            Text("persistentn.version=[persistent.version]"),
            Text("_version=[_version]"),
            Text("state=[state]"),
            Text("t=[t]"),
            Text("cPlaylets=[cPlaylets]"),
            
            
            
            Text("cOneCG=[cOneCG]"),
            Text("cInteraction=[cInteraction]"),
            Text("cAction=[cAction]"),
            Text("cEvent=[cEvent]"),
            Text("cLabel=[cLabel]"),
            Text("cSay=[cSay]"),
            Text("_nz_detail=[_nz_detail]"),
            Text("_return=[_return]"),
            Text("A.love=[A.love.value]"),
            Text("B.love=[B.love.value]"),
            Text("C.love=[C.love.value]"),
            Text("D.love=[D.love.value]"),
            Text("E.love=[E.love.value]"),
            Text("F.love=[F.love.value]"),
            Text("G.love=[G.love.value]"),
        )
        return vb, 0
    main_var_dyn = DynamicDisplayable(main_var)


screen playleter():
    predict False
    key "p" action ToggleScreen("playleter")
    key "P" action ToggleScreen("playleter")

    zorder 1000
    default show_label = False
    frame:
        background Solid("#000000B0")
        xysize (1200, 900)
        align (0.05, 0.1)
        has viewport:
            xalign 0.5
            xsize 1200
            mousewheel True
            draggable True
        vbox:
            xalign 0.5
            spacing 2
            for nz, period_action_playlets in NZ_PLAYLETS.items():
                $ nz_color = get(nz).color if nz != "X" else "#7cd6be"
                hbox:
                    text "[nz]  " color nz_color
                    add Solid(nz_color, xfill=True, ysize=1, yalign=0.5)
                for period, action_playlets in period_action_playlets.items():
                    hbox:
                        text DAY_PERIOD_NAME[period] + "  " color "#a1bce0"
                        add Solid("#a1bce0", xfill=True, ysize=1, yalign=0.5)
                    for action, playlets in action_playlets.items():

                        for playlet in playlets:
                            $ playlet = get_playlet(playlet)
                            hbox:
                                style_prefix "eventer"
                                fixed:
                                    xsize 480
                                    text "[playlet.label]"
                                fixed:
                                    xsize 180
                                    text ("{color=#7cd6be}triggerable{/color}" if playlet.triggerable else "{color=#aaaaaa}untriggerable{/color}")
                                fixed:
                                    xsize 220
                                    if show_label:
                                        textbutton ("{color=#d6d500}[playlet.action]{/color}"):
                                            action ToggleScreenVariable("show_label")
                                    else:
                                        $ action = ACTIONS[playlet.action]
                                        textbutton ("{color=#d6d500}[action.name]{/color}"):
                                            action ToggleScreenVariable("show_label")
                                fixed:
                                    xsize 180
                                    for event in playlet.in_event:
                                        $ event = get_event(event)
                                        if event.seen:
                                            text "{color=#8dd7a2}[event.name]{/color}"
                                        else:
                                            text "{color=#aaaaaa}[event.name]{/color}"
                                fixed:
                                    xsize 120
                                    textbutton "Run" action Function(playlet.run)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
