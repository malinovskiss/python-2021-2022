import sqlite3

db = sqlite3.connect('test.db')

#Tabulas izveide
# db.execute("""CREATE TABLE IF NOT EXISTS edienkarte
#     (id        INT     PRIMARY KEY      NOT NULL,
#     nosaukums  TEXT    NOT NULL,
#     cena       REAL    NOT NULL,
#     alergeni   CHAR(50)
#     )""")

#Datu pievienošana
# db.execute("""INSERT INTO edienkarte
#             (id,nosaukums,cena,alergeni)
#             VALUES (1,'makaroni',1.5,'glutēns')
# """)

#db.commit()

#Datu iegūšana
# dati = db.execute("SELECT * FROM edienkarte WHERE cena > 0.5")
# rezultats = dati.fetchall()

# print(rezultats)

#Tabulas izveide, izmantojot AUTOINCREMENT
# db.execute("""CREATE TABLE IF NOT EXISTS sastavdalas
#     (id        INTEGER     PRIMARY KEY AUTOINCREMENT     NOT NULL,
#     pirma  CHAR(50)    NOT NULL,
#     otra    CHAR(50),
#     tresa   CHAR(50)
#     )""")

# pirma = input("Pirmā sastāvdaļa: ")
# otra = input("Otrā sastāvdaļa: ")
# tresa = input("Trešā sastāvdaļa: ")

# #Datu ievietošana
# db.execute("""INSERT INTO sastavdalas
#             (pirma,otra,tresa)
#             VALUES (:pirma,:otra,:tresa)
# """,{'pirma':pirma,'otra':otra,'tresa':tresa})

# db.commit()


dati = db.execute("SELECT * FROM edienkarte")
for rinda in dati:
    print("ID: ", rinda[0])
    print("Nosaukums: ", rinda[1])
    print("Cena: ", rinda[2])
    print("Alergēni: ", rinda[3], "\n")

db.close()

#29.03.2022

from xlwt import workbook

wb = workbook()

lapa1 = wb.add_sheet('Lapa1')

#lapa1.write(rinda,kolonna,dati,stils)

lapa1.write(0,0,'Sveiki')
lapa1.write(1,0,'Sveiki')
lapa1.write(2,0,'Sveiki')
lapa1.write(3,0,'Sveiki')

wb.save('meginajums.xls')

import XlsxWriter

fails = XlsxWriter.Workbook('meginajums2.xlsx')
lapa = fails.add_worksheet()

lapa.write('A1','Riga')
lapa.write('C2','Londona')

fails.close()
