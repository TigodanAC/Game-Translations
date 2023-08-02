init python:
    def get_findee_subplots():
        x = {}
        x = SUBPLOTS.get(findee.code, x)
        x = {name:dname for name,dname in x.items() if seen(name)}
        return x

    def get_all_subplots():
        x = {}
        for spdict in SUBPLOTS.values():
            seen_spdict = {name:dname for name,dname in spdict.items() if seen(name)}
            x.update(seen_spdict)
        return x
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
