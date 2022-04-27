import random

# Pierre Papier Ciseau

#pierre > ciseau
#ciseau > papier
#papier > pierre


jeux = True
pierre = "pierre"
papier = "papier"
ciseau = "ciseau"
a = random.randint(0, 2)
b = (papier, pierre, ciseau)
c = b[a]


user = input("Entre une réponse")


while jeux:
    if user == papier:
        if c == user:
            print("Egaliter")
    elif user == pierre:
        if c ==
    elif user != c:
        user = input("Entre une autre réponse : ")
        a = random.randint(0, 2)
        b = (papier, pierre, ciseau)
        c = b[a]
    else:
        jeux = False
        print("ERREUR")
        break


print("gg mec")
print(c)
