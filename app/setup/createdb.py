import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print("Error creating database.")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection(r"../db/pipo.db")
