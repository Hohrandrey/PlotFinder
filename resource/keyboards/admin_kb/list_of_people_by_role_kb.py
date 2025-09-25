# клавиатура со списком людей по ролям

from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types
from db.db_request.list_of_people_by_role_db import list_of_people_by_role_db
from resource.commands.admin_commands.adding_and_removing_users import adding_removing_users

builder = ReplyKeyboardBuilder()

list_of_people_by_role_db(adding_removing_users.role)
for i in list_of_people_by_role_db:
    builder.add(types.KeyboardButton(text=str(i)))

list_of_people_by_role_kb = builder.as_murkup(
    resize_keyboard = True,
    one_time_keyboard = True
)