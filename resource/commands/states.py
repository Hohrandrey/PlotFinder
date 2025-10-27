# для хранения состояний
from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup): # список состояний
    '''
    общее
    '''
    start = State() # начальное состояние для всех
    changing_personal_data = State()  # смена пд
    waiting_for_last_name = State()  # смена фамилии
    waiting_for_first_name = State()  # смена имени
    waiting_for_patronymic = State() # смена отчества
    back_and_menu = State() # ожидание для кнопок назад и в меню

    '''
    админ
    '''
    admin_start = State() # выбор дальнейших действий для админа

    # управление пользователями
    user_management = State() # состояние управления пользователями
    adding_user = State() # добавление пользователя
    removing_user = State() # удаление пользователя
    user_removed = State() # удалён пользователь
    user_choosen = State() # выбран пользователя
    user_added = State() # добавлен пользователь

    username_waiting = State() # ожидание ввода username
    role_waiting = State() # ожидание выбора роли
    first_name_waiting = State() # ожидание ввода имени
    last_name_waiting = State() # ожидание ввода фамилии

    dop_info_need_waiting = State() # ожидание выбора нужен ли доп параметр в виде телефона, отчества или названия компании
    dop_info_waiting = State() # ожидание выбора доп параметра
    patronymic_waiting = State() # ожидание ввода отчества
    phone_waiting = State() # ожидание ввода номера телефона
    company_name_waiting = State() # ожидание ввода названия компании


    # управление участками
    plot_management = State() # состояние управления участками


    '''
    продавец
    '''
    seller_start = State()#  выбор дальнейших действий для продавца


    '''
    покупатель
    '''
    buyer_start = State() # выбор дальнейших действий для покупателя