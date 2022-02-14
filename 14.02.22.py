import csv

#Definēt funkciju, kuras argumenti ir divi csv failu nosaukumi

file = open("csv_meg.csv"'w')

print(type(file))

lasīt_csv = csv.reader(file)

print(lasīt_csv)

kolonnuNosaukumi = ('Vārds', '1.atzīme', '2.atzīme')
dati = [('Pēteris',7,9), ('Annika',6,10), ('Megija',8,9)]

with open('skolenu_dati.csv', 'w',encoding="utf-8") as fails:
    csvwrite = csv.writer(fails)
    csvwrite.writerow(kolonnuNosaukumi)
    csvwrite.writerows(dati)

#Pārveidot failus masīvos

with open('skolenu_dati.csv', 'w',encoding="utf-8") as fails:
    lasīt_csv = csv.reader(file)
    saturs = []
    for rinda in lasīt_csv:
        saturs.append(rinda)

#Masīva garums

print(len(saturs))

#Tos apvieno un rezultātu saglabā jaunā datnē

def izvadi_funkc(datne):
    with open('skolenu_dati.csv', 'w',encoding="utf-8") as fails:
        lasīt_csv = csv.reader(file)
        saturs = []
        for rinda in lasīt_csv:
            saturs.append(rinda)

        print(saturs)