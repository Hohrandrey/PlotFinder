from aiogram import F
from aiogram import Router
from aiogram.types import Message
from db.db_request.changing_first_name import changing_first_name
from ..states import Form


router = Router()


@router.message(F.text == "Имя")
async def changing_first_name(message: Message):
    """
    Здесь реализация изменения Имени в БД через db_request
    """
    username = message.from_user.username
    await message.answer("Введите новое имя")
    new_first_name = message.from_user
    await message.answer(username)
    await changing_first_name(new_first_name, username)
    await message.reply("Имя изменено")