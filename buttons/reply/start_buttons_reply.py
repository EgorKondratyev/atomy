from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from databases.client import SentencesDB


async def create_start_menu(language: bool, sentences_db: SentencesDB) -> ReplyKeyboardMarkup:
    start_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    # Кнопка слогана
    text_button_slogan = sentences_db.get_sentence(type_sentence='button_slogan', language=language)
    button_slogan = KeyboardButton(text=text_button_slogan)
    start_menu.insert(button_slogan)

    return start_menu
