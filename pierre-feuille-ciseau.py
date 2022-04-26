import random
import re

# Pierre Papier Ciseau


def ordi():
    global c
    pierre = 0
    papier = 1
    ciseau = 2
    a = random.randint(0, 2)
    b = (papier, pierre, ciseau)
    c = b[a]
    return c


user = input("Enter ")

if user == c:
    print("gg mec")

user = input("Entre une réponse")
