# кнопки назад и в меню
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = [
    [KeyboardButton(text='Назад')],
    [KeyboardButton(text='В меню')]
]


back_and_menu_button = ReplyKeyboardMarkup(
    keyboard = kb,
    resize_keyboard=True,
    one_time_keyboard=True
)