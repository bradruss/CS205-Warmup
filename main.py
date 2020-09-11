import sqlite3
from sqlite3 import Error

def createTables(conn, sqlStatement):
    try:
        cursor = conn.cursor()
        cursor.execute(sqlStatement)

    except Error as e:
        print(e)

def dbConnect():
    connection = None
    try:
        connection = sqlite3.connect("nba.db")

    except Error as e:
        print(e)

    return connection

def main():
    conn = dbConnect()
    if conn is not None:
        query1 = ""

        createTables(conn, query1)


    conn.close()

main()