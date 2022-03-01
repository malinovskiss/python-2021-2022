import json

while True:
    vardss = input('ievadiet vardu: ')
    if vardss.isdigit() == False:
        if vardss.strip() == '':
            print('ievadiet vardu atkartoti')
            continue
        else:
            break
    else:
        print('ievadiet vardu atkartoti')
        continue

        

while True:
    uzvardss = input('ievadiet uzvardu: ')
    if uzvardss.isdigit() == False:
        if uzvardss.strip() == '':
            print('ievadiet uzvardu atkartoti')
            continue
        else:
            break
    else:
        print('ievadiet uzvardu atkartoti')
        continue


while True:
    vecumss = input('ievadiet vecumu: ')
    if vecumss.isdigit():
        break
    else:
        print('ievadiet vecumu atkartoti')
        continue

while True:
    tell = input('ievadiet telefona numuru: ')
    if tell.isdigit():
        if len(tell) == 8:
            break
    else:
        print('ievadiet telefona numuru atkartoti')
        continue

vardnica = {
    "Uzvārds":uzvardss,
    "Vecums":vecumss,
    "Telefona numurs":tell
}

with open("ievaktieDati.json","r", encoding="utf-8") as fails:
    json_data = json.load(fails)

    ir_saraksta = True
    for key in json_data.keys():
        if key == vardss:
            break
        if key != vardss:
            print(key)
            ir_saraksta == False

    if ir_saraksta == True:
        print('Vards ir saraksta')
    else:
        json_data[vardss]=vardnica


with open("ievaktieDati.json","w", encoding="utf-8") as fails:
    json.dump(json_data,fails, indent = 4, ensure_ascii=False)
    
    #Datu meklēšana

mekl_vards = input("Ievadi vārdu, kuru vēlies atrast: ")

with open("ievaktieDati.json","r", encoding="utf-8") as fails:
    json_data = json.load(fails)

for key in json_data.keys():
    if key == mekl_vards:
        dati = json_data[key]
        break
    else:
        dati = "Nav sarakstā"

#Savāktie dati jāsaglabā failā ievaktieDati.json

with open("ievaktieDati.json","w", encoding="utf-8") as fails:
    json.dump(json_data,fails, indent = 4, ensure_ascii=False)

while True:
    print("\nIzvēlies darbību:")
    print("1 - kontakta pievienošana")
    print("2 - kontakta meklēšana")

    ievad_dati = (
        "Uzvārds":uzvards,
        "Vecums":vecums,
        "Telefona numurs":tel_nr
    )

    kont_saglabat(vards,ievad_dati)

def kont_saglabat(vards,ievad_dati):
    with open("ievaktieDati.json","r", encoding="utf-8") as fails:
        json_data = json.load(fails)

    ir_saraksta = False

    izveele = input()

    if izveele =="1":
        kont_piev()
    elif int(izveele) == 2:
        kont_mekl()
    elif int(izveele) == 3:
        exit()
    else:
        print("\nIzvēlies kādu no darbībām!")

import datetime

print(datetime.datetime.now())

print(datetime.datetime(2020,7,12))

"""
%A - diena
%d - mēneša diena
%j - diena gadā
%B - mēnesis
"""

a = datetime.datetime.now()
parv_laiks = a.isoformat()
json_a = json.dump(a)
print(json_a)
