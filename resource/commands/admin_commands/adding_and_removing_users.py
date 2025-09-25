# добавление и удаление пользователей
from aiogram import F
from ..states import Form
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from ...keyboards.admin_kb.user_management_kb import user_management_kb
from db.db_request.adding_and_removing.adding_users_db import adding_users_db
from db.db_request.adding_and_removing.removing_users_db import removing_users_db
from ...keyboards.admin_kb.list_of_people_by_role_kb import list_of_people_by_role_kb
from ...keyboards.admin_kb.adding_and_removing_users_kb import adding_and_removing_users_kb


router = Router()


@router.message(F.text == 'Добавить пользователя', Form.user_management)
async def adding_user(message: Message, state: FSMContext):
    await message.answer("Выберите кого добавить", reply_markup = adding_and_removing_users_kb)
    await state.set_state(Form.adding_user)


@router.message(F.text == 'Удалить пользователя', Form.user_management)
async def removing_user(message: Message, state: FSMContext):
    await message.answer("Выберите кого удалить", reply_markup = adding_and_removing_users_kb)
    await state.set_state(Form.removing_user)


@router.message(F.text == 'Админ', Form.removing_user)
@router.message(F.text == 'Админ', Form.adding_user)
@router.message(F.text == 'Продавец', Form.removing_user)
@router.message(F.text == 'Продавец', Form.adding_user)
@router.message(F.text == 'Покупатель', Form.removing_user)
@router.message(F.text == 'Покупатель', Form.adding_user)
async def adding_removing_users(message: Message, state: FSMContext):
    role_names = {
        'Админ': 'admin',
        'Продавец': 'seller',
        'Покупатель': 'buyer'
    }

    role = role_names[message.text]
    username = message.from_user.username

    if await state.get_state() == 'adding_user':
        await message.answer('Выберите админа для добавления', reply_muprkup = list_of_people_by_role_kb)
    else:
        await message.answer('Выберите админа для удаления', reply_muprkup = list_of_people_by_role_kb)
        removing_users_db(username, role)
        await message.answer('Админ удалён')


@router.message(F.text == 'Назад', Form.adding_user)
@router.message(F.text == 'Назад', Form.removing_user)
async def back_button(message: Message, state: FSMContext):
    await state.set_state(Form.user_management)
    await message.answer("Меню управления пользователями", reply_markup=user_management_kb)