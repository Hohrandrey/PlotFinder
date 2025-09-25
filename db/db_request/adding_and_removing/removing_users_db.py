# удаление пользователей из БД
import sqlite3
from config import DB_NAME


def removing_users_db(username, role):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    roles_tables = {
        'admin' : 'admins',
        'seller' : 'sellers',
        'buyer' : 'customers'
    }

    cursor.execute('delete from users where username = ?', (username,))
    cursor.execute(f'delete from {roles_tables[role]} where username = ?', (username,))


    conn.commit()
    conn.close()
