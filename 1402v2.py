#Definēt funkciju, kuras argumenti ir divi csv failu nosaukumi
#Pārveidot failus masīvos
#Jāsalīdzina masīvu garumi

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

    if len(saturs) == len(saturs_otrajam):
        with open('divikopa.csv', 'w',encoding="utf-8",newline='') as fails:
            csvwrite = csv.writer(fails)
            csvwrite.writerow(saturs)
            csvwrite.writerows(saturs_otrajam)

#Ja masīvi ir vienādi
#Masīva garums
#Tos apvieno un rezultātu saglabā jaunā datnē
#Salīdzināt pirmās un otrās datnes masīvus
#Saglabājot tikai atšķirīgos datus
