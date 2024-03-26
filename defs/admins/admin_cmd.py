import app_logger as loger
from aiogram import types
from aiogram.dispatcher import FSMContext
from fsm.admins import StateAdmin
from aiogram.utils import markdown as fmt
from defs.classes import User
from database.admins.admin_query import get_users_list, get_answers_list
from keyboards.inline.admin import AdminDates
from datetime import datetime, timedelta


log = loger.get_logger(__name__)
admin_commands = ['/get_users', '/get_answers']


async def admin_cmd(message: types.Message, state: FSMContext):
    u = User(message.from_user)
    log.info(u.info_user())
    log.info(f'Вход в режим Admin. Пользователь {u.info_user()}')
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await state.set_state(StateAdmin.admin_enter)
    await message.bot.send_message(chat_id=u.id,
                                   text=fmt.text(
                                       fmt.text(f'Привет, {u.get_url()}!'),
                                       fmt.text('Вы вошли в режим администратора.'),
                                       fmt.text(f'Доступны команды: {", ".join(admin_commands)}'),
                                       fmt.text('Для выхода из режима администратора отправьте команду /exit_admin'),
                                       sep='\n')
                                   )


async def exit_admin(message: types.Message, state: FSMContext):
    u = User(message.from_user)
    log.info(u.info_user())
    log.info(f'Выход из режима Admin. Пользователь {u.info_user()}')
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await state.reset_state()
    await message.bot.send_message(chat_id=u.id,
                                   text=fmt.text(
                                       fmt.text(f'{u.get_url()}, Вы вышли из режима администратора.'),
                                       sep='\n')
                                   )


async def get_users(message: types.Message, state: FSMContext):
    u = User(message.from_user)
    log.info(u.info_user())
    log.info(f'Admin. Получение всех пользователей. Пользователь {u.info_user()}')
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await state.set_data({'stat': 'users'})
    await message.bot.send_message(chat_id=u.id,
                                   text=fmt.text(
                                       fmt.text('Всего зарегистрировано пользователей'),
                                       fmt.text(len(get_users_list())),
                                       sep=' '),
                                   reply_markup=AdminDates().create_kb()
                                   )


async def get_answers(message: types.Message, state: FSMContext):
    u = User(message.from_user)
    log.info(u.info_user())
    log.info(f'Admin. Получение всех ответов. Пользователь {u.info_user()}')
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await state.set_data({'stat': 'answers'})
    await message.bot.send_message(chat_id=u.id,
                                   text=fmt.text(
                                       fmt.text('Всего получено ответов'),
                                       fmt.text(len(get_answers_list())),
                                       sep=' '),
                                   reply_markup=AdminDates().create_kb()
                                   )


def between_list(period: str):
    if period == 'today':
        return [str(datetime.now().date()), str(datetime.now().date()+timedelta(days=+1))]
    if period == 'yesterday':
        return [str(datetime.now().date()+timedelta(days=-1)), str(datetime.now().date())]
    if period == 'week':
        return [str(datetime.now().date()+timedelta(weeks=-1)), str(datetime.now().date())]
    if period == 'month':
        return [str(datetime.now().date()+timedelta(weeks=-4)), str(datetime.now().date())]


async def get_data_between(cb: types.CallbackQuery, state: FSMContext):
    u = User(cb.from_user)
    log.info(u.info_user())
    log.info(f'Admin. Уточнение диапазона дат. Пользователь {u.info_user()}')
    period = between_list(cb.data.split(':')[1])
    print(period)
    data = await state.get_data()
    if data['stat'] == 'users':
        res = get_users_list(period)
    elif data['stat'] == 'answers':
        res = get_answers_list(period)
    else:
        log.info(f'Admin. Уточнение диапазона дат. Получено значение {data}. Пользователь {u.info_user()}')
    await cb.message.bot.send_message(chat_id=u.id,
                                      text=fmt.text(
                                          fmt.text('За период'),
                                          fmt.text(len(res)),
                                          sep=' ')
                                      )
