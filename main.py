import sqlite3
from sqlite3 import Error
connection = None

abbrevDict = {
"Alabama": "AL", 
"Alaska": "AK", 
"Arizona": "AZ", 
"Arkansas": "AR", 
"California": "CA", 
"Colorado": "CO", 
"Delaware": "DE", 
"Florida": "FL", 
"Georgia": "GA", 
"Hawaii": "HI",
"Idaho": "ID", 
"Illinois": "IL", 
"Indiana": "IN", 
"Iowa": "IA",
"Kansas": "KS",
"Kentucky": "KY",
"Louisiana": "LA",
"Maine": "ME",
"Maryland": "MD",
"Massachusetts": "MA",
"Michigan": "MI",
"Minnesota": "MN",
"Mississippi": "MS",
"Missouri": "MO",
"Montana": "MT",
"Nebraska": "NE",
"Nevada": "NV",
"New Hampshire": "NH",
"New Jersey": "NJ",
"New Mexico": "NM",
"New York": "NY",
"North Carolina": "NC",
"North Dakota": "ND",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
"": ""}


def createTables():
    try:
		global connection
        cursor = connection.cursor()
		
		# Execute statement
        #cursor.execute(sqlStatement)

    except Error as e:
        print(e)

def dbConnect():
    global connection
    try:
        connection = sqlite3.connect("nba.db")
		return connection

    except Error as e:
        print(e)


def main():
    dbConnect()
	global connection
    if connection is not None:
		# should only create tables if not exists
        createTables()

		# Perform rest of tasks below

		
		
		
		
		
		
		
		
		connection.close()

main()