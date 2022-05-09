#1.uzd
# Dota programma, kuras uzdevums ir aprēķināt riņķa laukumu # Testēšana: 3 ----> 28.26 

#r = float(input("Ieraksti riņķa rādiusu: ")) 
#pi = 3.14 
#laukums = pi * r**2 
#print(f"Riņķa laukums ir {laukums}") 

#2.uzd
# Dota programma, kuras uzdevums ir izvadīt lietotāja ievadīto vārdu un  uzvārdu apgrieztā secībā (starp vārdu un uzvārdu ir jābūt atstarpei) # Testēšana: Anna Bērziņa -----> Bērziņa Anna 
#vards = input("Ievadi vārdu: ") 
#uzvards = input("Ievadi uzvārdu: ") 
#print(uzvards,vards)

#3.uzd
#Dota programma, kuras uzdevums ir - lietotāja ievadītos skaitļus (kas  atdalīti ar komatiem), izdrukāt kā sarakstu(list) un kortežu(tuples) #Testēšana: 1,2,3,4,5,6 -----> Saraksts: ['1','2','3','4','5','6'] # -----> Kortežs: ('1','2','3','4','5','6') 

#vertibas = input("Ievadi skaitļus, atdalot tos ar komatiem: ") 
#saraksts = vertibas.split(",") 
#kortezs = tuple(saraksts) 
#print('Saraksts : ',saraksts) 
#print('Kortežs : ',saraksts) 

#4.uzd
#Dota programma, kuras uzdevums ir izvadīt pirmo un pēdējo krāsu no dotā  saraksta 
#Testēšana: ------> Sarkans, melns
 
#krasu_saraksts = ["Sarkans","Zaļš","Balts""Melns"] 
#print( "%s %s"(krasu_saraksts[2],krasu_saraksts[1]))

#5.uzd
#Dota programma, kuras uzdevums ir veikt sekojošo matemātisko darbību ar  ievades skaitli (n): n+nn+nnn 
#Testēšana: 5 ----> 615 

#a = int(input("Ievadi veselu skaitli: ")) 
#n1 = int( "%s" % a ) 
#n2 = int( "%s%s" % (a,a) ) 
#n3 = int( "%s%s%s" % (a,a,a) ) 
#print (n1+n2+n3)

#6.uzd
#Dota programma, kuras uzdevums ir izvadīt lietotāja ievadītā mēneša kalendāru #Testēšana: 2015 ---------> May 2015 
# 4 ---------> Mo Tu We Th Fr Sa Su 
# 1 2 3 
# 4 5 6 7 8 9 10 
# 11 12 13 14 15 16 17 
# 18 19 20 21 22 23 24 
# 25 26 27 28 29 30 31 

#import calendar 
#y = int(input("Ievadi gadu :")) 
#m = (input("Ievadi mēnesi : ")) 
#print(calendar.month(y, m)) 







#num = (input("Ievadi veselu skaitli: ")) 
#mod = num < 2 
#if mod > 0: 
   #print("Nepāra skaitlis.") 
#else: 
   #print("Pāra skaitlis.") 