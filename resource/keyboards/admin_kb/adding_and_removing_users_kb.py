from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = [
    [KeyboardButton(text='Админ')],
    [KeyboardButton(text='Продавец')],
    [KeyboardButton(text='Покупатель')],
    [KeyboardButton(text='Назад')]
]


adding_and_removing_users_kb = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    one_time_keyboard=True
)