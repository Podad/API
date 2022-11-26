import colorama
from colorama import *
import time
import hashlib

colorama.init()

blue = Fore.BLUE
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
purple = Fore.MAGENTA

def main():
    print(f"{purple}Welcome to Hexa")
    print(f"{purple}Please choose an option")
    print(f"{red}1. Encrypt")
    print(f"{green}2. Decrypt")
    print(f"{yellow}3. Exit")
    choice = input(f"{blue}>> ")
    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    elif choice == "3":
        exit()
    else:
        print(f"{red}Invalid choice")
        time.sleep(1)
        main()

def encrypt():
    texte =  input(f"{red}Quelle est la chose a chiffrer?")
    hash_object = hashlib.sha256(texte.encode())
    hachage = hash_object.hexdigest()
    print(hachage)
    fichier = open("app.log", "a")
    texte = hachage
    fichier.write(texte+"\n")
    fichier.close()
    print(f"{red}Le hash est: {hachage}")
    time.sleep(1)
    main()

def decrypt():
    texte = input(f"{red}Quelle est la chose a Déchiffrer?")
    hash_object = hashlib.sha256(texte.encode())
    hachage = hash_object.hexdigest()
    f = open("texte.txt", "r+")
    f.read()
    print(f)
    print(hachage)
    time.sleep(1)
    main()

if __name__ == "__main__":
    main()
