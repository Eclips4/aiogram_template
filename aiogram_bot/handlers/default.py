from aiogram import types, Dispatcher


async def start(message: types.Message):
    await message.reply("Привет!")


def register_default_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')