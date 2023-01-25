import traceback

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from create_bot.bot import dp, bot
from databases.client import SentencesDB, UsersDB
from buttons.inline.start_buttons import language_menu
from buttons.reply.start_buttons_reply import create_start_menu
from states.start_states import ChoiceLanguageFSM


# @dp.message_handler(commands='start')
async def start_command(message: Message):
    user_db = UsersDB()
    if not user_db.exists_user(user_id=message.from_user.id):
        await message.answer('Please select a language for further interaction with the bot',
                             reply_markup=language_menu)
        await ChoiceLanguageFSM.choice.set()
    else:
        sentence_db = SentencesDB()
        language = user_db.get_language_user(user_id=message.from_user.id)
        sentence = sentence_db.get_sentence(type_sentence='start', language=language)
        if sentence:
            await message.answer(f'{sentence}', parse_mode='html',
                                 reply_markup=await create_start_menu(language=language, sentences_db=sentence_db))


# @dp.callback_query_handler(Text(startswith='language_'), state=ChoiceLanguageFSM.choice)
async def set_language(callback: CallbackQuery, state: FSMContext):
    language = callback.data.split('_')[1]
    user_db = UsersDB()
    if language == 'russian':
        await callback.answer('Успешно')
        user_db.add_user(user_id=callback.from_user.id, language=True)
    else:
        await callback.answer('Success')
        user_db.add_user(user_id=callback.from_user.id, language=False)
    await state.finish()

    sentence_db = SentencesDB()
    language = user_db.get_language_user(user_id=callback.from_user.id)
    sentence = sentence_db.get_sentence(type_sentence='start', language=language)
    if sentence:
        await callback.message.answer(f'{sentence}', parse_mode='html',
                                      reply_markup=await create_start_menu(language=language, sentences_db=sentence_db))


def register_start_command_handlers():
    dp.register_message_handler(start_command, commands='start')
    dp.register_callback_query_handler(set_language, Text(startswith='language_'), state=ChoiceLanguageFSM.choice)
