from output import *

VALID_SEARCHES = ["team state", "population state", "capital state", "team capital", "capital team", "state team",
                  "population team", "state capital", "wins team", "losses team"]

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
            # TODO split userString into two strings (searchFields, searchTerm)

            # split on spaces
            # Example: state team "la lakers"
            # listInput = ["state", "team", "\"la", "lakers\""]

            # searchFields = ""
            # searchFields = listInput.pop(0)
            # searchFields += listInput.pop(1)

            # searchTerm =


            searchFields = ""
            if searchFields not in VALID_SEARCHES:
                print("ERROR")
            else:
                print()
                # TODO call the correct function from output correctFunction(searchTerm)
