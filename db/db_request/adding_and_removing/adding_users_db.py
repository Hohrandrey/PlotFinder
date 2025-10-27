# добавление пользователей в БД
import sqlite3
from sqlalchemy.sql.elements import Null
from datetime import date
from config import DB_NAME


def adding_users_db(username, role, first_name, last_name, patronymic = Null, phone = Null, company_name = Null):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    roles_tables = {
        'admin' : 'admins',
        'seller' : 'sellers',
        'buyer' : 'customers'
    }

    registration_date = date.today()

    cursor.execute('insert into users (username, role) values (?, ?)', (username, role))
    if role == "seller":
        cursor.execute(f'insert into {roles_tables[role]} \
        (username, first_name, last_name, patronymic, phone, company_name, registration_date) \
        values (?, ?, ?, ?, ?, ?, ?) ', (username, first_name, last_name, patronymic, phone, company_name, registration_date))
    elif role == "buyer":
        cursor.execute(f'insert into {roles_tables[role]} \
        (username, first_name, last_name, patronymic, phone, company_name, registration_date) \
        values (?, ?, ?, ?, ?, ?, ?) ', (username, first_name, last_name, patronymic, phone, company_name, registration_date))
    else:
        cursor.execute(f'insert into {roles_tables[role]} \
        (username, first_name, last_name, patronymic, registration_date) \
        values (?, ?, ?, ?, ?, ?, ?) ', (username, first_name, last_name, patronymic, registration_date))


    conn.commit()
    conn.close()
