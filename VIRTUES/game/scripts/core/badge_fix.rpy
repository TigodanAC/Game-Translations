image badge_red:
    contains:
        "gui/badge_glow.png"
        ease 0.7 alpha 1.0
        ease 0.7 alpha 0.0
        repeat
    contains:
        "gui/badge.png"

image badge2:
    pos (-15, -15)
    "gui/badge.png"

image badge_orange:
    contains:
        "gui/badge_orange_glow.png"
        ease 0.7 alpha 1.0
        ease 0.7 alpha 0.0
        repeat
    contains:
        "gui/badge_orange.png"

image badge_playlet:
    contains:
        "gui/badge_playlet.png"
    contains:
        "gui/badge_playlet_glowing.png"
        ease 0.7 alpha 1.0
        ease 0.7 alpha 0.0
        repeat

image badge_purple:
    contains:
        "gui/badge_purple_glow.png"
        ease 0.7 alpha 1.0
        ease 0.7 alpha 0.0
        repeat
    contains:
        "gui/badge_purple.png"

image badge_X:
    "gui/badge_X.png"

image badge_A:
    "gui/badge_A.png"
image badge_B:
    "gui/badge_B.png"
image badge_C:
    "gui/badge_C.png"
image badge_D:
    "gui/badge_D.png"
image badge_E:
    "gui/badge_E.png"
image badge_F:
    "gui/badge_F.png"
image badge_G:
    "gui/badge_G.png"

transform badge_blink:
    ease 0.7 alpha 0.0
    ease 0.7 alpha 1.0
    repeat


init python:
    def get_action_badge(action):
        
        if action.training_nz and get_nz_can_train(action.training_nz) and action.is_clickable:
            return "badge_red"
        
        runnable = action.get_triggerable()
        
        if not runnable:
            return
        
        tp = type(runnable) 
        
        if tp is Event:
            if runnable.label == "trailer_1":
                return "badge_purple"
            else:
                return "badge_red"
        
        elif tp is Playlet:
            if runnable.is_harem:
                return "badge_X"
            else:
                return "badge_{}".format(runnable.nz) 
        
        elif tp is OneCG: 
            return "badge_orange"

    def _get_children_badge(action):
        badges = set()
        for child in action.displaying_children:
            if child.displaying_children:
                badge = _get_children_badge(child)
                if badge:
                    badges = badge|badges
            else:
                badge = get_action_badge(child)
                if badge:
                    badges.add(badge)
        return badges

    def get_children_badge(action):
        if not action.is_clickable:
            return []
        
        badges = _get_children_badge(action)
        
        has_red = "badge_red" in badges
        has_orange = "badge_orange" in badges
        badges -= {"badge_red", "badge_orange"}
        badges = list(badges)
        if has_red:
            badges.insert(0, "badge_red")
        elif has_orange:
            badges.append("badge_orange")
        return badges

    def get_location_badge(action):
        if action._children:
            return get_children_badge(action)
        else:
            return [get_action_badge(action)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
