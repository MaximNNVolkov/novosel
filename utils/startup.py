import logging

from aiogram import types
import app_logger as loger


log = loger.get_logger(__name__)


async def set_default(dp):
    res = await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
    ])
    log.debug('commands set result {}'.format(res))
    dp.bot.parse_mode = 'HTML'
