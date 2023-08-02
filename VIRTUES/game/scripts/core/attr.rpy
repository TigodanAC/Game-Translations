init -4 python:
    class Attr(object):
        
        @classmethod
        def sum(cls, cs):
            result = Attr()
            _sum = 0
            for c in cs:
                _sum += c.value
            try:
                result.__dict__.update(cs[0].__dict__)
            except IndexError:
                result.__dict__.update(cs.__dict__)
            result.value = _sum
            return result
        
        def __init__(self, value=0.0, owner=None, name=None, **kwargs):
            self.value = value
            self.owner = owner
            self.name = name
            self.__dict__.update(kwargs)
        
        def __int__(self):
            return int(self.value)
        
        def __float__(self):
            return float(self.value)
        
        def add(self, value):
            self.value += value
        
        def sub(self, value):
            self.value -= value
        
        def __add__(self, other):
            try:
                return Attr(self.value + other.value, self.owner, self.name)
            except AttributeError:
                return Attr(self.value + other, self.owner, self.name)
        
        def __radd__(self, other):
            try:
                return Attr(self.value + other.value, self.owner, self.name)
            except AttributeError:
                return Attr(self.value + other, self.owner, self.name)
        
        def __sub__(self, other):
            try:
                return Attr(self.value - other.value, self.owner, self.name)
            except AttributeError:
                return Attr(self.value - other, self.owner, self.name)
        
        def __mul__(self, other):
            try:
                return Attr(self.value * other.value, self.owner, self.name)
            except AttributeError:
                return Attr(self.value * other, self.owner, self.name)
        
        def __div__(self, other):
            try:
                return Attr(self.value / other.value, self.owner, self.name)
            except AttributeError:
                return Attr(self.value / other, self.owner, self.name)
        
        def __cmp__(self, comparer):
            if self.value < comparer:
                return -1
            elif self.value > comparer:
                return 1
            else:
                return 0
        
        def set(self, value):
            self.value = value
        
        def __str__(self):
            return str(self.value)
        
        def __repr__(self):
            return "Attr({}, {})".format(type(self), self.name, self.value)
        
        @property
        def svalue(self):
            return self.sval()
        
        def sval(self):
            return str(self.value)

    class TimeUnit(object):
        Period = 1.0
        Day = 7.0
        Week = 42.0
        
        def __str__(self):
            return self.name

    TU = TimeUnit


    class CashFlow(Attr):
        def __init__(self, value, time, owner=None, name=None, **kwargs):
            super(CashFlow, self).__init__(value=value, owner=owner, name=name, **kwargs)
            
            
            self.time = time.copy()
            
            self.__dict__.update(kwargs)
        
        @property
        def str(self):
            if self.value > 0:
                return "+" + str(self.value)
            return str(self.value)
        
        @classmethod
        def sum(cls, cs, time_unit=None, current_time=None):
            if time_unit and current_time is None:
                total_value = .0
                if time_unit is TU.Day:
                    current_tu = current_time.day
                if time_unit is TU.Week:
                    current_tu = current_time.week
                
                reached_current_tu = False
                for c in cs:
                    if time_unit is TU.Day:
                        c_tu = c.time.day
                    if time_unit is TU.Week:
                        c_tu = c.time.week
                    
                    if c_tu is current_tu:
                        total_value += c.value
                        reached_current_tu = True
                    elif reached_current_tu: 
                        
                        break
                
                return CashFlowOverTime(total_value, time_unit)














    class Revenue(CashFlow):
        def __init__(self, value, thing, time, **kwargs):
            super(Revenue, self).__init__(value=value, time=time, **kwargs)
            self.thing = thing
            self.type = _("In")

    class Expanse(CashFlow):
        def __init__(self, value, thing, time, **kwargs):
            super(Expanse, self).__init__(value=value, time=time, **kwargs)
            self.thing = thing
            self.type = _("Out")

    class CashFlowOverTime(Attr):
        
        def __init__(self, value, time_unit, name=None, **kwargs):
            super(self.__class__, self).__init__(value=value, owner=owner, name=name, **kwargs)
            self.time_unit = time_unit
            self.suffix = "/TP" if time_unit is TU.Period else "/D" if time_unit is TU.Day else "/Wk"
            self.__dict__.update(kwargs)

    class Cash(object):
        
        def __init__(self, owner, value):
            self.name = _("Savings")
            self.owner = owner
            self._value = value
        
        def add(self, value):
            if value > 0:
                self._value += value
                return 1
            elif value is 0:
                return 0 
            else:
                raise ValueError ("wrong payment error")
        
        def pay(self, value):
            if self._value >= value > 0:
                self._value -= value
                return 1
            elif self._value < value:
                return 0
            else:
                raise ValueError ("wrong payment error")
        
        def buy(self, value, thing=""):
            if self._value >= value > 0:
                self._value -= value
                return 1
            elif self._value < value:
                return 0
            else:
                raise ValueError ("wrong payment error")
        
        def zero(self, thing=""):
            old_val = self._value
            self._value = 0
            return old_val
        
        @property
        def value(self):
            return self._value
        @value.setter
        def value(self, value):
            self._value = value
        
        def __cmp__ (self, other):
            if isinstance(other, float) or isinstance(other, int):
                if self._value < other:
                    return -1
                if self._value == other:
                    return 0
                if self._value > other:
                    return 1
            elif isinstance(other, Cash):
                if self._value < other._value:
                    return -1
                if self._value == other._value:
                    return 0
                if self._value > other._value:
                    return 1
        
        def __str__(self):
            
            return "{0:,.0f}".format(self.value)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
