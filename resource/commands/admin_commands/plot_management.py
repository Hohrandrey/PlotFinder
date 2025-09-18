from aiogram import Router
from aiogram.types import Message
from aiogram import F # F - способ создания фильтров для обработчиков
from ..states import Form
from aiogram.fsm.context import FSMContext
from resource.keyboards.admin_kb.plot_management_kb import plot_management_kb


router = Router()


@router.message(F.text == "Управление участками", Form.admin_start)
async def plot_management(message: Message, state: FSMContext):
    await message.answer(f'Меню управления участками', reply_markup = plot_management_kb) # сообщение и подключение клавиатуры
    await state.set_state(Form.plot_management)