init -3 python:
    class Meter(object):
        def __init__(self, owner, **kwargs):
            self._value = .0 
            
            self.is_stage_locked = False
            self.is_plot_locked = False
            
            self.owner_name = owner
            self.__dict__.update(kwargs)
        
        @property
        def owner(self):
            return self.owner_name.split('_')[0]
        
        
        
        
        
        
        
        
        @property
        def base(self):
            return get(self.owner_name).base
        
        @property
        def out_of_content(self):
            try:
                
                return self._value >= get(self.owner_name).max_value
            except AttributeError:
                return False
        
        @property
        def stage(self) :
            quotient = int(self._value / self.base)
            remainder = self._value % self.base
            if remainder > 0:
                return int(quotient) + 1
            elif remainder == 0:
                if self.is_stage_locked:
                    return quotient
                else:
                    return quotient + 1
        
        def next_stage(self):
            next_stage = (self.stage-1) + 1
            self._value = next_stage * self.base
            self.is_stage_locked = False          
        
        def lock(self):
            self.is_plot_locked = True
        
        def unlock(self):
            self.is_plot_locked = False
        
        def add(self, value):
            if value > 0.0:
                current_love_limit = self.stage * self.base
                sum = self._value + value
                if sum >= current_love_limit:
                    floored_added_value = current_love_limit - self._value
                    self._value = current_love_limit
                    self.is_stage_locked = True
                    return floored_added_value
                else:
                    self._value = sum
                    return value
            elif value == 0.0:
                return 0.0
        
        def sub(self, value):
            if value > .0:
                previous_love_limit = (self.stage-1) * self.base
                difference = self._value - value
                if difference >= previous_love_limit:
                    self._value = difference
                    return value
                else:
                    floored_subed_value = previous_love_limit - difference
                    self._value = previous_love_limit
                    return floored_subed_value
            elif value == .0:
                return .0
        
        
        def __cmp__(self, comparer):
            if self._value < comparer:
                return -1
            elif self._value > comparer:
                return 1
            else:
                return 0
        
        def __repr__(self):
            return "Meter({})".format(self._value)

    class MeterWrapper():
        
        def __init__(self):
            pass
        
        def __str__(self):
            return self.name
        
        
        
        
        
        
        
        
        @property
        def pct(self): 
            return self.value / self.base
        
        @property
        def owner(self):
            return self.meter.owner
        
        @property
        def is_stage_locked(self):
            return self.meter.is_stage_locked
        
        @property
        def is_plot_locked(self):
            return self.meter.is_plot_locked
        
        @property
        def out_of_content(self):
            return self.meter.out_of_content
        
        @property
        def is_locked(self):
            return self.is_stage_locked or self.is_plot_locked or self.out_of_content
        
        
        
        
        
        @property
        def stage(self):
            return self.meter.stage
        @stage.setter
        def stage(self, value):
            if value > 0 and isinstance(value, int):
                self.meter._value += (value - self.meter.stage) * self.base
            else:
                raise ValueError("Stage must be positive integar.")
        
        def next_stage(self):
            return self.meter.next_stage()
        
        def lock(self):
            return self.meter.lock()
        
        def unlock(self):
            return self.meter.unlock()
        
        def add(self, value, chance=0):
            random.seed(t.total_period)
            if chance and random.random() > chance:
                return False
            if not self.out_of_content and not self.is_plot_locked and not self.is_stage_locked:
                return self.meter.add(value)              
            return False


    class Love(MeterWrapper):
        
        def __init__(self):
            super(MeterWrapper, self).__init__()
            self.name = _("Любовь")
            self.abbr = _("Любовь")
        
        def __cmp__(self, comparer):
            if self.value < comparer:
                return -1
            elif self.value > comparer:
                return 1
            else:
                return 0
        
        @property
        def type(self):
            return self.__class__.__name__
        
        def __repr__(self):
            return "{}({})".format(self.__class__.__name__, self.value)


    class TrueLove(Love):
        def __init__(self, meter, base=5.0, **kwargs):
            super(Love, self).__init__()
            self.meter_name = meter
            self.base = base
            self.__dict__.update(kwargs)
            self.name = _("Любовь")
            self.abbr = _("Любовь")
        
        @property
        def value(self):
            return self.meter._value
        @value.setter
        def value(self, value):
            self.meter._value = float(value)
        
        @property
        def meter(self):
            return get(self.meter_name)


    class FalseLove(Love):
        def __init__(self, meter, progress, base=6.0, **kwargs):
            super(Love, self).__init__()
            self.meter_name = meter
            self.progress = progress
            self.base = base
            self.__dict__.update(kwargs)
        
        @property
        def value(self):
            return (self.stage - 1.0) * 5
        @value.setter
        def value(self, value):
            if value % 5 == 0:
                self.stage = (int(value/5) + 1)
        
        @property
        def meter(self):
            return get(self.meter_name)


    class Lust(MeterWrapper):
        def __init__(self, meter, base=20.0, **kwargs):
            super(MeterWrapper, self).__init__()
            self.meter_name = meter
            self.base = base
            self.__dict__.update(kwargs)  
        
        @property
        def value(self):
            return self.meter._value
        @value.setter
        def value(self, value):
            self.meter._value = float(value)
        
        @property
        def name(self):
            return _("Похоть")
        
        @property
        def meter(self):
            return get(self.meter_name)
        
        def __cmp__(self, comparer):
            if self.value < comparer:
                return -1
            elif self.value > comparer:
                return 1
            else:
                return 0

    class Harem(MeterWrapper):
        def __init__(self, meter, base=100.0, max_value=10.0, **kwargs):
            super(MeterWrapper, self).__init__()
            self.meter_name = meter
            self.base = base
            self.name = _("Принятие Гарема")
            self.abbr = _("П.Г.")
            self.max_value = max_value
            self.__dict__.update(kwargs)  
        
        @property
        def value(self):
            return self.meter._value
        @value.setter
        def value(self, value):
            self.meter._value = float(value)
        
        @property
        def meter(self):
            return get(self.meter_name)
        
        def __cmp__(self, comparer):
            if self.value < comparer:
                return -1
            elif self.value > comparer:
                return 1
            else:
                return 0

    class Progress(MeterWrapper):
        def __init__(self, key, name, meter, base=6.0, nz=None, **kwargs):
            self.key = key
            self.name = name
            self.meter_name = meter
            self.base = base
            self.nz = nz
            self.__dict__.update(kwargs)
        
        @property
        def meter(self):
            return get(self.meter_name)
        
        @property
        def value(self):
            quotient = self.meter._value / self.base
            remainder = self.meter._value % self.base
            if remainder > .0:
                return remainder
            elif remainder == .0:
                if self.is_stage_locked:
                    return self.base
                else:
                    return .0
        
        @property
        def is_full(self):
            return self.value == self.base
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
