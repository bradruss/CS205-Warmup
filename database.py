import sqlite3
import os
from sqlite3 import Error
connection = None

# TODO: When dealing with the Wizards and Raptors, make sure that Canada/DC is returned correctly
# ie: This team is not part of the US

def checkDBStatus():
    # Check if file exists
    if os.path.isfile('./nba.db'):
        global connection
        cursor = connection.cursor()

        #Check if table exists
        try:
            qry = cursor.execute("SELECT NULL FROM states LIMIT 1")
            return True
        except Error as e:
            return False
    else :
        return False


# Create tables
def createTables():
    try:
        global connection
        cursor = connection.cursor()
        # Create tables
        cursor.execute("""CREATE TABLE IF NOT EXISTS states (
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
                    stateTemp = line.split(',')[1]
                    capital = line.split(',')[2]
                    population = line.split(',')[3]
                    population = population.replace('\n','')
                    cursor.execute("INSERT INTO states (State, Capital, Population) VALUES (?, ?, ?)", (stateTemp, capital, population))
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

def teamState(state):
    global connection
    cursor = connection.cursor()
    query = """SELECT Team FROM teams WHERE TeamState LIKE '""" + state + """'"""
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    return returnVal

def populationState(state):
    global connection
    cursor = connection.cursor()
    query = """SELECT Population FROM states WHERE State LIKE '""" + state + """'"""
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    return returnVal

def capitalState(state):
    global connection
    cursor = connection.cursor()
    query = """SELECT Capital FROM states WHERE State LIKE '""" + state + """'"""
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    return returnVal

def teamCapital(capital):
    global connection
    cursor = connection.cursor()
    query = """SELECT Team FROM teams LEFT OUTER JOIN states ON states.State = teams.TeamState WHERE Capital LIKE '""" + capital + """'"""
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    return returnVal

def capitalTeam(team):
    global connection
    cursor = connection.cursor()
    query = """SELECT Capital FROM states LEFT OUTER JOIN teams ON teams.TeamState = states.State WHERE Team LIKE '""" + team + """'"""
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    return returnVal

def stateTeam(team):
    global connection
    cursor = connection.cursor()
    query = """SELECT TeamState FROM teams WHERE Team LIKE '""" + team + """'"""
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    return returnVal

def populationTeam(team):
    global connection
    cursor = connection.cursor()
    query = """SELECT Population FROM states LEFT OUTER JOIN teams ON teams.TeamState = states.State WHERE Team LIKE '""" + team + """'"""
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    return returnVal

def stateCapital(capital):
    global connection
    cursor = connection.cursor()
    query = """SELECT State FROM states WHERE Capital LIKE '""" + capital + """'"""
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    return returnVal

def winsTeam(team):
    global connection
    cursor = connection.cursor()
    query = """SELECT Wins FROM teams WHERE Team LIKE '""" + team + """'"""
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    return returnVal

def lossesTeam(team):
    global connection
    cursor = connection.cursor()
    query = """SELECT Losses FROM teams WHERE Team LIKE '""" + team + """'"""
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    return returnVal
