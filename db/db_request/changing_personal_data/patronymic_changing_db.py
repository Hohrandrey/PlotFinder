# изменение отчества
import sqlite3
from config import DB_NAME


def patronymic_changing_db(new_patronymic, username):
    connection = sqlite3.connect(DB_NAME) # устанавливаем соединение с базой данных
    cursor = connection.cursor() # курсор для управления БД

    # обновляем имя пользователя с нужным нам username
    cursor.execute('UPDATE admins SET patronymic = ? WHERE username = ?', (new_patronymic, username))

    connection.commit() # сохранение изменений
    connection.close() # закрытие соединения
