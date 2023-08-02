init -4 python:

    def ver2num(v):
        if type(v) is unicode:
            m = re.match('(\d+(?:\.\d+)?)([a-z])?', v)
            f = float(m.group(1)) * 1000
            letter = m.group(2)
            letter_f = (ord(letter) - 96) if letter else 0
            return int(f + letter_f)
        elif isinstance(v, int):
            return v
        else:
            print("wrong type of version in ver2num(v).")
            return v

    def copy_func(f, name=None):
        import types
        return types.FunctionType(f.func_code, f.func_globals, name or f.func_name,
            f.func_defaults, f.func_closure)

    def get_random(denominator):
        return int(random.random() * denominator)

    def get(name):
        return globals()[name]

    def sval(obj):
        return obj.sval()

    def trange(beg, end=None):
        if end:
            return range(beg, end+1)
        else:
            return range(1, beg+1)

    class RandomChoice(object):
        def __init__(self, total):
            self.total = total
            self.value = random.random()
            self.unitchance = 1.0/total
        
        def __call__(self, index):
            if index > self.total:
                raise Exception("bigger than total choice number.")
            return int(self.value/self.unitchance) == index-1

init -1 python:

    weekday_range = [Monday,Tuesday,Wednesday,Thursday,Friday]

    weekend_range = [Saturday,Sunday]

    day_periods = [Morning, Forenoon, Afternoon]
    night_periods = [Evening, LateNight]

    def day_range(beg, end):
        return list(range(beg, end+1))

    def peirod_range(beg, end):
        return list(range(beg, end+1))

    def days_except(*args):
        return [x for x in [Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday] if x not in args]

    def periods_except(*args):
        return [x for x in [Morning, Forenoon, Afternoon, Evening, LateNight] if x not in args]

    def is_day(t=None):
        if not t:
            t = store.t
        return t.period in (Morning, Forenoon, Afternoon)

    def is_night(t=None):
        if not t:
            t = store.t
        return t.period in (Evening, LateNight, TimeToSleep)

    def is_weekend(t=None):
        if not t:
            t = store.t
        return t.day in (Saturday, Sunday)

    def is_weekday(t=None):
        if not t:
            t = store.t
        return t.day in day_range(Monday, Friday)

    def format(value, prec=1, force=False):
        if force:
            return '{:.{prec}f}'.format(value, prec=prec)
        else:
            return str(int(value)) if value.is_integer() else '{:.{prec}f}'.format(value, prec=prec)

    def xbtn(screen=None, action=None, **kwargs):
        if screen:
            btn_action = Hide(screen)
        else:
            btn_action = action
        return ImageButton(idle_image="gui/x_idle.png", hover_image="gui/x_hover.png", activate_image="gui/x_selected_hover.png", xsize=50, ysize=30, xalign=1.0, yalign=.0, clicked=btn_action, **kwargs)

    def wipeup(t):
        return CropMove(t, "wipeup")

    def wipedown(t):
        return CropMove(t, "wipedown")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
