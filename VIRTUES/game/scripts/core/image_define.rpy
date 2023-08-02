init python:
    for file in renpy.list_files():
        imagename = os.path.basename(file).split(".")[0]
        if file.endswith(('.webm', '.mkv', '.mov', '.mp4')):
            renpy.image(imagename, Movie(play=file, loop=True, start_image='{}_start'.format(imagename)))

image icon_bot = "gui/icons/icon_bot.png"
image icon_top = "gui/icons/icon_top.png"
image A_icon = "gui/icons/A_icon.png"
image B_icon = "gui/icons/B_icon.png"
image C_icon = "gui/icons/C_icon.png"
image D_icon = "gui/icons/D_icon.png"
image E_icon = "gui/icons/E_icon.png"
image F_icon = "gui/icons/F_icon.png"
image G_icon = "gui/icons/G_icon.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
