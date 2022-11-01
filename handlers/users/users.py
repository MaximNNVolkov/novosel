from fsm import StateUser
from aiogram import Dispatcher
from defs import enter_id


def register_user(dp: Dispatcher):
    dp.register_message_handler(enter_id, state=StateUser.waiting_id)
