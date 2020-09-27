from database import *
import string


VALID_SEARCHES = ["teamstate", "populationstate", "capitalstate", "teamcapital", "capitalteam", "stateteam",
                  "populationteam", "statecapital", "winsteam", "lossesteam"]

ALPHABET = list(string.ascii_lowercase)


def helpMenu():
    print('Valid Searches -> Type of return:')
    print('team state \"State Name\" -> Teams within state')
    print('team capital \"State Capital\" -> Teams in corresponding state of the searched capital')
    print('population state \"State Name\" -> Population of state')
    print('population team \"Team Name\" -> Population of the state from which team resides')
    print('capital state \"State Name\" -> Capital City of the state')
    print('capital team \"Team Name\" -> Capital of the state from which team resides')
    print('state team \"Team Name\" -> State from which team resides')
    print('state capital \"State Capital\" -> State from which capital resides')
    print('wins team \"Team Name\" -> Number of wins in 18/19 season of team')
    print('losses team \"Team Name\" -> Number of losses in 18/19 season of team')


def printResult(result):
    count = 1
    for x in result:
        for y in x:
            if y == "NA":
                print("Team has no Home State")
            else:
                print(y, end='')
                if count != len(result):
                    print(', ', end='')
                else:
                    print()
                count += 1




def main():
    end = False
    dbConnect()
    while not checkDBStatus():
        print("Database has not yet been loaded")
        print("Please use the command 'load data'")
        userString = input("> ")
        if userString == "load data":
            createTables()
    while not end:
        userString = input("> ")
        if userString == "quit":
            end = True
        elif userString == "help":
            helpMenu()
        elif userString == "load data":
            if connection is None:
                dbConnect()
            createTables()
        else:

            if connection is None:
                dbConnect()
            # split on spaces
            listInput = userString.split()

            if len(listInput) > 2:
                # add the first two terms as the search fields
                searchFields = ""
                for i in range(2):
                    searchFields += listInput.pop(0)

                # Remove quotes and make strings lowercase
                count = 1
                searchTerm = ""
                for item in listInput:
                    item = item.replace("\"", "")
                    item = item.lower()
                    if item[0] in ALPHABET:
                        item = item.capitalize()
                    if count != len(listInput):
                        item += " "
                    searchTerm += item
                    count += 1

                if searchFields not in VALID_SEARCHES:
                    print("Not a valid query. Type \"help\" for a list of valid queries.")
                else:
                    if searchFields == "teamstate":
                        val = teamState(searchTerm)
                        if val:
                            printResult(val)
                        else:
                            print(searchTerm, " not a valid state name")

                    elif searchFields == "populationstate":
                        val = populationState(searchTerm)
                        if val:
                            printResult(val)
                        else:
                            print(searchTerm, " not a valid state name")

                    elif searchFields == "capitalstate":
                        val = capitalState(searchTerm)
                        if val:
                            printResult(val)
                        else:
                            print(searchTerm, " not a valid state name")

                    elif searchFields == "teamcapital":
                        val = teamCapital(searchTerm)
                        if val:
                            printResult(val)
                        else:
                            print(searchTerm, " not a valid capital name")

                    elif searchFields == "captialteam":
                        val = capitalTeam(searchTerm)
                        if val:
                            printResult(val)
                        else:
                            print(searchTerm, " not a valid team name")

                    elif searchFields == "stateteam":
                        val = stateTeam(searchTerm)
                        if val:
                            printResult(val)
                        elif val == "NA":
                            print("Team not in the US")
                        else:
                            print(searchTerm, " not a valid team name")

                    elif searchFields == "populationteam":
                        val = populationTeam(searchTerm)
                        if val:
                            printResult(val)
                        else:
                            print(searchTerm, " not a valid team name")

                    elif searchFields == "statecapital":
                        val = stateCapital(searchTerm)
                        if val:
                            printResult(val)
                        else:
                            print(searchTerm, " not a valid capital name")

                    elif searchFields == "winsteam":
                        val = winsTeam(searchTerm)
                        if val:
                            printResult(val)
                        else:
                            print(searchTerm, " not a valid team name")

                    elif searchFields == "lossesteam":
                        val = lossesTeam(searchTerm)
                        if val:
                            printResult(val)
                        else:
                            print(searchTerm, " not a valid team name")
            else:
                print("Not a valid query. Type \"help\" for a list of valid queries.")

main()