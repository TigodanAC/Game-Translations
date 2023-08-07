default persistent.bg_states = {}
default persistent.bg_states_2 = {}
default save_bg_states = {}

python early:
    class BackgroundState(object):
        def __init__(self, name, has_password):
            self.name = name
            if has_password:
                self.is_password_unlocked = False
            else:
                self.is_password_unlocked = True
        
        def __repr__(self):
            return "{}".format("unlocked" if self.is_password_unlocked else "locked")
        
        def __eq__(self, other):
            if isinstance(self, BackgroundState) and self.name == other.name and self.is_password_unlocked == other.is_password_unlocked:
                return True
            else:
                return False

init python:
    class Background(object):
        def __init__(self, name, password=None, dname=[], pre_events=[], tweet=None):
            self.name = name
            self.dname = dname
            self.pre_events = pre_events
            self.thumbnail = name + "_thumbnail"
            self.password = password
            if password:
                
                self.mosaic_thumbnail = dark(im.Blur("images/thumbnails/"+name+"_thumbnail.webp", 3))
            self.darkins_thumbnail = dark_insensitive("images/thumbnails/"+name+"_thumbnail.webp")
            
            self.tweet = tweet
        
        @property
        def is_password_unlocked(self):
            if self.name in persistent.bg_states_2:
                return persistent.bg_states_2[self.name]
            else:
                return True
        
        @property
        def is_plot_unlocked(self):
            for event in self.pre_events:
                if not seen(event):
                    return False
            return True
        
        @property
        def is_shop_unlocked(self):
            if self.name in save_bg_states:
                return save_bg_states[self.name]
            else:
                return True
        
        @property
        def is_unlocked(self):
            return self.is_password_unlocked and self.is_plot_unlocked and self.is_shop_unlocked
        
        def unlock_from_shop(self):
            save_bg_states[self.name] = True
        
        def unlock_by_password(self, password):
            if password == self.password:
                persistent.bg_states_2[self.name] = True
                Push("Фон разблокирован.")
                return True
            else:
                Push("Неправильный пароль.")
                return False
        
        def __repr__(self):
            return "Фон(" + self.name + ")"

    class BackgroundSystem(object):
        data = {}
        states = {}
        current = {}
        
        @classmethod
        def add(cls, name, *args):
            bg = Background(name, *args)
            cls.data[name] = bg
            if not name in persistent.bg_states_2:
                
                persistent.bg_states_2[name] = False if bg.password else True
        
        
        @classmethod
        def add_to_shop(cls, name, *args):
            bg = Background(name, *args)
            cls.data[name] = bg
            if not name in save_bg_states:
                save_bg_states[name] = False
        
        @classmethod
        def get_backgrounds(cls):
            return cls.data.values()
        
        @classmethod
        def get_nz_backgrounds(cls, nz):
            return [bg for name, bg in cls.data.items() if name[0].upper() == nz.code]
        
        @classmethod
        def set_nz_background(cls, nz, bg):
            if bg:
                if bg.is_unlocked:
                    cls.current[nz.code] = bg.name
                    store._bubble_what = bg.tweet
                elif bg.is_shop_unlocked == False:
                    Push("Вы можете разблокировать эту картинку в магазине Позии или Минны.")
                else:
                    Push("Вы можете разблокировать эту картинку после того, как продвинетесь дальше в истории героини.")
            else:
                cls.current[nz.code] = None
                idx = int(random.random() * len(findee.tweets[findee.relation]))
                store._bubble_what = findee.tweets[findee.relation][idx]
        
        @classmethod
        def get_nz_background(cls, nz):
            if cls.current.get(nz.code, None):
                return cls.current.get(nz.code, None)
            return cls.get_default_nz_background(nz)
        
        @classmethod
        def get_default_nz_background_thumbnail(cls, nz):
            default_name = cls.get_default_nz_background(nz)
            for filepath in renpy.list_files():
                imagename = os.path.basename(filepath).split(".")[0]
                if imagename == default_name:
                    return im.Scale(filepath, 460, 259)
            return "void_thumbnail"
        
        @classmethod
        def get_default_nz_background(cls, nz):
            if nz.relation in ("girlfriend", "sexpartner", "fiancee"):
                relation = "gf"
            else:
                relation = nz.relation
            return "{}_{}_{}_{}".format(nz.code.lower(), relation, nz.clothes, "default")

    def find_bg(nz):
        if BackgroundSystem.get_nz_background(nz):
            return BackgroundSystem.get_nz_background(nz)
        if nz.relation in ("girlfriend", "sexpartner", "fiancee"):
            relation = "gf"
        else:
            relation = nz.relation
        return "{}_{}_{}_{}".format(nz.code.lower(), relation, nz.clothes, "default") 

    password_for_10 = "40379"
    password_for_20 = "80539"
    password_forbit = "𗀀"
    reward_str_for_10 = "{color=#dd6574}{size=-3}$10 Награда{/size}{/color}"
    reward_str_for_20 = "{color=#f4cc6c}{size=-3}$20 Награда{/size}{/color}"
    shop_str = "{color=#a186be}{size=-3}Магазин Позии{/size}{/color}"
    shop2_str = "{color=#a186be}{size=-3}Магазин Минны{/size}{/color}"

    BackgroundSystem.add("b_v7_10", password_for_10, ["[reward_str_for_10] Young Senning"], [],
        "Рада... видеть... тебя..., [P].")
    BackgroundSystem.add("c_v7_10", password_for_10, ["[reward_str_for_10] Young Theo"], [],
        "Ты же не забыл своё обещание, правда?")
    BackgroundSystem.add("c_v7_20", password_for_20, ["[reward_str_for_20] Gift Suit"], [],
        "Я не чей-ош подарок, но... ... неважно~")
    BackgroundSystem.add("d_v7_20", password_for_20, ["[reward_str_for_20] Gift Suit"], [],
        "Сюрприз!~ Айрин - подарок для тебя!~")
    BackgroundSystem.add("a_normal_1", None, ["Костюм горничной"], ["A_daily_10"],
        "Я твоя эксклюзивная горничная, хах~~")
    BackgroundSystem.add("b_normal_1", None, ["Желтая рубашка"], [],
        "Спасибо, что пришли, [P]..."),
    BackgroundSystem.add("b_normal_2", None, ["Женщина в черном"], ["B_train_sha_1"],
        "Ты предпочитаешь, чтобы я одевалась вот так?")
    BackgroundSystem.add("c_normal_1", None, ["Белое платье"], ["C_love_5"],
        "Присаживайся~")
    BackgroundSystem.add("d_normal_1", None, ["Студенческая форма"], [],
        "Айрин хорошая ученица~~ Айрин хорошая ученица~~"),
    BackgroundSystem.add("d_normal_2", None, ["Костюм кошечки"], ["D_love_6"],
        "Мяу~~ Мяу~~ Мяу-мяу-мяу~~~")
    BackgroundSystem.add("g_normal_1", None, ["Платье Coser"], [],
        "Приветствую, мой господин~")

    BackgroundSystem.add("d_v8_10", password_for_10, ["[reward_str_for_10] Mature Irene"], [],
        "Ах!~ Давно не виделись, Братик~")
    BackgroundSystem.add("e_v8_10", password_for_10, ["[reward_str_for_10] Young Elisa"], [],
        "Почему оно не может просто... перестать вытекать?")
    BackgroundSystem.add("e_v8_20", password_for_20, ["[reward_str_for_20] Gift suit"], [],
        "Будь осторожен, мастер, этот подарок очень хрупкий~")
    BackgroundSystem.add("a_v8_20", password_for_20, ["[reward_str_for_20] Dark Elf Vera"], [],
        "Это озеро... было испорчено человеческим запахом... ...")
    BackgroundSystem.add("c_v8_20", password_for_20, ["[reward_str_for_20] Warrior Theo"], [],
        "Смогу ли я когда-нибудь восстановить мир на этой земле?")

    BackgroundSystem.add("b_normal_3", None, ["Это моя рубашка!"], ["B_love_6"],
        "Я... Я верну тебе эту рубашку завтра, так что... ...")
    BackgroundSystem.add("g_normal_2", None, ["Ночнушка"], ["G_love_6"],
        "Это платье... все время спадает с моих плеч...")
    BackgroundSystem.add("d_v9_10", password_for_10, ["[reward_str_for_10] Vampire Princess Irene"], [],
        "Кошелек или жизнь!~~ Айрин не нужны конфеты, Айрин нужна твоя кровь или другие жидкости твоего тела~")
    BackgroundSystem.add("d_v9_20", password_for_20, ["[reward_str_for_20] Cat Ninja Irene"], [],
        "Мяу-мяу~ Возьми этот меч!~")
    BackgroundSystem.add("f_v9_10", password_for_10, ["[reward_str_for_10] Foreign Princess Rachel"], [],
        "Добро пожаловать в мое царство, Путешественник~")
    BackgroundSystem.add("g_v9_20", password_for_20, ["[reward_str_for_20] Cat Ninja Uno"], [],
        "Ты уверен... это часть моего обучения? Мяу... ...")


    BackgroundSystem.add("b_v10_10", password_for_10, ["[reward_str_for_10] Mature Senning"], [],
        "Мы... наконец встретились снова... ...")
    BackgroundSystem.add("g_v10_10", password_for_10, ["[reward_str_for_10] Bikini fighter"], [],
        "Можешь сфотографировать меня, пожалуйста?~~")
    BackgroundSystem.add("a_v10_20", password_for_20, ["[reward_str_for_20] Wild west"], [],
        "Давай, окунись со мной в дикую природу~")
    BackgroundSystem.add("e_v10_20", password_for_20, ["[reward_str_for_20] Wild west"], [],
        "Ну же, ковбой. Солнце вот-вот сядет~")


    BackgroundSystem.add("c_v11_10", password_for_10, ["[reward_str_for_10] Maid Suit Theodora"], [],
        "Не беспокой меня, у меня ещё есть дела...")
    BackgroundSystem.add("d_v11_10", password_for_10, ["[reward_str_for_10] Maid Suit Irene"], [],
        "Куда Айрин положила швабру?... ...")
    BackgroundSystem.add("e_v11_20", password_for_20, ["[reward_str_for_20] Queen Elisa"], [],
        "С возвращением, мой король~")
    BackgroundSystem.add("g_v11_20", password_for_20, ["[reward_str_for_20] Captured Cop Uno"], [],
        "Уууууууммммммммммм~~~~~~~~~")


    BackgroundSystem.add("b_v12_20", password_for_20, ["[reward_str_for_20] Practicing Nurse"], [],
        "Пожалуйста... просто укуси мой сосок, если я причиню тебе боль уколом... ...")
    BackgroundSystem.add("f_v12_20", password_for_20, ["[reward_str_for_20] Captain Rachel"], [],
        "Хмммммм... ... Но сначала я должена построить свой собственный корабль~")
    BackgroundSystem.add("a_v12_10", password_for_10, ["[reward_str_for_10] Horny Maid Vera"], [],
        "Я... как раз собиралась почистить ванную, мой хозяин...")
    BackgroundSystem.add("g_v12_10", password_for_10, ["[reward_str_for_10] Miko Uno"], [],
        "Я собираюсь в душ, хватит смотреть!~")


    BackgroundSystem.add("a_v13_10", password_for_10, ["[reward_str_for_10] Bikini Fighter Vera"], [],
        "Я могу... чем-нибудь помочь? Я умею драться~")
    BackgroundSystem.add("e_v13_10", password_for_10, ["[reward_str_for_10] Elisa Naked In Apron"], [],
        "Хочешь молочного пирога?")
    BackgroundSystem.add("c_v13_20", password_for_20, ["[reward_str_for_20] Wedding Dress"], [],
        "Теперь у тебя есть я... моё тело, моё сердце, моё всё~")
    BackgroundSystem.add("b_v13_20", password_for_20, ["[reward_str_for_20] Bunny Girl Senning"], [],
        "Я здесь... чтобы служить тебе~")


    BackgroundSystem.add("f_v135_10", password_for_10, ["[reward_str_for_10] Swimsuit Rachel"], [],
        "Я просто... пытаюсь быть более... женственной.")
    BackgroundSystem.add("d_v135_20", password_for_20, ["[reward_str_for_20] Little Mage Irene"], [],
        "Аууу~ Эта шляпа слишком тяжелая... ...")

    BackgroundSystem.add("d_v14_10", password_for_10, ["[reward_str_for_10] Oriental style Irene"], [],
        "Где мои штаны?")
    BackgroundSystem.add("g_v14_10", password_for_10, ["[reward_str_for_10] Student gym suit Uno"], [],
        "Оно слишком короткое. Я даже не могу засунуть его под грудь... ...")
    BackgroundSystem.add("c_v14_20", password_for_20, ["[reward_str_for_20] Pearl princess Theo"], [],
        "Кажется, я потерял несколько жемчужин где-то на земле, ты не хочешь их подобрать?~")
    BackgroundSystem.add("e_v14_20", password_for_20, ["[reward_str_for_20] Goddess Elisa"], [],
        "Это сияние света приведет тебя домой~")


    BackgroundSystem.add("c_v145_10", password_for_10, ["[reward_str_for_10] Bad student Theo"], [],
        "Ложись, доставай свой член. Ты знаешь, что делать~")
    BackgroundSystem.add("b_v145_20", password_for_20, ["[reward_str_for_20] Oriental style Senning"], [],
        "Не... не смотри на меня так~~")

    BackgroundSystem.add("b_v15_10", password_for_10, ["[reward_str_for_10] Senning or Minna"], [],
        "Удивлен? Хм~ Думаю, между мной и мамой не так уж много различий~")
    BackgroundSystem.add("d_v15_10", password_for_10, ["[reward_str_for_10] Neko hoodie Irene"], [],
        "Ня~ ня~ ня~")
    BackgroundSystem.add("e_v15_20", password_for_20, ["[reward_str_for_20] Elisa in the gym"], [],
        "Я действительно не могу тренироваться с такой огромной грудью... ...")
    BackgroundSystem.add("g_v15_20", password_for_20, ["[reward_str_for_20] Piggy Uno"], [],
        "Хрю~ хрю~ Мастер~~ Хочешь погладить свою прелестную розовую свинку?~")


    BackgroundSystem.add("e_v16_10", password_for_10, ["[reward_str_for_10] Full of love Elisa"], [],
        "Хочешь немного прогуляться со мной?")
    BackgroundSystem.add("d_v16_10", password_for_10, ["[reward_str_for_10] Whitecollar Irene"], [],
        "Нет-нет-нет, ты должен слушать все, что тебе говорит Айрин~")
    BackgroundSystem.add("a_v16_20", password_for_20, ["[reward_str_for_20] Pregnant Vera"], [],
        "Наш ребенок... пинает меня")
    BackgroundSystem.add("c_v16_20", password_for_20, ["[reward_str_for_20] Pregnant Theo"], [],
        "Ты уже придумал имя для нашего малыша?")
    BackgroundSystem.add("g_v16_20", password_for_20, ["[reward_str_for_20] Pregnant Uno"], [],
        "Уно становится все пухлее и пухлее~")


    def save_bg_init():
        BackgroundSystem.add_to_shop("a_store_1", None, ["[shop_str] Astrologer suit"], [],
            "Этот костюм... дорогой, не так ли?")
        BackgroundSystem.add_to_shop("b_store_1", None, ["[shop_str] Astrologer suit"], [],
            "Должна ли я носить пару тёмных очков? Это заставит меня выглядеть более убедительной, верно?")
        BackgroundSystem.add_to_shop("c_store_1", None, ["[shop_str] Astrologer suit"], [],
            "Веришь или нет, у тебя будет плохой день~")
        BackgroundSystem.add_to_shop("d_store_1", None, ["[shop_str] Astrologer suit"], [],
            "Айрин - маг~ Могу ли я превратить тебя в овцу или что-то в этом роде?~")
        BackgroundSystem.add_to_shop("e_store_1", None, ["[shop_str] Astrologer suit"], [],
            "Что... что мне теперь говорить? Абракадабра?")
        BackgroundSystem.add_to_shop("f_store_1", None, ["[shop_str] Astrologer suit"], [],
            "Оууу... это действительно не мой стиль... ...")
        BackgroundSystem.add_to_shop("g_store_1", None, ["[shop_str] Astrologer suit"], [],
            "Я чувствую, что теперь могу общаться с природой~")
        
        BackgroundSystem.add_to_shop("a_store_2", None, ["[shop2_str] Cheongsam"], [],
            "Спасибо, что купили это платье для меня. Мне очень нравится~")
        BackgroundSystem.add_to_shop("b_store_2", None, ["[shop2_str] Cheongsam"], [],
            "Желаю вам счастливого Нового года и счастливого Лунного фестиваля!")
        BackgroundSystem.add_to_shop("c_store_2", None, ["[shop2_str] Cheongsam"], [],
            "Я действительно не должна носить такое платье на работе, но... неважно... ...")
        BackgroundSystem.add_to_shop("d_store_2", None, ["[shop2_str] Cheongsam"], [],
            "Я... выгляжу взрослой в этом платье? Как взрослый котёнок, я имела ввиду~")
        BackgroundSystem.add_to_shop("e_store_2", None, ["[shop2_str] Cheongsam"], [],
            "Ах, ципао, его так редко можно увидеть. Я помню, как много лет назад я видел элегантную даму в этом платье на неделе моды.")
        BackgroundSystem.add_to_shop("f_store_2", None, ["[shop2_str] Cheongsam"], [],
            "Я никогда раньше не пробовала такой стиль... Что? Я выгляжу хорошо? Ты... уверен?")
        BackgroundSystem.add_to_shop("g_store_2", None, ["[shop2_str] Cheongsam"], [],
            "Не знаю, но... ...это платье очень подходит к моей косе.")


screen bg_selection():

    zorder 100

    button:
        action Hide("bg_selection", transition=Dissolve(0.3))

    frame:
        align 0.5, 0.5
        xysize 1600, 1080

        has vpgrid:
            cols 3
            mousewheel True
            arrowkeys True
            draggable True
            scrollbars "vertical"

            xysize 1520, 1216
            align 0.5, 0.5
            style_prefix "slot"
            spacing 20

        vbox spacing 10:
            $ thumbnail = BackgroundSystem.get_default_nz_background_thumbnail(findee)
            imagebutton:
                idle thumbnail
                hover thumbnail
                selected_idle thumbnail
                selected_hover thumbnail
                action Function(BackgroundSystem.set_nz_background, nz=findee, bg=None)
            text "Восстановление значений по умолчанию" align 0.5, 0.5

        for bg in BackgroundSystem.get_nz_backgrounds(findee):
            vbox spacing 10:
                if bg.is_unlocked:
                    imagebutton:
                        idle bg.thumbnail
                        hover bg.thumbnail
                        selected_idle bg.thumbnail
                        selected_hover bg.thumbnail
                        action Function(BackgroundSystem.set_nz_background, nz=findee, bg=bg)
                elif bg.password:
                    imagebutton:
                        idle bg.mosaic_thumbnail
                        hover bg.mosaic_thumbnail
                        selected_idle bg.mosaic_thumbnail
                        selected_hover bg.mosaic_thumbnail
                        action ShowTransient("bg_unlocker", bg=bg)
                else:
                    imagebutton:
                        idle bg.darkins_thumbnail
                        hover bg.darkins_thumbnail
                        selected_idle bg.darkins_thumbnail
                        selected_hover bg.darkins_thumbnail
                        action Function(BackgroundSystem.set_nz_background, nz=findee, bg=bg)
                for name in bg.dname:
                    text name align 0.5, 0.5

style bg_unlocker:
    align (0.5, 0.5)
    xsize 400

style bg_unlocker:
    variant "phone"
    align (0.5, 0.1)
    xsize 400

screen bg_unlocker(bg):
    default password = ""
    style_prefix "bg_unlocker"
    zorder 101

    frame:
        align 0.5, 0.5
        xsize 400

        has vbox:
            align 0.5, 0.5
        text "Введите пароль для разблокировки:"

        input:
            style "name_input_input"
            pixel_width 320
            copypaste True
            value ScreenVariableInputValue("password", default=True, returnable=False)

        hbox:
            align 0.5, 0.5
            button:
                style "name_input_button"
                text _("Подтвердить") style "name_input_button_text"
                action Function(bg.unlock_by_password, password=password)
            button:
                style "name_input_button"
                text _("Отмена") style "name_input_button_text"

                action Return()

        textbutton "Найти пароль":
            action OpenURL('https://www.patreon.com/posts/43901371')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
