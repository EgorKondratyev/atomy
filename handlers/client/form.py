from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from create_bot.bot import dp
from databases.client import UsersDB, SentencesDB
from handlers.base_handlers import get_sentences
from states.form_states import FormFSM


async def form_first(message: Message):
    user_db = UsersDB()
    language = user_db.get_language_user(message.from_user.id)
    sentence = SentencesDB().get_sentence(type_sentence='form_first', language=language)
    await message.answer(sentence, parse_mode='html')
    await FormFSM


def register_form_handlers():
    sentences_db = SentencesDB()

    rus_form, en_form = get_sentences(type_sentence='form_button', sentences_db=sentences_db)
    dp.register_message_handler(form_first, Text(equals=[rus_form, en_form]), state=None)
