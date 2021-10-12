'''
metodes:
.split() - sadala teksta mainīgo sarakstā
.lower()
'''
'''
def kk()
    a=5

    if a ==5:
        return True
    else:
        return False

print(kk())
a= "Maza Lama"

print(a)

print(type())

a = a.split()
'''


def sakas_vienadi(teksts):
    teksts = teksts.lower().split()

    print(teksts)

    if teksts[0][0] == teksts[1][0]:
        return True
    else:
       return False
print(sakas_vienadi("liela Lama"))
print(sakas_vienadi("maza lama"))