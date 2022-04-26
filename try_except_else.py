try:
    f = open('test file','w')
    f.write('Tests')
except IOError:
    print("Error: Fails netika atrasts vai nevar tikt nolasīts")
else:
    print("Viss sanāca!")
    f.close()
    

#f = open('testfile','r')
#f.write('Tests')

def askint():
    while True:
        try:
            val = int(input("Ievadi skaitli"))
        except:
            print("Izskatās,ka tas nav skaitlis")
            continue
        else:
            print("Jā, tas ir vesels skaitlis")
            break
        finally:
            print("Es te vienmēr būšu")
    print(val)

askint()

for i in ['a', 'b', 'c']:
    print(i**2)