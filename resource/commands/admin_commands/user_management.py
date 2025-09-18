from aiogram import Router
from aiogram.types import Message
from aiogram import F # F - способ создания фильтров для обработчиков
from ..states import Form
from aiogram.fsm.context import FSMContext
from resource.keyboards.admin_kb.user_management_kb import user_management_kb


router = Router()


@router.message(F.text == "Управление пользователями", Form.admin_start) # проверка на то ли это сообщение
async def user_management(message: Message, state: FSMContext):
    await message.answer("Меню управления пользователями", reply_markup = user_management_kb)
    await state.set_state(Form.user_management)