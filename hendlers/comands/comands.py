from main import dp, types
from comands import cmd_start, cmd_help, cmd_sales
# from aiogram.dispatcher.filters.builtin import ChatTypeFilter


dp.register_message_handler(cmd_start, commands="start")
dp.register_message_handler(cmd_help, commands="help")
dp.register_message_handler(cmd_sales, commands="sales")
