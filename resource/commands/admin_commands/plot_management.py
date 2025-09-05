from aiogram import Router
from aiogram.types import Message
from aiogram import F # F - способ создания фильтров для обработчиков
from resource.keyboards.admin_kb.plot_management_kb import plot_management_kb


router = Router()


@router.message(F.text == "Управление участками")
async def command_start_handler(message: Message):
    await message.answer(f'Меню управления участками') # сообщение

    await message.answer(f'', reply_markup = plot_management_kb) # подключение клавиатуры
