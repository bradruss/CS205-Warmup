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



def teamState(state):
    global connection
    cursor = connection.cursor()
    query = """SELECT Team FROM teams WHERE TeamState LIKE '""" + state + """'"""
    cursor.execute(query)
    returnVal = cursor.fetchall()
    cursor.close()
    connection.commit()
    return returnVal
    # if not returnVal:
    #     print("NONE")
    # else:
    #     for x in returnVal:
    #         for y in x:
    #             print(y, end='')
    #             if y != returnVal[-1]:
    #                 print(', ', end='')
    #             else:
    #                 print('\n')

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



def main():
    dbConnect()
    global connection
    if connection is not None:
        # should only create tables if not exists
        createTables()

        # Perform rest of tasks below
        print(teamState("California"))
        print(populationState("California"))
        print(capitalState("California"))
        print(teamCapital("Denver"))
        print(capitalTeam("Denver Nuggets"))
        print(stateTeam("Denver Nuggets"))
        print(populationTeam("Denver Nuggets"))
        print(stateCapital("Denver"))
        print(winsTeam("Denver Nuggets"))
        print(lossesTeam("Denver Nuggets"))

        print(teamState(""))
        print(teamCapital(""))
        print(capitalTeam(""))
        print(stateTeam(""))
        print(populationTeam(""))
        print(stateCapital(""))
        print(winsTeam(""))
        print(lossesTeam(""))

        print(teamState("ghhjhjgjhf"))
        print(teamCapital("safsfds"))
        print(capitalTeam("dsfdsfds"))
        print(stateTeam("afdsd"))
        print(populationTeam("dfsfdsaf"))
        print(stateCapital("dsfafdsa"))
        print(winsTeam("fdsafdas"))
        print(lossesTeam("dsfdasfd"))







        connection.close()

main()