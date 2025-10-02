# добавление и удаление пользователей
from aiogram import F
from ..states import Form
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from ...keyboards.admin_kb.admin_start_kb import admin_start_kb
from ...keyboards.admin_kb.user_management_kb import user_management_kb
from db.db_request.list_of_people_by_role_db import list_of_people_by_role_db
from db.db_request.adding_and_removing.removing_users_db import removing_users_db
from ...keyboards.admin_kb.adding_and_removing_users_kb import adding_and_removing_users_kb


router = Router()


@router.message(F.text == 'Добавить пользователя', Form.user_management)
async def adding_user_choose(message: Message, state: FSMContext):
    await message.answer("Выберите кого добавить", reply_markup = adding_and_removing_users_kb)
    await state.set_state(Form.adding_removing_user)


@router.message(F.text == 'Удалить пользователя', Form.user_management)
async def removing_user_choose(message: Message, state: FSMContext):
    await message.answer("Выберите кого удалить", reply_markup = adding_and_removing_users_kb)
    await state.set_state(Form.adding_removing_user)


@router.message(F.text == 'Админ', Form.adding_removing_user)
@router.message(F.text == 'Продавец', Form.adding_removing_user)
@router.message(F.text == 'Покупатель', Form.adding_removing_user)
async def adding_removing_users(message: Message, state: FSMContext):
    from ...keyboards.admin_kb.list_of_people_by_role_kb import list_of_people_by_role_kb
    role_names = {
        'Админ': 'admin',
        'Продавец': 'seller',
        'Покупатель': 'buyer'
    }

    role = role_names[message.text]
    people_list = list_of_people_by_role_db(role)
    kb = list_of_people_by_role_kb(role)

    if len(people_list) == 0:
        await message.answer('Список пользователей пуст')
        if await state.get_state() == 'adding_user':
            await state.set_state(Form.user_management)
            await message.answer("Выберите кого добавить", reply_markup=adding_and_removing_users_kb)
        else:
            await state.set_state(Form.user_management)
            await message.answer("Выберите кого удалить", reply_markup=adding_and_removing_users_kb)
    else:
        if await state.get_state() == 'adding_user':
            await message.answer('Выберите пользователя для добавления', reply_markup = kb)
            await state.set_state(Form.adding_user)
        else:
            await message.answer('Выберите пользователя для удаления', reply_markup = kb)
            await state.set_state(Form.removing_user)
            await state.update_data(role=role)



@router.message(Form.removing_user)
async def removing_user(message: Message, state: FSMContext):
    selected_person = message.text
    data = await state.get_data()
    role = data.get('role')
    removing_users_db(selected_person, role)
    await state.set_state(Form.user_choosen)
    await message.answer('Пользователь удалён')
    await state.set_state(Form.admin_start)  # состояние старта админа
    await message.answer(f'Сейчас вы в меню, выберите действие',reply_markup=admin_start_kb)



@router.message(F.text == 'Назад', Form.adding_removing_user)
async def back_button(message: Message, state: FSMContext):
    await state.set_state(Form.user_management)
    await message.answer("Меню управления пользователями", reply_markup=user_management_kb)