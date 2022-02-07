

import csv

file = open("csv_meg.csv"'w')

print(type(file))

lasīt_csv = csv.reader(file)

print(lasīt_csv)

#Kolonnu nosaukumi

header = []
header = next(lasīt_csv)
print(header)

#Satura nolasīšana

saturs = []
for rinda in lasīt_csv:
    saturs.append(rinda)

print(saturs)
print(type(saturs))

file.close()

#Jauna faila izveidošana

kolonnuNosaukumi = ('Vārds', '1.atzīme', '2.atzīme')
dati = [('Pēteris',6,8), ('Annika',7,5), ('Viesturis',8,9)]

with open('skolenu_dati.csv', 'w',encoding="utf-8") as fails:
    csvwrite = csv.writer(fails)
    csvwrite.writerow(kolonnuNosaukumi)
    csvwrite.writerows(dati)

#Ielasi datnes saturu, pārveido to par masīvu

with open('skolenu_dati.csv', 'w',encoding="utf-8") as fails:
    lasīt_csv = csv.reader(file)
    saturs = []
    for rinda in lasīt_csv:
        saturs.append(rinda)

    #Masīva garums
    print(len(saturs))

    #Pirmā elementa saturu
    print(saturs[0])

    #Izvadi uz ekrāna masīva pirmo 3 elementa saturu
    for s in range(3):
        print(saturs[s])
        
