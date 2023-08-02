init -1 python:

    if config.developer:
        config.overlay_screens.append("debug")
    config.overlay_screens.append("push")

    config.overlay_screens.append("quick_menu")

    config.overlay_screens.extend(("map_panel", "right_panel", "clock3", "top", "nz_panel"))








    config.layers = [ 'master', 'transient', 'screens', "windows", 'overlay' ]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
