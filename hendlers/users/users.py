from main import dp
from fsm import StateUser


dp.register_message_handler(cmd_start, state=StateUser.waiting_id)
