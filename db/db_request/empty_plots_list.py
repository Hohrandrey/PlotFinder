import sqlite3
from config import DB_NAME


def empty_plots_list():
    connection = sqlite3.connect(DB_NAME)  # устанавливаем соединение с базой данных
    cursor = connection.cursor()  # курсор для управления БД


    # достаём из таблицы
    cursor.execute('SELECT size_plot, location, cadastre, price, description FROM plots WHERE is_active = 1')


    connection.commit()  # сохранение изменений
    connection.close()  # закрытие соединения

empty_plots_list()