import json

#Kaut kāda vārdnīca
vārdnīca = {}

{"Vārds":"Jānis","izglītība":"Vidēja","vecums":45}

#Pārveidot python
a = json.dumps(vārdnīca)

print(a)

#Pārveidot JSON uz Python
b = json.loads(a)

print(json.dumps({"kivi", "citrons"}))

#Dict - Object
#list - Array
#tuple - Array
#int - Number
#float - Number
#True - true
#False - false
#None - null

py_data = {
    "Vārds":"Annika",
    "vecums":30,
    "Dzīvs":"true",
    "Nedzīvs":"false",
    "Berni":("Gatis","Anna"),
    "Dzivnieki":None,
    "Masinas":[
        {"Modelis":"Ford Focus","Gads":2007},
        {"Modelis":"Audi A6","Gads":2010},
    ]
}
json_dati = "a"
print(json.dumps(py_data, indent=4, separators=(".", "=")))

with open("pirmais_json.json","w", encoding="utf-8") as fails:
    json.dump(py_data,fails, indent = 4, ensure_ascii=False)

with open("pirmais_json.json","r", encoding="utf-8") as fails:
    json.dumps

#Vārdnīcas garums
print(len("json_dati"))

#Visas atslēgas
print("json_dati.keys"())

#Visas vērtības
print("json_dati.values"())

#Pārbaudi, vai dotā atslēga ir vārdnīca un izvadi tās vērtību
atsli = "Gadi"
key="b"
for atslega in json_dati.keys():
    if atslega == atsli:
        print(json_dati[atslega])
    if atsli != atslega:
        print(f"Izskatās, ka (atsli) nav sarakstā")


#Nodefinēt funkciju, kura kā argumentus izmantos, datnes nosaukumu un atslēgas nosaukumu
#Jāizvada atslēgas vērtību
def datnes_las (datnesnosaukums,atslega):
    for ley in datnesnosaukums:
        if key == atslega:
            print(datnesnosaukums[atslega])
            return
        else:
            break
    print("Nav atslēgas")
