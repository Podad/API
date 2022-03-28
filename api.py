import requests


class api():
    data = []
    ville = input("Entrer un nom de ville: ")
    url = "http://api.weatherapi.com/v1/current.json?key="mettre sa propre clé api "" & q = + ville
    content = requests.get(url)
    data = content.json()
    ville = data["location"]["name"]
    region = data["location"]["region"]
    heure = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    last_update = data["current"]["last_updated"]
    str_temperature = str(temperature)
    print("Dans la ville de : " + ville)
    print("Dans la region : " + region)
    print("Heure local : " + heure)
    print("Temperature : " + str_temperature + "°C")
    print("Derrnier mise a jour : " + last_update)


api()
