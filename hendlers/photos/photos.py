from main import dp, types
from defs.photos import photo_take
from aiogram.dispatcher.filters.builtin import ContentTypeFilter


dp.register_message_handler(photo_take,
                            content_types=types.ContentTypes.PHOTO)
