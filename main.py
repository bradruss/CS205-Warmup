import sqlite3
from sqlite3 import Error
from Input import *
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
        cursor.execute("""CREATE TABLE IF NOT EXISTS states (
        ID TEXT PRIMARY KEY,
        State TEXT DEFAULT NULL,
        Capital TEXT DEFAULT NULL,
        Population TEXT DEFAULT NULL);
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS teams(
        teamID TEXT PRIMARY KEY,
        Team TEXT DEFAULT NULL,
        TeamState TEXT DEFAULT NULL,
        Wins TEXT DEFAULT NULL,
        Losses TEXT DEFAULT NULL
        );
        """)

        #cursor.execute

        # Open csvs
        try:
            teamFile = open("team_stats.csv")
            statesFile = open("states.csv")
            for line in statesFile:
                if line != 'ï»¿ID,State,Capital,Population\n':
                    id = line.split(',')[0]
                    stateTemp = line.split(',')[1]
                    capital = line.split(',')[2]
                    population = line.split(',')[3]
                    population = population.replace('\n','')
                    cursor.execute("INSERT INTO states (ID, State, Capital, Population) VALUES (?, ?, ?, ?)", (id, stateTemp, capital, population))
                    connection.commit()

            statesFile.close()
            for line in teamFile:
                if line != 'ï»¿id,team,state,w,l\n':
                    id = line.split(',')[0]
                    team = line.split(',')[1]
                    state = line.split(',')[2]
                    wins = line.split(',')[3]
                    losses = line.split(',')[4]
                    losses = losses.replace('\n','')
                    cursor.execute("INSERT INTO teams (teamID, Team, TeamState, Wins, Losses) VALUES (?, ?, ?, ?, ?)",(id,team,state,wins,losses))
                    connection.commit()

        # Error opening CSVs
        except IOError as e:
            print(e)

    # Sql error
    except Error as e:
        print("SQL Error: %s",e)


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

# Help
def help() :
    print("")

# Load data


def main():
    dbConnect()
    global connection
    if connection is not None:
        # should only create tables if not exists
        createTables()

        # Perform rest of tasks below







        connection.close()

main()