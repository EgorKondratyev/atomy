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
    {
        'type_sentence': 'get_form_video_presentation',
        'sentence': '👍 Мне всё понятно из видео! Хочу стать партнёром или покупателем!',
        'language': True
    },
    {
        'type_sentence': 'get_form_video_presentation',
        'sentence': '👍 Everything is clear to me from the video! I want to become a partner or a buyer!',
        'language': False
    },
    #####################################Видео презентация###########################################################
    #####################################План компании###############################################################
    # План компании находится там же, где и what_pay
    {
        'type_sentence': 'company_plan_button',
        'sentence': '👉 Расскажу подробнее о маркетинг плане компании',
        'language': True
    },
    {
        'type_sentence': 'company_plan_button',
        'sentence': "👉 I will tell you more about the company's marketing plan",
        'language': False
    },
    {
        'type_sentence': 'company_plan',
        'sentence': '😇 Здесь я подробно расскажу обо всех ступенях в маркетинге, '
                    'какие бонусы ждут на каждом этапе и объясню как перейти на следующий уровень.\n\n'
                    'Для начала объясню тебе что такое PV. \n\n'
                    'PV (Point Value) - это баллы, которые начисляются за покупку продукции Atomy. \n\n'
                    'Есть личные PV, которые ты получаешь за покупку продукции для себя. '
                    'А есть групповые PV, которые начисляются за покупку других людей в одной из твоих веток.\n\n'
                    'Теперь, когда мы разобрались в терминологии, я могу рассказать тебе обо всём подробнее.\n\n'
                    '⬇️⬇️⬇️⬇️⬇️',
        'language': True
    },
    {
        'type_sentence': 'company_plan',
        'sentence': '😇 Here I will go into detail about all the steps in marketing, '
                    'what bonuses are waiting for each stage and explain how to go to the next level.\n\n'
                    'First, let me explain to you what PV is. \n\n'
                    'PV (Point Value) is the points that are awarded for the purchase of Atomy products. \n\n'
                    'There are personal PVs that you get for buying products for yourself. '
                    'And there are group PVs that are awarded for buying other people in one of your branches.\n\n'
                    "Now that we've sorted out the terminology, I can tell you more about everything.\n\n"
                    '⬇️⬇️⬇️⬇️⬇️',
        'language': False
    },
    #####################################План компании###############################################################
    #####################################План компании 2 (вложенные кнопки)##########################################
    {
        'type_sentence': 'company_plan_distributorship_button',  # - План компании 3
        'sentence': '✔️ Классификация и условия дистрибьюторства',
        'language': True
    },
    {
        'type_sentence': 'company_plan_distributorship_button',  # - План компании 3
        'sentence': '✔️ Classification and conditions of distribution',
        'language': False
    },
    {
        'type_sentence': 'company_plan_qualification_button',
        'sentence': '✔️ Квалификация мастеров',
        'language': True
    },
    {
        'type_sentence': 'company_plan_qualification_button',
        'sentence': '✔️ Qualification of masters',
        'language': False
    },
    {
        'type_sentence': 'company_plan_conditions_button',
        'sentence': '✔️ Условия повышения уровня мастерства',
        'language': True
    },
    {
        'type_sentence': 'company_plan_conditions_button',
        'sentence': '✔️ Conditions for increasing the skill level',
        'language': False
    },
    {
        'type_sentence': 'company_plan_bonus_button',
        'sentence': '✔️ Бонусы и поощрения для мастеров',
        'language': True
    },
    {
        'type_sentence': 'company_plan_bonus_button',
        'sentence': '✔️ Bonuses and incentives for masters',
        'language': False
    },
    {
        'type_sentence': 'company_plan_conditions',
        'sentence': '🔹Условия повышения уровня🔹\n\n'
                    'Отсутствуют для уровней: \n'
                    'Мастер продаж \n'
                    'Бриллиантовый мастер \n'
                    'Мастер Шаронской Розы \n\n'
                    'Условия для уровней Стар мастер, Роял мастер, Краун мастер, Империал мастер - '
                    'получить текущий уровень 3 раза.',
        'language': True
    },
    {
        'type_sentence': 'company_plan_conditions',
        'sentence': '🔹Level Up Conditions🔹\n\n'
                    'Not available for levels: \n'
                    'Master of Sales \n'
                    'Diamond Master \n'
                    'Master of the Rose of Sharon \n\n'
                    'Requirements for Star Master, Royal Master, Crown Master, Imperial Master - '
                    'get the current level 3 times.',
        'language': False
    },
    #####################################План компании 2 (вложенные кнопки)##########################################
    #####################################План компании 3 (вложенность в дистрибьюторства)############################
    {
        'type_sentence': 'distributorship',
        'sentence': '🔶Классификация и условия дистрибьюторства🔶 \n\n'
                    'Ниже я расположил ступени по мере возрастания товарооборота в вашей структуре. \n\n'
                    'Посмотрите какой рост может быть уже в первый месяц, два, три в вашем бизнесе!',
        'language': True
    },
    {
        'type_sentence': 'distributorship',
        'sentence': '🔶Classification and conditions of distributorship🔶\n\n'
                    'Below I have arranged the steps as the turnover in your structure increases.\n\n'
                    'See what growth can be already in the first month, two, three in your business!',
        'language': False
    },
    #####################################Торговый представитель##################################################
    {
        'type_sentence': 'distributorship_sales_representative_button',
        'sentence': '👉 Торговый представитель',
        'language': True
    },
    {
        'type_sentence': 'distributorship_sales_representative_button',
        'sentence': '👉 Sales Representative',
        'language': False
    },
    {
        'type_sentence': 'distributorship_sales_representative',
        'sentence': '🔶Торговый представитель🔶\n\n'
                    '💎Эта самая первая ступень вашего пути!\n'
                    '💡Когда ваши личные PV составляют от 10 000 PV до 299 999 PV (это от 1400 до 40000 руб.),'
                    ' а групповой оборот в меньшей ветки накопится до 300 000 PV, складывается бинарный шаг (степ), '
                    'за который вы получаете доход.\n'
                    '💸Ваш чек за каждый бинарный шаг составит около 1200 руб.\n\n'
                    '💰Бинарные шаги могут проходить ежедневно!',
        'language': True
    },
    {
        'type_sentence': 'distributorship_sales_representative',
        'sentence': '🔶Sales Representative🔶\n\n'
                    '💎This is the very first step of your path!\n'
                    '💡When your personal PV is between 10,000 PV and 299,999 PV, and '
                    'the group turnover in the smaller branch will accumulate up to 300,000 PV, '
                    'a binary step (step) is added, for which you receive income.\n'
                    '💸Your check for each binary step will be about 1200 rubles\n\n'
                    '💰Binary steps can be done daily!',
        'language': False
    },
    #####################################Агент##################################################################
    {
        'type_sentence': 'distributorship_agent_button',
        'sentence': '👉 Агент',
        'language': True
    },
    {
        'type_sentence': 'distributorship_agent_button',
        'sentence': '👉 Agent',
        'language': False
    },
    {
        'type_sentence': 'distributorship_agent',
        'sentence': '🔶Агент🔶\n\n'
                    '💎Это ранг, который позволяет получать за бинарный шаг сразу в 3 раза больше!!! \n\n'
                    '💡Стать Агентом можно при достижении одного из условий: \n'
                    '1. Личные PV >300000 \n'
                    '2. Накопление 600000 PV в меньшей ветке за предыдущий месяц\n\n'
                    '💸Ваш чек за КАЖДЫЙ бинарный шаг составит около 3600 руб.\n\n'
                    '💰Напомню, бинарные шаги могут проходить ежедневно!',
        'language': True
    },
    {
        'type_sentence': 'distributorship_agent',
        'sentence': '🔶Agent🔶\n\n'
                    '💎This is a rank that allows you to get 3 times more for a binary step at once!!! \n\n'
                    '💡You can become an Agent when one of the following conditions is met: \n'
                    '1. Personal PV >300000 \n'
                    '2. Accumulating 600,000 PV in a smaller branch from the previous month\n\n'
                    '💸Your check for EACH binary step will be about 3600 rubles\n\n'
                    '💰Remember, binary steps can be done daily!',
        'language': False
    },
    #####################################Специальный агент#######################################################
    {
        'type_sentence': 'distributorship_special_agent_button',
        'sentence': '👉 Специальный агент',
        'language': True
    },
    {
        'type_sentence': 'distributorship_special_agent_button',
        'sentence': '👉 Special Agent',
        'language': False
    },
    {
        'type_sentence': 'distributorship_special_agent',
        'sentence': '🔶Специальный агент🔶 \n\n'
                    '💎Этот статус присваивается при достижении одного из условий: \n'
                    '1. Личные PV >700000 \n'
                    '2. Накопление 1400000 PV в меньшей ветке за предыдущий месяц\n\n'
                    '💸Ваш чек за КАЖДЫЙ бинарный шаг составит около 7200 руб.',
        'language': True
    },
    {
        'type_sentence': 'distributorship_special_agent',
        'sentence': '🔶Special Agent🔶\n\n'
                    '💎This status is assigned when one of the conditions is met: \n'
                    '1. Personal PV >700000 \n'
                    '2. Accumulation of 1400000 PV in a smaller branch for the previous month\n\n'
                    '💸Your check for EACH binary step will be about 7,200 rubles.',
        'language': False
    },
    #####################################Дилер###################################################################
    {
        'type_sentence': 'distributorship_dealer_button',
        'sentence': '👉 Дилер',
        'language': True
    },
    {
        'type_sentence': 'distributorship_dealer_button',
        'sentence': '👉 Dealer',
        'language': False
    },
    {
        'type_sentence': 'distributorship_dealer',
        'sentence': '🔶Дилер🔶\n\n'
                    '💎Этот статус присваивается при достижении одного из условий: \n'
                    '1. Личные PV >1500000 \n'
                    '2. Накопление 3000000 PV в меньшей ветке за предыдущий месяц\n\n'
                    '💸Ваш чек за КАЖДЫЙ бинарный шаг составит около 14500 руб.',
        'language': True
    },
    {
        'type_sentence': 'distributorship_dealer',
        'sentence': '🔶Dealer🔶\n\n'
                    '💎This status is assigned when one of the following conditions is met: \n'
                    '1. Personal PV >1500000 \n'
                    '2. Accumulating 3,000,000 PV in a smaller branch from the previous month\n\n'
                    '💸Your check for EACH binary step will be about 14500 rubles.',
        'language': False
    },
    #####################################Эксклюзивный дистрибьютор#################################################
    {
        'type_sentence': 'distributorship_exclusive_distributor_button',
        'sentence': '👉 Эксклюзивный дистрибьютор',
        'language': True
    },
    {
        'type_sentence': 'distributorship_exclusive_distributor_button',
        'sentence': '👉 Exclusive distributor',
        'language': False
    },
    {
        'type_sentence': 'distributorship_exclusive_distributor',
        'sentence': '🔶Эксклюзивный дистрибьютор🔶\n\n'
                    '💎Этот статус присваивается при достижении одного из условий: \n'
                    '1. Личные PV >2400000 \n'
                    '2. Накопление 4800000PV в меньшей ветке за предыдущий месяц\n\n'
                    '💸Ваш чек за КАЖДЫЙ бинарный шаг составит примерно от 21000 до 72000 руб.\n\n'
                    '💰Внимание! Бинарный шаг может проходить ежедневно! Все зависит от товарооборота, '
                    'который будет проходить в вашей структуре...',
        'language': True
    },
    {
        'type_sentence': 'distributorship_exclusive_distributor',
        'sentence': '🔶Exclusive distributor🔶\n\n'
                    '💎This status is assigned when one of the following conditions is met: \n'
                    '1. Personal PV >2400000 \n'
                    '2. Accumulating 4800000PV in a smaller branch in the previous month\n\n'
                    '💸Your check for EACH binary step will be approximately from 21,000 to 72,000 rubles.\n\n'
                    '💰Attention! The binary step can take place daily! Everything depends on the turnover,'
                    'which will pass in your structure...',
        'language': False
    },
    #####################################План компании 3 (вложенность в дистрибьюторства)############################
    #####################################План компании 4 (вложенность в "квалификация мастеров")#####################
    {
        'type_sentence': 'qualification_master',
        'sentence': '🔹Мастерское вознаграждение и квалификация мастеров🔹\n\n'
                    '20% от общего количества PV компании распределяются между участниками согласно их '
                    'уровням мастерства.\n\n'
                    '✔️Мастерское вознаграждение выплачивается два раза в месяц на 7-ой день после завершения периода '
                    'подсчёта. Период подсчёта: с 1 по 15 число месяца, с 16 по конец месяца.',
        'language': True
    },
    {
        'type_sentence': 'qualification_master',
        'sentence': '🔹Master remuneration and qualifications of masters🔹\n\n'
                    '20% of the companys total PV is distributed among members according to their '
                    'skill levels.\n\n'
                    '✔️Masters reward is paid twice a month on the 7th day after the end of the period calculation. '
                    'Counting period: from the 1st to the 15th of the month, from the 16th to the end of the month.',
        'language': False
    },
    ######################################Мастер продаж##############################################################
    {
        'type_sentence': 'qualification_sales_master_button',
        'sentence': '👉 Мастер продаж',
        'language': True
    },
    {
        'type_sentence': 'qualification_sales_master_button',
        'sentence': '👉 Sales Master',
        'language': False
    },
    {
        'type_sentence': 'qualification_sales_master',
        'sentence': '🔹Мастер продаж🔹\n\n'
                    'Мастерское вознаграждение: 10% от общего количества PV компании распределяются только между '
                    'Мастерами продаж. \n\n'
                    'Требования: "Специальный агент" с накопленными 2 500 000 PV в каждой ветке в период\n'
                    'с 1 по 15 или с 16 по конец месяца. Если количество PV в меньшей ветке более 300 000, '
                    'то для достижения уровня мастерства меньшей ветке могут быть автоматически прибавлены личные PV, '
                    'накопленные в период подсчёта PV.',
        'language': True
    },
    {
        'type_sentence': 'qualification_sales_master',
        'sentence': '🔹Master of Sales🔹\n\n'
                    'Masters reward: 10% of the companys total PV is distributed only between '
                    'Masters of Sales. \n\n'
                    'Requirement: "Special Agent" with 2,500,000 PV accumulated in each track during the period\n'
                    'from 1 to 15 or from 16 to the end of the month. If the number of PVs in the smaller branch is '
                    'more than 300,000, then personal PVs can be automatically added to a lesser branch to achieve a '
                    'skill level, accumulated during the calculation period PV.',
        'language': False
    },
    ######################################Бриллиантовый мастер########################################################
    {
        'type_sentence': 'qualification_diamond_master_button',
        'sentence': '👉 Бриллиантовый мастер',
        'language': True
    },
    {
        'type_sentence': 'qualification_diamond_master_button',
        'sentence': '👉 Diamond master',
        'language': False
    },
    {
        'type_sentence': 'qualification_diamond_master',
        'sentence': '🔹Бриллиантовый мастер🔹\n\n'
                    'Мастерское вознаграждение: 5% от общего количества PV компании распределяются между '
                    'Бриллиантовыми мастерами и выше.\n\n'
                    'Требования: Дилер с двумя Мастерами продаж в каждой ветке.',
        'language': True
    },
    {
        'type_sentence': 'qualification_diamond_master',
        'sentence': '🔹Diamond Master🔹\n\n'
                    'Masters reward: 5% of the companys total PV is shared between Diamond Masters and above.\n\n'
                    'Requirements: Dealer with two Sales Masters in each branch.',
        'language': False
    },
    ######################################Мастер Шонской Розы#########################################################
    {
        'type_sentence': 'qualification_master_rose_button',
        'sentence': '👉 Мастер Шаронской Розы',
        'language': True
    },
    {
        'type_sentence': 'qualification_master_rose_button',
        'sentence': '👉 Master of the Sharon Rose',
        'language': False
    },
    {
        'type_sentence': 'qualification_master_rose',
        'sentence': '🔹Мастер Шаронской Розы🔹\n\n'
                    'Мастерское вознаграждение: 2% от общего количества PV компании распределяются между '
                    'Мастерами Шаронской Розы и выше.\n\n'
                    'Требования: Эксклюзивный дистрибьютор с двумя Бриллиантовыми мастерами в каждой ветке.',
        'language': True
    },
    {
        'type_sentence': 'qualification_master_rose',
        'sentence': '🔹Master of the Rose of Sharon🔹\n\n'
                    'Masters reward: 2% of the companys total PV is shared between '
                    'Masters of the Rose of Sharon and above.\n\n'
                    'Requirements: Exclusive distributor with two Diamond Masters in each branch.',
        'language': False
    },
    ######################################Стар Мастер#################################################################
    {
        'type_sentence': 'qualification_star_master_button',
        'sentence': '👉 Стар мастер',
        'language': True
    },
    {
        'type_sentence': 'qualification_star_master_button',
        'sentence': '👉 Star master',
        'language': False
    },
    {
        'type_sentence': 'qualification_star_master',
        'sentence': '🔹Стар мастер🔹\n\n'
                    'Мастерское вознаграждение: 1,2% от общего количества PV компании распределяются между Стар '
                    'мастерами и выше.\n\n'
                    'Требования: Эксклюзивный дистрибьютор с двумя Мастерами Шаронской Розы в каждой ветке.',
        'language': True
    },
    {
        'type_sentence': 'qualification_star_master',
        'sentence': '🔹Star master🔹\n\n'
                    'Masters reward: 1.2% of the companys total PV is shared between Star'
                    'masters and above.\n\n'
                    'Requirements: Exclusive distributor with two Masters of the Rose of Sharon in each branch.',
        'language': False
    },
    ######################################Роял Мастер#################################################################
    {
        'type_sentence': 'qualification_royal_master_button',
        'sentence': '👉 Роял мастер',
        'language': True
    },
    {
        'type_sentence': 'qualification_royal_master_button',
        'sentence': '👉 Royal Master',
        'language': False
    },
    {
        'type_sentence': 'qualification_royal_master',
        'sentence': '🔹Роял мастер🔹\n\n'
                    'Мастерское вознаграждение: 1% от общего количества PV компании распределяются между Роял '
                    'мастерами и выше.\n\n'
                    'Требования: Эксклюзивный дистрибьютор с двумя Стар мастерами в каждой ветке.',
        'language': True
    },
    {
        'type_sentence': 'qualification_royal_master',
        'sentence': '🔹Royal master🔹\n\n'
                    'Masters reward: 1% of the companys total PV is distributed among the Royal'
                    'masters and above.\n\n'
                    'Requirements: Exclusive distributor with two Star Masters in each branch.',
        'language': False
    },
    ######################################Краун Мастер#################################################################
    {
        'type_sentence': 'qualification_crown_master_button',
        'sentence': '👉 Краун мастер',
        'language': True
    },
    {
        'type_sentence': 'qualification_crown_master_button',
        'sentence': '👉 Crown Master',
        'language': False
    },
    {
        'type_sentence': 'qualification_crown_master',
        'sentence': '🔹Краун мастер🔹\n\n'
                    'Мастерское вознаграждение: 0,5% от общего количества PV компании распределяются между Краун '
                    'мастерами и выше.\n\n'
                    'Требования: Эксклюзивный дистрибьютор с двумя Роял мастерами в каждой ветке.',
        'language': True
    },
    {
        'type_sentence': 'qualification_crown_master',
        'sentence': '🔹Crown Master🔹\n\n'
                    'Masters reward: 0.5% of the companys total PV is distributed among the Crown'
                    'masters and above.\n\n'
                    'Requirements: Exclusive Distributor with two Royal Masters per branch.',
        'language': False
    },
    ######################################Империал Мастер############################################################
    {
        'type_sentence': 'qualification_imperial_master_button',
        'sentence': '👉 Империал мастер',
        'language': True
    },
    {
        'type_sentence': 'qualification_imperial_master_button',
        'sentence': '👉 Imperial Master',
        'language': False
    },
    {
        'type_sentence': 'qualification_imperial_master',
        'sentence': '🔹Империал мастер🔹\n\n'
                    'Мастерское вознаграждение: 0,3% от общего количества PV компании распределяются между Империал '
                    'мастерами и выше. \n\n'
                    'Требования: Эксклюзивный дистрибьютор с двумя Краун мастерами в каждой ветке.',
        'language': True
    },
    {
        'type_sentence': 'qualification_imperial_master',
        'sentence': '🔹Imperial Master🔹\n\n'
                    'Masters reward: 0.3% of the companys total PV is distributed among the Imperial '
                    'masters and above. \n\n'
                    'Requirements: Exclusive Distributor with two Crown Masters per branch.',
        'language': False
    },
    #####################################План компании 4 (вложенность в "квалификация мастеров")#####################
    #####################################План компании 5 (вложенность в "Бонусы и поощрения")#######################
    {
        'type_sentence': 'bonus',
        'sentence': '🔹Мастерское вознаграждение и квалификация мастеров🔹\n\n'
                    '20% от общего количества PV компании распределяются между участниками согласно их уровням '
                    'мастерства.\n\n'
                    '✔️Мастерское вознаграждение выплачивается два раза в месяц на 7-ой день после завершения периода '
                    'подсчёта. Период подсчёта: с 1 по 15 число месяца, с 16 по конец месяца.',
        'language': True
    },
    {
        'type_sentence': 'bonus',
        'sentence': '🔹Master remuneration and qualifications of masters🔹\n\n'
                    '20% of the companys total PV is distributed among members according to their levels'
                    'skill.\n\n'
                    '✔️Masters reward is paid twice a month on the 7th day after the end of the period calculation. '
                    'Counting period: from the 1st to the 15th of the month, from the 16th to the end of the month.',
        'language': False
    },
    ########################################Мастер продаж###########################################################
    {
        'type_sentence': 'bonus_sales_master_button',
        'sentence': '👉 Для мастера продаж',
        'language': True
    },
    {
        'type_sentence': 'bonus_sales_master_button',
        'sentence': '👉 For sales master',
        'language': False
    },
    {
        'type_sentence': 'bonus_sales_master',
        'sentence': '🔹Поощрения для уровня "Мастер продаж"🔹\n\n'
                    '1️⃣ Атоми Скин Кеар шестиступенчатая система по уходу за кожей (1 набор)\n'
                    '2️⃣ Атоми ХемоХИМ (1 набор)\n'
                    '3️⃣ Атоми Ивнинг Кеар набор для ночного ухода из 4 средств (1 набор)',
        'language': True
    },
    {
        'type_sentence': 'bonus_sales_master',
        'sentence': '🔹Master Sales Promotions🔹\n\n'
                    '1️⃣ Atomy Skin Care 6 step skin care system (1 set)\n'
                    '2️⃣ Atomy HemoCHIM (1 set)\n'
                    '3️⃣ Atomy Evening Care 4 night care set (1 set)',
        'language': False
    },
    ########################################Бриллиантовый мастер######################################################
    {
        'type_sentence': 'bonus_diamond_master_button',
        'sentence': '👉 Для Бриллиантового мастера',
        'language': True
    },
    {
        'type_sentence': 'bonus_diamond_master_button',
        'sentence': '👉 For the Diamond Master',
        'language': False
    },
    {
        'type_sentence': 'bonus_diamond_master',
        'sentence': '🔹Поощрения для уровня "Бриллиантовый мастер"🔹\n\n'
                    '1️⃣ Ноутбук или планшет\n'
                    '2️⃣ Атоми Скин Кеар шестиступенчатая система по уходу за кожей (1 набор)\n'
                    '3️⃣ Атоми ХемоХИМ (1 набор)\n'
                    '4️⃣ Атоми Ивнинг Кеар набор для ночного ухода из 4 средств (1 набор)',
        'language': True
    },
    {
        'type_sentence': 'bonus_diamond_master',
        'sentence': '🔹Diamond Master Promotions🔹\n\n'
                    '1️⃣ Laptop or tablet\n'
                    '2️⃣ Atomy Skin Care 6 step skin care system (1 set)\n'
                    '3️⃣ Atomy HemoCHIM (1 set)\n'
                    '4️⃣ Atomy Evening Care 4 night care set (1 set)',
        'language': False
    },
    ########################################Шаронской розы мастер####################################################
    {
        'type_sentence': 'bonus_sharon_rose_button',
        'sentence': '👉 Для Мастера Шаронской Розы',
        'language': True
    },
    {
        'type_sentence': 'bonus_sharon_rose_button',
        'sentence': '👉 For the Master of the Sharon Rose',
        'language': False
    },
    {
        'type_sentence': 'bonus_sharon_rose',
        'sentence': '🔹Поощрения для уровня "Мастер Шаронской Розы"🔹\n\n'
                    '1️⃣ Путешествие на двоих (3 ночи/4 дня)  👫✈️\n'
                    '2️⃣ Денежное вознаграждение в размере 110 тыс. руб.💰',
        'language': True
    },
    {
        'type_sentence': 'bonus_sharon_rose',
        'sentence': '🔹Rose of Sharon Master Rewards🔹\n\n'
                    '1️⃣ Trip for two (3 nights/4 days) 👫✈️\n'
                    '2️⃣ Cash reward in the amount of 110 thousand rubles.💰',
        'language': False
    },
    ########################################Стар мастер####################################################
    {
        'type_sentence': 'bonus_star_master_button',
        'sentence': '👉 Для Стар мастера',
        'language': True
    },
    {
        'type_sentence': 'bonus_star_master_button',
        'sentence': '👉 For the Old Master',
        'language': False
    },
    {
        'type_sentence': 'bonus_star_master',
        'sentence': '🔹Поощрения для уровня "Стар мастер"🔹\n\n'
                    '1️⃣ Путешествие на четверых (3 ночи/4 дня) 👨‍👦👩‍👧✈️\n'
                    '2️⃣ Денежное вознаграждение в размере 550 тыс. руб.💰💰',
        'language': True
    },
    {
        'type_sentence': 'bonus_star_master',
        'sentence': '🔹Star Master Rewards🔹\n\n'
                    '1️⃣ Trip for 4 (3 nights/4 days) 👨‍👦👩‍👧✈️\n'
                    '2️⃣ Cash reward in the amount of 550 thousand rubles.💰💰',
        'language': False
    },
    ########################################Роял мастер##############################################################
    {
        'type_sentence': 'bonus_royal_master_button',
        'sentence': '👉 Для Роял мастера',
        'language': True
    },
    {
        'type_sentence': 'bonus_royal_master_button',
        'sentence': '👉 For the Royal Master',
        'language': False
    },
    {
        'type_sentence': 'bonus_royal_master',
        'sentence': '🔹Поощрения для уровня "Роял мастер"🔹\n\n'
                    '1️⃣ Путешествие на четверых (10 ночей/11дней) 👨‍👦👫 ✈️\n'
                    '2️⃣ Бесплатная аренда седана бизнес класса 🚘\n'
                    '3️⃣ Корпоративная кредитная карта с балансом 110 тыс. руб. в месяц 💳\n'
                    '4️⃣ Денежное вознаграждение в размере 2,7 млн. руб. 💰💰💰',
        'language': True
    },
    {
        'type_sentence': 'bonus_royal_master',
        'sentence': '🔹Royal Master Rewards🔹\n\n'
                    '1️⃣ Trip for four (10 nights/11 days) 👨‍👦👫 ✈️\n'
                    '2️⃣ Free business sedan rental 🚘\n'
                    '3️⃣ Corporate credit card with a balance of 110 thousand rubles. per month 💳\n'
                    '4️⃣ Cash reward in the amount of 2.7 million rubles. 💰💰💰',
        'language': False
    },
    ########################################Краун мастер##############################################################
    {
        'type_sentence': 'bonus_crown_master_button',
        'sentence': '👉 Для Краун мастера',
        'language': True
    },
    {
        'type_sentence': 'bonus_crown_master_button',
        'sentence': '👉 For Crown Master',
        'language': False
    },
    {
        'type_sentence': 'bonus_crown_master',
        'sentence': '🔹Поощрения для уровня "Краун мастер"🔹\n\n'
                    '1️⃣ Путешествие на четверых (10 ночей/11дней)👩‍👦👨‍👦\n'
                    '2️⃣ Бесплатная аренда седана бизнес класса🚘\n'
                    '3️⃣ Корпоративная кредитная карта с балансом 110 тыс. руб. в месяц 💳\n'
                    '4️⃣ Денежное вознаграждение в размере 2,7 млн. руб. 💰💰💰',
        'language': True
    },
    {
        'type_sentence': 'bonus_crown_master',
        'sentence': '🔹Crown Master Rewards🔹\n\n'
                    '1️⃣ Trip for four (10 nights/11 days)👩‍👦👨‍👦\n'
                    '2️⃣ Free business sedan rental🚘\n'
                    '3️⃣ Corporate credit card with a balance of 110 thousand rubles. per month 💳\n'
                    '4️⃣ Cash reward in the amount of 2.7 million rubles. 💰💰💰',
        'language': False
    },
    ########################################Империал мастер###########################################################
    {
        'type_sentence': 'bonus_imperial_master_button',
        'sentence': '👉 Для Империал мастера',
        'language': True
    },
    {
        'type_sentence': 'bonus_imperial_master_button',
        'sentence': '👉 For Imperial Master',
        'language': False
    },
    {
        'type_sentence': 'bonus_imperial_master',
        'sentence': '🔹Поощрения для уровня "Империал мастер"🔹\n\n'
                    '1️⃣ Путешествие на четверых (10 ночей/11дней) 👨‍👦👩‍👧✈️\n'
                    '2️⃣ Машина класса люкс🚘\n'
                    '3️⃣ Корпоративная кредитная карта с балансом 550 тыс. руб. в месяц 💳\n'
                    '4️⃣ Бесплатная аренда офиса площадью 165 м2 🏢\n'
                    '5️⃣ Личный ассистент 👩‍💼\n'
                    '6️⃣ Денежное вознаграждение в размере 55 млн. руб. 💰💰💰',
        'language': True
    },
    {
        'type_sentence': 'bonus_imperial_master',
        'sentence': '🔹Imperial Master Rewards🔹\n\n'
                    '1️⃣ Trip for four (10 nights/11 days) 👨‍👦👩‍👧✈️\n'
                    '2️⃣ Luxury car🚘\n'
                    '3️⃣ Corporate credit card with a balance of 550 thousand rubles. per month 💳\n'
                    '4️⃣ Free office rental of 165 m2 🏢\n'
                    '5️⃣ Personal Assistant 👩‍💼\n'
                    '6️⃣ Cash reward in the amount of 55 million rubles. 💰💰💰',
        'language': False
    },
    #####################################План компании 5 (вложенность в "Бонусы и поощрения")#######################
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
