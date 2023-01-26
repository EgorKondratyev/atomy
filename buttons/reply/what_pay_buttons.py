from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from databases.client import SentencesDB


async def create_what_pay_menu(language: bool, sentences_db: SentencesDB) -> ReplyKeyboardMarkup:
    what_pay_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    text_video_presentation = sentences_db.get_sentence(type_sentence='video_presentation_button', language=language)
    video_presentation_button = KeyboardButton(text=text_video_presentation)
    what_pay_menu.insert(video_presentation_button)

    text_company_plan = sentences_db.get_sentence(type_sentence='company_plan_button', language=language)
    company_plan_button = KeyboardButton(text=text_company_plan)
    what_pay_menu.insert(company_plan_button)

    if language:
        back_text = 'Назад'
    else:
        back_text = 'Back'
    back_button = KeyboardButton(text=back_text)
    what_pay_menu.add(back_button)
    return what_pay_menu


async def create_video_presentation_menu(language: bool, sentences_db: SentencesDB) -> ReplyKeyboardMarkup:
    video_presentation_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    get_form_text = sentences_db.get_sentence(type_sentence='get_form_video_presentation', language=language)
    button_form = KeyboardButton(text=get_form_text)
    video_presentation_menu.insert(button_form)

    if language:
        back_text = 'Назад'
    else:
        back_text = 'Back'
    back_button = KeyboardButton(text=back_text)
    video_presentation_menu.add(back_button)
    return video_presentation_menu


async def create_company_plan_menu(language: bool, sentences_db: SentencesDB) -> ReplyKeyboardMarkup:
    company_plan_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    text_distributorship = sentences_db.get_sentence(type_sentence='company_plan_distributorship_button',
                                                     language=language)
    distributorship_button = KeyboardButton(text=text_distributorship)
    company_plan_menu.insert(distributorship_button)

    text_qualification = sentences_db.get_sentence(type_sentence='company_plan_qualification_button',
                                                   language=language)
    qualification_button = KeyboardButton(text=text_qualification)
    company_plan_menu.insert(qualification_button)

    text_conditions = sentences_db.get_sentence(type_sentence='company_plan_conditions_button',
                                                language=language)
    conditions_button = KeyboardButton(text=text_conditions)
    company_plan_menu.insert(conditions_button)

    text_bonus = sentences_db.get_sentence(type_sentence='company_plan_bonus_button',
                                           language=language)
    bonus_button = KeyboardButton(text=text_bonus)
    company_plan_menu.insert(bonus_button)

    if language:
        back_text = 'Назад'
    else:
        back_text = 'Back'
    back_button = KeyboardButton(text=back_text)
    company_plan_menu.add(back_button)
    return company_plan_menu


async def create_distributorship_menu(language: bool, sentences_db: SentencesDB) -> ReplyKeyboardMarkup:
    distributorship_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    sales_representative_text = sentences_db.get_sentence(type_sentence='distributorship_sales_representative_button',
                                                          language=language)
    sales_representative_button = KeyboardButton(text=sales_representative_text)
    distributorship_menu.insert(sales_representative_button)

    agent_text = sentences_db.get_sentence(type_sentence='distributorship_agent_button', language=language)
    agent_button = KeyboardButton(text=agent_text)
    distributorship_menu.insert(agent_button)

    special_agent_text = sentences_db.get_sentence(type_sentence='distributorship_special_agent_button',
                                                   language=language)
    special_agent_button = KeyboardButton(text=special_agent_text)
    distributorship_menu.insert(special_agent_button)

    dealer_text = sentences_db.get_sentence(type_sentence='distributorship_dealer_button', language=language)
    dealer_button = KeyboardButton(text=dealer_text)
    distributorship_menu.insert(dealer_button)

    exclusive_distributor_text = sentences_db.get_sentence(type_sentence='distributorship_exclusive_distributor_button',
                                                           language=language)
    exclusive_distributor_button = KeyboardButton(text=exclusive_distributor_text)
    distributorship_menu.insert(exclusive_distributor_button)

    if language:
        back_text = 'Назад'
    else:
        back_text = 'Back'
    back_button = KeyboardButton(text=back_text)
    distributorship_menu.add(back_button)
    return distributorship_menu


async def create_qualification_menu(language: bool, sentences_db: SentencesDB) -> ReplyKeyboardMarkup:
    qualification_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    sales_master_text = sentences_db.get_sentence(type_sentence='qualification_sales_master_button',
                                                  language=language)
    sales_master_button = KeyboardButton(text=sales_master_text)
    qualification_menu.insert(sales_master_text)

    diamond_master_text = sentences_db.get_sentence(type_sentence='qualification_diamond_master_button',
                                                    language=language)
    diamond_master_button = KeyboardButton(text=diamond_master_text)
    qualification_menu.insert(diamond_master_button)

    master_rose_text = sentences_db.get_sentence(type_sentence='qualification_master_rose_button',
                                                 language=language)
    master_rose_button = KeyboardButton(text=master_rose_text)
    qualification_menu.insert(master_rose_button)

    master_rose_text = sentences_db.get_sentence(type_sentence='qualification_master_rose_button',
                                                 language=language)
    master_rose_button = KeyboardButton(text=master_rose_text)
    qualification_menu.insert(master_rose_button)

    star_master_text = sentences_db.get_sentence(type_sentence='qualification_star_master_button',
                                                 language=language)
    star_master_button = KeyboardButton(text=star_master_text)
    qualification_menu.insert(star_master_button)

    royal_master_text = sentences_db.get_sentence(type_sentence='qualification_royal_master_button',
                                                  language=language)
    royal_master_button = KeyboardButton(text=royal_master_text)
    qualification_menu.insert(royal_master_button)

    crown_master_text = sentences_db.get_sentence(type_sentence='qualification_crown_master_button',
                                                  language=language)
    crown_master_button = KeyboardButton(text=crown_master_text)
    qualification_menu.insert(crown_master_button)

    imperial_master_text = sentences_db.get_sentence(type_sentence='qualification_imperial_master_button',
                                                     language=language)
    imperial_master_button = KeyboardButton(text=imperial_master_text)
    qualification_menu.insert(imperial_master_button)

    if language:
        back_text = 'Назад'
    else:
        back_text = 'Back'
    back_button = KeyboardButton(text=back_text)
    qualification_menu.add(back_button)
    return qualification_menu


async def create_bonus_menu(language: bool, sentences_db: SentencesDB) -> ReplyKeyboardMarkup:
    bonus_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    sales_master_text = sentences_db.get_sentence(type_sentence='bonus_sales_master_button',
                                                  language=language)
    sales_master_button = KeyboardButton(text=sales_master_text)
    bonus_menu.insert(sales_master_button)

    diamond_master_text = sentences_db.get_sentence(type_sentence='bonus_diamond_master_button',
                                                    language=language)
    diamond_master_button = KeyboardButton(text=diamond_master_text)
    bonus_menu.insert(diamond_master_button)

    sharon_rose_text = sentences_db.get_sentence(type_sentence='bonus_sharon_rose_button',
                                                 language=language)
    sharon_rose_button = KeyboardButton(text=sharon_rose_text)
    bonus_menu.insert(sharon_rose_button)

    star_master_text = sentences_db.get_sentence(type_sentence='bonus_star_master_button',
                                                 language=language)
    star_master_button = KeyboardButton(text=star_master_text)
    bonus_menu.insert(star_master_button)

    royal_master_text = sentences_db.get_sentence(type_sentence='bonus_royal_master_button',
                                                  language=language)
    royal_master_button = KeyboardButton(text=royal_master_text)
    bonus_menu.insert(royal_master_button)

    crown_master_text = sentences_db.get_sentence(type_sentence='bonus_crown_master_button',
                                                  language=language)
    crown_master_button = KeyboardButton(text=crown_master_text)
    bonus_menu.insert(crown_master_button)

    imperial_master_text = sentences_db.get_sentence(type_sentence='bonus_imperial_master_button',
                                                     language=language)
    imperial_master_button = KeyboardButton(text=imperial_master_text)
    bonus_menu.insert(imperial_master_button)

    if language:
        back_text = 'Назад'
    else:
        back_text = 'Back'
    back_button = KeyboardButton(text=back_text)
    bonus_menu.add(back_button)
    return bonus_menu
