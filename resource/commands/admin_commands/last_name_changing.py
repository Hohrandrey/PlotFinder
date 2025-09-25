# изменение фамилии
from aiogram import F
from ..states import Form
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from db.db_request.changing_personal_data.last_name_changing_db import last_name_changing_db
from ...keyboards.back_and_menu_button import back_and_menu_button
from ...keyboards.admin_kb.admin_start_kb import admin_start_kb
from ...keyboards.admin_kb.changing_personal_data_kb import changing_personal_data_kb

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
