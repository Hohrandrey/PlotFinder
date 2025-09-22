import asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F # F - способ создания фильтров для обработчиков
from aiogram.fsm.context import FSMContext
from .states import Form
from resource.keyboards.admin_kb.admin_start_kb import admin_start_kb
from db.db_request.check_role import check_role

router = Router()


@router.message(Command('start'))
async def admin_start(message: Message, state: FSMContext):
    await state.set_state(Form.start)
    username = message.from_user.username
    if check_role(username) == 'admin':
        await message.answer(f'Привет, ты админ бота для удобной покупки и продажи участков PlotFinder')
        await asyncio.sleep(0.5) # пауза между сообщениями в секунду
        await message.answer(f'Сейчас вы в меню, выберите действие', reply_markup = admin_start_kb) # сообщение и подключение клавиатуры
        await state.set_state(Form.admin_start) # состояние старта админа
    elif check_role(username) == 'seller':
        await message.answer(f'Привет, ты продавец в боте для удобной продажи участков PlotFinder')
        await asyncio.sleep(0.5)
        '''
        
        добавление клавиатуры продавца
        
        '''
        await state.set_state(Form.seller_start) # состояние старта продавца
    else:
        await message.answer(f'Привет, ты покупатель в боте для удобной покупки участков PlotFinder')
        await asyncio.sleep(0.7)
        '''
        добавление клавиатуры покупателя
        '''
        await state.set_state(Form.buyer_start) # состояние старта покупателя