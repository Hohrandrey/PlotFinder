from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = [
    [KeyboardButton(text='Фамилия')],
    [KeyboardButton(text='Имя')],
    [KeyboardButton(text='Отчество')],
    [KeyboardButton(text='Назад')]
]

сhanging_personal_data_kb = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    one_time_keyboard=True
)