init python:
    class Compare(object):
        def __init__(self, owner_name, obj_name, operator, value):
            self.owner_name = owner_name
            self.obj_name = obj_name
            self.operator = operator
            self.value = value
        
        def __repr__(self):
            return "Compare(%s.%s%s%s)" % (self.owner_name, self.obj_name, self.operator, self.value)
        
        def __call__(self):
            owner = getattr(store, self.owner_name)
            obj = getattr(owner, self.obj_name)
            
            operator = self.operator
            if operator in ("=", "=="):
                return obj == self.value
            elif operator == ">":
                return obj > self.value
            elif operator == ">=":
                return obj >= self.value
            elif operator == "<":
                return obj < self.value
            elif operator == "<=":
                return obj <= self.value
            elif operator == "!=":
                return obj != self.value

    class ValueOperate(object):
        def __init__(self, owner_name, obj_name, operator, value):
            self.owner_name = owner_name
            self.obj_name = obj_name
            self.operator = operator
            self.value = value
        
        def __call__(self):
            owner = getattr(store, self.owner_name)
            obj = getattr(owner, self.obj_name)
            
            operator = self.operator
            if operator == "+":
                return add(owner, obj, self.value)
            elif operator == "-":
                return sub(owner, obj, self.value)
        
        def __repr__(self):
            return "ValueOperate(%s.%s%s%s)" % (self.owner_name, self.obj_name, self.operator, self.value)

    class GetBool(object):
        def __init__(self, var_name, has_not=False):
            self.var_name = var_name
            self.has_not = has_not
        
        def __call__(self):
            if self.has_not:
                return not getattr(store, self.var_name)
            else:
                return getattr(store, self.var_name)
        
        def __repr__(self):
            return "GetBool(%s%s)" % ("not " if self.has_not else "", self.var_name)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
