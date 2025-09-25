# управление пользователями
from aiogram import Router
from aiogram.types import Message
from aiogram import F # F - способ создания фильтров для обработчиков
from ..states import Form
from aiogram.fsm.context import FSMContext
from ...keyboards.admin_kb.user_management_kb import user_management_kb
from ...keyboards.admin_kb.admin_start_kb import admin_start_kb


router = Router()


@router.message(F.text == "Управление пользователями", Form.admin_start) # проверка на то ли это сообщение
async def user_management(message: Message, state: FSMContext):
    await state.set_state(Form.user_management)
    await message.answer("Меню управления пользователями", reply_markup = user_management_kb)

@router.message(F.text == 'Назад', Form.user_management)
async def back_button(message: Message, state: FSMContext):
    await state.set_state(Form.admin_start)  # состояние старта админа
    await message.answer(f'Сейчас вы в меню, выберите действие',reply_markup=admin_start_kb)  # сообщение и подключение клавиатуры
