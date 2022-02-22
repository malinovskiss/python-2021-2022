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

while True:
    tel_nr = input("Ievadi savu telefona numuru:")

    if len(tel_nr) == "":
        print(vards)
        continue
    else:
        break
print(tel_nr)

#Labojumi

import json

while True:
    vardsss = input('ievadiet vardu:')
    if vardsss.strip() == "" and vardsss.isdigit() == True:
        print("ievadiet velreiz")
    else:
        break

while True:
    uzvardsss = input('ievadiet uzvardu: ')
    if uzvardsss.strip() == "" and uzvardsss.isdigit() == True:
        print("ievadiet velreiz")
    else:
        break

while True:
    vecumsss = input('ievadiet vecumu:')
    if len(vecumsss) <0 and len(vecumsss) >100 and vecumsss.isdigit() == False:
        continue
    else:
        break

while True:
    tell = input('ievadiet telefona numuru: ')
    if len(tell) <8 and tell.isdigit() == False and len(tell) >8:
        continue
    else:
        break

vardnica = {}
vardnica [vardsss] = {
    'Uzvards':uzvardsss,
    'Vecums':vecumsss,
    'Telefona Numurs':tell
}

def dati(vards,uzvards,vecums,tel):
    with open('ievaktieDati.json','w',encoding='utf-8') as file:
        json.dump(vardnica,file,indent=4,ensure_ascii=False)


dati(vardsss,uzvardsss,vecumsss,tell)
