init -2:




    define OneCGs = [[[] for j in range(6)] for i in range(7)]
    default cOneCG = None

init -1 python:

    def get_OneCG():
        if random.random() < 0.4:
            rooms = OneCGs[t.day-1][t.period-1]
            triggerable_rooms = [room for room in rooms if room.triggerable]
            if triggerable_rooms:
                return random.choice(triggerable_rooms)

    class OneCG(object):
        
        def __init__(self, cg, day=[1,2,3,4,5,6,7], period=[], nz=None, post=None, pre_event=[], love=0, action=None, screen=None, text=[]):
            self.label = "OneCG"
            self.cg = cg
            self.love = 0
            self.action = action[0]
            self.screen = screen
            self.post = Show(screen)
            
            self.day = day
            self.period = period
            self.nz = nz
            self.post = post
            self.pre_event = pre_event
            
            self.text = text
            
            for d in day:
                for p in period:
                    OneCGs[d-1][p-1].append(self)
        
        def run(self):
            renpy.call("run_OneCG", cg=self)
        
        def __str__(self):
            return "OneCG({})".format(self.cg)
        
        @property
        def triggerable(self):
            for ev in self.pre_event:
                if not seen(ev):
                    return False
            
            return True
        
        def __repr__(self):
            return "OneCG({})".format(self.cg)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
