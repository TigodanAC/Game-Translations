define guide_text = '''Вам не нужно прохождение, чтобы играть в эту игру. 

Все события в этой игре могут быть легко запущены. Мы не хотим добавлять какие-либо головоломки или сложные триггерные условия, которые могут вас оттолкнуть.

Самый главный способ продвинуть историю — поднять очки любви девочек. Вы можете добиться этого двумя способами:
1. Встретиться с девушками в определенных местах. Например, в будние дни Сеннин можно встретить на занятиях. Вы можете просто нажать на кнопку «пойти на занятия» на панели университета, встретиться с ней там, и тогда её очки любви будут повышены.

2. Запускайте короткие события для девочек, которые будут автоматически отображаться на карте со значком мини-аватаров девочек. Эти события появятся только после пролога.

Всякий раз, когда появляется новый триггерный сюжет и событие, они будет отображаться на карте со значком (красный/оранжевый/мини-аватары).
---------------------------------------------------------------
{size=-4}Если вы застряли в месте, где не можете продолжить игру, используйте кнопку Побег в контекстном меню, чтобы вернуться на карту. (или нажмите E, чтобы открыть меню побега.){/size}'''

screen guide():
    zorder 91

    button:
        action Hide("guide", transition=Dissolve(0.3))

    frame:
        if renpy.variant("small"):
            xfill True yfill True
        else:
            xsize 1200 ysize 900

        xalign .5 yalign .5
        background Solid("#000000e6")
        padding (gui.frame_padding-11, gui.frame_padding-11)

        if not renpy.variant("small"):
            add xbtn(action=Hide("guide", transition=Dissolve(0.3)), xpos=1211, ypos=-9)

        vbox:
            xalign .5 yalign .5
            spacing 10

            if renpy.variant("small"):
                xsize 1600 ysize 900

            else:
                xsize 1000 ysize 670 yoffset 20

            text "{size=+10}{color=#e8888a}Руководство{/color}{/size}"

            text guide_text:
                size 27
                if renpy.variant("small"):
                    size 32
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
