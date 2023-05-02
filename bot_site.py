import logging
import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode, InputFile
from aiogram.utils import executor
from create_bot import dp
from my_handlers import handlers_d , handlers_c

logging.basicConfig(level=logging.INFO)

handlers_d.register_handlers_d(dp)
handlers_c.register_handlers_c(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)