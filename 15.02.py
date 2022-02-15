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
