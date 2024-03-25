from aiogram import Dispatcher
from defs.admins.admin_cmd import admin_cmd, exit_admin, get_users, get_answers, get_data_between
from fsm.admins import StateAdmin
from keyboards.inline.admin import AdminDates


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_cmd, is_admin=True, commands="admin")
    dp.register_message_handler(exit_admin, state=StateAdmin.admin_enter, commands="exit_admin")
    dp.register_message_handler(get_users, state=StateAdmin.admin_enter, commands="get_users")
    dp.register_message_handler(get_answers, state=StateAdmin.admin_enter, commands="get_answers")
    dp.register_callback_query_handler(get_data_between, AdminDates().cb.filter(), state=StateAdmin.admin_enter)
