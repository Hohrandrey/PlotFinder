# стартовая клавиатура администратора
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = [
    [KeyboardButton(text = 'Управление пользователями')],
    [KeyboardButton(text = 'Управление участками')],
    [KeyboardButton(text = 'Изменение персональных данных')]
]


admin_start_kb = ReplyKeyboardMarkup(
    keyboard = kb,
    resize_keyboard = True,
    one_time_keyboard = True
)