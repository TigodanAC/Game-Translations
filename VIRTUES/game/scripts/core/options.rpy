






$ renpy.set_autoreload(False)








define config.name = _("V.I.R.T.U.E.S.")




define gui.show_name = True




define build.name = "virtues"

define config.hw_video = True





define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = "music/virtues_mainmenu_v05.ogg"








define config.enter_transition = Dissolve(.3)
define config.exit_transition = Dissolve(.3)




define config.intra_transition = Dissolve(.3)




define config.after_load_transition = Dissolve(.3)




define config.end_game_transition = dissolve



define config.enter_yesno_transition = Dissolve(0.2)
define config.exit_yesno_transition = Dissolve(0.2)


define config.game_main_transition = Dissolve(0.3)

define config.main_game_transition = Dissolve(0.3)


define config.enter_replay_transition = Pixellate(0.5, 6)

define config.exit_replay_transition = Pixellate(0.5, 6)


define config.end_splash_transition = None














define config.window = "hide"




define config.window_show_transition = CropMove(0.3, "wipeup")
define config.window_hide_transition = CropMove(0.3, "wipedown")






default preferences.text_cps = 0




default preferences.afm_time = 15














define config.save_directory = "virtues-1554812312"






define config.window_icon = "gui/window_icon.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
