import asyncio #асинхронный фреймворк
import logging #модуль для логирования
import sys # модуль для работы с системными модулями

from aiogram import Dispatcher, Bot, html #импорт диспетчера, класс для бота и html
from aiogram.client.default import DefaultBotProperties # импорт стандартных настроек для бота
from aiogram.enums import ParseMode #импорт форматирования текста
from aiogram.types import Message #импорт сообщений
from aiogram.filters import CommandStart #импорт каманды старт
from config import TOKEN # импорт токена


dp = Dispatcher() #объект для создания обработчиков


@dp.message(CommandStart()) #декоратор сообщения /start
async def command_start_handler(message: Message) -> None: #функция принимающая сообщение и не возвращает событие
    await message.answer(f'Привет, я бот для удобной покупки участков')
    await message.answer(f'Hello, {html.bold(message.from_user.full_name)}')


@dp.message() #декоратор для обработчика всех сообщений (без фильтров)
async def echo_handler(message: Message) -> None: #повторяет все сообщения
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None: # Создание в классе объекта Bot и его запуск
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)) #создание объекта  bot с стандартными настройками и своим токеном

    await dp.start_polling(bot) # запуск бота


if __name__ == '__main__': #запуск основной программы
    logging.basicConfig(level=logging.INFO, stream=sys.stdout) # Настройка логирования: уровень INFO (информационные сообщения), вывод в stdout
    asyncio.run(main()) # Запуск асинхронной функции main() с помощью asyncio
