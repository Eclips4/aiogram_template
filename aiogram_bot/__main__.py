import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram_bot.config import load_config
from aiogram_bot.handlers.default import register_default_handlers

logging.basicConfig(level=logging.INFO)


async def main():
    config = load_config('./aiogram_bot.ini')
    storage = MemoryStorage()
    bot = Bot(token=config.token)
    dp = Dispatcher(bot, storage=storage)
    register_default_handlers(dp)
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        logging.info("Bot is stopped.")
