from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from buttons.reply.about_company_product_buttons import create_about_company_product_menu
from create_bot.bot import dp
from databases.client import UsersDB, SentencesDB
from handlers.base_handlers import create_handler, get_sentences


async def about_company_products(message: Message):
    user_db = UsersDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence_db = SentencesDB()
    sentence = sentence_db.get_sentence(type_sentence='about_company_products', language=language)
    photo = sentence_db.get_photo_id(type_sentence='about_company_products', language=language)
    if not photo:
        await message.answer(sentence, parse_mode='html',
                             reply_markup=await create_about_company_product_menu(language=language,
                                                                                  sentences_db=sentence_db))
    else:
        path = 'beget_tech/media/' + photo
        with open(path, 'rb') as object_photo:
            await message.answer_photo(photo=object_photo, caption=sentence,
                                       reply_markup=await create_about_company_product_menu(language=language,
                                                                                            sentences_db=sentence_db),
                                       parse_mode='html')


async def about_company_product_health(message: Message):
    await create_handler(message, 'about_company_product_health')


async def about_company_product_hair(message: Message):
    await create_handler(message, 'about_company_product_hair')


async def about_company_product_skin(message: Message):
    await create_handler(message, 'about_company_product_skin')


async def about_company_product_oral(message: Message):
    await create_handler(message, 'about_company_product_oral')


def register_about_company_product_handlers():
    sentence_db = SentencesDB()
    rus_about_product, en_about_product = get_sentences(type_sentence='about_company_products_button',
                                                        sentences_db=sentence_db)
    dp.register_message_handler(about_company_products, Text(equals=[rus_about_product, en_about_product]))

    rus_health, en_health = get_sentences(type_sentence='about_company_product_health_button',
                                          sentences_db=sentence_db)
    dp.register_message_handler(about_company_product_health, Text(equals=[rus_health, en_health]))

    rus_hair, en_hair = get_sentences(type_sentence='about_company_product_hair_button',
                                      sentences_db=sentence_db)
    dp.register_message_handler(about_company_product_hair, Text(equals=[rus_hair, en_hair]))

    rus_skin, en_skin = get_sentences(type_sentence='about_company_product_skin_button',
                                      sentences_db=sentence_db)
    dp.register_message_handler(about_company_product_skin, Text(equals=[rus_skin, en_skin]))

    rus_oral, en_oral = get_sentences(type_sentence='about_company_product_oral_button',
                                      sentences_db=sentence_db)
    dp.register_message_handler(about_company_product_oral, Text(equals=[rus_oral, en_oral]))
