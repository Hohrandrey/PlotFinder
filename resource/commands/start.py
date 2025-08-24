from aiogram import Router, F # роутер для обработки сообщений, инструмент для создания фильтров сообщений
from aiogram.types import Message # обработчик входящих сообщений от пользователя
from aiogram.filters import Command # фильтр для обработки команд

router = Router() # Создаем объект роутера для обработки сообщений


@router.message(Command('start')) # обработчик сообщения /start
async def command_start_handler(message: Message): # функция принимающая сообщение
    await message.answer(f'Привет, я бот для удобной покупки участков') # отправка сообщения с текстом