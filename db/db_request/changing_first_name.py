import sqlite3
from config import DB_NAME


def changing_first_name(new_first_name, username):
    connection = sqlite3.connect(DB_NAME) # устанавливаем соединение с базой данных
    cursor = connection.cursor() # курсор для управления БД

    # обновляем имя пользователя с нужным нам username
    cursor.execute('UPDATE admins SET first_name = ? WHERE username = ?', (new_first_name, username))

    connection.commit() # сохранение изменений
    connection.close() # закрытие соединения
