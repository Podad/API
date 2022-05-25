import random
import time

password = input("Entre un mot de passe: ")

characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
tryPassword = ""
tryPasswordTries = 0
timeStart = time.time()

while True:
    tryPasswordTries += 1

    for character in range(len(password)):
        tryPassword = tryPassword + characters[random.randint(0, 9)]

    timeStop = time.time()
    timeTotal = round(timeStop - timeStart, 1)

    if tryPassword == password:
        print(f"{tryPasswordTries} | Valid | {tryPassword}  ({timeTotal}s)")
        break
    else:
        print(f"{tryPasswordTries} | Invalid | {tryPassword}")

        tryPassword = ""
