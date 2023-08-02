init -3 python:
    NZS = []

    class Nz(object):
        
        def __init__(self, code, name, age, **kwargs):            
            self.code = code
            self.name = name
            self.age = age
            
            self.__dict__.update(kwargs)
            
            self._hint = kwargs["hint"]
            
            self._state = None
            
            NZS.append(self)
        
        @property
        def hint(self):
            return self._hint()
        
        def __repr__(self):
            return ("{}, {}, {}").format(self.code, self.name, id(self))
        
        def __str__(self):
            return self.name
        
        @property
        def state(self):
            return get(self.code + "_state")
        
        @property
        def love(self):
            return get(self.code + "_love")
        
        @property
        def lust(self):  
            return get(self.code + "_lust")
        
        @property
        def harem(self):  
            return get(self.code + "_harem")
        
        @property
        def relation(self):
            return self.state.relation
        @relation.setter
        def relation(self, value):
            self.state.relation = value
        
        @property
        def clothes(self):
            return self.state.clothes
        @clothes.setter
        def clothes(self, value):
            self.state.clothes = value
        
        def __eq__(self, other):
            try:
                return self.code == other.code
            except AttributeError:
                return self.code == other

    class NzState(object):
        
        def __init__(self):
            self.relation = "general"
            self.clothes = 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
