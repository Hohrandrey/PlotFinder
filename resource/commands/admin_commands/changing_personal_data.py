from aiogram import F
from aiogram import Router
from aiogram.types import Message
from resource.keyboards.admin_kb.сhanging_personal_data_kb import сhanging_personal_data_kb


router = Router()


@router.message(F.text == "Изменение персональных данных")
async def сhanging_personal_data(message: Message):
    await message.answer(f'Меню изменения персональных данных', reply_markup = сhanging_personal_data_kb)