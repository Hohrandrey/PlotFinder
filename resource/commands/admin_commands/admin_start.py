from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from resource.keyboards.admin_kb.admin_start_kb import admin_start_kb


router = Router()


@router.message(Command('start'))
async def command_start_handler(message: Message):
    await message.answer(f'Привет, ты админ бота для удобной покупки и продажи участков PlotFinder', reply_markup=admin_start_kb)