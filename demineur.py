# cree une fenetre

from tkinter import *
from random import *


# cree les case du demineur
def creer_case():
    global cases
    cases = []
    for i in range(10):
        cases.append([])
        for j in range(10):
            cases[i].append(0)

# cree les mines
def creer_mines():
    global mines
    mines = []
    for i in range(10):
        mines.append([])
        for j in range(10):
            mines[i].append(0)

# cree les boutons
def creer_boutons():
    global boutons
    boutons = []
    for i in range(10):
        boutons.append([])
        for j in range(10):
            boutons[i].append(Button(fenetre, width=2, height=1, bg="grey", command=lambda i=i, j=j: clic(i, j)))
            boutons[i][j].grid(row=i, column=j)

# place les mines
def placer_mines():
    for i in range(10):
        for j in range(10):
            if randint(0, 100) < 20:
                mines[i][j] = 1

# on click droit sur le bouton cree un drapeau
def clic_droit(event):
    event.widget.config(text="D")

# fonction qui gere le clic
def clic(i, j):
    if mines[i][j] == 1:
        boutons[i][j].config(bg="red")
        boutons[i][j].config(text="X")
    else:
        boutons[i][j].config(bg="white")
        boutons[i][j].config(text="O")

# lance le programme

fenetre = Tk()
fenetre.title("Demineur")
creer_case()
creer_mines()
creer_boutons()
placer_mines()
fenetre.mainloop()

# fin du programme
