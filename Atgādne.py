#Motīvs jeb list

#Pirmais skaitlis ir 0

masivs = ["A", "B", "C", "D", "E", "F"]

print (masivs)
print (type(masivs))
print (masivs[3])

for x in masivs:
    print (x)

vārdnīca = {"Vārds":"Jānis","izglītība":"Vidēja","vecums":45}

print (vārdnīca)
print(type(vārdnīca))
print(vārdnīca["Vārds"])

personas = [
    {"Vārds":"Jānis","izglītība":"Vidēja","vecums":45},
    {"Vārds":"Viesturs","izglītība":"Augstākā","Vecums":27}
]

print(type(personas))

for persona in personas:
    print(persona["Vārds"])

file = open("meginajums.txt", "w", encoding = "utf-8")

file.write("MESSI")

saturs = ["ir 2022 gads /n"]

file.writelines(saturs)

file.close()

with open("meginajums.txt","r", encoding="utf-8") in file:

    print(file.read())
    print(file.readline())

    file.read(0)

    print(file.readline())