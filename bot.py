import logging
import asyncio

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('LogTag')

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from stickers import stickers

bot = Bot(token='5916056261:AAFYOJ34fmwBpbdY9uGtDVK20A2POdBB3JA')

dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Рад Вас приветствовать! Я могу протестировать Вас на наличие симптомов при диабете. Для начала напишите команду /begin"
                         "Если хотите узнать чем опасен диабет, напишите команду /info_d")#написать описание, дисклеймер

@dp.message_handler(commands=["stop"])
async def cmd_start(message: types.Message):
    await message.answer("Bye-bye :c")

@dp.message_handler()
async def hello_responce(msg:types.Message):
    if 'hello' in msg.text.lower():
        await bot.send_message(msg.from_user.id,f'hi,{msg.from_user.first_name})')
        await bot.send_sticker(msg.from_user.id,sticker=stickers['Puppy'])
    elif 'gotta go' in msg.text.lower():
        await bot.send_message(msg.from_user.id,f'have a nice day,{msg.from_user.first_name})')

@dp.message_handler(content_types=['sticker'])
async def st(msg:types.Message):
    print(msg.sticker)
    await msg.reply('imba')
    await bot.send_sticker(msg.from_user.id, sticker=stickers['Like'])

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
