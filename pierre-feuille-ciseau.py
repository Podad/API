from asyncio.windows_events import PipeServer
import time
import random

# Pierre Papier Ciseau

pierre = "pierre"
papier = "papier"
ciseau = "ciseau"
a = random.randint(0, 2)
g = True
user = input("Enter ")
b = (papier, pierre, ciseau)
c = b[a]
d = True

print(c)
time.sleep(1)
print(user)
