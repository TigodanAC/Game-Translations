label A_dgsjhx:

    scene void with tstmgr

    narrator "... ... ... ..."

    narrator "На следующий день."

    narrator "Утром я снова зашёл в кафе, где работает Вера, чтобы позавтракать."

    narrator "Ну, еда не очень, но, по крайней мере, у меня есть возможность поговорить с Верой."

    narrator "Все эти дни я не мог понять, почему я прихожу увидеться с этой девушкой. Я влюбился в неё? Или я просто чувствую вину за нашу ночь вместе?"

    narrator "Я не знаю. Не могу сказать."

    narrator "... ... ... ..."

    scene cafe_background with tstmgr

    narrator "... ... ... ..."

    a "Что бы ты хотел сегодня заказать?"

    player "Сэндвич с беконом, как обычно, и средний стакан горячего шоколада. Спасибо."

    a "... Сейчас принесу."

    player "Ты не выглядишь счастливой. В чём дело? Это из-за меня?"

    scene a_cafe_surprise with tstmgr

    a "О, нет... Это не имеет к тебе никакого отношения."

    player "Хочешь поговорить об этом?"

    scene a_cafe_weird with tstmgr

    a "... ... ... ..."

    a "Ладно..."

    a "Мне нужны деньги."

    player "Подожди, я уже решил твой жилищный вопрос. На что ещё тебе нужны деньги?"

    a "Моя мама случайно упала и сломала три ребра на прошлой неделе. Ей нужна операция, но она с трудом может себе это позволить."

    a "Так что я должна зарабатывать больше, чтобы поддержать её. Я сейчас ищу ещё одну работу, на котрой я смогла бы работать в ночное время."

    player "Мне очень жаль это слышать, Вера."

    player "Я могу помочь тебе с оплатой операции, если хочешь..."

    a "Нет, я не приму твои деньги."

    player "Тогда как насчёт того, чтобы позволить мне помочь тебе найти эту работу?"

    scene a_cafe_surprise with tstmgr

    a "Серьёзно? Ты знаешь какое-нибудь место?"

    player "Я могу познакомить тебя с владельцем ресторана. Босс - мой друг. Я уверен, что он будет счастлив, если такая красавица, как ты, будет работать на него."

    scene a_cafe_weird with tstmgr

    a "Я не уверена..."

    player "Это высококлассный ресторан с постоянным менеджментом. Там ты будешь в безопасности. Кроме того, могу тебя заверить, что уровень зарплаты там выше среднего."

    player "Я думаю, тебе стоит попробовать."

    scene a_cafe_normal1 with tstmgr

    a "... ... ... ..."

    scene a_cafe_smile2 with tstmgr

    a "Звучит неплохо. Я подумаю об этом сегодня вечером. Спасибо, спасибо за твою помощь. Я у тебя в долгу."

    player "Не стоит благодарности. Я просто делаю то, что должен делать друг."

    scene a_cafe_surprise with tstmgr

    a "Мы... друзья?"

    player "А разве нет?"

    scene a_cafe_weird with tstmgr

    a "Я не знаю..."

    a "... ... ... ..."

    player "О... ..."

    scene a_cafe_smile2 with tstmgr

    a "В любом случае, спасибо тебе. Теперь позволь мне сделать твой заказ. Ты, должно быть, уже проголодался."

    player "Всё в порядке, не торопись. Не надо спешить."

    jump event_post
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
