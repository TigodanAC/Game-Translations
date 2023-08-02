default t = Time(total_period=1)

define P_study = Progress("study", "Study", "B_love_meter", base=6.0, nz="Senning")
define P_work = Progress("work", "Work", "C_love_meter", base=6.0, nz="Theodora")

define P_sport = Progress("sport", "Sport", "F_love_meter", base=6.0, nz="Rachel")

define P = Player("P", state="P_state", color=color.cream)

default P_state = PlayerState(cash=500000.0)

define A_love = TrueLove("A_love_meter", max_value=65)
define B_love = TrueLove("B_love_meter", max_value=65)
define C_love = TrueLove("C_love_meter", max_value=80)
define D_love = TrueLove("D_love_meter", max_value=75)
define E_love = TrueLove("E_love_meter", max_value=70)
define F_love = TrueLove("F_love_meter", max_value=50)
define G_love = TrueLove("G_love_meter", max_value=65)

define A_lust = Lust("A_lust_meter", max_value=30)
define B_lust = Lust("B_lust_meter", max_value=30)
define C_lust = Lust("C_lust_meter", max_value=30)
define D_lust = Lust("D_lust_meter", max_value=30)
define E_lust = Lust("E_lust_meter", max_value=30)
define F_lust = Lust("F_lust_meter", max_value=30)
define G_lust = Lust("G_lust_meter", max_value=30)

define A_harem = Harem("A_harem_meter", max_value=30)
define B_harem = Harem("B_harem_meter", max_value=25)
define C_harem = Harem("C_harem_meter", max_value=30)
define D_harem = Harem("D_harem_meter", max_value=25)
define E_harem = Harem("E_harem_meter", max_value=25)
define F_harem = Harem("F_harem_meter", max_value=10)
define G_harem = Harem("G_harem_meter", max_value=30)

define color.A = "#d29881"
define color.B = "#aaaaaa"
define color.C = "#9dc8ca"
define color.D = "#a4d5a9"
define color.E = "#efe2a6"
define color.F = "#0b654f"
define color.G = "#ffbfbf"

define A = Nz("A", "Vera", 22,
    color="#d29881",
    intro='''A poor young countryside girl who came to this city alone with a dream of making a better life. She can only do the low-paid menial jobs now due to the lack of higher education.
She is super hardworking and she embraces this society with a golden heart no matter how bad it is.
I took her virginity on a drunken night.''',
    like=["Cooking", "Watching soccer game",  "Chicken curry"],
    hint=A_hint,
    zone=["Feet", "Mouth",  "Vagina"]
)

define B = Nz("B", "Senning", 21,
    color="#aaaaaa",
    intro='''She is my best friend in college, also the only daughter of a couple of Chinese billionaires.
She is talented at academic studies. Her GPA maintains 3.8 for the last two years. 
She is popular at school because of her kindness. But she is somehow introverted when talking with strangers. ''',
    like=["Studying at library", "Stocks investing", "Green tea"],
    zone=["Unknown"],
    hint=B_hint
)

define C = Nz("C", "Theodora", 23,
    color="#9dc8ca",
    intro='''As the older daughter of a famous entrepreneur, she is now a manager in one of her mother's companies.
We are engaged at our parents' wills, but there is no real love between us yet. In fact, we don't get along with each other, like the two poles of a magnet.
I don't like her cold and strong personalities.''',
    like=["Sky diving", "Quiet place", "Luxury roadster"],
    zone=["Nipples"],
    hint=C_hint
)
define D = Nz("D", "Irene", 18,
    color="#a4d5a9",
    intro='''She is Theodora's little sister.
Although she is young, she perfectly knows how to use her charm to get advantages from boys.
She looks naïve, but that may not be her true face.  
We grew up together and kept a close relationship until now. She takes me as her own brother.''',
    like=["Hand drawing", "Short skirt", "Cosplay"],
    zone=["Anus"],
    hint=D_hint
)
define E = Nz("E", "Elisa", 40,
    color="#efe2a6",
    intro='''A famous entrepreneur, the mother of Theodora and Irene, currently single.
She and my dad are close friends, and she takes me as her own son to care.
She now lives in her big mansion with her little daughter. Sometimes she would feel lonely.''',
    like=["Soap operas", "Programming", "Body SPA"],
    zone=["Breasts"],
    hint=E_hint
)
define F = Nz("F", "Rachel", 20,
    color="#0b654f",
    intro='''A member of university track team, the strongest girl I have ever met in my life. 
She is not aware of her beauty and being a little unconfident about her face.''',
    like=["Work out", "Karate", "Marathon"],
    zone=["Unknown"],
    hint=F_hint
)
define G = Nz("G", "Uno", 19,
    color="#ffbfbf",
    intro=G_intro,
    like=["Cosplay", "Manga", "Shooting short videos"],
    zone=["Nipples", "Breasts", "Neck"],
    hint=G_hint
)

init -1 python:

    def G_intro():
        intro = '''A famous coser, Irene's friend.
I don't know her very well yet.'''
        if seen("G_MoveIn"):
            intro = '''A famous coser, an amateur porn shooter, a bookstore clerk. This girl is full of mystery.
Somehow she is not confident with her breasts -- she thinks they are oversize. 
She doesn't talk much, but she has the ability to get along with strangers in a short time. '''
        return intro

    def A_clothes():
        clothes = ["Default"]
        return clothes

    def B_clothes():
        clothes = ["Default"]
        if seen("B_date_1"):
            clothes.append("Yellow Shirt")
        if B.relation != "general":
            clothes.append("Men's Shirt")
        return clothes

    def C_clothes():
        clothes = ["Default"]
        return clothes

    def D_clothes():
        clothes = ["Default"]
        if seen("pcsj"):
            clothes.append("School Uniform")
        if seen("D_love_6"):
            clothes.append("Uniform with neko ears")
        return clothes

    def E_clothes():
        clothes = ["Default"]
        if seen("CDE_Picnic"):
            clothes.append("Twisted Shirt")
        return clothes

    def F_clothes():
        clothes = ["Default"]
        return clothes

    def G_clothes():
        clothes = ["Default"]
        clothes.append("Default (Coser)")
        return clothes

    def A_hint():
        hint = "Try go to her workplaces and talk with her to get along with her."
        if seen("A_love_2") and not seen("pcsj"):
            hint = "I have found Vera for too many times recently, perhaps I should spend some time on Senning."
        return hint

    def B_hint():
        hint = "Nothing yet."
        if seen("d6_1"):
            hint = "Try buy her a gift at \"downtown\", and then find her in the afternoon after her love reaches 5."
        if seen("B_love_1"):
            hint = "She admires people who are good at studying. You should go study at school and try to impress her."
        if seen("B_love_2"):
            hint = "I have found Senning for too many times recently, perhaps I should spend some time on Vera."
        if seen("pcsj"):
            hint = "She admires people who are good at studying. You should go study at school and try to impress her."
        return hint

    def C_hint():
        hint = "Nothing yet."
        if seen("pcsj"):
            hint = "She admires people who work hard. You should go to work regularly and try to impress her."
        return hint

    def D_hint():
        hint = "Try buy her a gift, then visit her at her home in the afternoon."
        if seen("D_dqsj"):
            hint = "Nothing yet."
        if seen("pcsj"):
            hint = "You can tutor her everyday in the afternoon or evening."
        return hint

    def E_hint():
        hint = "Nothing yet."
        if seen("pcsj"):
            hint = "She gave you two jobs, one is working at her company, and the other one is tutoring her little daughter. You need to prove to her that you can do well in those jobs."
        return hint

    def F_hint():
        hint = "She admires people with strong body. You should work-out at the park more often and try to impress her."
        return hint

    def G_hint():
        hint="Nothing yet."
        if seen("G_MoveIn"):
            hint = "She works at the bookstore in the afternoon, you can always find her there during weekdays."
        return hint


default A_love_meter = Meter("A_love")
default B_love_meter = Meter("B_love")
default C_love_meter = Meter("C_love")
default D_love_meter = Meter("D_love")
default E_love_meter = Meter("E_love")
default F_love_meter = Meter("F_love")
default G_love_meter = Meter("G_love")

default A_lust_meter = Meter("A_lust")
default B_lust_meter = Meter("B_lust")
default C_lust_meter = Meter("C_lust")
default D_lust_meter = Meter("D_lust")
default E_lust_meter = Meter("E_lust")
default F_lust_meter = Meter("F_lust")
default G_lust_meter = Meter("G_lust")

default A_harem_meter = Meter("A_harem")
default B_harem_meter = Meter("B_harem")
default C_harem_meter = Meter("C_harem")
default D_harem_meter = Meter("D_harem")
default E_harem_meter = Meter("E_harem")
default F_harem_meter = Meter("F_harem")
default G_harem_meter = Meter("G_harem")

default A_state = NzState()
default B_state = NzState()
default C_state = NzState()
default D_state = NzState()
default E_state = NzState()
default F_state = NzState()
default G_state = NzState()


define a = Character("[A]", who_color=A.color)
define b = Character("[B]", who_color=B.color)
define c = Character("[C]", who_color=C.color)
define c_qm = Character("[C]?", who_color=C.color)
define d = Character("[D]", who_color=D.color)
define e = Character("[E]", who_color=E.color)
define f = Character("[F]", who_color=F.color)
define g = Character("[G]", who_color=G.color)
define narrator = Character(None, what_color=gui.dialogue_color)
define player = Character("[P.name]", who_color=P.color)


define posia = Character("Posia", who_color="#A657C4")
define minna = Character("Lady Minna", who_color="#6E0C1B")
define bubble_a = Character(None, screen="bubble", show_color=A.color)
define bubble_b = Character(None, screen="bubble", show_color=B.color)
define bubble_c = Character(None, screen="bubble", show_color=C.color)
define bubble_d = Character(None, screen="bubble", show_color=D.color)
define bubble_e = Character(None, screen="bubble", show_color=E.color)
define bubble_f = Character(None, screen="bubble", show_color=F.color)
define bubble_g = Character(None, screen="bubble", show_color=G.color)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
