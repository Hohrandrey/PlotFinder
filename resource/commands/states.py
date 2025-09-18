# для хранения состояний
from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup): # список состояний
    admin_start = State() # выбор дальнейших действий для админа
    user_management = State() # состояние управления пользователями
    plot_management = State() # состояние управления участками
    # состояния для смены ПД
    changing_personal_data = State() # смена пд
    waiting_for_last_name = State() # смена фамилии
    waiting_for_first_name = State() # смена имени