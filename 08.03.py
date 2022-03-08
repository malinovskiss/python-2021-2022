from itertools import combinations_with_replacement
import sqlite3

db = sqlite3.connect("test.db")

#Tabulas izveide
db.execute ('''CREATE TABLE IF NOT EXISTS edienkarte
#    (id        INT     PRIMARY KEY     NOT NULL,
#    nosaukums  TEXT    NOT NULL,
#    cena       REAL    NOT NULL,
#    alergeni   CHAR(50),
#    )''')

#Datu pievienošana
db.execute("""INSERT INTO edienkarte
            (id,nosaukums,cena,alergeni)
            VALUES (2,"siers",1,"laktoze")
""")

db.execute("""INSERT INTO edienkarte
            (id,nosaukums,cena,alergeni)
            VALUES (1,"makaroni",1.5,"glutēns")
""")

db.execute("""INSERT INTO edienkarte
            (id,nosaukums,cena,alergeni)
            VALUES (1,"makaroni",1.5,"glutēns")
""")


db.commit()


dati = db.execute("SELECT* FROM edienkarte WHERE cena > 0.5")
rezultats = dati.fetchall()

print(rezultats)

db.execute ('''CREATE TABLE IF NOT EXISTS sastavdalas
#    (id        INTEGER     PRIMARY KEY AUTOINCREMENT     NOT NULL,
#    pirma  CHAR(50)    NOT NULL,
#    OTRA    CHAR(50),
#    TRESA   CHAR(50)
#    )''')

pirma = input("Pirmā sastāvdaļa: ")
otra = input("Otrā sastāvdaļa: ")
tresa = input("Trešā sastāvdaļa: ")

db.execute("""INSERT INTO sastavdalas
            (pirma,otra,tresa)
            VALUES (:pirma,:otra,:tresa)
""",{"pirma":"pirma","otra":"otra","tresa":"tresa"})

db.commit()

dati = db.execute("SELECT * FROM edienkarte")
for rinda in dati:
    print("ID:", rinda[0])
    print("Nosaukums:", rinda[1])
    print("Cena:", rinda[2])
    print("Alergēni:", rinda[3], "/n")

db.close()
