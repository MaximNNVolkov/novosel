from aiogram.dispatcher.filters.state import State, StatesGroup


class StateAdmin(StatesGroup):
    admin_enter = State()
    add_admin = State()
    add_photo = State()
