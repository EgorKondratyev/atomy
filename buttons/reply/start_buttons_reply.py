from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from databases.client import SentencesDB


async def create_start_menu(language: bool, sentences_db: SentencesDB) -> ReplyKeyboardMarkup:
    start_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    # Кнопка слогана
    text_button_slogan = sentences_db.get_sentence(type_sentence='button_slogan', language=language)
    button_slogan = KeyboardButton(text=text_button_slogan)
    start_menu.insert(button_slogan)

    # Кнопка за что платят?
    text_button_what_pay = sentences_db.get_sentence(type_sentence='what_pay_button', language=language)
    button_what_pay = KeyboardButton(text=text_button_what_pay)
    start_menu.insert(button_what_pay)

    text_about_product = sentences_db.get_sentence(type_sentence='about_company_products_button', language=language)
    button_about_product = KeyboardButton(text=text_about_product)
    start_menu.insert(button_about_product)

    text_form = sentences_db.get_sentence(type_sentence='form_button', language=language)
    button_form = KeyboardButton(text=text_form)
    start_menu.insert(button_form)

    return start_menu
