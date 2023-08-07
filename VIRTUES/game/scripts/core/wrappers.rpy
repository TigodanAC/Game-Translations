define nz_display_list = []
define progress_display_list = []

init -2 python:
    def pass_time():
        time_proceed(1)
        if t.period == Evening:
            renpy.show("map_latenight", at_list=[show_t(0.7)])
        auto_event()

    def has_event(name):
        return EVENTS.get(name)

    def run_event(name):
        store.cEvent = name
        renpy.jump('run_event')

    def run_label(name):
        store.cLabel = name
        renpy.jump('run_label')

    def show_find_fix(nz=None):
        store.cInteraction = None
        show_find(nz)

    def show_find(nz=None):
        set_scene("Find")
        if nz:
            store.findee = nz
        idx = int(random.random() * len(findee.tweets[findee.relation]))
        store._bubble_what = findee.tweets[findee.relation][idx]
        store._bubble_color = findee.color
        renpy.show_screen('find')

    def show_home():
        set_scene("Home")
        renpy.show_screen('home')

    def set_time(time):
        store.t = time
        _on_time_change()

    def time_proceed(period=1):
        store.t.proceed(period)
        _on_time_change()

    def new_day():
        renpy.hide_screen('mansion')
        renpy.hide_screen('college')
        renpy.hide_screen('bnb')
        store.t.new_day()
        _on_time_change()
        auto_event()

    def time_proceed_to(time):
        store.t.proceed_to(time)
        _on_time_change()

    def next_stage(owner, obj, handle=True):
        obj.next_stage()
        if not obj.out_of_content:
            Push(_("{} {} разблокирован, новый сюжет разблокирован").format(owner, obj))
        else:
            try:
                storyline_owner = obj.nz
            except AttributeError:
                storyline_owner = owner
            
            
            Push(_("Её любовь не может стать больше"))
            return

    def lock(obj, handle=True):
        obj.lock()

    def unlock(obj, handle=True):
        obj.unlock()


    def add(owner, obj, value, chance=0, handle=True):
        try:
            storyline_owner = obj.nz
        except AttributeError:
            storyline_owner = owner
        
        if type(obj) is Harem:
            if obj.value + value > obj.max_value:
                Push(_("Уровень принятия гарема {} не может быть повышен в текущей версии.").format(storyline_owner))
                return
        
        if obj.is_plot_locked:
            if obj is B.love:
                if seen("B_love_1"): 
                    Push("Я устал для учёбы, может быть, я должен потратить немного времени на Веру?")
            if obj is A.love:
                if seen("A_love_1"):
                    Push("Я слишком много времени потратил на Веру, может, мне стоит чаще ходить на занятия?")
            return
        
        if obj.is_stage_locked:
            _stage_lock_notification(owner, obj)
            return
        
        if obj.out_of_content:
            Push(_("Вы дошли до конца сюжетной линии {}.").format(storyline_owner))
            Push(_("Пожалуйста, дождитесь нашего следующего обновления."))
            return
        
        r = obj.add(value, chance)
        if r != 0.0:
            Push(_("{} {} увеличилось на {}").format(obj, owner, r))
        else:
            Push(_("{} {} не изменилась").format(obj, owner))
        
        if obj.is_stage_locked:
            _stage_lock_notification(owner, obj)

    def _stage_lock_notification(owner, obj):
        if obj >= obj.max_value:
            Push(_("Её любовь не может стать больше."))
            return
        
        if obj.owner == 'A':
            if obj >= 30:
                Push(_("{} {} на максимуме, найдите её в комнате и прокачайте её атрибуты.").format(obj, owner))
            else:
                Push(_("{} {} на максимуме, попробуте разблокировать по соответствующему событию").format(obj, owner))
        
        elif obj.owner == 'B':
            if obj >= 60 and not seen("B_daily_21"):
                Push(_("Сначала тебе следует улучшить отношения с Минной и Айрин."))
            elif obj >= 35:
                Push(_("{} {} на максимуме, найдите её в комнате и прокачайте её атрибуты.").format(obj, owner))
            else:
                Push(_("{} {} на максимуме, попробуте разблокировать по соответствующему событию").format(obj, owner))
        
        elif obj.owner == 'C':
            if obj >= 40:
                Push(_("{} {} на максимуме, найдите её в комнате и прокачайте её атрибуты.").format(obj, owner))
            else:
                Push(_("{} {} на максимуме, попробуте разблокировать по соответствующему событию").format(obj, owner))
        
        elif obj.owner == 'D':
            if obj >= 35:
                Push(_("{} {} на максимуме, найдите её в комнате и прокачайте её атрибуты.").format(obj, owner))
            else:
                Push(_("{} {} на максимуме, попробуте разблокировать по соответствующему событию").format(obj, owner))
        
        elif obj.owner == 'E':
            if obj >= 45:
                Push(_("{} {} на максимуме, найдите её в комнате и прокачайте её атрибуты.").format(obj, owner))
            else:
                Push(_("{} {} на максимуме, попробуте разблокировать по соответствующему событию").format(obj, owner))
        
        elif obj.owner == 'F':
            if obj >= 25 and not seen("A_love_5"):
                Push(_("Дальнейшая история Рэйчел будет доступна после того, как вы улучшите отношения с Верой."))
            elif obj is F.love and obj >= 30 and not seen("B_train_inti_1"):
                Push(_("Дальнейшая история Рэйчел будет доступна после того, как вы улучшите отношения с Сеннин."))
            elif obj is F.love and obj >= 35 and not seen("G_train_sha_2"):
                Push(_("Дальнейшая история Рэйчел будет доступна после того, как вы улучшите отношения с Уно."))
            elif obj is F.love and obj >= 40 and not seen ('ACG_duo_4'):
                Push(_("Сначала вы должны поднять принятие гарема у Веры, Тео и Уно."))
            else:
                Push(_("{} {} на максимуме, попробуте разблокировать по соответствующему событию").format(obj, owner))
        
        elif obj.owner == 'G':
            if obj >= 35:
                Push(_("{} {} на максимуме, найдите её в комнате и прокачайте её атрибуты.").format(obj, owner))
            else:
                Push(_("{} {} на максимуме, попробуте разблокировать по соответствующему событию").format(obj, owner))
        
        return

    def sub(owner, obj, value):
        r = obj.sub(value)
        Push(_("{} {} уменьшилась на {}").format(obj.name, owner, value))


    def not_implemented_message():
        Push("Извините, эта история будет реализована в будущей версии.")








    def time_warp(type):
        def ease(t):
            return .5 - math.cos(math.pi * t) / 2.0
        
        if type == "ease":
            return ease

    def show_map(at=False, time=0.7):
        set_scene("Map")
        
        renpy.music.play("music/Imagination - Rayn.opus", loop=True, if_changed=True)
        
        if is_day():
            
            if at:
                renpy.show("map_day", at_list=[show_t(time)])
            else:
                renpy.scene()
                renpy.show("map_day")
                renpy.with_statement(trans=Dissolve(time, time_warp=time_warp("ease")), always=False)
        else:
            
            if at:
                renpy.show("map_latenight", at_list=[show_t(time)])
            else:
                renpy.scene()
                renpy.show("map_latenight")
                renpy.with_statement(trans=Dissolve(time, time_warp=time_warp("ease")), always=False)

    def insensitive(image):
        return im.MatrixColor(image, im.matrix.saturation(0.0) * im.matrix.colorize("#303030", "#f0eee9"))

    def colorize(image, white_color):
        return im.MatrixColor(image, im.matrix.colorize("#000000", white_color))

    def dark_colorize(image, color):
        return im.MatrixColor(image, im.matrix.colorize(color, color) * im.matrix.brightness(-0.5))

    def dark(image):
        return im.MatrixColor(image, im.matrix.brightness(-0.3))

    def dark_insensitive(image):
        return im.MatrixColor(image,  im.matrix.brightness(-0.3) * im.matrix.saturation(0.0) * im.matrix.colorize("#303030", "#f0eee9"))

    class Handle(object):
        
        @classmethod
        def stage_locked(cls, obj):
            Push(_("{} {} на максимуме, попробуте разблокировать по соответствующему событию").format(obj.name, obj.owner.name))
        
        @classmethod
        def plot_locked(cls, obj):
            try:
                if not obj.is_visible:
                    return
            except AttributeError:
                pass
            Push(_("{} {} на максимуме, попробуте разблокировать по соответствующему событию").format(obj.name, obj.owner.name))
        
        @classmethod
        def unlocked(cls, obj):
            pass
            if isinstance(obj, Meter):
                Push(_("{} {} заблокирована").format(obj.name, obj.owner.name))
        
        @classmethod
        def increase(cls, obj, value):
            if value == 0.0:
                cls.unchanged()
            else:
                Push(_("{} {} увеличилась на {}").format(obj.name, obj.owner.name, value))
        
        @classmethod
        def decrease(cls, obj, value):
            if value == 0.0:
                cls.unchanged()
            else:
                Push(_("{} {} уменьшилось на {}").format(obj.name, obj.owner.name, value))
        
        @classmethod
        def unchanged(cls, obj):
            Push(_("{} {} без изменений").format(obj.name, obj.owner.name))
        
        @classmethod
        def cash_zero(cls, obj, value):
            Push(_("{} потерял все сбережения, всего {}".format(obj.name, value)))
        
        @classmethod           
        def cash_earn(cls, person, value, thing):
            Push(_("Вы заработали {}$ от {}").format(value, thing))
        
        @classmethod
        def purchase_succeeded(cls, obj, thing, value):
            Push(_("Сбережения {0} уменьшились на {1}$ после покупки {2}").format(obj.name, value, thing))
        
        @classmethod
        def purchase_failed(cls, thing):
            Push(_("Не хватает денег на покупку {}").format(thing))
        
        @classmethod
        def payment_succeeded(cls, obj, thing, value):
            Push(_("Сбережения {0} уменьшились на {1}$ после оплаты {2}").format(obj.name, value, thing))
        
        @classmethod
        def payment_failed(cls, thing):
            Push(_("Не хватает денег для оплаты {}").format(thing))
            run_event('suicide_ending')
        
        @classmethod
        def notify_new_location(cls, *args):
            Push(_("{} разблокирован").format(*args))
        
        @classmethod
        def time_pass(cls, value):
            if value == 1:
                Push(_("{} период времени пропущен").format(value))
            else:
                Push(_("{} временных периодов пропущено").format(value))
        
        @classmethod
        def lock_in_version(cls, obj):
            Push(_("Вы дошли до конца сюжетной линии {} на данный момент.").format(obj.owner))
            Push(_("Пожалуйста, дождитесь нашего следующего обновления."))
        
        @classmethod
        def out_of_content(cls, obj):
            Push(_("Вы дошли до конца сюжетной линии {}.").format(obj.owner))
            Push(_("Пожалуйста, дождитесь нашего следующего обновления."))


default available_interactions = defaultdict(set)
default available_clothes = defaultdict(set)
default auto_event_queue = set()

init python:

    def queue_auto_event():
        for ev_name in AUTO_EVENTS:
            ev = get_event(ev_name)
            if ev.is_auto_event and ev.triggerable and ev.runnable:
                auto_event_queue.add(ev_name)
                print("queue AutoEvent %s" % ev_name)

    def auto_event():
        if auto_event_queue:
            get_event(auto_event_queue.pop()).run()

    def _on_time_change():
        
        
        store.cPlaylets = get_cPlaylets()
        queue_auto_event()

    def _on_event_complete():
        print('_on_event_complete()')
        set_nz_locks()
        store.nz_display_list = get_displaying_nzs()
        store.fixed_rooms = get_bnb_rooms()
        update_nz_interactions()
        update_sleepers()
        
        store.cPlaylets = get_cPlaylets()


    def get_displaying_nzs():
        r = []
        if seen("d4_4") or seen('d4_4_bLine'):
            r.append(A)
        if seen("d1_1"):
            r.append(B)
        if seen("d2_1"):
            r.append(C)
        if seen("d7_1"):
            r.append(D)
        if seen("D_dqsj"):
            r.append(E)
        if seen("B_daily_5"):
            r.append(F)
        if seen("D_daily_3"):
            r.append(G)
        return r


    def set_nz_locks():
        plot_lock = False
        if seen("A_love_1"):
            plot_lock = True
        if seen("pcsj"):
            plot_lock = False
        
        A.love.meter.is_plot_locked = plot_lock
        
        
        plot_lock = True 
        if seen("d6_1"):
            plot_lock = False
        if seen("B_love_1"):
            plot_lock = True
        if seen("pcsj"):
            plot_lock = False
        
        B.love.meter.is_plot_locked = plot_lock

    def get_interaction(label):
        return INTERACTIONS.get(label)

    def get_nz_interactions(nz_code):
        return [it for it in NZ_INTERACTIONS[nz_code] if it.displaying]

    def get_nz_interaction_labels(nz_code):
        return [it.label for it in NZ_INTERACTIONS[nz_code] if it.displaying]




    def get_available_interactions(nz_code, type):
        its = []
        for it in available_interactions[nz_code]:
            it = get_interaction(it)
            if it.type == type:
                its.append(it)
        return its





    def update_nz_interactions():
        for nz in nz_display_list:
            old = available_interactions.get(nz.code, set())
            new = set(get_nz_interaction_labels(nz.code))
            for label in (new - old):
                Push('Новое взаимодействие с {} "{}" разблокировано.'.format(nz, get_interaction(label).name))
            available_interactions[nz.code] = new

    def get_nz_clothes(nz_code):
        return getattr(store, '%s_clothes' % nz_code)()

    def update_nz_clothes():
        for nz in nz_display_list:
            old = available_clothes.get(nz.code, set())
            new = set(get_nz_clothes(nz.code))
            for clothes in (new - old):
                if not clothes.startswith("Default"):
                    Push('Новый наряд для {} "{}" unlocked.'.format(nz, clothes))
            available_clothes[nz.code] = new

    def to_next_day():
        t.proceed_to(Morning)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
