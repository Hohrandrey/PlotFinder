from aiogram import F
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from db.db_request.changing_first_name_db import changing_first_name_db
from ..states import Form


router = Router()


@router.message(F.text == "Имя", Form.changing_personal_data)
async def changing_first_name(message: Message, state: FSMContext):
    """
    Реализация изменения Имени в БД через db_request
    """
    await message.answer("Введите новое имя:")
    await state.set_state(Form.waiting_for_first_name)  # Ожидание ввода имени


@router.message(Form.waiting_for_first_name)
async def process_new_first_name(message: Message, state: FSMContext):
    username = message.from_user.username
    new_first_name = message.text.strip()
    changing_first_name_db(new_first_name, username)
    await message.answer(f"Имя изменено на: {new_first_name}")
