import requests
from tkinter import *
import time


def api():
    data = []
    ville = input("Entrer un nom de ville: ")
    time.sleep(5)
    url = "http://api.weatherapi.com/v1/current.json?key=30dc9a70cb174cc88bf93846220802&q=" + ville
    content = requests.get(url)
    data = content.json()
    ville = data["location"]["name"]
    region = data["location"]["region"]
    heure = data["location"]["localtime"]
    last_update = data["current"]["last_updated"]
    temperature = data["current"]["temp_c"]
    return ville, region, heure, last_update, temperature


# windows interface
window = Tk()
window.title("Météo")
window.geometry("480x450")
window.iconbitmap("")
window.config(background='#dee5dc')

# Frame principale

label1 = Label(window, text=api(), font=("Courrier", 20), bg="#dee5dc")
label1.pack()

window.mainloop()
