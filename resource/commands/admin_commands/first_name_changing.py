from aiogram import F
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from db.db_request.changing_first_name_db import changing_first_name_db
from ...keyboards.back_and_menu_button import back_and_menu_button
from ...keyboards.admin_kb.admin_start_kb import admin_start_kb
from ...keyboards.admin_kb.changing_personal_data_kb import changing_personal_data_kb
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
    await state.set_state(Form.back_and_menu)
    await message.answer("Выберите действие", reply_markup=back_and_menu_button)


@router.message(F.text == 'Назад', Form.back_and_menu)
async def back_button(message: Message, state: FSMContext):
    await state.set_state(Form.changing_personal_data)
    await message.answer(f'Меню изменения персональных данных', reply_markup=changing_personal_data_kb)

@router.message(F.text == 'В меню', Form.back_and_menu)
async def menu_button(message: Message, state: FSMContext):
    await state.set_state(Form.admin_start)  # состояние старта админа
    await message.answer(f'Сейчас вы в меню, выберите действие', reply_markup=admin_start_kb)  # сообщение и подключение клавиатуры
