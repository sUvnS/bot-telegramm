import logging
import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode, InputFile
from aiogram.utils import executor
from create_bot import dp

logging.basicConfig(level=logging.INFO)

from my_handlers import handlers

handlers.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)