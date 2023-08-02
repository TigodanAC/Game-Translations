init -2:
    define NZ_PLAYLETS = {}
    define PLAYLETS = {}
    default cPlaylets = None

init -1 python:

    def get_playlet(label):
        try:
            return store.PLAYLETS[label]
        except:
            print("Playlet %s not found" % cPlaylet)

    def get_cPlaylets():
        results = []
        used_actions = []
        
        nz_display_codes = ["X"] + [nz.code for nz in nz_display_list]
        
        for nz in nz_display_codes:
            
            if renpy.random.random() < 0.5:
                continue
            
            try:
                actions_playlets = NZ_PLAYLETS[nz][t.period]
            except KeyError:
                continue
            
            actions = actions_playlets.keys()
            clickable_actions = [action for action in actions \
                if action not in used_actions and Action.get(action).is_clickable]
            
            if not clickable_actions:
                continue
            
            action = renpy.random.choice(clickable_actions)
            
            
            playlets = actions_playlets[action]
            triggerable_playlets = []
            for playlet in playlets:
                playlet = get_playlet(playlet)
                if playlet.triggerable:
                    triggerable_playlets.append(playlet)
            
            if not triggerable_playlets:
                continue
            
            playlet = renpy.random.choice(triggerable_playlets)
            
            results.append(playlet)
            used_actions.append(action)
        
        return results


    class Playlet(object):
        
        def __init__(self, label, nz, action, period, in_event=[], out_event=[], results=[], condition=None):
            self.label = label
            self.nz = nz
            self.is_harem = True if nz == "X" else False
            
            action = action[0]
            self.action = action
            self.parent = Action.get(Action.get(action).parent).label
            
            period = period[0]
            self.period = period
            
            self.in_event = in_event
            self.out_event = out_event
            self.results = results
            self.condition = condition
            
            PLAYLETS[label] = self
            
            if nz not in NZ_PLAYLETS:
                NZ_PLAYLETS[nz] = {}
            if period not in NZ_PLAYLETS[nz]:
                NZ_PLAYLETS[nz][period] = {}
            if action not in NZ_PLAYLETS[nz][period]:
                NZ_PLAYLETS[nz][period][action] = []
            NZ_PLAYLETS[nz][period][action].append(label)
        
        
        def run(self):
            renpy.call("run_playlet", playlet=self)
        
        def __str__(self):
            return "Playlet({})".format(self.cg)
        
        def run_results(self):
            for result in self.results:
                result()
        
        @property
        def triggerable(self):
            if self.condition and not eval(self.condition):
                return False
            
            for ev in self.out_event:
                if seen(ev):
                    return False
            
            for ev in self.in_event:
                if not seen(ev):
                    return False     
            return True
        
        def __repr__(self):
            return "Playlet({})".format(self.label)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
