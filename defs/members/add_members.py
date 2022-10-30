import app_logger as loger
from main import types
from aiogram.utils import markdown as fmt
from defs.classes import User


log = loger.get_logger(__name__)


async def new_member(message: types.Message):
    for u in message.new_chat_members:
        u = User(u, message.chat.id)
        log.info(u.info_user())
        if u.add_user() == 'new_user':
            await message.reply(text=fmt.text(
                fmt.text(u.get_url(), ', ', sep=''),
                fmt.text('расскажите немного подробнее. Нам очень интересно узнать побольше о Вас.'),
                sep=''))
