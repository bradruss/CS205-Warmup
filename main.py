import sqlite3
from sqlite3 import Error
connection = None

def dbConnect():
    try:
        connection = sqlite3.connect("nba.db")

    except Error as e:
        print(e)

    finally:
        if connection:
            connection.close()



def main():
    dbConnect()



main()