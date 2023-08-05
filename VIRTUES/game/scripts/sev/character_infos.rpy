default t = Time(total_period=1)

define P_study = Progress("study", "Учёба", "B_love_meter", base=6.0, nz="Senning")
define P_work = Progress("work", "Работа", "C_love_meter", base=6.0, nz="Theodora")

define P_sport = Progress("sport", "Спорт", "F_love_meter", base=6.0, nz="Rachel")

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

define A = Nz("A", "Вера", 22,
    color="#d29881",
    intro='''Бедная сельская девушка, которая приехала в этот город совсем одна с мечтой о лучшей жизни. Теперь она может выполнять только низкооплачиваемую черную работу из-за отсутствия высшего образования.
Она очень трудолюбива и с открытым сердцем принимает это общество, каким бы плохим оно ни было.
Я лишил ее девственности пьяной ночью.''',
    like=["Готовка", "Просмотр футбольного матча",  "Курица-карри"],
    hint=A_hint,
    zone=["Ноги", "Рот",  "Вагина"]
)

define B = Nz("B", "Сеннин", 21,
    color="#aaaaaa",
    intro='''Она моя лучшая подруга в колледже, а также единственная дочь пары китайских миллиардеров.
Она очень талантлива в академических исследованиях. Ее средний балл составляет 3.8 в течение последних двух лет.
Она популярна в школе из-за своей доброты. Но она почему-то становится интровертом, когда разговаривает с незнакомцами. ''',
    like=["Учеба в библиотеке", "Инвестиции в акции", "Зеленый чай"],
    zone=["Неизвестно"],
    hint=B_hint
)

define C = Nz("C", "Теодора", 23,
    color="#9dc8ca",
    intro='''Будучи старшей дочерью известной предпринимательницы, она сейчас работает менеджером в одной из компаний своей матери.
Мы помолвлены по воле родителей, но настоящей любви между нами пока нет. На самом деле мы не ладим друг с другом, как два полюса магнита.
Мне не нравяится её холодная и сильная личность.''',
    like=["Скайдайвинг", "Тихие места", "Роскошный экипаж"],
    zone=["Соски"],
    hint=C_hint
)
define D = Nz("D", "Айрин", 18,
    color="#a4d5a9",
    intro='''Она младшая сестра Теодоры.
Хоть она и молода, но прекрасно умеет использовать свое обаяние, чтобы получить преимущества от парней.
Она выглядит наивной, но это может быть не её истинное лицо.
Мы выросли вместе и сохраняем близкие отношения до сих пор. Она считает меня своим братом.''',
    like=["Рисунки от руки", "Короткая юбка", "Косплей"],
    zone=["Анус"],
    hint=D_hint
)
define E = Nz("E", "Элиза", 40,
    color="#efe2a6",
    intro='''Известная предпринимательница, мать Феодоры и Ирины, в настоящее время не замужем..
Она и мой папа близкие друзья, и она заботится обо мне, как о собственном сыне.
Сейчас она живет в своем большом особняке со своей младшей дочерью. Иногда она чувствует себя одинокой.''',
    like=["Мыльные оперы", "Программирование", "СПА для тела"],
    zone=["Грудь"],
    hint=E_hint
)
define F = Nz("F", "Рэйчел", 20,
    color="#0b654f",
    intro='''Член университетской команды по легкой атлетике, самая сильная девушка, которую я когда-либо встречал в своей жизни. 
Она не осознает своей красоты и немного неуверенна в красоте своего лица.''',
    like=["Тренировка", "Каратэ", "Марафон"],
    zone=["Неизвестно"],
    hint=F_hint
)
define G = Nz("G", "Уно", 19,
    color="#ffbfbf",
    intro=G_intro,
    like=["Косплей", "Манга", "Съемка коротких видеороликов"],
    zone=["Соски", "Грудь", "Шея"],
    hint=G_hint
)

init -1 python:

    def G_intro():
        intro = '''Известная швея, друг Айрин.
Я ещё не очень хорошо её знаю.'''
        if seen("G_MoveIn"):
            intro = '''Известная швея, любительницы снимать порно, продавщица в книжном магазине. Эта девушка полна тайн.
Почему-то она не уверена в своей груди — она думает, что она слишком большая.
Она мало говорит, но умеет быстро находить общий язык с незнакомцами.'''
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
        hint = "Попробуйте пойти к ней на работу и поговорить с там, чтобы поладить с ней."
        if seen("A_love_2") and not seen("pcsj"):
            hint = "В последнее время я посещал Веру слишком много раз, возможно, мне следует уделить немного времени Сеннин."
        return hint

    def B_hint():
        hint = "Пока ничего."
        if seen("d6_1"):
            hint = "Попробуйте купить ей подарок в \"центре города\", а потом найти её во второй половине дня после того, как её любовь достигнет 5."
        if seen("B_love_1"):
            hint = "Она восхищается людьми, которые хорошо учатся. Вы должны пойти учиться в школу и попытаться произвести на неё впечатление."
        if seen("B_love_2"):
            hint = "В последнее время я посещал Сеннин слишком много раз, возможно, мне стоит уделить немного времени Вере."
        if seen("pcsj"):
            hint = "Она восхищается людьми, которые хорошо учатся. Я должен пойти учиться в школу и попытаться произвести на неё впечатление."
        return hint

    def C_hint():
        hint = "Пока ничего."
        if seen("pcsj"):
            hint = "Она восхищается людьми, которые много работают. Вы должны регулярно ходить на работу и стараться произвести на нее впечатление."
        return hint

    def D_hint():
        hint = "Попробуйте купить ей подарок, а после обеда навестить её дома."
        if seen("D_dqsj"):
            hint = "Пока ничего."
        if seen("pcsj"):
            hint = "Вы можете заниматься с ней каждый день днем ​​или вечером."
        return hint

    def E_hint():
        hint = "Пока ничего."
        if seen("pcsj"):
            hint = "Она дала вам две работы, одна в её компании, а другая - репетиторство её младшей дочери. Вам нужно доказать ей, что вы можете хорошо справляться с обеими этими работами."
        return hint

    def F_hint():
        hint = "Она восхищается людьми с сильным телом. Вам следует чаще тренироваться в парке и пытаться произвести на неё впечатление.."
        return hint

    def G_hint():
        hint="Пока ничего."
        if seen("G_MoveIn"):
            hint = "Днем она работает в книжном магазине, её всегда можно найти там в будние дни."
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


define a = Character("[A.name]", who_color=A.color)
define b = Character("[B.name]", who_color=B.color)
define c = Character("[C.name]", who_color=C.color)
define c_qm = Character("[C.name]?", who_color=C.color)
define d = Character("[D.name]", who_color=D.color)
define e = Character("[E.name]", who_color=E.color)
define f = Character("[F.name]", who_color=F.color)
define g = Character("[G.name]", who_color=G.color)
define narrator = Character(None, what_color=gui.dialogue_color)
define player = Character("[P.name]", who_color=P.color)


define posia = Character("Позия", who_color="#A657C4")
define minna = Character("Леди Минна", who_color="#6E0C1B")
define bubble_a = Character(None, screen="bubble", show_color=A.color)
define bubble_b = Character(None, screen="bubble", show_color=B.color)
define bubble_c = Character(None, screen="bubble", show_color=C.color)
define bubble_d = Character(None, screen="bubble", show_color=D.color)
define bubble_e = Character(None, screen="bubble", show_color=E.color)
define bubble_f = Character(None, screen="bubble", show_color=F.color)
define bubble_g = Character(None, screen="bubble", show_color=G.color)

