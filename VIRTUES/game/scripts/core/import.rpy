define load_data_enabled = True

init 1 python:
    import os
    import subprocess
    import codecs
    import json

    encoding = "utf-8"

    def flatten(x):
        if isinstance(x, list):
            return [a for i in x for a in flatten(i)]
        else:
            return [x]

    def get_last_cgs():
        last_cgs = {}
        for file in renpy.list_files():
            file = os.path.basename(file).split(".")[0]
            m = re.search("(.*?)(\d+)$", file)
            if m:
                pattern = m.group(1) + "{}"
                index = int(m.group(2))
                old_index = last_cgs.get(pattern)
                if old_index:
                    if index > old_index:
                        last_cgs[pattern] = index
                else:
                    last_cgs[pattern] = index
            else:
                continue
        
        return last_cgs

    def handle_gallery_item(arg_dict, last_cgs):
        
        thumbnail = arg_dict["thumbnail"]
        
        pattern = re.search("(.*?)(\d+)$", thumbnail).group(1) + "{}"
        
        
        
        altertive_pattern = arg_dict.pop('alt_pattern', None)
        
        range_exps = arg_dict.pop('range', None)
        full_range = not bool(range_exps)
        
        images = []
        arg_dict["images"] = images
        
        if full_range:
            rang = trange(last_cgs[pattern])
            for i in rang:
                images.append(pattern.format(i))
        
        else:
            for range_exp in range_exps:
                
                alternative = False
                
                if range_exp.startswith("@"):
                    alternative = True
                    range_exp = range_exp[1:]
                
                nums = range_exp.split("~")
                
                
                nums = [int(i) for i in nums]        
                rang = trange(*nums)
                
                for i in rang:
                    if alternative:
                        images.append(altertive_pattern.format(i))
                    
                    
                    
                    else:
                        images.append(pattern.format(i))





    def parse_proceed_to(args):
        day = None
        period = None
        offset = None
        
        for arg in args:
            
            if arg.startswith(('+', '-')):
                offset = eval(arg)
            else:
                var = get_enum_value(arg)
                var_type = type(var)
                
                
                if var_type is DayPeriod:
                    period = var
                elif var_type is WeekDay:
                    day = var 
                else:
                    print('unkown proceed_to(%s) data type(%s)' % arg, var_type)               
        
        dynamic_time = Time(day=day, period=period, offset=offset)
        
        try:
            return dynamic_time
        except ValueError:
            print("Error: day(%s) period(%s) offset(%s)"%(day,period,offset))

    def parse_ifs(ifs):
        compare_re = re.compile("(\w+)\.?(\w*)(=|>|<|>=|<|<=|!=)(\d+)")
        checkbool_re = re.compile('(not )?(\w+)')
        
        results = []
        
        for statement in ifs:
            compare_match = compare_re.search(statement)
            checkbool_match = checkbool_re.search(statement)
            
            if compare_match:
                parent_name = compare_match.group(1)
                attr_name = compare_match.group(2)   
                operator = compare_match.group(3) 
                value = int(compare_match.group(4))
                results.append(Compare(parent_name, attr_name, operator, value))
            
            elif checkbool_match:
                has_not = bool(checkbool_match.group(1))
                var_name = checkbool_match.group(2)
                results.append(GetBool(var_name, has_not))
            
            else:
                print("known if statement: %s" % statement)
        
        return results

    def parse_results(statements):
        add_re = re.compile("(\w+)\.?(\w*)(\+|-)(\d+)")
        
        results = []
        
        for statement in statements:
            add_match = add_re.search(statement)
            
            if statement.startswith('$'):
                results.append(getattr(store, statement[1:]))
            elif add_match:
                parent_name = add_match.group(1)
                attr_name = add_match.group(2)   
                operator = add_match.group(3) 
                value = int(add_match.group(4))
                results.append(ValueOperate(parent_name, attr_name, operator, value))
            else:
                print("known result statement: %s" % statement)
        
        return results

    ENUMS = dict([(enum.name, enum) for enum in DayPeriod] + [(enum.name, enum) for enum in WeekDay])

    def get_enum_value(name):
        return ENUMS.get(name)

    def convert_enums(arg_dict):
        if 'day' in arg_dict: arg_dict["day"] = [WeekDay[s] for s in arg_dict["day"]]
        if 'period' in arg_dict: arg_dict["period"] = [DayPeriod[s] for s in arg_dict["period"]]

    def load_events():
        
        
        
        with renpy.file('scripts/events.json') as stream:
            data_loaded = json.load(stream)
        
        events = {}
        for event in data_loaded:
            
            convert_enums(event)
            
            proceed_to = event.get('proceed_to')
            if proceed_to:
                
                
                event['proceed_to'] = parse_proceed_to(proceed_to)
            
            
            
            ifs = event.get('ifs')
            if ifs:
                event['ifs'] = parse_ifs(ifs)
            
            results = event.get('results')
            if results:
                event['results'] = parse_results(results)
            
            
            
            try:
                Event(**event)
            except Exception as e:
                print("cannot create event %s" % event['name'])
                print(e)
                traceback.print_exc()

    def load_subplots():
        with renpy.file('scripts/subplots.json') as stream:
            store.SUBPLOTS = json.load(stream)


    def load_interactions():
        with renpy.file("scripts/interactions.json") as stream:
            data_loaded = json.load(stream)
            for arg_dict in data_loaded:
                Interaction(**arg_dict)

    def load_playlets():
        with renpy.file("scripts/playlets.json") as stream:
            data_loaded = json.load(stream)
            for arg_dict in data_loaded:
                convert_enums(arg_dict)
                
                results = arg_dict.get('results')
                if results:
                    arg_dict['results'] = parse_results(results)
                
                Playlet(**arg_dict)

    def load_gallery():
        last_cgs = get_last_cgs()
        with renpy.file("scripts/gallery.json") as stream:
            data_loaded = json.load(stream)
            for arg_dict in data_loaded:
                handle_gallery_item(arg_dict, last_cgs)
                EventCGSet(**arg_dict)

    def load_roomCGs():
        args = []
        with renpy.file("scripts/roomcgs.json") as stream:
            data_loaded = json.load(stream)
            for arg_dict in data_loaded:
                convert_enums(arg_dict)
                OneCG(**arg_dict)

    def clear_data():
        store.EVENTS = {}
        
        store.AUTO_EVENTS = []
        store.INTERACTIONS = defaultdict(list)
        
        store.PLAYLETS = {}
        store.NZ_PLAYLETS = {}
        store.CGSETS = defaultdict(list) 
        store.gallery = None
        debug.events = store.defaultdict(list)
        print("data cleared.")

    def load_data():
        try:
            clear_data()
            load_gallery()
            load_interactions()
            load_events()
            
            
            load_playlets()
            print("data loaded.")
            debug.init()
        except:
            traceback.print_exc()

    def load_data_thread():
        renpy.invoke_in_thread(load_data)
        print("loading data in thread...")

    if load_data_enabled and not EVENTS:
        load_data_thread()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
