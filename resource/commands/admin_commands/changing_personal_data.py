from aiogram import Router
from aiogram.types import Message
from aiogram import F # F - способ создания фильтров для обработчиков
from resource.keyboards.admin_kb.changing_personal_data_kb import changing_personal_data_kb


router = Router()


@router.message(F.text == "Изменение персональных данных")
async def changing_personal_data(message: Message):
    await message.answer(f'Меню изменения персональных данных', reply_markup = changing_personal_data_kb)