from aiogram import F
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from db.db_request.patronymic_changing_db import patronymic_changing_db
from ..states import Form


router = Router()


@router.message(F.text == "Отчество", Form.changing_personal_data)
async def patronymic_changing(message: Message, state: FSMContext):
    """
    Реализация изменения Имени в БД через db_request
    """
    await message.answer("Введите новое отчество:")
    await state.set_state(Form.waiting_for_patronymic)  # Ожидание ввода отчества


@router.message(Form.waiting_for_patronymic)
async def process_new_patronymic(message: Message, state: FSMContext):
    username = message.from_user.username
    new_first_patronymic = message.text.strip()
    patronymic_changing_db(new_first_patronymic, username)
    await message.answer(f"Отчество изменено на: {new_first_patronymic}")
