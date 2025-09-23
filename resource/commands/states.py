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

    # управление участками
    plot_management = State() # состояние управления участками


    '''
    продавец
    '''
    seller_start = State()


    '''
    покупатель
    '''
    buyer_start = State()