import logging

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, InputFile
from aiogram.utils import executor

from bot1.config.config import TOKEN
from bot1.keyboard.keybard import reply_keyboard
from bot1.perevod import Translate

logging.basicConfig(level=logging.INFO)




bot = Bot(token=TOKEN)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

t=Translate()

# States
class Form(StatesGroup):
    #name = State()  # Will be represented in storage as 'Form:name'
    age = State()  # Will be represented in storage as 'Form:age'
    gender = State()  # Will be represented in storage as 'Form:gender'
    q1 = State()
    # q2 = State()
    # q3 = State()
    # q4 = State()
    # q5 = State()
    # q6 = State()
    # q7 = State()
    # q8 = State()
    # q9 = State()
    # q10 = State()
    # q11 = State()
    # q12 = State()
    # q13 = State()
    q14 = State()


@dp.message_handler(commands='begin')
async def cmd_start(message: types.Message):
    """
    начало опроса
    """
    # Set state
    await Form.age.set()

    await message.reply("Укажи свой возраст")



# You can use state '*' if you need to handle all states
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())



@dp.message_handler(state=Form.q1)
async def process_name(message: types.Message, state: FSMContext):
    """
    первый вопрос
    """
    async with state.proxy() as data:
        data['q1'] = t.process_one(message.text)

    await Form.next()
    await message.reply("второй вопрос",reply_markup=reply_keyboard)

@dp.message_handler(state=Form.q14)
async def process_name(message: types.Message, state: FSMContext):
    """
    последний вопрос
    """
    async with state.proxy() as data:
        data['q14'] = t.process_one(message.text)
    markup = types.ReplyKeyboardRemove()
    #тут надо отправить ответ
    # Finish conversation


    # And send message
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text('Age:', md.code(data['age'])),
            md.text('Gender:', data['gender']),
            md.text('Q1:', data['q1']),
            md.text('Q14:', data['q1']),
            sep='\n',
        ),
        reply_markup=markup,
        parse_mode=ParseMode.MARKDOWN,
    )

    await state.finish()

# Check age. Age gotta be digit
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def process_age_invalid(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Age gotta be a number.\nHow old are you? (digits only)")


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    # Update state and data
    await Form.next()
    await state.update_data(age=int(message.text))

    # Configure ReplyKeyboardMarkup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Мужской", "Женский")

    await message.reply("Укажи свой пол", reply_markup=markup)


@dp.message_handler(lambda message: message.text not in ["Мужской", "Женский"], state=Form.gender)
async def process_gender_invalid(message: types.Message):
    """
    In this example gender has to be one of: Male, Female, Other.
    """
    return await message.reply("Я тебя не понимаю. Выбери свой пол из клавиатуры")


@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = t.process_one(message.text)
        await Form.next()
        await message.reply("ПЕРВЫЙ вопрос", reply_markup=reply_keyboard)





@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Рад Вас приветствовать! Я могу протестировать Вас на наличие симптомов при диабете. Для начала напишите команду /begin \n" \
                         "Если хотите узнать, чем опасен диабет, напишите команду /info \n" \
                         "Для завершения работы бота напишите команду /stop")#написать описание, дисклеймер

@dp.message_handler(commands=["stop"])
async def cmd_start(message: types.Message):
    await message.answer("Bye-bye :c")

@dp.message_handler(commands=["info"])
async def cmd_start(msg: types.Message):
    photo = InputFile("diabetes.jpg")
    await bot.send_photo(msg.chat.id, photo=photo)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)