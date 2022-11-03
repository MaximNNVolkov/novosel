from comands import cmd_start, cmd_help, cmd_sales
from aiogram import Dispatcher
from fsm.users import StateUser


def register_commands(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state='*')
    dp.register_message_handler(cmd_help, commands="help", state='*')
    dp.register_message_handler(cmd_sales, commands="sales", state='*')
