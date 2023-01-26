from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from databases.client import SentencesDB


async def create_about_company_product_menu(language: bool, sentences_db: SentencesDB) -> ReplyKeyboardMarkup:
    about_company_product_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    health_text = sentences_db.get_sentence(type_sentence='about_company_product_health_button', language=language)
    health_button = KeyboardButton(text=health_text)
    about_company_product_menu.insert(health_button)

    hair_text = sentences_db.get_sentence(type_sentence='about_company_product_hair_button', language=language)
    hair_button = KeyboardButton(text=hair_text)
    about_company_product_menu.insert(hair_button)

    skin_text = sentences_db.get_sentence(type_sentence='about_company_product_skin_button', language=language)
    skin_button = KeyboardButton(text=skin_text)
    about_company_product_menu.insert(skin_button)

    oral_text = sentences_db.get_sentence(type_sentence='about_company_product_oral_button', language=language)
    oral_button = KeyboardButton(text=oral_text)
    about_company_product_menu.insert(oral_button)

    if language:
        back_text = 'Назад'
    else:
        back_text = 'Back'
    back_button = KeyboardButton(text=back_text)
    about_company_product_menu.add(back_button)
    return about_company_product_menu
