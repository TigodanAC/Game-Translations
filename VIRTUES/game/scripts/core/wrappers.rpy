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
            Push(_("{}'s {} unlocked, new plot unlocked").format(owner, obj))
        else:
            try:
                storyline_owner = obj.nz
            except AttributeError:
                storyline_owner = owner
            
            
            Push(_("Her love cannot be raised further."))
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
                Push(_("{}'s harem acceptance level can't be further raised in current version.").format(storyline_owner))
                return
        
        if obj.is_plot_locked:
            if obj is B.love:
                if seen("B_love_1"): 
                    Push("I am tired of studying right now, perhaps I should spend some time on Вера")
            if obj is A.love:
                if seen("A_love_1"):
                    Push("I have spent too much time on Вера, maybe I should go to classes more often.")
            return
        
        if obj.is_stage_locked:
            _stage_lock_notification(owner, obj)
            return
        
        if obj.out_of_content:
            Push(_("You have reached the end of {}'s storyline for now.").format(storyline_owner))
            Push(_("Please wait for our next update."))
            return
        
        r = obj.add(value, chance)
        if r != 0.0:
            Push(_("{}'s {} increased by {}").format(owner, obj, r))
        else:
            Push(_("{}'s {} is unchanged").format(owner, obj))
        
        if obj.is_stage_locked:
            _stage_lock_notification(owner, obj)

    def _stage_lock_notification(owner, obj):
        if obj >= obj.max_value:
            Push(_("Her love cannot be raised further."))
            return
        
        if obj.owner == 'A':
            if obj >= 30:
                Push(_("{}'s {} is full, find her in her room and level up her attributes.").format(owner, obj))
            else:
                Push(_("{}'s {} is full, try unlock it by the relevant event").format(owner, obj))
        
        elif obj.owner == 'B':
            if obj >= 60 and not seen("B_daily_21"):
                Push(_("You should improve the relationship with Minna and Айрин first."))
            elif obj >= 35:
                Push(_("{}'s {} is full, find her in her room and level up her attributes.").format(owner, obj))
            else:
                Push(_("{}'s {} is full, try unlock it by the relevant event").format(owner, obj))
        
        elif obj.owner == 'C':
            if obj >= 40:
                Push(_("{}'s {} is full, find her in her room and level up her attributes.").format(owner, obj))
            else:
                Push(_("{}'s {} is full, try unlock it by the relevant event").format(owner, obj))
        
        elif obj.owner == 'D':
            if obj >= 35:
                Push(_("{}'s {} is full, find her in her room and level up her attributes.").format(owner, obj))
            else:
                Push(_("{}'s {} is full, try unlock it by the relevant event").format(owner, obj))
        
        elif obj.owner == 'E':
            if obj >= 45:
                Push(_("{}'s {} is full, find her in her room and level up her attributes.").format(owner, obj))
            else:
                Push(_("{}'s {} is full, try unlock it by the relevant event").format(owner, obj))
        
        elif obj.owner == 'F':
            if obj >= 25 and not seen("A_love_5"):
                Push(_("More of Рэйчел's story will be unlocked after you improve relationship with Вера."))
            elif obj is F.love and obj >= 30 and not seen("B_train_inti_1"):
                Push(_("More of Рэйчел's story will be unlocked after you improve relationship with Сеннин."))
            elif obj is F.love and obj >= 35 and not seen("G_train_sha_2"):
                Push(_("More of Рэйчел's story will be unlocked after you improve relationship with Уно."))
            elif obj is F.love and obj >= 40 and not seen ('ACG_duo_4'):
                Push(_("You should raise Вера, Theo, and Уно's harem acceptance first."))
            else:
                Push(_("{}'s {} is full, try unlock it by the relevant event").format(owner, obj))
        
        elif obj.owner == 'G':
            if obj >= 35:
                Push(_("{}'s {} is full, find her in her room and level up her attributes.").format(owner, obj))
            else:
                Push(_("{}'s {} is full, try unlock it by the relevant event").format(owner, obj))
        
        return

    def sub(owner, obj, value):
        r = obj.sub(value)
        Push(_("{}'s {} decreased by {}").format(owner, obj.name, value))


    def not_implemented_message():
        Push("Sorry, this story will be implemented in future version.")








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
            Push(_("{}'s {} is full, try unlock it by the relevant event").format(obj.owner.name, obj.name))
        
        @classmethod
        def plot_locked(cls, obj):
            try:
                if not obj.is_visible:
                    return
            except AttributeError:
                pass
            Push(_("{}'s {} locked, try unlock it by the relevant event").format(obj.owner.name, obj.name))
        
        @classmethod
        def unlocked(cls, obj):
            pass
            if isinstance(obj, Meter):
                Push(_("{}'s {} locked").format(obj.owner.name, obj.name))
        
        @classmethod
        def increase(cls, obj, value):
            if value == 0.0:
                cls.unchanged()
            else:
                Push(_("{}'s {} increased by {}").format(obj.owner.name, obj.name, value))
        
        @classmethod
        def decrease(cls, obj, value):
            if value == 0.0:
                cls.unchanged()
            else:
                Push(_("{}'s {} decreased by {}").format(obj.owner.name, obj.name, value))
        
        @classmethod
        def unchanged(cls, obj):
            Push(_("{}'s {} is unchanged").format(obj.owner.name, obj.name))
        
        @classmethod
        def cash_zero(cls, obj, value):
            Push(_("{} lost all the savings, {} in total".format(obj.name, value)))
        
        @classmethod           
        def cash_earn(cls, person, value, thing):
            Push(_("You have earned ${} from {}").format(value, thing))
        
        @classmethod
        def purchase_succeeded(cls, obj, thing, value):
            Push(_("{0}'s savings decreased by ${1} for purchasing {2}").format(obj.name, value, thing))
        
        @classmethod
        def purchase_failed(cls, thing):
            Push(_("No enough money for buying {}").format(thing))
        
        @classmethod
        def payment_succeeded(cls, obj, thing, value):
            Push(_("{0}'s savings decreased by ${1} for paying {2}").format(obj.name, value, thing))
        
        @classmethod
        def payment_failed(cls, thing):
            Push(_("No enough money for paying {}").format(thing))
            run_event('suicide_ending')
        
        @classmethod
        def notify_new_location(cls, *args):
            Push(_("{} unlocked").format(*args))
        
        @classmethod
        def time_pass(cls, value):
            if value == 1:
                Push(_("{} period of time passed").format(value))
            else:
                Push(_("{} periods of time passed").format(value))
        
        @classmethod
        def lock_in_version(cls, obj):
            Push(_("You have reached the end of {}'s storyline for now.").format(obj.owner))
            Push(_("Please wait for our next update."))
        
        @classmethod
        def out_of_content(cls, obj):
            Push(_("You have reached the end of {}'s storyline for now.").format(obj.owner))
            Push(_("Please wait for our next update."))


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
                Push('New interaction with {} "{}" unlocked.'.format(nz, get_interaction(label).name))
            available_interactions[nz.code] = new

    def get_nz_clothes(nz_code):
        return getattr(store, '%s_clothes' % nz_code)()

    def update_nz_clothes():
        for nz in nz_display_list:
            old = available_clothes.get(nz.code, set())
            new = set(get_nz_clothes(nz.code))
            for clothes in (new - old):
                if not clothes.startswith("Default"):
                    Push('{}\'s new outfit "{}" unlocked.'.format(nz, clothes))
            available_clothes[nz.code] = new

    def to_next_day():
        t.proceed_to(Morning)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
