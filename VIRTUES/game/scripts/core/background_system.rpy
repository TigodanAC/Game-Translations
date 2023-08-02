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
                Push("Background unlocked.")
                return True
            else:
                Push("Wrong password.")
                return False
        
        def __repr__(self):
            return "Background(" + self.name + ")"

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
                    Push("You can unlock this picture at Posia's or Minna's store.")
                else:
                    Push("You can unlock this picture after advancing more of her story.")
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
    reward_str_for_10 = "{color=#dd6574}{size=-3}$10 Reward{/size}{/color}"
    reward_str_for_20 = "{color=#f4cc6c}{size=-3}$20 Reward{/size}{/color}"
    shop_str = "{color=#a186be}{size=-3}Posia's Shop{/size}{/color}"
    shop2_str = "{color=#a186be}{size=-3}Minna's Shop{/size}{/color}"

    BackgroundSystem.add("b_v7_10", password_for_10, ["[reward_str_for_10] Young Senning"], [],
        "It's... nice... to... see you, [P].")
    BackgroundSystem.add("c_v7_10", password_for_10, ["[reward_str_for_10] Young Theo"], [],
        "You didn't forget what you have promised to me, did you?")
    BackgroundSystem.add("c_v7_20", password_for_20, ["[reward_str_for_20] Gift Suit"], [],
        "I'm no one's gift, but... ... whatever~")
    BackgroundSystem.add("d_v7_20", password_for_20, ["[reward_str_for_20] Gift Suit"], [],
        "Surprise!~ Irene is the gift for you!~")
    BackgroundSystem.add("a_normal_1", None, ["Maid Suit"], ["A_daily_10"],
        "I am your exclusive maid, hah~~")
    BackgroundSystem.add("b_normal_1", None, ["Yellow Shirt"], [],
        "Thanks for coming by, [P]..."),
    BackgroundSystem.add("b_normal_2", None, ["Lady in Black"], ["B_train_sha_1"],
        "Do you prefer me to dress like this?")
    BackgroundSystem.add("c_normal_1", None, ["White Dress"], ["C_love_5"],
        "Take a seat~")
    BackgroundSystem.add("d_normal_1", None, ["Student Uniform"], [],
        "Irene is a good student~ Irene is a good student~~"),
    BackgroundSystem.add("d_normal_2", None, ["Cat Uniform"], ["D_love_6"],
        "Meow~~ Meow~~ Meow meow meow~~~")
    BackgroundSystem.add("g_normal_1", None, ["Coser Dress"], [],
        "Hi, my landlord sir~")

    BackgroundSystem.add("d_v8_10", password_for_10, ["[reward_str_for_10] Mature Irene"], [],
        "Ah!~ Long time no see, Oniichan~")
    BackgroundSystem.add("e_v8_10", password_for_10, ["[reward_str_for_10] Young Elisa"], [],
        "Why can't it just... stop leaking out?")
    BackgroundSystem.add("e_v8_20", password_for_20, ["[reward_str_for_20] Gift suit"], [],
        "Be careful, master, this gift is fragile~")
    BackgroundSystem.add("a_v8_20", password_for_20, ["[reward_str_for_20] Dark Elf Vera"], [],
        "This lake... has been corrupted by human's scent... ...")
    BackgroundSystem.add("c_v8_20", password_for_20, ["[reward_str_for_20] Warrior Theo"], [],
        "Can I restore peace to this land one day?")

    BackgroundSystem.add("b_normal_3", None, ["That's my shirt!"], ["B_love_6"],
        "I... I will give this shirt back to you tomorrow, so... ...")
    BackgroundSystem.add("g_normal_2", None, ["Nightgown"], ["G_love_6"],
        "This dress... just keeps falling off from my shoulders...")
    BackgroundSystem.add("d_v9_10", password_for_10, ["[reward_str_for_10] Vampire Princess Irene"], [],
        "Trick or treat!~~ Irene doesn't need candies, Irene needs your blood, or other fluids from your body~")
    BackgroundSystem.add("d_v9_20", password_for_20, ["[reward_str_for_20] Cat Ninja Irene"], [],
        "Meow meow~ Take this sword!~")
    BackgroundSystem.add("f_v9_10", password_for_10, ["[reward_str_for_10] Foreign Princess Rachel"], [],
        "Welcome to my realm, Traveler~")
    BackgroundSystem.add("g_v9_20", password_for_20, ["[reward_str_for_20] Cat Ninja Uno"], [],
        "Are you sure... this is part of my training? Meow... ...")


    BackgroundSystem.add("b_v10_10", password_for_10, ["[reward_str_for_10] Mature Senning"], [],
        "We... finally meet again... ...")
    BackgroundSystem.add("g_v10_10", password_for_10, ["[reward_str_for_10] Bikini fighter"], [],
        "Can you take a picture for me, please?~~")
    BackgroundSystem.add("a_v10_20", password_for_20, ["[reward_str_for_20] Wild west"], [],
        "Come on, immersing yourself in the wild with me~")
    BackgroundSystem.add("e_v10_20", password_for_20, ["[reward_str_for_20] Wild west"], [],
        "Keep up, cowboy. The sun is about to set~")


    BackgroundSystem.add("c_v11_10", password_for_10, ["[reward_str_for_10] Maid Suit Theodora"], [],
        "Don't bother me yet, I still have works to do...")
    BackgroundSystem.add("d_v11_10", password_for_10, ["[reward_str_for_10] Maid Suit Irene"], [],
        "Where did Irene put the mop at?... ...")
    BackgroundSystem.add("e_v11_20", password_for_20, ["[reward_str_for_20] Queen Elisa"], [],
        "Welcome back, my king~")
    BackgroundSystem.add("g_v11_20", password_for_20, ["[reward_str_for_20] Captured Cop Uno"], [],
        "Wuuuuuummmmmmmmmmm~~~~~~~~")


    BackgroundSystem.add("b_v12_20", password_for_20, ["[reward_str_for_20] Practicing Nurse"], [],
        "Please... just bite my nipple if I hurt you with the injection... ...")
    BackgroundSystem.add("f_v12_20", password_for_20, ["[reward_str_for_20] Captain Rachel"], [],
        "Hmmmmmmm... ... But first I have to build my own ship~")
    BackgroundSystem.add("a_v12_10", password_for_10, ["[reward_str_for_10] Horny Maid Vera"], [],
        "I was... just about to clean the bathroom, my master...")
    BackgroundSystem.add("g_v12_10", password_for_10, ["[reward_str_for_10] Miko Uno"], [],
        "I'm going to wash myself now, stop watching!~")


    BackgroundSystem.add("a_v13_10", password_for_10, ["[reward_str_for_10] Bikini Fighter Vera"], [],
        "Is there... anything I can help? I can fight~")
    BackgroundSystem.add("e_v13_10", password_for_10, ["[reward_str_for_10] Elisa Naked In Apron"], [],
        "Do you want to have some milk cake?")
    BackgroundSystem.add("c_v13_20", password_for_20, ["[reward_str_for_20] Wedding Dress"], [],
        "Now you have me... my body, my heart, my everything~")
    BackgroundSystem.add("b_v13_20", password_for_20, ["[reward_str_for_20] Bunny Girl Senning"], [],
        "I am here... to serve you~")


    BackgroundSystem.add("f_v135_10", password_for_10, ["[reward_str_for_10] Swimsuit Rachel"], [],
        "I'm just... trying to be more... feminine.")
    BackgroundSystem.add("d_v135_20", password_for_20, ["[reward_str_for_20] Little Mage Irene"], [],
        "Awww~ This hat is too heavy... ...")

    BackgroundSystem.add("d_v14_10", password_for_10, ["[reward_str_for_10] Oriental style Irene"], [],
        "Where are my pants?")
    BackgroundSystem.add("g_v14_10", password_for_10, ["[reward_str_for_10] Student gym suit Uno"], [],
        "It is too short. I can't even pull it under my breasts... ...")
    BackgroundSystem.add("c_v14_20", password_for_20, ["[reward_str_for_20] Pearl princess Theo"], [],
        "I think I lost several pearls on the ground, would you like to pick them up?~")
    BackgroundSystem.add("e_v14_20", password_for_20, ["[reward_str_for_20] Goddess Elisa"], [],
        "This glow of light will lead you the way home~")


    BackgroundSystem.add("c_v145_10", password_for_10, ["[reward_str_for_10] Bad student Theo"], [],
        "Lie yourself down, show your cock out, you know what to do~")
    BackgroundSystem.add("b_v145_20", password_for_20, ["[reward_str_for_20] Oriental style Senning"], [],
        "Don't... don't stare at me like that~~")

    BackgroundSystem.add("b_v15_10", password_for_10, ["[reward_str_for_10] Senning or Minna"], [],
        "Surprised? Humph~ Guess there aren't too many differences between me and mama~")
    BackgroundSystem.add("d_v15_10", password_for_10, ["[reward_str_for_10] Neko hoodie Irene"], [],
        "Nya~ nya~ nya~")
    BackgroundSystem.add("e_v15_20", password_for_20, ["[reward_str_for_20] Elisa in the gym"], [],
        "I really can't work out with these huge breasts... ...")
    BackgroundSystem.add("g_v15_20", password_for_20, ["[reward_str_for_20] Piggy Uno"], [],
        "Oink~ oink~ Master~~ Do you want to caress your lovely pink piggy?~")


    BackgroundSystem.add("e_v16_10", password_for_10, ["[reward_str_for_10] Full of love Elisa"], [],
        "Would you like to walk with me for a while?")
    BackgroundSystem.add("d_v16_10", password_for_10, ["[reward_str_for_10] Whitecollar Irene"], [],
        "No no no, you have to listen to everything Irene tells you~")
    BackgroundSystem.add("a_v16_20", password_for_20, ["[reward_str_for_20] Pregnant Vera"], [],
        "Our baby... is kicking me")
    BackgroundSystem.add("c_v16_20", password_for_20, ["[reward_str_for_20] Pregnant Theo"], [],
        "Have you thought about our baby's name?")
    BackgroundSystem.add("g_v16_20", password_for_20, ["[reward_str_for_20] Pregnant Uno"], [],
        "Uno is getting chubbier and chubbier~")


    def save_bg_init():
        BackgroundSystem.add_to_shop("a_store_1", None, ["[shop_str] Astrologer suit"], [],
            "This suit... is expensive, isn't it?")
        BackgroundSystem.add_to_shop("b_store_1", None, ["[shop_str] Astrologer suit"], [],
            "Should I wear a pair of dark glasses? That will make me look more convincing, right?")
        BackgroundSystem.add_to_shop("c_store_1", None, ["[shop_str] Astrologer suit"], [],
            "Believe it or not, you are going to have a bad day~")
        BackgroundSystem.add_to_shop("d_store_1", None, ["[shop_str] Astrologer suit"], [],
            "Irene is a mage~ Can I turn you into a sheep or something?~")
        BackgroundSystem.add_to_shop("e_store_1", None, ["[shop_str] Astrologer suit"], [],
            "What... what should I say now? Abracadabra?")
        BackgroundSystem.add_to_shop("f_store_1", None, ["[shop_str] Astrologer suit"], [],
            "Awwww... this is really not my style... ...")
        BackgroundSystem.add_to_shop("g_store_1", None, ["[shop_str] Astrologer suit"], [],
            "I feel like I can communicate with the nature now~")
        
        BackgroundSystem.add_to_shop("a_store_2", None, ["[shop2_str] Cheongsam"], [],
            "Thanks for buying this dress for me. I like it very much~")
        BackgroundSystem.add_to_shop("b_store_2", None, ["[shop2_str] Cheongsam"], [],
            "I wish you a happy new year and a happy Lunar Festival!")
        BackgroundSystem.add_to_shop("c_store_2", None, ["[shop2_str] Cheongsam"], [],
            "I really shouldn't wear a dress like this at work, but... whatever... ...")
        BackgroundSystem.add_to_shop("d_store_2", None, ["[shop2_str] Cheongsam"], [],
            "Do I... look mature with this dress? I mean, a mature kitty~")
        BackgroundSystem.add_to_shop("e_store_2", None, ["[shop2_str] Cheongsam"], [],
            "Ah, a cheongsam, so rare to see. I remember I once saw an elegant lady wearing this during a fashion week many years ago.")
        BackgroundSystem.add_to_shop("f_store_2", None, ["[shop2_str] Cheongsam"], [],
            "I have never tried such a style before... What? I look good? Are you... sure?")
        BackgroundSystem.add_to_shop("g_store_2", None, ["[shop2_str] Cheongsam"], [],
            "I don't know, but... ... this dress really suits my braid.")


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
            text "Reset to default" align 0.5, 0.5

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
        text "Input password to unlock:"

        input:
            style "name_input_input"
            pixel_width 320
            copypaste True
            value ScreenVariableInputValue("password", default=True, returnable=False)

        hbox:
            align 0.5, 0.5
            button:
                style "name_input_button"
                text _("Confirm") style "name_input_button_text"
                action Function(bg.unlock_by_password, password=password)
            button:
                style "name_input_button"
                text _("Cancel") style "name_input_button_text"

                action Return()

        textbutton "Look for password":
            action OpenURL('https://www.patreon.com/posts/43901371')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
