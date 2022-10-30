from main import dp, types
from aiogram.dispatcher.filters.builtin import ChatTypeFilter
from defs.hashtags.example import example

dp.register_message_handler(example,
                            ChatTypeFilter(chat_type=types.ChatType.SUPERGROUP),
                            hashtags='example')
