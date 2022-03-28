import sqlite3

#Tabulas izveide

db = sqlite3.connect('edienkarte DB.sqbpro')

db.execute("""CREATE TABLE IF NOT EXISTS edienkarte
(id        INT     PRIMARY KEY      NOT NULL,
vards  TEXT    NOT NULL,
vecums       REAL    NOT NULL,
ediens   CHAR(50)
""")

#Datu pievienošana
db.execute("""INSERT INTO edienkarte
(id,vards,vecums,ediens)
VALUES (1,'Janis',23'makaroni')
""")

db.commit()

#Datu iegūšana
dati = db.execute("SELECT * FROM edienkarte WHERE cena > 0.5")
rezultats = dati.fetchall()

print(rezultats)

#Tabulas izveide, izmantojot AUTOINCREMENT
db.execute("""CREATE TABLE IF NOT EXISTS sastavdalas
(id        INTEGER     PRIMARY KEY AUTOINCREMENT     NOT NULL,
vards  CHAR(50)    NOT NULL,
vecums    CHAR(50),
ediens   CHAR(50)
""")