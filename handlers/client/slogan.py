from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from create_bot.bot import dp
from databases.client import UsersDB, SentencesDB


# @dp.message_handler(content_types='any')
# async def foo(message: Message):
#     print(message)


async def slogan(message: Message):
    user_db = UsersDB()
    sentences_db = SentencesDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence = sentences_db.get_sentence(type_sentence='slogan', language=language)
    await message.answer(sentence, parse_mode='html')



def register_slogan_handlers():
    sentences_db = SentencesDB()
    rus_slogan = sentences_db.get_sentence(type_sentence='button_slogan', language=True)
    en_slogan = sentences_db.get_sentence(type_sentence='button_slogan', language=False)
    dp.register_message_handler(slogan, Text(equals=[en_slogan, rus_slogan]))
