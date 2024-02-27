from fsm import StateUser
from aiogram import Dispatcher
from defs.users.user_opros import write_answer_1, write_answer_2, write_answer_3, write_answer_4, write_answer_5
from keyboards.inline import UsersVopros_1, UsersVopros_2, UsersVopros_3, UsersVopros_4, UsersVopros_5


def register_user(dp: Dispatcher):
    dp.register_callback_query_handler(write_answer_1, UsersVopros_1().cb.filter(), state=StateUser.vopros_1)
    dp.register_callback_query_handler(write_answer_2, UsersVopros_2().cb.filter(), state=StateUser.vopros_2)
    dp.register_callback_query_handler(write_answer_3, UsersVopros_3().cb.filter(), state=StateUser.vopros_3)
    dp.register_callback_query_handler(write_answer_4, UsersVopros_4().cb.filter(), state=StateUser.vopros_4)
    dp.register_callback_query_handler(write_answer_5, UsersVopros_5().cb.filter(), state=StateUser.vopros_5)
