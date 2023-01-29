from importlib import reload
from aiogram.types import Message

from create_bot.bot import dp


# @dp.message_handler(commands='help_admin')
async def help_command_for_admin(message: Message):
    from handlers import register_handlers
    reload(register_handlers)
    await message.answer('Все кнопки успешно перезагружены!')


def register_change_admin_handlers():
    dp.register_message_handler(help_command_for_admin, commands='reload')
