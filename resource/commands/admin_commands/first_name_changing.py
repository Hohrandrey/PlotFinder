from aiogram import F
from aiogram import Router
from aiogram.types import Message
from db.db_request.changing_first_name import changing_first_name


router = Router()


@router.message(F.text == "Фамилия")
async def changing_first_name(message: Message):
    """
    Здесь реализация изменения фамилии в БД через db_request
    """
    username = message.from_user.username
    await message.answer("Введите новую фамилию")
    new_first_name = message.from_user
    await message.answer(username)
    await changing_first_name(new_first_name, username)
    await message.reply("Фамилия изменена")