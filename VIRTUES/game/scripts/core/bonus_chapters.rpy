screen bonus_chapters():








    fixed:
        use game_menu(_("Bonus Chapters"))

    style_prefix "about" tag menu

    vbox:
        ypos 240 ysize 730
        xsize 1600 xalign 0.5
        spacing 8
        null height 20
        hbox:
            spacing 32

            hbox:
                spacing 16
                button:
                    add "bonus1_thumbnail"
                    action OpenURL('https://www.patreon.com/posts/32612707')
                text "{a=https://www.patreon.com/posts/32612707}Bonus Chapter 1{/a}" yalign 0.5
            hbox:
                spacing 16
                button:
                    add "bonus3_thumbnail"
                    action OpenURL('https://www.patreon.com/posts/40351525')
                text "{a=https://www.patreon.com/posts/40351525}Bonus Chapter 3{/a}" yalign 0.5

        hbox:
            spacing 16
            button:
                add "bonus2_thumbnail"
                action OpenURL('https://www.patreon.com/posts/35693091')
            text "{a=https://www.patreon.com/posts/35693091}Bonus Chapter 2{/a}" yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
