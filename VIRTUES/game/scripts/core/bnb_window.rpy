transform in_room:
    on idle:
        zoom 0.9
        ease 0.3 yoffset -3
        ease 0.3 yoffset +3
        repeat
    on hover:
        ease 0.2 zoom 1.0

default bnb = Bnb("Гавань Аганга")

init python:

    Room.type_names = {
        "basic": "Гостевые спальни",
        "private": "Основные спальни",
        "facility": "Общественные места"
    }

    Room("basic", "basic_room", "gui/action/basic.png", revenue=100.0, expanse=.0, cost=500.0)
    Room("private", "my_room", "gui/action/my_room.png", revenue=0.0, expanse=.0, cost=500.0)
    Room("private", "A_room", "gui/action/A_room.png", revenue=0.0, expanse=.0, cost=500.0) 
    Room("private", "G_room", "gui/action/G_room.png", revenue=0.0, expanse=.0, cost=500.0) 
    Room("private", "C_room_2", "gui/action/C_room_2.png", size="small", revenue=0.0, expanse=.0, cost=500.0)

    Room("facility", "frontyard", "gui/action/frontyard.png", revenue=0.0, expanse=.0, cost=500.0)
    Room("facility", "livingroom", "gui/action/livingroom.png", revenue=0.0, expanse=.0, cost=500.0)
    Room("facility", "kitchen", "gui/action/kitchen.png", size="small", revenue=0.0, expanse=.0, cost=500.0)
    Room("facility", "bathroom", "gui/action/bathroom.png", size="small", revenue=0.0, expanse=.0, cost=500.0)
    Room("facility", "toilet", "gui/action/toilet.png", size="small", revenue=0.0, expanse=.0, cost=500.0)

define fixed_rooms = None

default player_rooms = {
    "basic_room": 4
}

init python:

    def get_bnb_rooms(flat=False):
        rooms = {
            "facility": ["frontyard", "livingroom", "kitchen", "bathroom", "toilet"],
            "private": ["my_room", "A_room"]
        }
        
        if seen("G_MoveIn"):
            rooms["private"].append("G_room")
        
        if seen("C_daily_12"):
            rooms["private"].append("C_room_2")
        
        if flat:
            flat_list = []
            for sublist in rooms.values():
                for item in sublist:
                    flat_list.append(item)
            return flat_list
        else:
            return rooms

    def get_bnb_revenue():
        total_revenue = 0
        for name, count in player_rooms.items():
            room = ROOMS[name]
            total_revenue = room.revenue * count
        return total_revenue


screen room_hover(room, message=None):
    style_prefix "room_hover"
    default pos = renpy.get_mouse_pos()
    zorder 91
    frame at normal_t(0.3):
        pos pos anchor (0.5, 0.5)
        has vbox:
            spacing 4
        text "[room.name]"
        if room.revenue > 0:
            text "Доход: $[room.revenue] /День"
        if room.expanse > 0:
            text "Расход: $[room.expanse]"
        if message:
            text "[message]"





screen bnb():




    zorder 90

    button:
        padding (0,0)
        action Hide("bnb")
        alternate Hide("bnb")

    if is_scene("Map"):
        button at normal_t(0.2):
            alternate Hide("bnb")
            background gui.bi70_frame
            action NullAction()
            xysize (1400, 900)
            align (0.5, 0.5)
            padding (60, 60)

            vbox:
                yalign 0.2
                style_prefix "bnbwvb"
                align (1.0, 0.0)

                spacing 10








                vbox:
                    text "[bnb.revenue.name]"
                    text "${}/День".format(get_bnb_revenue())
                vbox:
                    text "[bnb.expanse.name]"
                    text "$[bnb.expanse.value]/Неделя"

                null height 20

                use sub_action_panel(bnb_action)

            frame:
                xsize 1000 ysize 800
                padding (30, 30)

                has vbox:
                    yalign 0.5

                for type in sorted(fixed_rooms, key=sort_type):

                    hbox:
                        text "{}".format(Room.type_name(type))
                        null width 18
                        add Solid("#ffffffb0", ysize=2, yalign=0.5)

                    hbox:
                        box_wrap True
                        box_wrap_spacing 16
                        spacing 16
                        for room in fixed_rooms[type]:
                            $ room = ROOMS[room]
                            vbox spacing 10:

                                button:
                                    alternate Hide("bnb")
                                    xysize room.xysize

                                    if room.action.is_clickable:
                                        add "gui/action/{}.png".format(room.label) align (0.5, 0.5)
                                        action room.action.run
                                    else:
                                        add im.Grayscale("gui/action/{}.png".format(room.label)) align (0.5, 0.5)
                                        action NullAction()

                                    add get_action_badge(room.action) align (0.0, 0.0) offset (-20, -25)

                                    hovered ShowTransient("room_hover", room=room, message=room.action.hover_message)
                                    unhovered Hide("room_hover")

                                text room.name align (0.5, 1.0) size 24


                    null height 36

                hbox:
                    text "Гостевые спальни"
                    null width 18
                    add Solid("#ffffffb0", ysize=2, yalign=0.5)

                for room, total in player_rooms.items():
                    $ room = ROOMS[room]
                    hbox:
                        vbox spacing 10:

                            button:
                                alternate Hide("bnb")
                                action NullAction()
                                xysize room.xysize
                                add room.image
                                hovered ShowTransient("room_hover", room=room, message=room.action.hover_message)
                                unhovered Hide("room_hover")

                            text room.name align (0.5, 1.0) size 24

                        hbox:
                            yalign 0.5 offset (36, -12)
                            text "x" yalign 1.0 size 32
                            text "[total]" yalign 1.0 size 42


init python:
    def sort_type(type):
        if type=="facility":
            return 0
        elif type == "private":
            return 1
        return type

init -1 python:

    ROOMS = {}
    TYPE_ROOMS = defaultdict(list)

    class Room(object):
        
        type_names = {}
        
        def __init__(self, type, label, image, size="regular", name=None, revenue=0.0, expanse=0.0, cost=0.0):
            self.type = type
            self.label = label
            self.image = image
            self.size = size
            if self.size == "regular":
                self.xysize = (225, 124)
            elif self.size == "small":
                self.xysize = (135, 124)
            self._name = name
            
            
            self.revenue = revenue
            self.expanse = expanse
            self.cost = cost
            global ROOMS, TYPE_ROOMS
            ROOMS[self.label] = self
            TYPE_ROOMS[type].append(self)
        
        @property
        def types(self):
            global TYPE_ROOMS
            return store.TYPE_ROOMS.keys()
        
        @staticmethod
        def type_name(type):
            return Room.type_names[type]
        
        def __repr__(self):
            return self.type +"("+str(self.name)+")"
        
        @property
        def action(self):
            return Action.get(self.label)
        
        @property
        def name(self):
            if self._name:
                return self._name
            else:
                return self.action.display_name
        
        @property
        def x(self):
            return self.pos[0]
        @property
        def y(self):
            return self.pos[1]
        @property
        def z(self):
            return self.pos[2]


    class Facility(Room):
        def __new__(self, type="Facility", name=None, pos=None, revenue=.0, expanse=.0, cost=500.0, action=None, multiplier=.0):
            facility = Room(type, name, action, pos, revenue, expanse, cost)
            facility.multiplier = multiplier
            return facility


    class Bnb(object):
        def __init__(self, name, owner=None, lease=.0, maintenance_fee=.0, rooms=[], facilities=[], stage=0, charm=0, xsize=4, ysize=4, zsize=1, star=1):
            self.name = name
            self.owner = owner
            
            self.lease = Attr(1400.0, name=_("Земельный налог"), owner=self)
            self.maintenance_fee = Attr(600.0, name=_("Стоимость технического обслуживания"), owner=self)
            self.rooms_revenue = Attr(.0, name=_("Доходы от номеров"), owner=self)
            self.rooms_expanse = Attr(.0, name=_("Расходы на номер"), owner=self)
            self.rooms_revenues = []
            
            self.cleaning_count_of_week = 0
            self.rooms = rooms
            self.charm = charm
            self.stage = stage
            self.facilities = facilities
            
            self.xsize = xsize
            self.ysize = ysize
            
            def room_revenues_str(self):
                return "Доход от номера ({}) * [Star({}) + Facility Multiplier({})]".format(self.room_revenue, self.stage, self.facility_buff)
            self.rooms_revenues.sval = room_revenues_str(self)
            self.update()
        
        @property
        def revenues(self):
            return [self.tip, self.room_revenue]
        
        @property
        def expanses(self):
            return [self.lease, self.maintenance_fee, self.rooms_expanse]
        
        
        def update(self):
            self.rooms_revenues = self.room_revenue * (self.star + self.facility_buff) + self.tip
        
        @property
        def star(self):
            return int(self.charm / 20)
        
        def add_room(self, room):
            self.rooms.append(room)
        
        @property
        def room_number(self):
            
            return len([room for room in self.rooms if room.type in ("BasicRoom", "CoupleRoom")])
        
        @property
        def facility_buff(self):
            if not self.facilities:
                return 0.0
            return Attr.sum([facility.multiplier for facility in self.facilities])
        
        @property
        def room_revenue(self):
            if not self.rooms:
                return 0.0
            return Attr.sum([room.revenue for room in self.rooms])
        
        @property
        def tip(self):
            return Attr(self.cleaning_count_of_week * 30.0, name=_("Чаевые"), owner=self)
        
        @property
        def expanse(self):
            expanse = self.lease + self.maintenance_fee + Attr.sum([room.expanse for room in self.rooms])
            expanse.name = "Расход"
            return expanse
        
        @property
        def revenue(self):
            revenue = self.tip + Attr.sum([room.revenue for room in self.rooms])
            revenue.value *= 1.0
            revenue.name = "Доход"
            return revenue
        
        def get_revenue(self):
            return self.revenue
        
        @property
        def revenue_str(self):
            return ("{} * ")
        
        @property
        def income(self):
            return self.revenue - self.expanse
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
