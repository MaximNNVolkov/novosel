from fsm import StateUser
from aiogram import Dispatcher
from defs import enter_id, enter_bch


def register_user(dp: Dispatcher):
    dp.register_message_handler(enter_id, state=StateUser.enter_id)
    dp.register_message_handler(enter_bch, state=StateUser.enter_bch)
