from aiogram import types, Dispatcher
import logging
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import dp, bot
from bot1.perevod import Translate



class Form1(StatesGroup):
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


list=[]
t=Translate()
from new_covid import predict_c


async def cmd_start1(message: types.Message):
    """
    начало опроса
    """
    global list
    # Set state
    list = []

    await Form1.age.set()

    await message.reply("Укажите свой возраст")

@dp.message_handler(state='*', commands='cancel')
#@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
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

#@dp.message_handler(lambda message: message.text.isdigit(), state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    # Update state and data

    age = int(message.text)
    if age <= 9:
        list.append(1)
        list.append(0)
        list.append(0)
        list.append(0)
        list.append(0)
    elif 10 <= (age) <= 19:
        list.append(0)
        list.append(1)
        list.append(0)
        list.append(0)
        list.append(0)
    elif 20 <= (age) <= 24:
        list.append(0)
        list.append(0)
        list.append(1)
        list.append(0)
        list.append(0)
    elif 25 <= (age) <= 59:
        list.append(0)
        list.append(0)
        list.append(0)
        list.append(1)
        list.append(0)
    elif (age) >= 60:
        list.append(0)
        list.append(0)
        list.append(0)
        list.append(0)
        list.append(1)

    # Configure ReplyKeyboardMarkup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Мужской", "Женский")

    await Form1.next()
    await message.reply("Укажите свой пол", reply_markup=markup)

#@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
async def process_age_invalid(message: types.Message):
    """
    If age is invalid
    """
    return await message.reply("Требуются цифры.\nСколько тебе лет? (только цифры)")

#@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = t.process_one(message.text)
        if t.process_one(message.text)==1:
            list.append(0)
            list.append(1)
        else:
            list.append(1)
            list.append(0)
        contact_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        contact_keyboard.add("Да", "Нет", "Не знаю")
        await Form1.next()
        await message.reply("Вы контактировали с людьми, которые больны covid_19?", reply_markup=contact_keyboard)

#@dp.message_handler(lambda message: message.text not in ["Мужской", "Женский"], state=Form.gender)
async def process_gender_invalid(message: types.Message):
    """
    In this example gender has to be one of: Male, Female, Other.
    """
    return await message.reply("Я тебя не понимаю. Выбери свой пол из клавиатуры")

#@dp.message_handler(state=Form.q1)
async def process_name1(message: types.Message, state: FSMContext):
    """
    первый вопрос
    """
    async with state.proxy() as data:
        data['q1'] = t.process_three(message.text)
    if t.process_three(message.text) == 1:
        list.append(0)
        list.append(0)
        list.append(1)
    if t.process_three(message.text) == 2:
        list.append(0)
        list.append(1)
        list.append(0)
    if t.process_three(message.text) == 3:
        list.append(1)
        list.append(0)
        list.append(0)

    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form1.next()
    await message.reply("У Вас лихорадка?",reply_markup=reply_keyboard)

#@dp.message_handler(state=Form.q2)
async def process_name2(message: types.Message, state: FSMContext):
    """
    второй вопрос
    """
    async with state.proxy() as data:
        data['q2'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form1.next()
    await message.reply("Вы испытываете усталость?",reply_markup=reply_keyboard)

#@dp.message_handler(state=Form.q3)
async def process_name3(message: types.Message, state: FSMContext):
    """
    третий вопрос
    """
    async with state.proxy() as data:
        data['q3'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form1.next()
    await message.reply("У Вас есть сухой кашель?",reply_markup=reply_keyboard)

#@dp.message_handler(state=Form.q4)
async def process_name4(message: types.Message, state: FSMContext):
    """
    четвертый вопрос
    """
    async with state.proxy() as data:
        data['q4'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form1.next()
    await message.reply("Трудно дышать?",reply_markup=reply_keyboard)

#@dp.message_handler(state=Form.q5)
async def process_name5(message: types.Message, state: FSMContext):
    """
    пятый вопрос
    """
    async with state.proxy() as data:
        data['q5'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form1.next()
    await message.reply("У Вас болит горло?", reply_markup=reply_keyboard)

#@dp.message_handler(state=Form.q6)
async def process_name6(message: types.Message, state: FSMContext):
    """
    шестой вопрос
    """
    async with state.proxy() as data:
        data['q6'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form1.next()
    await message.reply("Вы страдаете?", reply_markup=reply_keyboard)

#@dp.message_handler(state=Form.q7)
async def process_name7(message: types.Message, state: FSMContext):
    """
    седьмой вопрос
    """
    async with state.proxy() as data:
        data['q7'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form1.next()
    await message.reply("Заложен нос?", reply_markup=reply_keyboard)

#@dp.message_handler(state=Form.q8)
async def process_name8(message: types.Message, state: FSMContext):
    """
    восьмой вопрос
    """
    async with state.proxy() as data:
        data['q8'] = t.process_one(message.text)
    list.append(t.process_one(message.text))
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    reply_keyboard.add("Да", "Нет")

    await Form1.next()
    await message.reply("Насморк?", reply_markup=reply_keyboard)

async def process_name9(message: types.Message, state: FSMContext):
    """
    последний вопрос
    """
    async with state.proxy() as data:
        data['q9'] = t.process_one(message.text)
        list.append(t.process_one(message.text))
    markup = types.ReplyKeyboardRemove()
    #тут надо отправить ответ
    # Finish conversation

    await message.answer('Загрузка..')
    reply = predict_c(list)
    otvet = t.process_four(reply)
    await bot.send_message(message.chat.id, otvet,reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN)

    await state.finish()

def register_handlers_c(dp : Dispatcher):
    dp.register_message_handler(cmd_start1, commands='begin_covid')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(process_name1, state=Form1.q1)
    dp.register_message_handler(process_name2, state=Form1.q2)
    dp.register_message_handler(process_name3, state=Form1.q3)
    dp.register_message_handler(process_name4, state=Form1.q4)
    dp.register_message_handler(process_name5, state=Form1.q5)
    dp.register_message_handler(process_name6, state=Form1.q6)
    dp.register_message_handler(process_name7, state=Form1.q7)
    dp.register_message_handler(process_name8, state=Form1.q8)
    dp.register_message_handler(process_name9, state=Form1.q9)
    dp.register_message_handler(process_age_invalid, lambda message: not message.text.isdigit(), state=Form1.age)
    dp.register_message_handler(process_age, lambda message: message.text.isdigit(), state=Form1.age)
    dp.register_message_handler(process_gender_invalid, lambda message: message.text not in ["Мужской", "Женский"], state=Form1.gender)
    dp.register_message_handler(process_gender, state=Form1.gender)