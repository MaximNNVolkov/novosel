from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from database.admins.admin_query import admins_list
from aiogram.utils import markdown as fmt


class IsAdmin(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, msg: Message):
        admins = admins_list()
        admins = [x[0] for x in admins]
        user = msg.from_user.id
        if user not in admins:
            await msg.answer(fmt.text(
                fmt.text('Эта команда доступна только  для администраторов.'),
                fmt.text('Обратитесь к @MaximVolkov для получения доступа'),
                sep='\n')
            )
        return user in admins
