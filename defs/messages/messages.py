import app_logger as loger
from main import types
from aiogram.utils import markdown as fmt
from defs.classes import User


log = loger.get_logger(__name__)


async def other_msg(message: types.Message):
    u = User(message.from_user, message.chat.id)
    log.info(u.info_user())
    await message.reply(text=fmt.text(
            fmt.text(u.get_url(), ', ', sep=''),
            fmt.text('Я прочитал Ваше сообщение'),
            sep=''))
