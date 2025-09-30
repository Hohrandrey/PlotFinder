# клавиатура со списком людей по ролям

from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types
from db.db_request.list_of_people_by_role_db import list_of_people_by_role_db


def list_of_people_by_role_kb(role):
    builder = ReplyKeyboardBuilder()


    people_list = list_of_people_by_role_db(role)
    for person in people_list:
        builder.add(types.KeyboardButton(text=str(person)))

    return builder.as_markup(
        resize_keyboard = True,
        one_time_keyboard = True
    )