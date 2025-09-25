# список пользователей с определённой ролью
import sqlite3
from config import DB_NAME


def list_of_people_by_role_db(role):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('select username from users where role = ?', (role,))

    conn.commit()
    conn.close()