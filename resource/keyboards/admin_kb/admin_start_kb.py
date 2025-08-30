from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = [
    [KeyboardButton(text='Управление пользователями')],
    [KeyboardButton(text='Управление участками')]
]


keyboard = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True
)