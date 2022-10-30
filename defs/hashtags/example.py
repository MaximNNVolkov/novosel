import app_logger as loger
from main import types
from defs import User
from aiogram.utils import markdown as fmt


log = loger.get_logger(__name__)


async def example(message: types.Message):
    u = User(message.from_user, message.chat.id)
    log.info('пример работы с хэштегом' + u.info_user())
    await message.reply(text=fmt.text(
            fmt.text(u.get_url(), ', ', sep=''),
            fmt.text('Получено сообщение с хэштегом '),
            sep=''))
