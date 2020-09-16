import sqlite3
from sqlite3 import Error
connection = None

# TODO: When dealing with the Wizards and Raptors, make sure that Canada/DC is returned correctly
# ie: This team is not part of the US
# TODO: Make it so create tables isnt automatic and forces user to use load()


# Create tables
def createTables():
    try:
        global connection
        cursor = connection.cursor()
        # Create tables
        cursor.execute("CREATE TABLE states ")
        cursor.execute("")


        # Open csvs
        try:
            #teamFile = open("teams.csv")
            statesFile = open("states.csv")
            for line in statesFile:
                print(line.split(','))



            # Read data from csvs

            # Execute statement
            # cursor.execute(sqlStatement)

        except IOError as e:
            print(e)

    # Sql error
    except Error as e:
        print(e)


# Establish DB connection
def dbConnect():
    global connection
    try:
        connection = sqlite3.connect("nba.db")
        return connection

    except Error as e:
        print(e)



def capitalStateQuery(statement):
    print()

def capitalTeamQuery(statement):
    print()

def lossTeamQuery(statement):
    print()

def populationStateQuery(statement):
    print()

def populationTeamQuery(statement):
    print()

def stateCapitalQuery(statement):
    print()

def stateTeamQuery(statement):
    print()

def teamStateQuery(statement):
    print()

def teamCapitalQuery(statement):
    print()

def winsTeamQuery(statement):
    print()




def main():
    dbConnect()
    global connection
    if connection is not None:
        # should only create tables if not exists
        createTables()

        # Perform rest of tasks below







        connection.close()

main()