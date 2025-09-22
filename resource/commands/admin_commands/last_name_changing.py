from aiogram import F
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from db.db_request.last_name_changing_db import last_name_changing_db
from ..states import Form


router = Router()


@router.message(F.text == "Фамилия", Form.changing_personal_data)
async def changing_first_name(message: Message, state: FSMContext):
    """
    Реализация изменения Имени в БД через db_request
    """
    await message.answer("Введите новую фамилию:")
    await state.set_state(Form.waiting_for_last_name)  # Ожидание ввода фамилии


@router.message(Form.waiting_for_last_name)
async def process_new_last_name(message: Message, state: FSMContext):
    username = message.from_user.username
    new_last_name = message.text.strip()
    last_name_changing_db(new_last_name, username)
    await message.answer(f"Фамилия изменена на: {new_last_name}")
