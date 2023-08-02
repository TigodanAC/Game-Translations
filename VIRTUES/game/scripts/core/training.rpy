default TRAINING = {
        "A": TrainingStatus("A"),
        "B": TrainingStatus("B"),
        "C": TrainingStatus("C"),
        "D": TrainingStatus("D"),
        "E": TrainingStatus("E", shame=1),
        "F": TrainingStatus("F"),
        "G": TrainingStatus("G", sub=1, shame=1)
    }

define TRAINING_EVENTS = defaultdict(lambda: defaultdict(list))

init python:

    def get_trainning_active():
        if findee == A and seen('A_love_5'):
            return True
        if findee == B and seen('B_love_6'):
            return True
        if findee == C and seen('C_love_7'):
            return True
        if findee == D and seen('D_love_6'):
            return True
        if findee == E and seen('E_love_8'):
            return True
        if findee == G and seen('G_love_6'):
            return True
        return False

    class TrainingStatus(object):
        types = ["inti", "skill", "sub", "shame"]
        type_names = {
                "inti": "Intimacy",
                "skill": "Sex Skill",
                "sub": "Submissiveness",
                "shame": "Shamelessness"
            }
        
        def __init__(self, nz, inti=0, skill=0, sub=0, shame=0):
            self.nz = nz
            self.inti = inti
            self.skill = skill
            self.sub = sub
            self.shame = shame      

    def get_findee_training_status():
        return TRAINING.get(findee.code)

    def get_findee_training_level(type):
        return getattr(TRAINING.get(findee.code), type)

    def add_findee_training_level(type):
        old_value = get_findee_training_level(type)
        setattr(get_findee_training_status(), type, old_value+1)

    def get_trainning_action(type):
        for event in TRAINING_EVENTS[findee.code][type]:
            if event.triggerable:
                status = get_findee_training_status()
                return [Function(add_findee_training_level, type=type), event.run]

    def get_nz_can_train(nz):
        for type, events in TRAINING_EVENTS[nz].items():
            for event in events:
                if event.triggerable:
                    return True 

    def get_training_status(nz):
        return TRAINING.get(nz.code)

    def get_training_level(nz, type):
        return getattr(TRAINING.get(nz.code), type)

    def add_training_level(nz, type):
        old_value = get_training_level(nz, type)
        setattr(get_training_status(nz), type, old_value+1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
