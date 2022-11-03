import app_logger as loger
from aiogram.utils import markdown as fmt
from defs.classes import User
from fsm import StateUser
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from .checks import CheckMsg

log = loger.get_logger(__name__)


async def sales_start(msg: Message, state: FSMContext):
    u = User(msg.from_user)
    log.info(u.info_user())
    await state.set_state(StateUser.waiting_id)
    await msg.answer(text=fmt.text(
            fmt.text(u.get_url(), ', ', sep=''),
            fmt.text('Введите Ваш id'),
            sep=''))


async def enter_id(msg: Message, state: FSMContext):
    u = User(msg.from_user)
    log.info(await state.get_state())
    if CheckMsg.CheckNum(msg.text):
        await state.set_state(StateUser.check_id)
        await msg.answer(text='Отлично')
    else:
        await state.set_state(StateUser.waiting_id)
        await msg.answer(text='Только цифры. Давай снова')
