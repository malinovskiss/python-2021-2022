#podesti

def materialaUzskaite(tips, izmers1, izmers2, skaits):
    #materialAprekins() nodos datus

    #tips - "FINIERIS", "LISTE", "LENKIS"




    pass





def materialuAprekins(platums, garums, augstums, skaits):
    #Mainīgie raksturo podestu

    #Finieris

    #Podestam augša un apakša
    materialaUzskaite("FINIERIS", platums, garums, 2*skaits)

    #Podesta priekšējā un aizmugurējā mala
    materialaUzskaite("FINIERIS", garums, augstums, 2*skaits)

    #Podesta sānu malas
    materialaUzskaite("FINIERIS", platums, augstums, 2*skaits)



#Līstes

# Augšējā finiera plāksne - 4 līstes
#Apakšējā finiera plāksne - 4 līstes
#Sānu malas - 4 līstes

    materialaUzskaite("LISTE", garums, 0, 4*skaits)

    materialaUzskaite("LISTE", platums, 0, 4*skaits)

    materialaUzskaite("LISTE", augstums, 0, 4*skaits)



#Leņķi

    materialaUzskaite("LENKIS", 0, 0, 8*skaits)