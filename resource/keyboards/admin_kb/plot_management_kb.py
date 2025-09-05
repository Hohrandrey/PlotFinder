# клавиатура с просмотром участков для их модерирования
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = [
    [KeyboardButton(text = 'Оставить участок')],
    [KeyboardButton(text = 'Удалить участок')]
]


plot_management_kb = ReplyKeyboardMarkup(
    keybord = kb,
    resize_keyboard = True,
    one_time_keyboard = True
)