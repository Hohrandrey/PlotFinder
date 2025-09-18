from aiogram import F
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from db.db_request.changing_first_name import changing_first_name
from ..states import Form


router = Router()


@router.message(F.text == "Имя", Form.admin_start)
async def changing_first_name(message: Message, state: FSMContext):
    """
    Здесь реализация изменения Имени в БД через db_request
    """
    username = message.from_user.username
    await state.set_state(Form.waiting_for_first_name) # Ожидание ввода имени
    new_first_name = message.text
    await message.answer(username)
    await changing_first_name(new_first_name, username)
    await message.reply("Имя изменено")