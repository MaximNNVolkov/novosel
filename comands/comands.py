import app_logger as log
from aiogram import types
from aiogram.utils import markdown as fmt
from defs.users import opros_start
from defs.classes import User
from aiogram.dispatcher import FSMContext
from keyboards import inline


log = log.get_logger(__name__)


async def cmd_start(message: types.Message, state: FSMContext):
    u = User(message.from_user)
    log.info('кнопка старт. ' + u.info_user())
    await state.reset_state(with_data=True)
    await message.bot.delete_message(chat_id=u.id, message_id=message.message_id)
    await message.bot.send_message(chat_id=message.from_user.id,
                                   text=fmt.text(
        fmt.text('Добрый день,'),
        fmt.text(u.get_url(), '!', sep=''),
        fmt.text("Сбер непрерывно работает над улучшением качества жизни своих клиентов,"),
        fmt.text('проявляя заботу и создавая комфорт.'),
        fmt.text('Помогите нам стать ещё лучше для Вас!'),
        fmt.text('Ответьте, пожалуйста, на вопросы:'),
        sep=' '))
    await opros_start(msg=message, state=state)


async def cmd_help(message: types.Message, state: FSMContext):
    u = User(message.from_user)
    log.info('кнопка хэлп ' + u.info_user())
    await state.reset_state(with_data=True)
    await message.bot.delete_message(chat_id=u.id, message_id=message.message_id)
    await message.bot.send_message(chat_id=message.from_user.id, text=fmt.text(
            fmt.text(u.get_url(), ', ', sep=''),
            fmt.text('Напишите Ваш вопрос, перешлю его админимстратору.'),
            sep=''), reply_markup=inline.UsersHelp.create_kb())


async def bot_block_error(message: types.Message):
    await message.reply("Что то не так. Давай снова /start")
