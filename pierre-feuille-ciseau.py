from asyncio.windows_events import PipeServer
import time
import random

# Pierre Papier Ciseau

pierre = "pierre"
papier = "papier"
ciseau = "ciseau"
a = random.randint(0, 2)
g = True
user = input("Enter")
b = (papier, pierre, ciseau)
c = b[a]
d = True

print(c)


while d == True:

    if c == "papier":
        if user == c:
            print("papier")
    elif c == "pierre":
        if user == c:
            print("pierre")
    elif c == "ciseau":
        if user == c:
            print("ciseau")
