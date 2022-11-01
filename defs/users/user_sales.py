import app_logger as loger
from aiogram.utils import markdown as fmt
from defs.classes import User
from fsm import StateUser
from aiogram.dispatcher import FSMContext
from aiogram import Bot
from aiogram.types import Message


log = loger.get_logger(__name__)


async def sales_start(bot: Bot, user, state: FSMContext):
    u = User(user)
    log.info(u.info_user())
    await state.set_state(StateUser.waiting_id)
    await bot.send_message(chat_id=u.id, text=fmt.text(
            fmt.text(u.get_url(), ', ', sep=''),
            fmt.text('Введите Ваш id'),
            sep=''))


async def enter_id(msg: Message, state: FSMContext):
    u = User(msg.from_user)
    log.info(u.info_user())
    await state.set_state(StateUser.waiting_id)
    await msg.answer(text='OK')
