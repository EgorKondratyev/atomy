from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from create_bot.bot import dp
from create_bot.config import admins
from databases.client import SentencesDB
from handlers.stop_fsm import create_keyboard_stop_fsm
from states.set_video_states import SetVideoFSM


# @dp.message_handler(commands='video_rus', state=None)
async def get_video_rus(message: Message):
    if message.from_user.id in admins:
        await message.answer('Отправь мне видео, которые будет отображаться только для русских пользователей!')
        await SetVideoFSM.get_video_rus.set()


# @dp.message_handler(content_types='any', state=SetVideoFSM.get_video_rus)
async def set_video_rus(message: Message, state: FSMContext):
    if message.video:
        await state.finish()
        SentencesDB().set_video_in_sentence(type_sentence='video_presentation', language=True,
                                            video_id=message.video.file_id)
        await message.answer('Видео успешно установлено!')
    else:
        await message.answer('Необходимо отправить видео!', reply_markup=create_keyboard_stop_fsm())


async def get_video_en(message: Message, state: FSMContext):
    if message.from_user.id in admins:
        await message.answer('Отправь мне видео, которые будет отображаться только для англоязычных пользователей!')
        await SetVideoFSM.get_video_en.set()


# @dp.message_handler(content_types='any', state=SetVideoFSM.get_video_en)
async def set_video_en(message: Message, state: FSMContext):
    if message.video:
        await state.finish()
        SentencesDB().set_video_in_sentence(type_sentence='video_presentation', language=False,
                                            video_id=message.video.file_id)
        await message.answer('Видео успешно установлено!')
    else:
        await message.answer('Необходимо отправить видео!', reply_markup=create_keyboard_stop_fsm())


def register_set_video_handlers():
    dp.register_message_handler(get_video_rus, commands='video_rus', state=None)
    dp.register_message_handler(set_video_rus, content_types='any', state=SetVideoFSM.get_video_rus)
    dp.register_message_handler(get_video_en, commands='video_en', state=None)
    dp.register_message_handler(set_video_en, content_types='any', state=SetVideoFSM.get_video_en)
