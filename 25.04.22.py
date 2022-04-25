#1
a = int(input("Ievadi a:"))
b = int(input("Ievadi b:"))

for i in range(a, b):
 print(i)

#2
sk = int(input("Ievadi skaitli:"))
while sk > 0:
 print(sk)
sk -= 1

#3
saraksts = [int(sk) for sk in input("Ievadi skaitlus, atdalot tos ar atstarpi:").split()]

for i in range(len(saraksts)):
 if saraksts[i] == saraksts[i + 1]:
   print(saraksts[i], saraksts[i + 1])

#4
skaitli = [int(skaitli) for skaitli in input("Ievadi skaitlus, atdalot tos ar atstarpi:").split()]

lielIndex = 0

for i in range(1, len(skaitli)):
 if skaitli[i] > skaitli[lielIndex]:
    lielIndex = i

print(f"Lielakais skaitlis: {skaitli[lielIndex]} ar indeksu {lielIndex}")

#Vajadzēja 6 rindiņā vienu atstarpi un 7 rindiņā 4 atstarpes, un 9 rindiņā ļipiņas(") un pēc tam iekavu beigas