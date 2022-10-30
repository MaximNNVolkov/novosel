from main import dp, types
from aiogram.dispatcher.filters.builtin import ChatTypeFilter
from defs.members.add_members import new_member


# dp.register_message_handler(new_member, ChatTypeFilter(chat_type=types.ChatType.SUPERGROUP),
#                            content_types=types.ContentType.NEW_CHAT_MEMBERS)
