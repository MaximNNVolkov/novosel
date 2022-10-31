import app_logger as log
from aiogram import types
from defs.users import sales_start


my_log = log.get_logger(__name__)


async def cmd_start(message: types.Message):
    my_log.info('кнопка старт')
    await message.bot.send_message(chat_id=message.from_user.id, text="Привет. Пришли фотографию чека с QR кодом.")


async def cmd_help(message: types.Message):
    my_log.info('кнопка хэлп')
    await message.bot.send_message(chat_id=message.from_user.id, text="Получил просьбу о помощи")


async def cmd_sales(message: types.Message, state='*'):
    my_log.info('кнопка sales')
    await message.bot.send_message(chat_id=message.from_user.id, text="Введите Ваш ID")
    await sales_start(message=message, state=state)


async def bot_block_error(message: types.Message):
    await message.reply("Что то не так. Давай снова /start")
