from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = [
    [KeyboardButton(text='Добавить пользователя')],
    [KeyboardButton(text='Удалить пользователя')],
    [KeyboardButton(text='Назад')]
]


user_management_kb = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    one_time_keyboard=True
)