import app_logger as logger
from aiogram.dispatcher.filters.state import State, StatesGroup
log = logger.getLogger(__name__)


class StateUser(StatesGroup):
    waiting_id = State()
    check_id = State()
    waiting_bch = State()
    waiting_sup = State()
    waiting_sprime = State()
    waiting_szdor = State()
