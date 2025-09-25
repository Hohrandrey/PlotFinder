# изменение отчества
from aiogram import F
from ..states import Form
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from db.db_request.changing_personal_data.patronymic_changing_db import patronymic_changing_db
from ...keyboards.back_and_menu_button import back_and_menu_button
from ...keyboards.admin_kb.admin_start_kb import admin_start_kb
from ...keyboards.admin_kb.changing_personal_data_kb import changing_personal_data_kb


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
