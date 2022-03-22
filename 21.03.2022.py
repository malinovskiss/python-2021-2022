import random
import json
import sqlite3

masivs = ['a','b','c']
a = ("Akmens")
b = ("Šķēres")
c = ("Papīrs")

izveele = random.choice(masivs)


name_list = ['Akmens', 'Šķēres', 'Papīrs']

print(random.choice(name_list))

from random import choice

def random_element():
   return choice() 

print(random_element(['Akmens', 'Šķēres', 'Papīrs']))

while True:

    vecums = input("Ievadi savu vecumu:")
    if vecums.isdigit() == True:
        continue
    else:
        break

print(vecums)


while True:
    vards = input("Ievadi savu vārdu:")

    if vards.strip() == "":
        print(vards)
        continue
    else:
        break

print(vards)

with open("ievaktieDati.json","r", encoding="utf-8") as fails:
    json_data = json.load(fails)

db = sqlite3.connect("test.db")

dati = db.execute("Vecums * FROM Vārds")
for rinda in dati:
    print("Vecums:", rinda[0])
    print("Vārds:", rinda[1], "/n")

db.close()
