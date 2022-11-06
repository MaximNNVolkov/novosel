import app_logger as loger
from aiogram.utils import markdown as fmt
from defs.classes import User
from fsm import StateUser
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from .checks import CheckMsg


log = loger.get_logger(__name__)
txt_false = 'Вводи только цифры. Давай снова'


async def sales_start(msg: Message, state: FSMContext):
    u = User(msg.from_user)
    log.info(u.info_user())
    await state.set_state(StateUser.enter_id)
    await msg.answer(text=fmt.text(
            fmt.text(u.get_url(), ', ', sep=''),
            fmt.text('Введите Ваш id'),
            sep=''))


async def enter_id(msg: Message, state: FSMContext):
    u = User(msg.from_user)
    log.info(' '.join([await state.get_state(), msg.text]))
    if CheckMsg.CheckNum(msg.text):
        await state.set_data(msg.text)
        await state.set_state(StateUser.enter_bch)
        await msg.answer(text='Отлично. {}'.format(await state.get_data()))
        await msg.answer(text='Введи БЧ.')
    else:
        await msg.answer(text=txt_false)


async def enter_bch(msg: Message, state: FSMContext):
    u = User(msg.from_user)
    log.info(' '.join([await state.get_state(), msg.text]))
    if CheckMsg.CheckNum(msg.text):
        await state.set_data(msg.text)
        await state.set_state(StateUser.enter_sup)
        await msg.answer(text='Отлично. {}'.format(await state.get_data()))
        await msg.answer(text='Введите СУП.')
    else:
        await msg.answer(text=txt_false)


async def enter_sup(msg: Message, state: FSMContext):
    u = User(msg.from_user)
    log.info(' '.join([await state.get_state(), msg.text]))
    if CheckMsg.CheckNum(msg.text):
        await state.set_data(msg.text)
        await state.set_state(StateUser.enter_sprime)
        await msg.answer(text='Отлично. {}'.format(await state.get_data()))
    else:
        await msg.answer(text=txt_false)
