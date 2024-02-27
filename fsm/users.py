import app_logger as logger
from aiogram.dispatcher.filters.state import State, StatesGroup


log = logger.get_logger(__name__)


class StateUser(StatesGroup):
    vopros_1 = State()
    vopros_2 = State()
    vopros_3 = State()
    vopros_4 = State()
    vopros_5 = State()
    result = State()
