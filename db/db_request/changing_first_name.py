import sqlite3
from config import db_name


def changing_first_name(new_first_name, username):
    connection = sqlite3.connect(db_name) # устанавливаем соединение с базой данных
    cursor = connection.cursor() # курсор для управления БД

    # обновляем фамилию пользователя с нужным нам username
    cursor.execute('UPDATE admins SET first_name = ? WHERE username = ?', (new_first_name, username))

    connection.commit() # сохранение изменений
    connection.close() # закрытие соединения
