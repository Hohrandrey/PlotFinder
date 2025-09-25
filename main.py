# основное тело программы

import asyncio # для асинхронного запуска бота
import sqlite3, os # для работы с БД
import logging # модуль для логирования
from resource.commands.__routers import * # импорт всех роутеров
from aiogram import Dispatcher, Bot # импорт диспетчера, класс для бота
from config import TOKEN # импорт токена

bot = Bot(token=TOKEN) # создание объекта bot со своим токеном
dp = Dispatcher() # объект для создания обработчиков


# список общих роутеров
dp.include_router(start_router) # команда старт

# список всех роутеров админа
dp.include_router(user_management_router) # управление пользователями
dp.include_router(plot_management) # управление участками
dp.include_router(changing_personal_data) # изменение персональных данных
dp.include_router(changing_first_name) # изменение имени
dp.include_router(changing_patronymic) # изменение отчества
dp.include_router(changing_last_name) # изменение фамилии
dp.include_router(adding_and_removing_users) # добавление и удаление пользователей


# список всех роутеров покупателя


async def main(): # Создание в классе объекта Bot и его запуск
    await bot.delete_webhook(drop_pending_updates=True) # удаляет все обновления, которые произошли после последнего завершения работы бота
    await dp.start_polling(bot) # запуск бота


if __name__ == '__main__': # запуск основной программы

    # Путь к базе данных
    db_path = "db/db/PlotFinder_db.db"

    # Проверяем существует ли файл базы данных
    if not os.path.exists(db_path):
        print(f"Ошибка: Файл базы данных не найден: {db_path}")
    else:
        try:
            # Подключаемся к базе данных
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()

                # Проверяем соединение - получаем список таблиц
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()

                print("✅ Успешное подключение к базе данных!")
                print(f"📊 Найдено таблиц: {len(tables)}")

                # Выводим список таблиц
                print("\n📋 Список таблиц:")
                for table in tables:
                    print(f" - {table[0]}")
        except sqlite3.Error as e:
            print(f"❌ Ошибка при работе с базой данных: {e}")

    logging.basicConfig(level=logging.INFO) # Настройка логирования: уровень INFO (информационные сообщения)
    asyncio.run(main()) # Запуск асинхронной функции main() с помощью asyncio
