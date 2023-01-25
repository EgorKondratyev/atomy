# Базовый набор команд и предложений в боте. Если в процессе работы были изменены предложения/команды, то базовые
# предложения будут игнорироваться.

# type_sentence - Тип предложения
# sentence - базовое предложение (текст)
# language - язык текущего предложения (True - RUS, False - EN)

sentences = [
    #####################################START########################################################################
    {
        'type_sentence': 'start',
        'sentence': '✅ Наш бот - ваш гид по вопросу сотрудничества с компанией Atomy.',
        'language': True
    },
    {
        'type_sentence': 'start',
        'sentence': '✅ Our bot is your guide on cooperation with Atomy.',
        'language': False
    },
    #####################################Девиз и ценности############################################################
    {
        # Перевод кнопки девиза
        'type_sentence': 'button_slogan',
        'sentence': '✅ Девиз и ценности компании Atomy',
        'language': True
    },
    {
        # Перевод кнопки девиза
        'type_sentence': 'button_slogan',
        'sentence': "✅ Atomy's motto and values",
        'language': False
    },
    {
        # Девиз
        'type_sentence': 'slogan',
        'sentence': 'В компании Atomy развита стратегия Masstige - массовость и престиж.\n\n'
                    'Девиз Atomy: "Абсолютное качество - абсолютная цена!"\n\n'
                    'Мы используем глобальные ресурсы для глобальных продаж и постоянно расширяем свою линейку.\n\n'
                    '🔸Приверженность принципам\n'
                    'Atomy соблюдает основополагающие столпы структурного бизнеса и всегда держит сказанное слово.\n\n'
                    '🔸Культура совместного роста\n'
                    'Аtomy помогает фирмам-партнёрам производить лучшее.\n\n'
                    '🔸Взаимопомощь всех консультантов.\n\n'
                    '🔸Значительная важность придаётся достижению успеха каждым участником.\n\n'
                    '🔶«Огромный потенциал – это та компания, сотрудники и клиенты которой счастливы, успешны, '
                    'которая вносит большой вклад в общество.» - Пак Хан Гиль, председатель Atomy.',
        'language': True
    },
    {
        # Девиз
        'type_sentence': 'slogan',
        'sentence': 'Atomy has developed the Masstige strategy - mass and prestige.\n\n'
                    'Atomys motto is "Absolute quality - absolute price!"\n\n'
                    'We use global resources for global sales and are constantly expanding our product line.\n\n'
                    '🔸Adherence to principles\n'
                    'Atomy upholds the fundamental pillars of the structural business and always keeps its word.\n\n'
                    '🔸Growing culture together\n'
                    'Atomy helps partner firms produce the best.\n\n'
                    '🔸Mutual assistance of all consultants.\n\n'
                    '🔸Much importance is attached to the success of each member.\n\n'
                    '🔶“Huge potential is a company whose employees and customers are happy, successful,'
                    ' which makes a great contribution to society.” - Pak Han-gil, Chairman of Atomy.',
        'language': False
    },
    #####################################Девиз и ценности############################################################
    #####################################За что платят компании######################################################
    {
        'type_sentence': 'what_pay_button',
        'sentence': '✅ За что и сколько платит компания?',
        'language': True
    },
    {
        'type_sentence': 'what_pay_button',
        'sentence': '✅ What does the company pay for and how much?',
        'language': False
    },
    {
        'type_sentence': 'what_pay',
        'sentence': '🔹Бизнес с "Atomy" - это прекрасный шанс начать с нуля и добиваться высот, о которых прежде '
                    'не мог и мечтать! \n\n'
                    '☝️Начать бизнес можно без опыта сетевого маркетинга (всему обучат бесплатно)! \n\n'
                    '✅ По средней статистике, в нашей компании на первый Мастерский ранг самые простые люди '
                    'выходят за год – полтора, а это доход уже от 100 000 руб. и выше! \n\n'
                    '✔️ У нас нет обязательных ежемесячных закупок! \n'
                    '✔️ У нас нет необходимости заниматься продажами и что-то кому-то навязывать! \n'
                    '✔️ У нас не обнуляются баллы (личные вообще никогда, а групповые пока за них не получишь доход)!\n'
                    '✔️ Команду строим вместе! Что это значит? Вышестоящие спонсоры своих новичков будут '
                    'отдавать в вашу структуру! \n'
                    '✔️ Доход получаем со всей глубины, независимо от того кто пригласил человека – '
                    'Вы, спонсор или новичок в структуре. \n\n'
                    '🤝 Мы всегда готовы помочь! \n'
                    '🤝 Поделиться знаниями и научить необходимым навыкам!💯 \n'
                    '🤝 Присоединяйтесь к нашей команде!🎯\n',
        'language': True
    },
    {
        'type_sentence': 'what_pay',
        'sentence': '🔹Business with "Atomy" is a great chance to start from scratch and achieve heights that '
                    'were previously mentioned I couldnt even dream! \n\n'
                    '☝️You can start a business without network marketing experience '
                    '(everything will be taught for free)! \n\n'
                    '✅ According to average statistics, in our company, the first Master rank is the simplest people'
                    'come out in a year - one and a half, and this is an income already from 100,000 rubles. '
                    'and higher! \n\n'
                    '✔️ We have no mandatory monthly purchases! \n'
                    '✔️ We do not need to engage in sales and impose something on someone! \n'
                    '✔️ Our points are not reset to zero '
                    '(personal points never at all, and group points until you receive income for them)!\n'
                    '✔️ Lets build a team together! What does it mean? Upstream sponsors of their newcomers will be '
                    'give to your structure! \n'
                    '✔️ We receive income from all depths, regardless of who invited the person - '
                    'You, sponsor or new to the structure. \n\n'
                    '🤝 We are always ready to help! \n'
                    '🤝 Share knowledge and teach skills!💯 \n'
                    '🤝 Join our team!🎯\n',
        'language': False
    },
    #####################################За что платят компании######################################################
    #####################################Видео презентация###########################################################
    {
        'type_sentence': 'video_presentation_button',
        'sentence': '👉 3-х минутная видео презентация компании',
        'language': True
    },
    {
        'type_sentence': 'video_presentation_button',
        'sentence': '👉 3 minute video presentation of the company',
        'language': False
    },
    {
        'type_sentence': 'video_presentation',
        'sentence': 'Знаете, я ещё не видел ни одного человека, который бы понял систему начислений (маркетинг-план) '
                    'с первого раза...😉\n\n'
                    '🤔В двух словах могу сказать, что в Atomy можно зарабатывать от 1200 рублей в месяц до '
                    '200 000 рублей в день!\n\n'
                    '☝️Самое важное - когда начнёте получать 1200 рублей, дальнейший рост '
                    'вашего дохода невозможно остановить.\n\n'
                    '💯 Компания Atomy создала схему сотрудничества выгодную всем участникам! \n\n'
                    'Смотрите видео и оцените масштаб идеи!',
        'language': True
    },
    {
        'type_sentence': 'video_presentation',
        'sentence': 'You know, I have not yet seen a single person who understands the accrual system (marketing plan)'
                    'from the first time...😉\n\n'
                    '🤔In a nutshell, I can say that in Atomy you can earn from 1200 rubles a month to '
                    '200,000 rubles a day!\n\n'
                    '☝️The most important thing is when you start getting 1200 rubles, further growth '
                    'Your income is unstoppable.\n\n'
                    '💯 Atomy has created a cooperation scheme that is beneficial to all participants! \n\n'
                    'Watch the video and see the scale of the idea!',
        'language': False
    },
    #####################################Видео презентация###########################################################
    {
        'type_sentence': '',
        'sentence': '',
        'language': True
    },
    {
        'type_sentence': '',
        'sentence': '',
        'language': True
    },
    {
        'type_sentence': '',
        'sentence': '',
        'language': True
    },
    {
        'type_sentence': '',
        'sentence': '',
        'language': True
    },

]
