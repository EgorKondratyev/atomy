import traceback

from aiogram.types import Message, ContentType

from create_bot.bot import dp, bot


# @dp.message_handler(commands='start')
async def start_command(message: Message):
    await message.answer('hello')


def register_start_command_handlers():
    dp.register_message_handler(start_command, commands='/start')
