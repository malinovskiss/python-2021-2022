vārdnīca = {"Vārds":"Nauris","uzvārds":"Skuja","vecums":45,"Telefona numurs":"27798261"}

print (vārdnīca)
print(type(vārdnīca))
print(vārdnīca["Vārds"])

personas = [
    {"Vārds":"Nauris","uzvārds":"Skuja","vecums":45,"Telefona numurs":"27798261"},
    {"Vārds":"Viesturs","izglītība":"Augstākā","Vecums":27,"Telefona numurs":"27798261"}
]

print(type(personas))

for persona in personas:
    print(persona["Vārds"])

    #Savaktie dati jasaglaba faila 'ievaktieDati.json'

import json
vards = input('ievadit vardu:')
uzvards = input('ievadit uzvardu:')
vecums = input('ievadit vecumu:')
tel = input('ievadit telefona numuru:')

vardnica = {
    'Vards':vards,
    'Uzvards':uzvards,
    'Vecums':vecums,
    'Telefona Numurs':tel
}

def dati(vards,uzvards,vecums,tel):
    with open('ievaktieDati.json','w',encoding='utf-8') as file:
        json.dump(vardnica,file,indent=4,ensure_ascii=False)
dati(vards,uzvards,vecums,tel)
