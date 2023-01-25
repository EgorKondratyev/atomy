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
    ##################################################################################################################
    # {
    #     'type_sentence': '',
    #     'sentence': '',
    #     'language': True
    # },
    # {
    #     'type_sentence': '',
    #     'sentence': '',
    #     'language': True
    # },

]
