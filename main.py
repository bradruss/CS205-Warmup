from database import *
import string

VALID_SEARCHES = ["team state", "population state", "capital state", "team capital", "capital team", "state team",
                  "population team", "state capital", "wins team", "losses team"]

ALPHABET = list(string.ascii_lowercase)

def main():
    end = False
    while not end:
        userString = input("> ")
        if userString == "quit":
            end = True
        elif userString == "help":
            # TODO call help function
            print()
        elif userString == "load data":
            # TODO call load data function
            print()
        else:

            if connection is None:
                dbConnect()
            # split on spaces
            listInput = userString.split()

            # add the first two terms as the search fields
            searchFields = ""
            searchFields += listInput.pop(0)
            searchFields += listInput.pop(1)

            # Remove quotes and make strings lowercase
            for item1 in listInput:
                item1.replace("\"", "")
                item1 = item1.lower()

            # make the first letter of each word capital
            for item2 in listInput:
                if item2[0] in ALPHABET:
                    item2[0].upper()

            # Add each word to the searchTerm string
            searchTerm = ""
            for item3 in listInput:
                searchTerm += item3

            if searchFields not in VALID_SEARCHES:
                print("Not a valid query. Type \"help\" for a list of valid queries.")
            else:
                if searchFields == "teamstate":
                    val = teamState(searchTerm)
                    if val != "":
                        print(val)
                    else:
                        print(searchTerm, " not a valid state name")

                elif searchFields == "populationstate":
                    val = populationState(searchTerm)
                    if val != "":
                        print(val)
                    else:
                        print(searchTerm, " not a valid state name")

                elif searchFields == "capitalstate":
                    val = capitalState(searchTerm)
                    if val != "":
                        print(val)
                    else:
                        print(searchTerm, " not a valid state name")

                elif searchFields == "teamcapital":
                    val = teamCapital(searchTerm)
                    if val != "":
                        print(val)
                    else:
                        print(searchTerm, " not a valid capital name")

                elif searchFields == "captialteam":
                    val = capitalTeam(searchTerm)
                    if val != "":
                        print(val)
                    else:
                        print(searchTerm, " not a valid team name")

                elif searchFields == "stateteam":
                    val = stateTeam(searchTerm)
                    if val != "":
                        print(val)
                    elif val == "NA":
                        print("Team not in the US")
                    else:
                        print(searchTerm, " not a valid team name")

                elif searchFields == "populationteam":
                    val = populationTeam(searchTerm)
                    if val != "":
                        print(val)
                    else:
                        print(searchTerm, " not a valid team name")

                elif searchFields == "statecapital":
                    val = stateCapital(searchTerm)
                    if val != "":
                        print(val)
                    else:
                        print(searchTerm, " not a valid capital name")

                elif searchFields == "winsteam":
                    val = winsTeam(searchTerm)
                    if val != "":
                        print(val)
                    else:
                        print(searchTerm, " not a valid team name")

                elif searchFields == "lossesteam":
                    val = lossesTeam(searchTerm)
                    if val != "":
                        print(val)
                    else:
                        print(searchTerm, " not a valid team name")