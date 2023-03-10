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
from bot1.perevod import Translate
from diabet import predict

logging.basicConfig(level=logging.INFO)


list=list()

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
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State()
    q8 = State()
    q9 = State()
    q10 = State()
    q11 = State()
    q12 = State()
    q13 = State()
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
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("Вы испытываете неутолимую жажду?",reply_markup=reply_keyboard)

@dp.message_handler(state=Form.q2)
async def process_name(message: types.Message, state: FSMContext):
    """
    второй вопрос
    """
    async with state.proxy() as data:
        data['q2'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("Внезапная потеря веса?",reply_markup=reply_keyboard)

@dp.message_handler(state=Form.q3)
async def process_name(message: types.Message, state: FSMContext):
    """
    третий вопрос
    """
    async with state.proxy() as data:
        data['q3'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("слабость?",reply_markup=reply_keyboard)

@dp.message_handler(state=Form.q4)
async def process_name(message: types.Message, state: FSMContext):
    """
    четвертый вопрос
    """
    async with state.proxy() as data:
        data['q4'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("Повышенный аппетит, прожорливость?",reply_markup=reply_keyboard)


@dp.message_handler(state=Form.q5)
async def process_name(message: types.Message, state: FSMContext):
    """
    пятый вопрос
    """
    async with state.proxy() as data:
        data['q5'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("Вы больны кандидозом(жжение и зуд в области наружных половых органов)?", reply_markup=reply_keyboard)


@dp.message_handler(state=Form.q6)
async def process_name(message: types.Message, state: FSMContext):
    """
    шестой вопрос
    """
    async with state.proxy() as data:
        data['q6'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("Визуальное размытие?", reply_markup=reply_keyboard)


@dp.message_handler(state=Form.q7)
async def process_name(message: types.Message, state: FSMContext):
    """
    седьмой вопрос
    """
    async with state.proxy() as data:
        data['q7'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("Зуд?", reply_markup=reply_keyboard)


@dp.message_handler(state=Form.q8)
async def process_name(message: types.Message, state: FSMContext):
    """
    восьмой вопрос
    """
    async with state.proxy() as data:
        data['q8'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("Раздражительность?", reply_markup=reply_keyboard)


@dp.message_handler(state=Form.q9)
async def process_name(message: types.Message, state: FSMContext):
    """
    девятый вопрос
    """
    async with state.proxy() as data:
        data['q9'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("Есть задержка заживления ран?", reply_markup=reply_keyboard)


@dp.message_handler(state=Form.q10)
async def process_name(message: types.Message, state: FSMContext):
    """
    десятый вопрос
    """
    async with state.proxy() as data:
        data['q10'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("Вы больны синдромом Пареза(Неврологический синдром, при котором снижаются силы мышц)?", reply_markup=reply_keyboard)


@dp.message_handler(state=Form.q11)
async def process_name(message: types.Message, state: FSMContext):
    """
    одиннадцатый вопрос
    """
    async with state.proxy() as data:
        data['q11'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("Вы ощущаете скованность в мышцах?", reply_markup=reply_keyboard)


@dp.message_handler(state=Form.q12)
async def process_name(message: types.Message, state: FSMContext):
    """
    двенадцатый вопрос
    """
    async with state.proxy() as data:
        data['q12'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("Вы больны алопецией(патологическое выпадение волос)?", reply_markup=reply_keyboard)


@dp.message_handler(state=Form.q13)
async def process_name(message: types.Message, state: FSMContext):
    """
    тринадцатый вопрос
    """
    async with state.proxy() as data:
        data['q13'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form.next()
    await message.reply("Ожирение?", reply_markup=reply_keyboard)


@dp.message_handler(state=Form.q14)
async def process_name(message: types.Message, state: FSMContext):
    """
    последний вопрос
    """
    async with state.proxy() as data:
        data['q14'] = t.process_one(message.text)
        list.append(t.process_one(message.text))
    markup = types.ReplyKeyboardRemove()
    #тут надо отправить ответ
    # Finish conversation


    reply = predict(list)
    otvet = t.process_two(reply)
    await bot.send_message(message.chat.id, otvet,reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN)

    await state.finish()




# Check age. Age gotta be digit
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def process_age_invalid(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Требуются цифры.\nСколько тебе лет? (только цифры)")


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    # Update state and data
    await Form.next()
    await state.update_data(age=int(message.text))
    list.append(float(message.text))
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

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q1)
async def process_q1_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q2)
async def process_q2_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q3)
async def process_q3_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")


@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q4)
async def process_q4_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q5)
async def process_q5_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q6)
async def process_q6_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q7)
async def process_q7_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q8)
async def process_q8_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q9)
async def process_q9_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q10)
async def process_q10_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q11)
async def process_q11_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q12)
async def process_q12_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q13)
async def process_q13_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")

@dp.message_handler(lambda message: message.text not in ["Да", "Нет"], state=Form.q14)
async def process_q14_invalid(message: types.Message):
    """
    проверка да/нет
    """
    return await message.reply("Я тебя не понимаю. Выбери ответ из клавиатуры")


@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = t.process_one(message.text)
        list.append(t.process_one(message.text))
        reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        reply_keyboard.add("Да", "Нет")
        await Form.next()
        await message.reply("Есть ли у Вас признаки полиурии(увеличенное образование мочи)?", reply_markup=reply_keyboard)





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