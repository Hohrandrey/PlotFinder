import sqlite3
from config import DB_NAME


def check_role(username):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()


    cursor.execute('SELECT role FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()


    connection.commit()
    connection.close()