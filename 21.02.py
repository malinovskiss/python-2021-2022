#Dati, kurus ievadīs:
#Vārds
#Uzvārds
#Vecums
#Telefona numurs

import json

vards = input("Ievadi vārdu: ")
uzvards = input("Ievadi uzvārdu: ")
vecums = input("Ievadi vecumu: ")
tel_nr = input("Ievadi telefona numuru: ")

def check_if_digit(a):
    if a.isdigit():
        return True
    else:
        return False
def check_lenght(a):
    if len(a)<8:
        return False
    else:
        return True

while True:
    vards= input("Ievadi uzvārdu: ")
    if check_if_digit(uzvards) or check_if_digit(uzvards):
        continue
    else:
        break

while True:
    vecums = input("Ievadi vecumu: ")
    if check_if_digit(vecums):
        break
    else:
        break



#Dati jāsaglabā vārdnīcā ({})

ievad_dati = {
    "Uzvārds":uzvards,
    "Vecums":vecums,
    "Telefona numurs":tel_nr
}

with open("ievaktieDati.json","r", encoding="utf-8") as fails:
    json_data = json.load(fails)

    ir_saraksta =False
    for key in json_data.keys():
        if key == vards:
            break
        if key != vards:
            ir_saraksta = True

    if ir_saraksta == False:
        print("Vārds ir sarakstā")
    else:
        json_data[vards]=ievad_dati

#Savaktie dati jasaglaba faila 'ievaktieDati.json'

with open("ievaktieDati.json","w", encoding="utf-8") as fails:
    json.dump(json_data,fails, indent = 4, ensure_ascii=False) 

{
    "Vards": "Annnika",
    "Vecums": 30,
    "Dzives vieta": True,
    "NeDzivs": False,
    "Berni": [
        "Gatis",
        "Anna"
    ],
    "Gramatas": True,
    "Masinas": [
        {
            "Modelis": "Ford Focus",
            "Gads": 2007
        },
        {
            "Modelis": "Audi A6",
            "Gads": 2010
        }
    ]
} 