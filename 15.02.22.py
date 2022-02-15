#Definē funkciju, kuras argumenti ir divu json failu nosaukumi
#Pārveido failus par vārdnīcu
#Abas vārdnīcas apvienot un ierakstīt rezultātu jaunā json failā
#Salīdzināt vārdnīcu atslēgas un izvadīt tikai tos datus, kuri ir atrodami vienā no šīm vārdnīcām
#Salīdzināt vārdnīcu atslēgas un izvadīt tikai tos datus, kuri ir atrodami abās vārdnīcās

import csv

def kopa_csv(pirmaisCSV, otraisCSV):

    with open('pirmaisCSV', 'r',encoding="utf-8") as fails:
        lasīt_csv = csv.reader(fails)
        saturs = []
        for rinda in lasīt_csv:
            saturs.append(rinda)

    with open('otraisCSV', 'r',encoding="utf-8") as fails:
        lasīt_csv = csv.reader(fails)
        saturs_otrajam = []
    for rinda in lasīt_csv:
        saturs_otrajam.append(rinda)

json_dati = "a"

atsli = "Gadi"
key="b"
for atslega in json_dati.keys():
    if atslega == atsli:
        print(json_dati[atslega])
    if atsli != atslega:
        print(f"Izskatās, ka (atsli) nav sarakstā")

def datnes_las (datnesnosaukums,atslega):
    for ley in datnesnosaukums:
        if key == atslega:
            print(datnesnosaukums[atslega])
            return
        else:
            break
    print("Nav atslēgas")
