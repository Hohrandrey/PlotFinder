from aiogram import Router
from aiogram.types import Message
from aiogram import F # F - способ создания фильтров для обработчиков
from ..states import Form
from aiogram.fsm.context import FSMContext
from resource.keyboards.admin_kb.changing_personal_data_kb import changing_personal_data_kb


router = Router()


@router.message(F.text == "Изменение персональных данных", Form.admin_start)
async def changing_personal_data(message: Message):
    await message.answer(f'Меню изменения персональных данных', reply_markup = changing_personal_data_kb)