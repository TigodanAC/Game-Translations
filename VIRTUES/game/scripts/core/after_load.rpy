default escaped_events = []
label escape:
    hide screen quick_navigation
    call screen hint("Эта кнопка выхода предназначена для того, чтобы вы могли избежать любого состояния, которое приводит к невозможности продолжить игру. Вы можете повторить события, из которых вы вышли, открыв это меню на карте, или подождать, пока оно снова не станет кликабельным.")
    menu:
        "Подтвердить":
            if cEvent:
                $ escaped_events.append(cEvent)
            $ show_map()
            jump pauser
        "Повторный запуск событий" if escaped_events and is_scene("Map"):
            python:
                while(escaped_events):
                    event = store.escaped_events.pop(0)
                    if event and not seen(event):
                        run_event(event)
            "Все пропущенные события просмотрены."
        "Отмена":
            return

default persistent.version = config.version
init python:
    print("config.version is %s" % config.version)

    if persistent.version != config.version:
        persistent.update_note_dontshowagain = False
        print("global version is %s, older than current version." % persistent.version)
        persistent.version = config.version
        print("global version set to %s.\n" % persistent.version)

    def migrate_event(old, new):
        print('migrate %s to %s' % (old, new))
        old_state = events_states.get(old)
        if old_state:
            events_states[new] = old_state
            events_states[new].label = new
        else:
            print('state of %s not found' % old)
        
        if store.cEvent == old:
            store.cEvent = new


    def _missing_label_callback(what):
        if type(what) is tuple:
            pass
        elif what in ("after_warp", "before_main_menu", "quit", "main_menu") or what.startswith(("_", "post")):
            pass
        else:
            Push("Hi there, the dialog \"{}\" seems to be missing from the game.".format(what))
        return "pauser_map"






    class EzClock():
        def dynamic_solid_func():
            pass
        def dynamic_period_func():
            pass
        def dynamic_date_func():
            pass

    RoomCG = OneCG



define config.missing_label_callback = _missing_label_callback



label after_load:

    $ print("_version = %s" % _version)

    $ load_data()

    $ _game_menu_screen = "save_screen"

    if type(_version) is int and 1000 <= _version < 1100:
        python:
            if cEvent is None:
                renpy.set_return_stack(["pauser_map"])
                renpy.block_rollback()
            else:
                renpy.set_return_stack(["pauser_map"])
                getCEvent().start_time = None
                getCEvent().seeing = False
                cEvent = None
                renpy.block_rollback()

    if ver2num(_version) < ver2num("0.4"):
        $ print ("applying 0.4 save fix,")

        python:
            clock_t = t.copy()

            B.love.value = int(B.love.value/6.0*5.0)
            C.love.value = int(C.love.value/6.0*5.0)
            F.love.value = int(F.love.value/6.0*5.0)

            if A.relation == "sexual":
                A.relation = "sexpartner"








            if cEvent is None:
                renpy.set_return_stack(["pauser_map"])
                renpy.block_rollback()
            else:
                renpy.set_return_stack(["pauser_map"])
                cEvent.start_time = None
                cEvent.seeing = False
                cEvent = None
                renpy.block_rollback()


        $ print ("0.4 save fix applied.")

    if ver2num(_version) < ver2num("0.5b"):
        $ print ("applying 0.5b save fix")

        if seen('pcsj'):
            $ fake_run('pcsjhx', 'bjsj', 'sbsj', 'jjsj')

        $ print ("0.5 save fix applied.")

    if ver2num(_version) < ver2num("0.6"):
        $ print ("applying 0.6 save fix,")

        if isinstance(cEvent, Event):
            $ cEvent = cEvent.name
            $ print ("cEvent = %s" % cEvent)

        python:
            for i in range(len(escaped_events)):
                if isinstance(escaped_events[i], Event):
                    escaped_events[i] = escaped_events[i].name

        if seen('d4_1'):
            $ fake_run('d4_1_bLine')

        if seen('d4_4'):
            $ fake_run('d4_4_bLine')

        if seen('d5_2'):
            $ fake_run('d5_2_bLine')

        if seen('d5_4'):
            $ fake_run('d5_4_bLine')

        if seen('A_love_2'):
            $ fake_run('A_love_2_bLine')

        if seen('AG_duo'):
            $ fake_run('AG_duo')

        if seen('DE_duo'):
            $ fake_run('DE_duo')

        if is_scene("PreMap"):
            $ set_scene("Map")

        if not findee:
            hide screen find

        if not is_scene("Home"):
            hide screen home

        $ migrate_event('A_love_6', 'A_train_sexskill_1')
        $ migrate_event('B_love_7', 'B_train_sexskill_1')

        if seen('A_train_sexskill_1'):
            $ add_training_level(A, 'skill')

        if seen('B_train_sexskill_1'):
            $ add_training_level(B, 'skill')

        python:
            for event in EVENTS.values():
                if event.seen and not event.repeatable:
                    event.run_results()

        $ available_clothes = {k.code:set(v) for k, v in available_clothes.items() if type(k) is Nz}

        $ print ("0.6 save fix applied.")

    if ver2num(_version) < ver2num("0.7"):
        $ cOneCG = None
        $ store.OneCGs = []
        python:
            for nz in [A,B,C,D,E,F,G]:
                nz.clothes = 1
        $ print ("0.7 save fix applied.")

    if _version != config.version:
        $ _version = config.version
        $ print("save version set to %s" % _version)

    if 'E' in TRAINING and TRAINING['E'].shame == 0:
        $ TRAINING['E'].shame = 1

    if D.love.is_stage_locked and D.love == 65 and seen("D_train_sha_2"):
        $ D.love.next_stage()

    python:
        for ev in EVENTS.values():
            if ev.state.seen:
                persistent.seens.append(ev.label)

    $ _on_time_change()
    $ _on_event_complete()

    $ save_bg_init()


    return

init 1 python:
    if persistent.bg_states:
        print("hacking persistent.bg_states...")
        
        for bg, bg_state in persistent.bg_states.items():
            persistent.bg_states_2[bg] = bg_state.is_password_unlocked
        
        persistent.bg_states.clear()
        
        print("hacked.")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
