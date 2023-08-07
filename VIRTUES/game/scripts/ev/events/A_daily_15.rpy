label A_daily_15:


    scene void with tstmgr

    play music happy

    if seen("G_love_1"):
        jump A_daily_15.line_c
    else:
        jump A_daily_15.line_d

    jump event_post

label A_daily_15.end:

    stop music fadeout 1.0

    jump event_post

label A_daily_15.line_c:

    "*Следующий сюжет с точки зрения Веры*"



    scene a_daily15_1 with dissolve

    g "Доброе утро, Вера... ..."



    scene a_daily15_2 with tstmgr

    a "О, привет, Уно~ Почему ты сегодня так рано проснулась?"



    scene a_daily15_3 with tstmgr

    g "*Зевая* Ах... ... хх... ...ххх... ..."



    scene a_daily15_4 with tstmgr

    g "Я только что встала, чтобы пописать... ... Пойду... и сразу же вернусь в свою постель."



    a "О, ты хочешь что-нибудь на завтрак?"



    scene a_daily15_5 with tstmgr

    g "Нет, я в порядке, мамочка, спасибо, что спросила~"



    scene a_daily15_6 with tstmgr

    a "Мамочка... ...я не настолько старая!~"



    g "Хи хи~~~"



    g "Я уверена, что после рождения ребёнка ты будешь отличной мамой~"



    scene a_daily15_7 with tstmgr

    a "... ребёнка... ..."



    g "Как можно так рано вставать каждый день и при этом быть полным энергии? Жизнь так несправедлива~"



    g "Увидимся сегодня вечером, хорошего дня~"



    scene a_daily15_8 with tstmgr

    a "Приятных снов~"



    "Уно вышла из гостиной и снова заснула."



    scene a_daily15_9 with tstmgr

    a "... ... ... ..."



    scene a_daily15_10 with tstmgr

    a "(Хммм~ Пора будить [P]~)"



    scene a_daily15_11 with tstmgr

    a "... ... ... ..."



    scene a_daily15_12 with tstmgr

    a "(Подожди секунду... ... я чувствую... ...)"



    scene a_daily15_13 with tstmgr

    a "(Фуууууу... ... Я... меня, кажется, вырвет... ...)"



    scene void with tstmgr

    "Вера побежала в туалет со всех ног и даже забыла выключить газовую плиту..."



    "... ... ... ..."





    "10 минут спустя... ..."



    scene a_daily15_14 with dissolve

    a "*Выходя из туалета* Ах... ...Это странно, такого раньше не было."



    scene a_daily15_15 with tstmgr

    a "У меня проблемы с желудком?"



    a "Или... ... ... ..."



    a "Было ли это на самом деле утренней тошнотой?"



    scene a_daily15_16 with tstmgr

    a "Кроме того, у меня... в этом месяце не было месячных."



    a "Я... беременна?"



    scene a_daily15_5 with flashback

    g "Я уверена, что после рождения ребёнка ты будешь отличной мамой~"



    scene a_daily15_16 with flashback

    a "О, Боже... ... ... ..."



    scene a_daily15_17 with tstmgr

    a "Я действительно стану мамой?"



    scene void with tstmgr

    "... ... ... ..."

    jump A_daily_15.end

label A_daily_15.line_d:

    "*Следующий сюжет с точки зрения Веры*"



    scene a_daily15_1 with dissolve

    "Гостья в отеле" "Доброе утро, Вера... ..."



    scene a_daily15_2 with tstmgr

    a "О, здравствуйте, миссис Смит~ Завтрак почти готов~"



    "Гостья в отеле" "Ах, мне бы очень хотелось позавтракать, но я сейчас иду на собеседование, так что... ..."



    scene a_daily15_8 with tstmgr

    a "Всё в порядке~ Удачи на собеседовании. У Вас всё получится!"



    "Гостья в отеле" "Я постараюсь, спасибо..."



    "Гостья в отеле" "... ... ... ..."



    "Гостья в отеле" "Хотела бы я иметь такую ​​маму, как Вы... ..."



    scene a_daily15_6 with tstmgr

    a "Хм?"



    "Гостья в отеле" "О, я имею в виду... Вы такая добрая женщина, я здесь всего несколько дней, но Вы уже дали мне почувствовать, что обо мне заботятся, как в семье... ..."



    "Гостья в отеле" "Я уверена, что после рождения ребёнка Вы будете отличной мамой~"



    scene a_daily15_7 with tstmgr

    a "... ребёнка... ..."



    "Гостья в отеле" "В любом случае, увидимся вечером, Вера, хорошего дня~"



    scene a_daily15_8 with tstmgr

    a "И Вам, миссис Смит~"



    "Затем гостья вышла из дома на собеседование... ..."



    scene a_daily15_9 with tstmgr

    a "... ... ... ..."



    scene a_daily15_10 with tstmgr

    a "(Хммм~ Пора будить [P]~)"



    scene a_daily15_11 with tstmgr

    a "... ... ... ..."



    scene a_daily15_12 with tstmgr

    a "(Подожди секунду... ... я чувствую... ...)"



    scene a_daily15_13 with tstmgr

    a "(Фуууууу... ... Я... меня, кажется, вырвет... ...)"



    scene void with tstmgr

    "Вера побежала в туалет со всех ног и даже забыла выключить газовую плиту..."



    "... ... ... ..."



    "10 минут спустя... ..."



    scene a_daily15_14 with dissolve

    a "*Выходя из туалета* Ах... ...Это странно, такого раньше не было."



    scene a_daily15_15 with tstmgr

    a "У меня проблемы с желудком?"



    a "Или... ... ... ..."



    a "Было ли это на самом деле утренней тошнотой?"



    scene a_daily15_16 with tstmgr

    a "Кроме того, у меня... в этом месяце не было месячных."



    a "Я... беременна?"



    scene a_daily15_6 with flashback

    "Гостья в отеле" "Я уверена, что после рождения ребёнка Вы будете отличной мамой~"



    scene a_daily15_16 with flashback

    a "О, Боже... ... ... ..."



    scene a_daily15_17 with tstmgr

    a "Я действительно стану мамой?"



    scene void with tstmgr

    "... ... ... ..."

    jump A_daily_15.end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
