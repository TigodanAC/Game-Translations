
default action_states = {}

init -3 python:

    ACTIONS = {}

    class Action(object):
        actions_to_delete = []
        current_parent = None
        
        @classmethod
        def get(cls, action):
            global ACTIONS
            return ACTIONS.get(action)
        
        def __init__(self, label, name, clickable=None, displaying=None, link=None, has_children=False, is_not_implemented=False, post=None, rename=[], pos=None, hover_message=None, xysize=(225, 124), screen=None, to_map=True, training_nz=None, **kwargs):
            self.label = label
            self.name = name
            self.rename = rename
            
            self.xysize = xysize
            
            self.pos = pos
            self.idle_icon = "gui/map/{}.png".format(self.label)
            self.insensitive_icon = im.MatrixColor(self.idle_icon, im.matrix.colorize("#000", "#888888"))
            
            
            
            
            self.events = []
            self.post = post
            self.screen = screen
            self.to_map = to_map
            
            
            self._children = []
            self.has_children = False
            
            self.parent = Action.current_parent
            if self.parent is not None:
                Action.get(self.parent)._children.append(self.label)
            
            if has_children:
                Action.current_parent = self.label
            
            self.get_displaying = displaying
            
            
            
            
            self.link = link
            
            if clickable:
                self.get_clickable = clickable
            elif has_children:
                self.get_clickable = self.is_any_child_clickable
            elif link:
                self.set_link(link)
            else:
                self.get_clickable = True
            
            self.post = post
            
            self._hover_message = hover_message
            
            self.is_not_implemented = is_not_implemented
            
            self.training_nz = training_nz
            
            self.__dict__.update(kwargs)
            
            global ACTIONS
            ACTIONS[self.label] = self
        
        def get_icon(self):
            return self.idle_icon if self.is_clickable else self.insensitive_icon
        
        @property
        def state(self):
            if self.label not in action_states:
                action_states[self.label] = ActionState()
            return action_states[self.label]
        
        def __repr__(self):
            return ("Action({}, {}, {})".format(self.label, self.display_name, id(self)))
        
        def __str__(self):
            return self.display_name
        
        def delete(self):
            Action.actions_to_delete.append(self.label)
            try:
                Action.__dict__.pop(self, None)
            except:
                pass
        
        
        @property
        def display_name(self):
            if not self.rename:
                return self.name
            else:
                name = self.name
                for pair in self.rename:
                    if eval(pair[1]):
                        name = pair[0]
                return name
        
        
        @property
        def children(self):
            children = []
            for child in self._children:
                if child in Action.actions_to_delete:
                    self._children.remove(child)
                    del Action.actions_to_delete[:]
                else:
                    children.append(Action.get(child))
            
            
            return children
        
        @property
        def displaying_children(self):
            return [child for child in self.children if child.displaying]
        
        @property 
        def is_event(self):
            return not self._children
        
        @property 
        def is_location(self):
            return bool(self._children)
        
        @property
        def is_link(self):
            return bool(self.link)
        
        def set_link(self, link):
            self.link = link
            self.get_clickable = Action.get(link).get_clickable
        
        @property 
        def is_clickable(self):
            get_clickable = self.get_clickable
            if get_clickable is True:
                return True
            elif isinstance(get_clickable, basestring):
                return eval(get_clickable)
            else:
                return get_clickable()
        
        def is_any_child_clickable(self):
            return Action.get_any_child_clickable(self)
        
        @classmethod
        def get_any_child_clickable(cls, parent_action):
            for action_key in parent_action._children:
                action = cls.get(action_key)
                if action.is_location:
                    if cls.get_any_child_clickable(action) is True:
                        return True
                elif action.is_link:
                    continue
                elif action.is_not_implemented:
                    continue
                elif action.is_clickable is True:
                    return True
            
            return False
        
        @property 
        def displaying(self):
            get_displaying = self.get_displaying
            if not get_displaying:
                return True
            elif isinstance(get_displaying, basestring):
                return eval(get_displaying)
            else:
                return self.get_displaying()
        
        def get_triggerable(self):
            if not self.is_clickable:
                return
            
            event = self.get_self_triggerable_event()
            if event:
                return event
            
            playlet = self.get_playlet()
            if playlet:
                return playlet
            
            oneCG = self.get_OneCG()
            if oneCG:
                return oneCG
        
        
        def get_runnable(self):
            if not self.is_clickable:
                return None
            
            if self._children:
                return None
            
            event = self.get_self_triggerable_event()
            if event and event.runnable:
                return event.run
            
            playlet = self.get_playlet()
            if playlet:
                return playlet.run
            
            oneCG = self.get_OneCG()
            if oneCG:
                return oneCG.run
            
            if self.is_not_implemented:
                not_implemented_message
            elif self.link:
                return Call("run_action", action=Action.get(self.link))
            else:
                return Call("run_action", action=self)
        
        def run(self):
            self.get_runnable()()
        
        @property
        def hover_message(self):
            if callable(self._hover_message):
                return self._hover_message()
            return self._hover_message
        
        def has_children_triggerable_event(self):
            for child in self.displaying_children:
                if child.get_self_triggerable_event():
                    return True
            return False
        
        def get_self_triggerable_event(self):    
            for event in self.events:
                event = get_event(event)
                if event.triggerable:
                    return event
            return None
        
        def get_playlet(self):
            for playlet in cPlaylets:
                if self.label == playlet.action:
                    return playlet
        
        def get_children_playlets(self):
            results = []
            for child in self.displaying_children:
                playlet = child.get_playlet()
                if playlet:
                    results.append(p)
            return results
        
        def get_OneCG(self):
            if cOneCG and cOneCG.action == self.label:
                return cOneCG
        
        def has_children_OneCG(self):
            if cOneCG:
                for child in self.displaying_children:
                    if child.get_OneCG():
                        return True
            return False
        
        @property
        def count_of_day(self):
            return self.state.count_of_day
        
        @property
        def count(self):
            return self.state.count
        
        def add_count_of_day(self):
            self.state.add_count_of_day()
        
        def add_count(self):
            self.state.add_count()



    class ActionState(object):
        
        def __init__(self):
            self._count_of_day = 0
            self.count_day = None
            self.count = 0
        
        @property
        def count_of_day(self):
            if self.count_day and self.count_day == Date(store.t):
                return self._count_of_day
            else:
                self.count_day = Date(store.t)
                self._count_of_day = 0
                return self._count_of_day
        
        def add_count_of_day(self):
            if self.count_day and self.count_day == Date(store.t):
                self._count_of_day += 1
            else:
                self.count_day = Date(store.t)
                self._count_of_day = 1
        
        def add_count(self):
            self.count += 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
