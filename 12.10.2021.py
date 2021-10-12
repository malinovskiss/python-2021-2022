'''
Uzraksti funkciju, kura atgriež mazāko skaitli, ja abi skaitļi ir pāra skaitļi
Atgriež lielāko skaiti, ja abi skaitļi ir nepāra vai viens no skaitļiem ir nepāra skaitlis

print(atgriez_skaitli(2,4))------ > 2
print(atgriez_skaitli(2,5))------ > 5
'''

'''
4%2=0
min()
max()

return
'''
#Pirmā pārbaude

print(min(1,4,6,8))
print(max(2,5,9,2))
def atgriez_skaitli(a,b): 

    if a%2 == 0 and b%2 == 0:

        return min (a,b)

    else:
        return max (a,b)

print(atgriez_skaitli(2,4))
print(atgriez_skaitli(5,6))