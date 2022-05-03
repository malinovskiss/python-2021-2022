stop = True
while stop == True:
    try:
        laiks = int(input("ievadi laiku(0-23): "))
        if laiks >= 0 and laiks <= 23:
            stop = True
        else:
            print("mēģini vēlreiz")
    elif laiks >= 5 and laiks <=11:
    print("labrīt!")
    elif laiks >= 12 and laiks <= 17:
    print("labdien!")
    elif laiks >= 18 and laiks <=20:
    print("labvakar!")
    elif laiks >= 21 and laiks <=23:
    print("Uzredzēšanos")
