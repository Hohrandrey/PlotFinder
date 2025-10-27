# добавление и удаление пользователей
from aiogram import F
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from ..states import Form
from ...keyboards.admin_kb.admin_start_kb import admin_start_kb
from ...keyboards.admin_kb.user_management_kb import user_management_kb
from ...keyboards.admin_kb.adding_and_removing_users_kb import adding_and_removing_users_kb
from ...keyboards.admin_kb.role_selection_kb import role_selection_kb
from db.db_request.list_of_people_by_role_db import list_of_people_by_role_db
from db.db_request.adding_and_removing.adding_users_db import adding_users_db
from db.db_request.adding_and_removing.removing_users_db import removing_users_db


router = Router()


@router.message(F.text == 'Добавить пользователя', Form.user_management)
async def adding_user_choose(message: Message, state: FSMContext):
    await message.answer("Выберите кого добавить", reply_markup = adding_and_removing_users_kb)
    await state.set_state(Form.adding_user)


@router.message(F.text == 'Удалить пользователя', Form.user_management)
@router.message(F.text == 'Админ', Form.user_management)
@router.message(F.text == 'Продавец', Form.user_management)
@router.message(F.text == 'Покупатель', Form.user_management)
async def removing_user_choose(message: Message, state: FSMContext):
    await message.answer("Выберите кого удалить", reply_markup = adding_and_removing_users_kb)
    await state.set_state(Form.removing_user)


@router.message(F.text == 'Админ', Form.adding_user)
@router.message(F.text == 'Продавец', Form.adding_user)
@router.message(F.text == 'Покупатель', Form.adding_user)
@router.message(F.text == 'Админ', Form.removing_user)
@router.message(F.text == 'Продавец', Form.removing_user)
@router.message(F.text == 'Покупатель', Form.removing_user)
async def adding_removing_users(message: Message, state: FSMContext):
    from ...keyboards.admin_kb.list_of_people_by_role_kb import list_of_people_by_role_kb # список пользователей в клавиатуре
    role_names = {
        'Админ': 'admin',
        'Продавец': 'seller',
        'Покупатель': 'buyer'
    }

    role = role_names[message.text]
    people_list = list_of_people_by_role_db(role)
    kb = list_of_people_by_role_kb(role)


    if len(people_list) == 0 and await state.get_state() == Form.removing_user:
        await message.answer('Список пользователей пуст')
        await removing_user_choose(message, state)
        return
    else:
        if await state.get_state() == Form.adding_user:
            await message.answer('Выберите пользователя для добавления')
            await state.set_state(Form.user_added)
        else:
            await message.answer('Выберите пользователя для удаления', reply_markup = kb)
            await state.set_state(Form.user_removed)
            await state.update_data(role=role) # загрузка сообщения в память



@router.message(Form.user_removed)
async def removing_user(message: Message, state: FSMContext):
    selected_person = message.text # получение сообщения от пользователя
    data = await state.get_data() # загрузка сообщения из памяти
    role = data.get('role') # запись из памяти в переменную
    removing_users_db(selected_person, role)
    await state.set_state(Form.user_choosen)
    await message.answer('Пользователь удалён')
    await state.set_state(Form.admin_start)  # состояние старта админа
    await message.answer(f'Сейчас вы в меню, выберите действие',reply_markup=admin_start_kb)



@router.message(Form.user_added)
async def adding_user(message: Message, state: FSMContext):
    '''Дописать реализацию'''
    await message.answer('Введите username пользователя')
    await state.set_state(Form.username_waiting)
    username = message.text

    await message.answer('Выберите роль пользователя', reply_murkup = role_selection_kb)
    await state.set_state(Form.role_waiting)
    role = message.text

    await message.answer('Введите имя пользователя')
    await state.set_state(Form.first_name_waiting)
    first_name = message.text

    await message.answer('Введите фамилию пользователя')
    await state.set_state(Form.last_name_waiting)
    last_name = message.text

    await message.answer('Нужно ли добавить отчество, телефон или название компании?')
    await message.answer('Ответьте: да/нет')
    await state.set_state(Form.dop_info_need_waiting)
    dop_info_need = message.text
    if dop_info_need.lower() == 'да':
        '''
        сделать так, чтобы повторялось
        '''
        await message.answer('Выберите что добавить')
        await message.answer('1-отчество\n2-телефон\n3-название компании\n4-ничего')
        await state.set_state(Form.dop_info_waiting)
        dop_info = message.text
        try:
            match dop_info:
                case '1':
                    await message.answer('Введите отчество пользователя')
                    await state.set_state(Form.patronymic_waiting)
                    patronymic = message.text
                case '2':
                    await message.answer('Введите номер телефона')
                    await state.set_state(Form.phone_waiting)
                    phone = message.text
                case '3':
                    await message.answer('Введите название компании')
                    await state.set_state(Form.company_name_waiting)
                    company_name = message.text
                case '4':
                    '''
                            сделать выход из цикла
                        '''
        except:
            await message.answer('Выбор некорректен, попробуйте снова')
            await state.set_state(Form.dop_info_waiting)

    adding_users_db(username, role, first_name, last_name, patronymic, phone, company_name)
    await message.answer('Пользователь добавлен')
    await state.set_state(Form.admin_start)  # состояние старта админа
    await message.answer(f'Сейчас вы в меню, выберите действие', reply_markup=admin_start_kb)



@router.message(F.text == 'Назад', Form.removing_user)
@router.message(F.text == 'Назад', Form.adding_user)
async def back_button(message: Message, state: FSMContext):
    await state.set_state(Form.user_management)
    await message.answer("Меню управления пользователями", reply_markup=user_management_kb)