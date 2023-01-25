from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from databases.client import SentencesDB


language_menu = InlineKeyboardMarkup(row_width=2)
rus_button = InlineKeyboardButton(text='Русский🇷🇺', callback_data='language_russian')
en_button = InlineKeyboardButton(text='English🇬🇧', callback_data='language_english')
language_menu.insert(rus_button).insert(en_button)


async def create_start_menu(language: bool):
    sentences_db = SentencesDB()
    text_button_slogan = sentences_db.get_sentence(type_sentence='button_slogan', language=language)

