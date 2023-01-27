import traceback

from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from create_bot.bot import dp
from databases.client import UsersDB, SentencesDB


async def slogan(message: Message):
    user_db = UsersDB()
    sentences_db = SentencesDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence = sentences_db.get_sentence(type_sentence='slogan', language=language)
    photo = sentences_db.get_photo_id(type_sentence='slogan', language=language)
    if not photo:
        await message.answer(sentence, parse_mode='html')
    else:
        path = 'beget_tech/media/' + photo
        with open(path, 'rb') as object_photo:
            await message.answer_photo(photo=object_photo, caption=sentence)




def register_slogan_handlers():
    sentences_db = SentencesDB()
    rus_slogan = sentences_db.get_sentence(type_sentence='button_slogan', language=True)
    en_slogan = sentences_db.get_sentence(type_sentence='button_slogan', language=False)
    dp.register_message_handler(slogan, Text(equals=[en_slogan, rus_slogan]))
