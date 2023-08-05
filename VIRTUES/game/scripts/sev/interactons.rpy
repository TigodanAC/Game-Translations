label A_PreInteraction:



    return True

label B_PreInteraction:
    return True

label C_PreInteraction:
    return True

label D_PreInteraction:
    return True

label E_PreInteraction:
    return True

label F_PreInteraction:
    return True

label G_PreInteraction:
    return True

label TouchHead_A_general:

    scene a_general_1_frown with tstmgr

    bubble_a "Почему ты хочешь это сделать?"

    bubble_b "Но ладно... ..."

    scene a_touchead_night_1 with tstmgr

    a "... ... ... ..."

    a "Эх... Такое ощущение... зудит..."

    scene a_touchead_night_2 with tstmgr

    a "Подожди... Ты слишком близко ко мне."

    a "Это становится странным..."

    scene a_touchead_night_3 with tstmgr

    a "Остановись..."

    a "(Слегка постанывая) Ах... нет..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label TouchHead_A_girlfriend:

    scene a_gf_1_default with tstmgr

    bubble_a "Дотронуться до моей головы?"

    bubble_a "Конечно... любимый."

    scene a_gf_1_touchead_1 with tstmgr

    a "Никто еще не был так добр ко мне."

    a "Я так счастлива... ..."

    scene a_gf_1_touchead_2 with tstmgr

    a "Спасибо... за то, что ты со мной."

    a "... ... ... ..."

    scene a_gf_1_touchead_3 with tstmgr

    a "Знаешь... ты можешь сделать что-то большее, если захочешь."

    a "Я твоя..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label TouchHead_A_sexpartner:

    scene a_gf_1_default with tstmgr

    bubble_a "Дотронуться до моей головы?"

    bubble_a "Конечно, [P]."

    scene a_gf_1_touchead_1 with tstmgr

    a "Мы как любовники... ..."

    a "Я просто говорю... не думай слишком много..."

    scene a_gf_1_touchead_2 with tstmgr

    a "Спасибо... за то, что ты со мной."

    a "... ... ... ..."

    scene a_gf_1_touchead_3 with tstmgr

    a "Знаешь... ты можешь сделать что-то большее, если захочешь."

    a "Я не сбегу..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label Hug_A_general:

    scene a_general_1_frown with tstmgr

    bubble_a "Ты думаешь, что это действительно необходимо?"

    bubble_a "... ... ... ..."

    scene a_general_1_hug_1 with tstmgr

    a "Я знаю, ты делаешь это, чтобы утешить меня."

    a "Спасибо... ..."

    scene a_general_1_hug_2 with tstmgr

    a "Твоё плечо... оно заставляет меня чувствовать себя в безопасности."

    a "Так тепло..."

    scene a_general_1_hug_3 with tstmgr

    a "... ... ... ..."

    a "Почему ты так мил со мной?"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label Hug_A_girlfriend:

    scene a_gf_1_default with tstmgr

    bubble_a "Давай сделаем это."

    bubble_a "Я хочу снова оказаться в твоих руках..."

    scene a_gf_1_hug_1 with tstmgr

    a "Не улыбайся так..."

    a "Это немного... смущает."

    scene a_gf_1_hug_2 with tstmgr

    a "(Стонет от удовольствия) Ах... ... [P]... ..."

    a "Постарайся... не оставить засос на моей шее.."

    scene a_gf_1_hug_3 with tstmgr

    a "Я люблю, когда ты такой агрессивный..."

    a "(Стонет от удовольствия) Аххх... ..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label Hug_A_sexpartner:

    scene a_gf_1_default with tstmgr

    bubble_a "Если ты так говоришь..."

    bubble_a "Я счастлива сделать это."

    scene a_gf_1_hug_1 with tstmgr

    a "Не улыбайся так..."

    a "Это немного... смущает."

    scene a_gf_1_hug_2 with tstmgr

    a "(Стонет от удовольствия) Ах... ... [P]... ..."

    a "Да... я хочу больше..."

    scene a_gf_1_hug_3 with tstmgr

    a "Тебе нравится трогать мою задницу?..."

    a "(Стонет от удовольствия) Аххх... ..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label Doggie_A_girlfriend:

    scene a_gf_1_default with tstmgr

    bubble_a "Да... Я хочу попробовать это... тоже."

    bubble_a "Любимый... ..."

    scene void with tstmgr

    "... ... ... ..."

    window hide

    scene a_love_5_26 with tstmgr

    pause

    scene a_love_5_28 with tstmgr

    pause

    scene a_love_5_27 with tstmgr

    pause

    scene a_love_5_30 with tstmgr

    a "Я кончаююю~~~~~~"

    $ flashlight()

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label Doggie_A_sexpartner:

    scene a_gf_1_frown with tstmgr

    bubble_a "Хорошо... ..."

    bubble_a "Если это то, что ты хочешь."

    scene void with tstmgr

    "... ... ... ..."

    window hide

    scene a_love_5_25 with tstmgr

    pause

    scene a_love_5_28 with tstmgr

    pause

    scene a_love_5_27 with tstmgr

    pause

    scene a_love_5_30 with tstmgr

    a "Я кончаю~~~~~~"

    $ flashlight()

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post

label TouchHead_B_general:

    if B.clothes == 1:
        scene b_general_1_frown with tstmgr
    elif B.clothes == 2:
        scene b_general_2_frown with tstmgr

    bubble_b "Дотронуться... до моей головы?"
    bubble_b "Хм... ... хорошо..."

    if B.clothes == 1:
        scene b_touchead_day_1 with tstmgr
    elif B.clothes == 2:
        scene b_general_2_touchead_1 with tstmgr
    b "... ... ... ..."
    b "Тебе нравится это делать?"

    if B.clothes == 1:
        scene b_touchead_day_2 with tstmgr
    elif B.clothes == 2:
        scene b_general_2_touchead_2 with tstmgr
    b "Твоя рука такая большая..."
    b "... ... ... ..."

    if B.clothes == 1:
        scene b_touchead_day_3 with tstmgr
    elif B.clothes == 2:
        scene b_general_2_touchead_3 with tstmgr
    b "И это так приятно..."
    b "На самом деле мне это начинает нравиться..."

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label ShouderRub_C_general:

    scene c_general_1_smile with tstmgr

    bubble_c "... ... ... ..."
    bubble_c "Это мило."
    bubble_c "Ты пытаешься доставить мне удовольствие? Я не буду повышать тебе зарплату за это, просто даю знать."
    bubble_c "Я подожду тебя на диване."

    scene c_sdmassage_1 with tstmgr

    c "... ... ... ..."

    c "... ... ... ... ... ..."

    scene c_sdmassage_2 with tstmgr

    c "Хмм... ..."

    scene c_sdmassage_3 with tstmgr

    c "?... ..."

    c "(Он снова это делает... Я должна была это понять.)"

    c "... ... ... ..."

    scene c_sdmassage_2 with tstmgr

    c "(Неважно... лишь бы он не зашел слишком далеко...)"

    c "... ... ... ..."

    scene void with tstmgr

    "... ... ... ..."
    jump interaction_post


label TouchHead_D_general:

    if D.clothes == 1:
        scene d_general_1_default with tstmgr
    elif D.clothes == 2:
        scene d_general_2_default with tstmgr
    bubble_d "Ха? Прикосновение к голове?"
    bubble_d "Отлично! Давай сделаем это."

    if D.clothes == 1:
        scene d_touchead_1 with tstmgr
    elif D.clothes == 2:
        scene d_general_2_touchead_1 with tstmgr
    d "... ... ... ..."
    d "Это приятно..."

    if D.clothes == 1:
        scene d_touchead_2 with tstmgr
    elif D.clothes == 2:
        scene d_general_2_touchead_2 with tstmgr
    d "Это как будто... меня гладят."
    d "Так расслабляет..."

    if D.clothes == 1:
        scene d_touchead_3 with tstmgr
    elif D.clothes == 2:
        scene d_general_2_touchead_3 with tstmgr
    d "Мяу, Мяу!"
    d "Тебе нравится слышать, как я мяукаю?"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label LapPillow_E_general:

    if E.clothes == 1:
        scene e_general_1_frown with tstmgr
    elif E.clothes == 2:
        scene e_general_2_frown with tstmgr
    bubble_e "Ты хочешь... сделать это снова?"
    bubble_e "(Этот бедный ребенок ищет материнской любви. Я должна помочь ему.)"
    bubble_e "... ... ... ..."
    bubble_e "Ладно, сынок, иди сюда."

    if E.clothes == 1:
        scene e_lapillow_1 with tstmgr
    elif E.clothes == 2:
        scene e_general_2_lapillow_1 with tstmgr
    e "Спи, спи, дитя..."
    e "Я с тобой..."

    if E.clothes == 1:
        scene e_lapillow_2 with tstmgr
    elif E.clothes == 2:
        scene e_general_2_lapillow_2 with tstmgr
    e "(Ох, его спящее лицо такое милое.)"
    e "(Я всегда хотела иметь собственного сына...)"

    if E.clothes == 1:
        scene e_lapillow_3 with tstmgr
    elif E.clothes == 2:
        scene e_general_2_lapillow_3 with tstmgr
    e "(Ему, должно быть, сейчас сниться отличный сон...)"
    e "(Я хочу знать, о чём его сон...)"

    scene void with tstmgr

    "... ... ... ..."

    jump interaction_post


label TouchBreasts_G_general:

    if G.clothes == 1:
        scene g_general_1_smile with tstmgr
    elif G.clothes == 2:
        scene g_general_2_smile with tstmgr

    bubble_g "Не торопись, 30 секунд."

    if G.clothes == 1:

        scene g_general_1_breastouch_1 with tstmgr

        g "Просто помни, что нельзя делать ничего... странного."

        g "... ... ... ..."

        scene g_general_1_breastouch_2 with tstmgr

        g "Будь... нежнее, пожалуйста."

        g "Не оставляй синяков. На следующей неделе у меня косплей."

        scene g_general_1_breastouch_3 with tstmgr

        g "Хмм?... ..."

        g "Тебе действительно нужно снимать с меня лифчик?"

        scene g_general_1_breastouch_4 with tstmgr

        g "... ... ... ..."

        g "Они... уродливые, да? В такой позе... Хотела бы я, чтобы они были поменьше."

        scene g_general_1_breastouch_5 with tstmgr

        g "Действительно? Они тебе нравятся?"

        g "Ну... тогда... сегодня у тебя есть ещё 5 дополнительных секунд."

        scene void with tstmgr

        "... ... ... ..."

    elif G.clothes == 2:

        scene g_general_2_breastouch_1 with tstmgr

        g "Просто помни, что нельзя делать ничего... странного."

        g "... ... ... ..."

        scene g_general_2_breastouch_2 with tstmgr

        g "Будь... нежнее, пожалуйста."

        g "Не оставляй синяков. На следующей неделе у меня косплей."

        scene g_general_2_breastouch_3 with tstmgr

        g "Почему ты... держишь их, как свои игрушки?"

        g "Они тяжелые, не так ли?"

        scene g_general_2_breastouch_4 with tstmgr

        g "(Стонет от удовольствия) Ауу... ... ... ..."

        g "Сосок..."

        scene g_general_2_breastouch_5 with tstmgr

        g "(Стонет) Это чувство... странное..."

        g "(Стонет) Твоё... время... закончилось..."

        g "Отпусти меня..."

        scene void with tstmgr

        "... ... ... ..."

    jump interaction_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
