from aiogram import executor
from create_bot.bot import dp
from log.create_logger import logger
from utils.translator.initialization import start_initialization_sentences


async def start(_):
    logger.debug('Бот успешно запущен!')


async def end(_):
    logger.debug('Бот успешно отключен!')


if __name__ == '__main__':
    start_initialization_sentences()
    from handlers import register_handlers
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=start, on_shutdown=end)
