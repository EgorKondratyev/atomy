from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from databases.client import SentencesDB


async def create_start_menu(language: bool, sentences_db: SentencesDB) -> ReplyKeyboardMarkup:
    start_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    # Кнопка слогана
    text_button_slogan = sentences_db.get_sentence(type_sentence='button_slogan', language=language)
    button_slogan = KeyboardButton(text=text_button_slogan)
    start_menu.insert(button_slogan)

    text_button_what_pay = sentences_db.get_sentence(type_sentence='what_pay_button', language=language)
    button_what_pay = KeyboardButton(text=text_button_what_pay)
    start_menu.insert(button_what_pay)

    return start_menu
