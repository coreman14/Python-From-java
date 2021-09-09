from colorama import Fore, Back, Style, init
init(autoreset=True,strip=True)
red = Fore.RED
def doubleInputCheck(ask): #Python doenst have a way to check for input type like java, so we make a simple one
    while True:
        val = input(ask) #Keep asking for a number until one is given
        try:
            val = float(val)
            return val
        except ValueError:
            print(red + "Please enter a number")

def intInputCheck(ask): #same thing but for integer
    while True:
        val = input(ask) #Keep asking for a number until one is given
        try:
            val = int(val)
            return val
        except ValueError:
            print(red + "Please enter a whole number")

def doubleInputCheckMulti(*args): #Python doenst have a way to check for input type like java, so we make a simple one
    vals = []
    for ask in args:
        while True:
            val = input(ask) #Keep asking for a number until one is given
            try:
                val = float(val)
                vals.append(val)
                break
            except ValueError:
                print(red + "Please enter a number")
    return vals

def intInputCheckMulti(*args): #same thing but for integer
    vals = []
    for ask in args:
        while True:
            val = input(ask) #Keep asking for a number until one is given
            try:
                val = float(val)
                vals.append(val)
                break
            except ValueError:
                print(red + "Please enter a whole number")
    return vals