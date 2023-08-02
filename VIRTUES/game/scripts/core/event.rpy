default cEvent = None
default EventHistory = []

init -3:
    define EVENTS = {}
    define AUTO_EVENTS = []
    default events_states = {}

init -1 python:

    class Event(object):
        
        def __init__(self, name=None, no_label=False, func=None, type=None, condition=None, time=None, day=None, period=None, action=None, love=None, duration=1, repeatable=False, proceed_to=None, pre_event=[], desc="", runnable=True, triggerable=True, training_type=None, ifs=[], results=[], auto=None):
            
            self.name = name
            self.label = 0
            self.func = func
            if runnable and not func and not no_label:
                self.label = name
            self._triggerable = triggerable
            
            self.type = type
            self.desc = desc
            self.repeatable = repeatable
            self.runnable = runnable
            
            self.duration = duration
            self.proceed_to = proceed_to
            
            
            self.condition = condition
            self.pre_event = pre_event
            
            self.day = day
            self.period = period
            
            
            self.action = action
            
            self.action_name = None
            
            self.is_auto_event = False
            if action:
                self.auto = False
                self.action_name = []
                for aclabel in action:
                    ac = Action.get(aclabel)
                    if ac:
                        ac.events.append(name)
                        self.action_name.append(ac.name)
                    else:
                        print("non-exist action: %s in Event(%s)" % (action, name))
            elif auto in (None, True):
                self.auto = True
                self.is_auto_event = True
                AUTO_EVENTS.append(name)
            else:
                self.auto = False
            
            EVENTS[name] = self
            
            self.nz = None
            match_nz = pattern.nz_related.match(name)
            if match_nz:
                self.type = "NzRelated"
                self.nz = get(match_nz.group(1))
                self.love = love
                
                match_love = pattern.love.match(name) 
                if match_love:
                    
                    
                    self.stage = int(match_love.group(2))
                    
                    if self.nz.love.type == "TrueLove":
                        self.type = "TrueLove"
                    else: 
                        self.type = "FalseLove"
                
                match_daily = pattern.daily.match(name)
                if match_daily:
                    self.nz = get(match_daily.group(1))
                    self.type = "daily"
            
            self._time = time
            match_intro = pattern.intro.match(name)
            if match_intro:
                tg_tp = (int(match_intro.group(1))-1)*6 + int(match_intro.group(2))
                self._time = Time(tg_tp)
                self.duration = 0
                self.type = "Intro"
            
            self.training_type = training_type
            if training_type:
                self.type = "Training"
                TRAINING_EVENTS[self.nz.code][training_type].append(self)
            
            self.ifs = ifs
            self.results = results
        
        def __repr__(self):
            return "Event({})".format(self.name)
        
        def run(self):
            store.cEvent = self.name
            renpy.jump("run_event")
        
        
        def get_triggerable(self):
            if not self._triggerable:
                return False
            if getCEvent() and getCEvent().name == self.name:
                return False
            if not self.repeatable and self.seen:
                return False
            
            if self.count_of_day > 0 and self.count_day == Date(t):
                return False
            else:
                self.count_day = Date(t)
                self.count_of_day = 0
            
            if self.pre_event and any(not seen(ev) for ev in self.pre_event):
                return False
            
            if self._time and t < self._time:
                return False
            
            if self.period and (t.period not in self.period):
                return False
            
            if self.day and (t.day not in self.day):
                return False
            
            if self.type == "TrueLove" and not (self.nz.love >= self.stage * self.nz.love.base):
                return False
            elif self.type == "FalseLove" and not (self.nz.love.progress.is_full and self.nz.love.stage == self.stage):
                return False
            elif self.nz and self.nz.love < self.love:
                return False
            
            for ifer in self.ifs:
                if ifer() == False:
                    return False
            
            try:
                if self.condition and not eval(self.condition):
                    return False
            except Exception as e:
                msg = "Error Message:{}".format(traceback.format_exc())
                return False
            
            return True
        
        def get_triggerable_detail(self):
            results = []
            pre_event_OK = False
            if not self._triggerable:
                results.append("always untriggerable")
            if getCEvent() and getCEvent().name == self.name:
                results.append("current event")
            if not self.repeatable and self.seen:
                results.append("seen")
            if self.count_of_day > 0 and self.count_day == Date(t):
                results.append("has run today")
            
            if self.pre_event:
                unseens = [ev for ev in self.pre_event if not seen(ev)]
                if unseens:
                    results.append("{} was not seen".format(", ".join(unseens)))
                else:
                    pre_event_OK = True
            
            if self._time and t < self._time:
                results.append("t < {}".format(self._time))
            
            if self.period and (t.period not in self.period):
                results.append("period not in {}".format(self.period))
            
            if self.day and (t.day not in self.day):
                results.append("day not in {}".format(self.day))
            
            if self.type == "TrueLove" and not (self.nz.love >= self.stage * self.nz.love.base):
                results.append("{}.love < {}".format(self.nz, self.stage * self.nz.love.base)) 
            elif self.type == "FalseLove" and not (self.nz.love.progress.is_full and self.nz.love.stage == self.stage):
                results.append("not (self.nz.love.progress.is_full and self.nz.love.stage == self.stage)") 
            elif self.nz and self.nz.love < self.love:
                results.append("{}.love < {}".format(self.nz, self.love))
            
            if self.ifs:
                false_ifs = [ifer for ifer in self.ifs if ifer() == False]
                if false_ifs:
                    results.append('{} == False'.format(false_ifs))
            
            if pre_event_OK:
                try:
                    if self.condition and not eval(self.condition):
                        results.append('{} == False'.format(self.condition)) 
                except Exception as e:
                    msg = "Error Message:{}".format(traceback.format_exc())
                    results.append(msg)
            else:
                try:
                    if self.condition and not eval(self.condition):
                        results.append('{} == False'.format(self.condition)) 
                except Exception as e:
                    results.append(str(e))
            
            if not results:
                return ["is triggerable"]
            else:
                return results
        
        def run_results(self):
            for result in self.results:
                result()
        
        @property
        def triggerable(self):
            return self.get_triggerable()
        
        def __str__(self):
            return "{}".format(self.label)
        
        @property
        def state(self):
            if self.name not in events_states:
                events_states[self.name] = EventState(self.name)
            return events_states[self.name]
        
        
        @property
        def time(self):
            if self._time:
                return self._time
            else:
                return self.end_time
        
        @property
        def date(self):
            return self.end_date
        
        
        @property
        def seeing(self):
            return self.state.seeing
        @seeing.setter
        def seeing(self, value):
            self.state.seeing = value
        
        @property
        def seen(self):
            return self.state.seen
        @seen.setter
        def seen(self, value):
            self.state.seen = value
        
        @property
        def count(self):
            return self.state.count
        @count.setter
        def count(self, value):
            self.state.count = value
        
        @property
        def start_time(self):
            return self.state.start_time
        @start_time.setter
        def start_time(self, value):
            self.state.start_time = value
        
        @property
        def start_date(self):
            return self.state.start_date
        
        @property
        def end_time(self):
            return self.state.end_time
        @end_time.setter
        def end_time(self, value):
            self.state.end_time = value
        
        @property
        def end_date(self):
            return self.state.end_date
        
        @property
        def count_day(self):
            return self.state.count_day
        @count_day.setter
        def count_day(self, value):
            self.state.count_day = value
        
        @property
        def count_of_day(self):
            return self.state.count_of_day
        @count_of_day.setter
        def count_of_day(self, value):
            self.state.count_of_day = value
        
        
        def __eq__(self, other):
            return self.name == other.name

    class EventState():
        
        def __init__(self, label):
            self.label = label
            self.seeing = False
            self.seen = False
            self.start_time = None
            self.end_time = None
            self.count = 0
            self.count_of_day = 0
            self.count_day = None
            events_states[label] = self
        
        @property
        def start_date(self):
            if self.start_time:
                return Date(time=self.start_time)
        
        @property
        def end_date(self):
            if self.end_time:
                return Date(time=self.end_time)

    def get_event(name):
        try:
            return EVENTS[name]
        except:
            
            print("event %s not found" % name)

    def getCEvent():
        if cEvent:
            try:
                return EVENTS[store.cEvent]
            except:
                print("cEvent %s not found" % cEvent)
        
        else:
            return None

    def clearCEvent():
        store.cEvent = None

    def seen(*names):
        try:
            
            for name in names:
                if not get_event(name).seen:
                    return False
            return True
        except AttributeError:
            return False

    def seen_event(*events):
        if any(not event.seen for event in events):
            return False
        return True

    def fake_run(*names):
        for name in names:
            event = EVENTS.get(name)
            event.state.seen = True
            event.state.start_time = t.copy()
            event.state.end_time = t.copy()
            event.state.count += 1
        _on_event_complete()

    def fake_run_alternate(event):
        event.state.seen = True
        event.state.start_time = t.copy()
        event.state.end_time = t.copy()
        event.state.count += 1
        _on_event_complete()

    def unrun(event):
        event.state.seen = False
        event.state.start_time = None
        event.state.end_time = None
        event.state.count -= 1 
        _on_event_complete()

    def get_events(names):
        return [get_event(name) for name in names]

    def latest_date(events):
        return max(events, key=lambda event: event.date).date

    def is_after_completion(events, day=1, week=0):
        events = get_events(events)
        lastest = latest_date(events)
        if lastest:
            return Date(t) >= lastest + Day(day) + Week(week)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
