import asyncio # для асинхронного запуска бота
import logging # модуль для логирования
from resource.commands.__routers import * # импорт всех роутеров
from aiogram import Dispatcher, Bot # импорт диспетчера, класс для бота
from config import TOKEN # импорт токена


bot = Bot(token=TOKEN) # создание объекта bot со своим токеном
dp = Dispatcher() # объект для создания обработчиков


#dp.include_router(admin_start_router)
dp.include_router(buyer_start_router)


async def main(): # Создание в классе объекта Bot и его запуск
    await bot.delete_webhook(drop_pending_updates=True) # удаляет все обновления, которые произошли после последнего завершения работы бота
    await dp.start_polling(bot) # запуск бота


if __name__ == '__main__': # запуск основной программы
    logging.basicConfig(level=logging.INFO) # Настройка логирования: уровень INFO (информационные сообщения)
    asyncio.run(main()) # Запуск асинхронной функции main() с помощью asyncio
