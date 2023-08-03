label A_daily_2:

    scene cafe_background with tstmgr
    play music happy

    player "Привет, Вера."

    scene a_cafe_weird with tstmgr

    a "... ... ... ..."

    a "Ты снова пришёл."

    player "Что не так?"

    a "В последнее время ты часто заходишь. Это кажется... ненормальным."

    player "Что ты хочешь этим сказать?"

    a "Это заставляет меня задуматься, не преследуешь ли ты меня..."

    player "Конечно, нет. Я прихожу сюда, потому что мне нравится здесь завтракать, и больше ничего."

    narrator "Это ложь, по крайней мере отчасти."

    narrator "Я не могу отрицать, что у меня есть чувства к этой девушке и я стремлюсь улучшить наши взаимоотношения, но я не преследую её. По крайней мере, пока что нет..."

    scene a_cafe_surprise with tstmgr

    a "Неужели?"

    player "Да..."

    scene a_cafe_normal1 with tstmgr

    a "... ... ... ..."

    a "Извини, что побеспокоила тебя таким странным вопросом."

    narrator "Её лицо кажется нормальным, но голос звучит так, будто она расстроена."

    scene a_cafe_smile2 with tstmgr

    a "Что бы ты хотел сегодня заказать?"

    narrator "Возможно, я слишком сильно задумался."

    player "Сэндвич с беконом и ванильный молочный коктейль."

    a "Хорошо, я вернусь через минуту."

    scene cafe_background with tstmgr

    narrator "... ... ... ..."

    stop music fadeout 1.0

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
