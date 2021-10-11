# 1.specifikācija

'''
Uzrakstīt funkciju:
*ievadīt linoleja cenu
*ievadīt telpas izmēru
*izvadīt cenu
'''

def lin_cena(cenu, izmers):
    kopa = cenu * izmers

    return kopa

print(lin_cena(5, 20))

# 2.specifikācija

'''
Uzrakstīt funkciju grīdas_izmaksas(cena, telpas_garums, telpas_platumu)

*Cena EUR/m2
*Telpas platums un garums
*aprēķināt izmaksas, noapaļojot telpas garumu un platumu uz augšu
*izvadīt izmaksas
'''

def gridas_izmaksas(cena,telpas_garums,telpas_platumu):

    return telpas_garums * telpas_platumu * cena



    gridas_izmaksas(6,2,5,5)
