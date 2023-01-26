from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from buttons.reply.what_pay_buttons import create_what_pay_menu, create_video_presentation_menu, \
    create_company_plan_menu, create_distributorship_menu, create_qualification_menu, create_bonus_menu
from create_bot.bot import dp
from databases.client import UsersDB, SentencesDB


async def create_handler(message: Message, type_sentence: str):
    """
    Создание обработчиков без ReplyMarkup
    """
    user_db = UsersDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence_db = SentencesDB()
    sentence = sentence_db.get_sentence(type_sentence=type_sentence, language=language)
    await message.answer(sentence, parse_mode='html')


def get_sentences(type_sentence: str, sentences_db: SentencesDB):
    """
    Получение предложения на двух языках
    """
    rus = sentences_db.get_sentence(type_sentence=type_sentence, language=True)
    en = sentences_db.get_sentence(type_sentence=type_sentence, language=False)
    return rus, en


async def what_pay(message: Message):
    user_db = UsersDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence_db = SentencesDB()
    sentence = sentence_db.get_sentence(type_sentence='what_pay', language=language)
    await message.answer(sentence, parse_mode='html',
                         reply_markup=await create_what_pay_menu(language=language, sentences_db=sentence_db))


async def video_presentation(message: Message):
    user_db = UsersDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence_db = SentencesDB()
    sentence = sentence_db.get_sentence(type_sentence='video_presentation', language=language)
    await message.answer(sentence, parse_mode='html',
                         reply_markup=await create_video_presentation_menu(language=language, sentences_db=sentence_db))


async def company_plan(message: Message):
    user_db = UsersDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence_db = SentencesDB()
    sentence = sentence_db.get_sentence(type_sentence='company_plan', language=language)
    await message.answer(sentence, parse_mode='html',
                         reply_markup=await create_company_plan_menu(language=language, sentences_db=sentence_db))


async def distributorship(message: Message):
    user_db = UsersDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence_db = SentencesDB()
    sentence = sentence_db.get_sentence(type_sentence='distributorship', language=language)
    await message.answer(sentence, parse_mode='html',
                         reply_markup=await create_distributorship_menu(language=language, sentences_db=sentence_db))


async def distributorship_sales_representative(message: Message):
    await create_handler(message, 'distributorship_sales_representative')


async def distributorship_agent(message: Message):
    await create_handler(message, 'distributorship_agent')


async def distributorship_special_agent(message: Message):
    await create_handler(message, 'distributorship_special_agent')


async def distributorship_dealer(message: Message):
    await create_handler(message, 'distributorship_dealer')


async def distributorship_exclusive_distributor(message: Message):
    await create_handler(message, 'distributorship_exclusive_distributor')


async def qualification_master(message: Message):
    user_db = UsersDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence_db = SentencesDB()
    sentence = sentence_db.get_sentence(type_sentence='qualification_master', language=language)
    await message.answer(sentence, parse_mode='html',
                         reply_markup=await create_qualification_menu(language=language, sentences_db=sentence_db))


async def qualification_sales_master(message: Message):
    await create_handler(message, 'qualification_sales_master')


async def qualification_diamond_master(message: Message):
    await create_handler(message, 'qualification_diamond_master')


async def qualification_master_rose(message: Message):
    await create_handler(message, 'qualification_master_rose')


async def qualification_star_master(message: Message):
    await create_handler(message, 'qualification_star_master')


async def qualification_royal_master(message: Message):
    await create_handler(message, 'qualification_royal_master')


async def qualification_crown_master(message: Message):
    await create_handler(message, 'qualification_crown_master')


async def qualification_imperial_master(message: Message):
    await create_handler(message, 'qualification_imperial_master')


async def company_plan_conditions(message: Message):
    await create_handler(message, 'company_plan_conditions')


async def bonus(message: Message):
    user_db = UsersDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence_db = SentencesDB()
    sentence = sentence_db.get_sentence(type_sentence='bonus', language=language)
    await message.answer(sentence, parse_mode='html',
                         reply_markup=await create_bonus_menu(language=language, sentences_db=sentence_db))


async def bonus_sales_master(message: Message):
    await create_handler(message, 'bonus_sales_master')


async def bonus_diamond_master(message: Message):
    await create_handler(message, 'bonus_diamond_master')


async def bonus_sharon_rose(message: Message):
    await create_handler(message, 'bonus_sharon_rose')


async def bonus_star_master(message: Message):
    await create_handler(message, 'bonus_star_master')


async def bonus_royal_master(message: Message):
    await create_handler(message, 'bonus_royal_master')


async def bonus_crown_master(message: Message):
    await create_handler(message, 'bonus_crown_master')


async def bonus_imperial_master(message: Message):
    await create_handler(message, 'bonus_imperial_master')


def register_what_pay_handlers():
    sentences_db = SentencesDB()
    rus_what_pay, en_what_pay = get_sentences(type_sentence='what_pay_button', sentences_db=sentences_db)
    dp.register_message_handler(what_pay, Text(equals=[rus_what_pay, en_what_pay]))

    rus_video_presentation, en_video_presentation = get_sentences(type_sentence='video_presentation_button',
                                                                  sentences_db=sentences_db)
    dp.register_message_handler(video_presentation, Text(equals=[rus_video_presentation, en_video_presentation]))

    rus_company_plan, en_company_plan = get_sentences(type_sentence='company_plan_button', sentences_db=sentences_db)
    dp.register_message_handler(company_plan, Text(equals=[rus_company_plan, en_company_plan]))

    rus_distributorship, en_distributorship = get_sentences(type_sentence='company_plan_distributorship_button',
                                                            sentences_db=sentences_db)
    dp.register_message_handler(distributorship, Text(equals=[rus_distributorship, en_distributorship]))

    rus_sales_representative, en_sales_representative = get_sentences(
        type_sentence='distributorship_sales_representative_button',
        sentences_db=sentences_db)
    dp.register_message_handler(distributorship_sales_representative,
                                Text(equals=[rus_sales_representative, en_sales_representative]))

    rus_agent, en_agent = get_sentences(type_sentence='distributorship_agent_button',
                                        sentences_db=sentences_db)
    dp.register_message_handler(distributorship_agent, Text(equals=[rus_agent, en_agent]))

    rus_special_agent, en_special_agent = get_sentences(type_sentence='distributorship_special_agent_button',
                                                        sentences_db=sentences_db)
    dp.register_message_handler(distributorship_special_agent, Text(equals=[rus_special_agent, en_special_agent]))

    rus_dealer, en_dealer = get_sentences(type_sentence='distributorship_dealer_button', sentences_db=sentences_db)
    dp.register_message_handler(distributorship_dealer, Text(equals=[rus_dealer, en_dealer]))

    rus_exclusive_distributor, en_exclusive_distributor = get_sentences(
        type_sentence='distributorship_exclusive_distributor_button',
        sentences_db=sentences_db)
    dp.register_message_handler(distributorship_exclusive_distributor, Text(equals=[rus_exclusive_distributor,
                                                                                    en_exclusive_distributor]))
    ##########################################################################################################
    rus_plan_qualification, en_plan_qualification = get_sentences(type_sentence='company_plan_qualification_button',
                                                                  sentences_db=sentences_db)
    dp.register_message_handler(qualification_master, Text(equals=[rus_plan_qualification, en_plan_qualification]))

    rus_qualification_sales_master, en_qualification_sales_master = get_sentences(
        type_sentence='qualification_sales_master_button',
        sentences_db=sentences_db)
    dp.register_message_handler(qualification_sales_master, Text(equals=[rus_qualification_sales_master,
                                                                         en_qualification_sales_master]))

    rus_qualification_diamond_master, en_qualification_diamond_master = get_sentences(
        type_sentence='qualification_diamond_master_button',
        sentences_db=sentences_db)
    dp.register_message_handler(qualification_diamond_master, Text(equals=[rus_qualification_diamond_master,
                                                                           en_qualification_diamond_master]))

    rus_qualification_master_rose, en_qualification_master_rose = get_sentences(
        type_sentence='qualification_master_rose_button',
        sentences_db=sentences_db)
    dp.register_message_handler(qualification_master_rose, Text(equals=[rus_qualification_master_rose,
                                                                        en_qualification_master_rose]))

    rus_qualification_star_master, en_qualification_star_master = get_sentences(
        type_sentence='qualification_star_master_button',
        sentences_db=sentences_db)
    dp.register_message_handler(qualification_star_master, Text(equals=[rus_qualification_star_master,
                                                                        en_qualification_star_master]))

    rus_qualification_royal_master, en_qualification_royal_master = get_sentences(
        type_sentence='qualification_royal_master_button',
        sentences_db=sentences_db)
    dp.register_message_handler(qualification_royal_master, Text(equals=[rus_qualification_royal_master,
                                                                         en_qualification_royal_master]))

    rus_qualification_crown_master, en_qualification_crown_master = get_sentences(
        type_sentence='qualification_crown_master_button',
        sentences_db=sentences_db)
    dp.register_message_handler(qualification_crown_master, Text(equals=[rus_qualification_crown_master,
                                                                         en_qualification_crown_master]))

    rus_qualification_imperial_master, en_qualification_imperial_master = get_sentences(
        type_sentence='qualification_imperial_master_button',
        sentences_db=sentences_db)
    dp.register_message_handler(qualification_imperial_master, Text(equals=[rus_qualification_imperial_master,
                                                                            en_qualification_imperial_master]))
    ##########################################################################################################
    rus_conditions, en_conditions = get_sentences(
        type_sentence='company_plan_conditions_button',
        sentences_db=sentences_db)
    dp.register_message_handler(company_plan_conditions, Text(equals=[rus_conditions, en_conditions]))
    ##########################################################################################################
    rus_bonus, en_bonus = get_sentences(
        type_sentence='company_plan_bonus_button',
        sentences_db=sentences_db)
    dp.register_message_handler(bonus, Text(equals=[rus_bonus, en_bonus]))

    rus_bonus_sales_master, en_bonus_sales_master = get_sentences(
        type_sentence='bonus_sales_master_button',
        sentences_db=sentences_db)
    dp.register_message_handler(bonus_sales_master, Text(equals=[rus_bonus_sales_master, en_bonus_sales_master]))

    rus_bonus_diamond_master, en_bonus_diamond_master = get_sentences(
        type_sentence='bonus_diamond_master_button',
        sentences_db=sentences_db)
    dp.register_message_handler(bonus_diamond_master, Text(equals=[rus_bonus_diamond_master, en_bonus_diamond_master]))

    rus_bonus_sharon_rose, en_bonus_sharon_rose = get_sentences(
        type_sentence='bonus_sharon_rose_button',
        sentences_db=sentences_db)
    dp.register_message_handler(bonus_sharon_rose, Text(equals=[rus_bonus_sharon_rose, en_bonus_sharon_rose]))

    rus_bonus_star_master, en_bonus_star_master = get_sentences(
        type_sentence='bonus_star_master_button',
        sentences_db=sentences_db)
    dp.register_message_handler(bonus_star_master, Text(equals=[rus_bonus_star_master, en_bonus_star_master]))

    rus_bonus_royal_master, en_bonus_royal_master = get_sentences(
        type_sentence='bonus_royal_master_button',
        sentences_db=sentences_db)
    dp.register_message_handler(bonus_royal_master, Text(equals=[rus_bonus_royal_master, en_bonus_royal_master]))

    rus_bonus_crown_master, en_bonus_crown_master = get_sentences(
        type_sentence='bonus_crown_master_button',
        sentences_db=sentences_db)
    dp.register_message_handler(bonus_crown_master, Text(equals=[rus_bonus_crown_master, en_bonus_crown_master]))

    rus_bonus_imperial_master, en_bonus_imperial_master = get_sentences(
        type_sentence='bonus_imperial_master_button',
        sentences_db=sentences_db)
    dp.register_message_handler(bonus_imperial_master, Text(equals=[rus_bonus_imperial_master,
                                                                    en_bonus_imperial_master]))
