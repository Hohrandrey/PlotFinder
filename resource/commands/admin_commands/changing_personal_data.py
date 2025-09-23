from aiogram import Router
from aiogram.types import Message
from aiogram import F # F - способ создания фильтров для обработчиков
from ..states import Form
from aiogram.fsm.context import FSMContext
from resource.keyboards.admin_kb.changing_personal_data_kb import changing_personal_data_kb
from ...keyboards.admin_kb.admin_start_kb import admin_start_kb

router = Router()


@router.message(F.text == "Изменение персональных данных", Form.admin_start)
async def changing_personal_data(message: Message, state: FSMContext):
    await state.set_state(Form.changing_personal_data)
    await message.answer(f'Меню изменения персональных данных', reply_markup = changing_personal_data_kb)


@router.message(F.text == 'Назад', Form.changing_personal_data)
async def back_button(message: Message, state: FSMContext):
    await state.set_state(Form.admin_start)
    await message.answer("Сейчас вы в меню, выберите действие", reply_markup=admin_start_kb)
