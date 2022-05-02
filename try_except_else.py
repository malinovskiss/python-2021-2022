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
    # #askint()


    #02.05.

    import sys

    saraksts = ['a',0,2]

for i in saraksts:
    try:
        print("Skaitlis ir:",i)
        a = 1/int(i)
        break
    except:
        print("Kļūda:",sys.exc_info()[0])
print(a)
