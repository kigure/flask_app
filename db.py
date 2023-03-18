import sqlite3

database = 'database.db'


def create_book_table():
    con = sqlite3.connect(database)
    con.execute("CREATE TABLE IF NOT EXISTS book (title, price, arrival_day)")
    con.close()
