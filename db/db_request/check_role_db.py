# проверка какая у пользователя роль
import sqlite3
from config import DB_NAME


def check_role_db(username):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute('SELECT role FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()

    connection.commit()
    connection.close()
    return result[0]