import os
import sys 

def checkArgLen(expectedArgs, parsedCommand) -> bool:
    if len(parsedCommand) != expectedArgs:
        print("\033[1m\033[91m" + "SCLI:" + "\033[0m Not Enough Arguments Supplied")
        return False
    else:
        return True
