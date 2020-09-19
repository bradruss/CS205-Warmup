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



def teamState(statement):
    print()

def populationState(statement):
    print()

def capitalState(statement):
    print()

def teamCapital(capital):
    global connection
    cursor = connection.cursor()

    # VVVVVVVVVVV DOES NOT WORK YET VVVVVVVVVVVV
    query = "SELECT team FROM teams (FULL OUTER JOIN states ON team.state = states.state)" \
            " WHERE capital LIKE '" + capital + "' "
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    for x in returnVal:
        for y in x:
            print(y)

def capitalTeam(team):
    global connection
    cursor = connection.cursor()

    # VVVVVVVVVVV DOES NOT WORK YET VVVVVVVVVVVV
    query = "SELECT capital FROM teams (FULL OUTER JOIN states ON team.state = states.state)" \
            " WHERE team LIKE '" + team + "' "
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    for x in returnVal:
        for y in x:
            print(y)

def stateTeam(team):
    global connection
    cursor = connection.cursor()
    query = "SELECT state FROM teams WHERE team LIKE '" + team + "'"
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    for x in returnVal:
        for y in x:
            print(y)

def populationTeam(team):
    global connection
    cursor = connection.cursor()

    # VVVVVVVVVVV DOES NOT WORK YET VVVVVVVVVVVV
    query = "SELECT population FROM states (FULL OUTER JOIN teams ON states.state = teams.state)" \
            " WHERE team LIKE '" + team + "' "
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    for x in returnVal:
        for y in x:
            print(y)

def stateCapital(capital):
    global connection
    cursor = connection.cursor()
    query = "SELECT state FROM states WHERE capital LIKE '" + capital + "'"
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    for x in returnVal:
        for y in x:
            print(y)

def winsTeam(team):
    global connection
    cursor = connection.cursor()
    query = "SELECT w FROM teams WHERE team LIKE '" + team + "'"
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    for x in returnVal:
        for y in x:
            print(y)

def lossesTeam(team):
    global connection
    cursor = connection.cursor()
    query = "SELECT l FROM teams WHERE team LIKE '" + team + "'"
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    for x in returnVal:
        for y in x:
            print(y)




def main():
    dbConnect()
    global connection
    if connection is not None:
        # should only create tables if not exists
        createTables()

        # Perform rest of tasks below







        connection.close()

main()