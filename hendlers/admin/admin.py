from main import dp, types
from defs.admins.admin_cmd import admin_cmd
from aiogram.dispatcher.filters.builtin import ChatTypeFilter, AdminFilter


dp.register_message_handler(admin_cmd,
                            ChatTypeFilter(chat_type=types.ChatType.PRIVATE) and AdminFilter(),
                            commands="admin")
