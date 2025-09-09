# для хранения состояний
from aiogram.fsm.state import State, StateGroup


class Form(StateGroup):
    # список состояний
    # состояния для смены ПД
    waiting_for_first_name = State() # смена фамилии