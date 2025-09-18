import asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F # F - способ создания фильтров для обработчиков
from aiogram.fsm.context import FSMContext
from ..states import Form
from resource.keyboards.admin_kb.admin_start_kb import admin_start_kb


router = Router()


@router.message(Command('start'))
async def admin_start(message: Message, state: FSMContext):
    await message.answer(f'Привет, ты админ бота для удобной покупки и продажи участков PlotFinder')
    await asyncio.sleep(0.7) # пауза между сообщениями в секунду
    await message.answer(f'Сейчас вы в меню, выберите действие', reply_markup = admin_start_kb) # сообщение и подключение клавиатуры
    await state.set_state(Form.admin_start)