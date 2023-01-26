from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


language_menu = InlineKeyboardMarkup(row_width=2)
rus_button = InlineKeyboardButton(text='Русский🇷🇺', callback_data='language_russian')
en_button = InlineKeyboardButton(text='English🇬🇧', callback_data='language_english')
language_menu.insert(rus_button).insert(en_button)
