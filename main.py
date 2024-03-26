import app_logger as log
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.startup import set_default
from config_reader import config


# переменные
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot, storage=MemoryStorage())
logger = log.get_logger(__name__)


if __name__ == "__main__":
    logger.info('bot started')
    executor.start_polling(dispatcher=dp,
                           skip_updates=False,
                           on_startup=set_default)
