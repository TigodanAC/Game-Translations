init -2 python:
    Morning = DayPeriod.Morning
    Forenoon = DayPeriod.Forenoon
    Afternoon = DayPeriod.Afternoon
    Evening = DayPeriod.Evening
    LateNight = DayPeriod.LateNight
    TimeToSleep = DayPeriod.TimeToSleep

    Monday = WeekDay.Monday
    Tuesday = WeekDay.Tuesday
    Wednesday = WeekDay.Wednesday
    Thursday = WeekDay.Thursday
    Friday = WeekDay.Friday
    Saturday = WeekDay.Saturday
    Sunday = WeekDay.Sunday

init -3 python:
    DAY_PERIOD_NAME = [
        None,
        _("Morning"),
        _("Forenoon"),
        _("Afternoon"),
        _("Evening"),
        _("LateNight"),
        _("LateNight")
    ]

    DAY_PERIOD_STR = [
        None,
        _("Morning"),
        _("Forenoon"),
        _("Afternoon"),
        _("Evening"),
        _("Late Night"),
        _("Late Night")
    ]

    WEEK_DAY_NAME = [
        None,
        _("Monday"),
        _("Tuesday"),
        _("Wednesday"),
        _("Thursday"),
        _("Friday"),
        _("Saturday"),
        _("Sunday"),
    ]

    WEEK_DAY_STR = [
        None,
        _("Monday"),
        _("Tuesday"),
        _("Wednesday"),
        _("Thursday"),
        _("Friday"),
        _("Saturday"),
        _("Sunday"),
    ]

    total_period_of_day = 6.0

    class DayPeriod(IntEnum):
        Morning = 1
        Forenoon = 2
        Afternoon = 3
        Evening = 4
        LateNight = 5
        TimeToSleep = 6
        
        def __str__(self):
            return DAY_PERIOD_STR[self.value]
        
        def __repr__(self):
            return DAY_PERIOD_NAME[self.value]

    class WeekDay(IntEnum):
        Monday = 1
        Tuesday = 2
        Wednesday = 3
        Thursday = 4
        Friday = 5
        Saturday = 6
        Sunday = 7
        
        def __str__(self):
            return WEEK_DAY_STR[self.value]
        
        def __repr__(self):
            return WEEK_DAY_NAME[self.value]

    class Week(object):
        def __init__(self, number):
            self.number = number
        @property
        def total_period(self): 
            return self.number * 7 * total_period_of_day
        @property
        def total_day(self): 
            return self.number * 7
        
        def __neg__(self):
            return Week(-self.number)
        
        def __pos__(self):
            return self
        
        def __repr__(self):
            return 'Week({})'.format(self.number)


    class Day(object):
        def __init__(self, number):
            self.number = number
        @property
        def total_period(self): 
            return self.number * total_period_of_day
        @property
        def total_day(self): 
            return self.number
        
        def __neg__(self):
            return Day(-self.number)
        
        def __pos__(self):
            return self
        
        
        
        
        
        
        
        
        
        def __repr__(self):
            return 'Day({})'.format(self.number)

    class Time(object):
        
        def __init__(self, total_period=None, week=None, day=None, period=None, time=None, date=None, offset=None, dynamic=False):
            self.dyn_week = week
            self.dyn_day = day
            self.dyn_period = period
            self.dyn_date = date
            self.dyn_time = time
            self.dyn_total_period = total_period
            self.offset = offset
            self.dynamic = dynamic
            
            if None not in (week, day, period):
                self.type = "full_para"
            elif week is None and day is not None is not period:
                self.type = "current_week"
                self.dynamic = True
            elif week is None is day and period is not None:
                self.type = "current_day"
                self.dynamic = True
            elif time is not None:
                self.type = "time"
            elif date is not None:
                self.type = "date"
            elif total_period is not None:
                self.type = "true"
            elif week is None and day is None and period is None:
                self.type = "current_time"
                self.dynamic = True
            else:
                raise ValueError("wrong parameter of Time init")
            
            if not self.dynamic:
                self._total_period = self.get_total_period()
                self.type = "static"
        
        def get_total_period(self):
            if self.type == "full_para":
                r = Time.to_total_period(self.dyn_week, self.dyn_day, self.dyn_period)
            elif self.type == "current_time":
                r = store.t.total_period
            elif self.type == "current_week":
                r = Time.to_total_period(store.t.week, self.dyn_day, self.dyn_period)
            elif self.type == "current_day":
                r = Time.to_total_period(store.t.week, store.t.day, self.dyn_period)
            elif self.type == "time":
                r = self.dyn_time.total_period
            elif self.type == "date":
                r = self.dyn_date.total_period 
            elif self.type == "true":
                r = self.dyn_total_period
            
            if self.offset:
                if isinstance(self.offset, int):
                    r += self.offset
                else:
                    r += self.offset.total_period
            
            return r
        
        @property
        def total_period(self):
            if self.dynamic:
                self._total_period = self.get_total_period()
            return self._total_period
        
        @total_period.setter
        def total_period(self, value):
            self._total_period = value
        
        
        def copy(self):
            return Time(total_period=self.total_period)
        
        @staticmethod
        def to_total_period(week, day, period):
            return ( (week-1)*7 + (day-1) )*total_period_of_day + period
        
        @staticmethod
        def to_total_day(week, day):
            return (week-1)*7 + day
        
        def __repr__(self):
            return ("Time{}(dyn_tp={}, dyn_week={}, dyn_day={}, dyn_period={}, day_date={}, dyn_time={}, offset={})".format(('Dynamic' if self.dynamic else ''), self.dyn_total_period, self.dyn_week, self.dyn_period, self.dyn_period, self.dyn_date, self.dyn_time, self.offset))
        
        def __str__(self):
            return _("Week{} {} {}").format(self.week, str(self.day), str(self.period))
        
        @property
        def short(self):
            return _("Week{} {} {}").format(self.week, str(self.day)[:3], str(self.period)[:3])
        
        @property
        def week(self):
            return int(math.ceil( (self.total_period / (7*total_period_of_day)) ))
        @property
        def day(self):
            week_day_reminder = int(math.ceil( (self.total_period / total_period_of_day) % 7 ))
            if week_day_reminder is 0:
                return WeekDay(7)
            else:
                return WeekDay(week_day_reminder)
        @property
        def period(self):
            day_period_reminder = int(self.total_period % total_period_of_day)
            if day_period_reminder is 0:
                return DayPeriod(total_period_of_day)
            else:
                return DayPeriod(day_period_reminder)
        
        @property
        def total_day(self):
            return int(math.ceil(self.total_period / total_period_of_day))
        
        @property
        def new_day_period(self):
            return Time.to_total_period(t.week, t.day+1, DayPeriod.Morning)
        
        def __add__(self, value):
            if isinstance(value, int):
                value = value
            elif isinstance(value, Day):
                value = value.total_period 
            elif isinstance(value, Week):
                value = value.total_period 
            else:
                raise TypeError("unknown __add__ type of time")
            return Time(total_period=self.total_period + value)
        
        
        def proceed(self, value=1):
            if isinstance(value, int):
                if value == 0:
                    return
                if self.period + value <= total_period_of_day:
                    self.total_period += value
                    return "period_pass"
                elif self.period + value >= total_period_of_day:
                    
                    Push("DON'T mess with time.")
                else:
                    raise ValueError("wrong period value added")
            else:
                raise TypeError("wrong type added")
        
        def hard_proceed(self, value=1):
            self._total_period += value
        
        def new_day(self):    
            self.total_period = self.new_day_period
        
        def proceed_to(self, arg):
            if isinstance(arg, DayPeriod):
                period = arg
                if period > self.period:
                    self.total_period += period - self.period
                else:
                    
                    raise ValueError("wrong proceed_to value")
            elif isinstance(arg, Time):
                new_time = arg
                if new_time.total_period > self.total_period:
                    self.total_period = new_time.total_period
        
        
        
        def __eq__(self, other):
            return self.total_period == other.total_period
        def __ne__(self, other):
            return self.total_period != other.total_period
        def __lt__(self, other):
            return self.total_period < other.total_period
        def __le__(self, other):
            return self.total_period <= other.total_period
        def __gt__(self, other):
            return self.total_period > other.total_period
        def __ge__(self, other):
            return self.total_period >= other.total_period


    class Date(object):
        def __init__(self, time=None, week=None, day=None, total_day=None):
            if week is not None is not day:
                self.total_day = Time.to_total_day(week, day)
            elif time is not None:
                self.total_day = time.total_day
            elif total_day is not None:
                self.total_day = total_day
            else:
                raise TypeError("wrong parameter of Date init")
        
        @property
        def week(self):
            return int(math.ceil((self.total_day/7.0)))
        @property
        def day(self):
            week_day_reminder = int(math.ceil(self.total_day%7))
            if week_day_reminder is 0:
                return WeekDay(7)
            else:
                return WeekDay(week_day_reminder)
        
        def __add__(self, value):
            if isinstance(value, Day):
                return Date(total_day=(self.total_day + value.total_day))
            elif isinstance(value, Week):
                return Date(total_day=(self.total_day + value.total_day))
            else:
                raise ValueError("unknown __add__ type of date")
        
        @property
        def total_period(self):
            return (self.total_day-1) * total_period_of_day + (total_period_of_day-1)
        
        def __eq__(self, other):
            return self.total_day == other.total_day
        def __ne__(self, other):
            return self.total_day != other.total_day
        def __lt__(self, other):
            return self.total_day < other.total_day
        def __le__(self, other):
            return self.total_day <= other.total_day
        def __gt__(self, other):
            return self.total_day > other.total_day
        def __ge__(self, other):
            return self.total_day >= other.total_day
        
        def __repr__(self):
            return _("Time(total_day={}; Wk{}, {}) at {}").format(self.total_day, self.week, str(self.day), id(self))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
