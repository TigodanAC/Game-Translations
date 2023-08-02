define INTERACTIONS = {}
define NZ_INTERACTIONS = defaultdict(list)
default interaction_states = {}
init python:

    class Interaction(object):
        
        def __init__(self, nz, label, name, pre_event, type, condition=None):
            self.nz_code = nz
            self.label = label
            self.name = name
            self.type = type
            if isinstance(pre_event, basestring):
                self.pre_event = [pre_event]
            else:
                self.pre_event = pre_event
            self.condition = condition
            INTERACTIONS[label] = self
            NZ_INTERACTIONS[nz].append(self)
        
        def __repr__(self):
            return "Interaction({})".format(self.label)
        
        @property
        def nz(self):
            return get(self.nz_code)
        
        @property
        def displaying(self):
            for event in self.pre_event:
                if not seen(event):
                    return False
            if self.condition and not eval(self.condition):
                return False
            return True
        
        @property
        def state(self):
            if self.label not in interaction_states:
                interaction_states[self.label] = InteractionState(self.label)
            return interaction_states[self.label]
        
        def run(self):
            store.cInteraction = self
            renpy.jump("run_interaction")
        
        @property
        def count_of_day(self):
            try:
                return self.state.count_of_day
            except AttributeError:
                self.state.count_of_day = [Date(t), 0]
                return self.state.count_of_day
        @count_of_day.setter
        def count_of_day(self, value):
            self.state.count_of_day = value
        
        @property
        def count(self):
            return self.state.count
        @count.setter
        def count(self, value):
            self.state.count = value
        
        @property
        def triggerable(self):
            if not self.displaying:
                return False
            
            time, count = self.count_of_day
            try:
                if time == Date(t):
                    if count > 0:
                        return False
                elif time != store.t:
                    self.count_of_day = [Date(t), 0]
            except AttributeError:
                self.count_of_day = [Date(t), 0]
            return True
        
        def __repr__(self):
            return "Interaction({})".format(self.label)

    class InteractionState(object):
        def __init__(self, label):
            self.count_of_day = [0, None]
            self.count = 0
            interaction_states[label] = self
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
