# изменение фамилии
import sqlite3
from config import DB_NAME


def last_name_changing_db(new_last_name, username):
    connection = sqlite3.connect(DB_NAME) # устанавливаем соединение с базой данных
    cursor = connection.cursor() # курсор для управления БД

    # обновляем имя пользователя с нужным нам username
    cursor.execute('UPDATE admins SET last_name = ? WHERE username = ?', (new_last_name, username))

    connection.commit() # сохранение изменений
    connection.close() # закрытие соединения
