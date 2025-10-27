# клавиатура для вывода доступных ролей
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = [
    [KeyboardButton(text = 'admin')],
    [KeyboardButton(text = 'seller')],
    [KeyboardButton(text = 'buyer')]
]


role_selection_kb = ReplyKeyboardMarkup(
    keyboard = kb,
    resize_keyboard=True,
    one_time_keyboard=True
)