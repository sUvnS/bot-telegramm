from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
        text='Да'
        ),
        KeyboardButton(
        text='Нет'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери кнопку ↓', selective=True)

contact_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
        text='Да'
        ),
        KeyboardButton(
        text='Нет'
        ),
        KeyboardButton(
            text='Не знаю'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери кнопку ↓', selective=True)