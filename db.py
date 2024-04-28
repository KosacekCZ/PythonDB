import sqlite3
from sqlite3 import Error as SQLError

def connect_db(database_file):
    connection = None
    try:
        connection = sqlite3.connect(database_file)
        return connection
    except SQLError as error:
        print(error)

def get_users(cursor):
    cursor.execute('SELECT * FROM "uzivatele"')
    for c in cursor.fetchall():
        print(c)

def add_user(cursor, prezdivka, email, heslo):
    cursor.execute(f'INSERT INTO uzivatele(prezdivka, email, heslo) VALUES ("{prezdivka}", "{email}", "{heslo}")')


def get_tables(cursor):
    sql_query =  'SELECT name FROM sqlite_master WHERE type="table"'

    cursor.execute(sql_query)
    for t in cursor.fetchall() :
        print(t)



