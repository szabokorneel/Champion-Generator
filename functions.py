import time
from data import csapatok
from os import system
filename = 'csapatok.csv'   

def menu():
    system('cls')
    print('0 - Csapatnév megadása')
    print('1 - Csapatok Listázás')
    print('2 - Meccs lejátszása')
    print('3 - Kilépés')
    return input('Kérem válasszon: ')

   
def addYourTeam():
    choice = False
    while choice != True:
        system('cls')
        bekertNev = input(f'Adja meg a csapata nevét: ')
        if bekertNev.capitalize() in csapatok:
            system('cls')
            print(f'Ez a csapat már létezik') 
            time.sleep(1.5)
        else: 
            system('cls')
            print('Csapata rögzítésre került')
            csapatok.append(bekertNev.capitalize())
            time.sleep(1.5)
            choice = True



def teamsList():
    system('cls')
    print('A jelenlegi csapatok: ')
    for i in range(len(csapatok)):
        print('\t\t     ',csapatok[i])
    time.sleep(3.5)



def playMatch():
    pass

def kilepes():
    system('cls')
    print('Kilépés.')
    time.sleep(0.5)
    system('cls')
    print('Kilépés..')
    time.sleep(0.5)
    system('cls')
    print('Kilépés...')
    time.sleep(0.5)
    system('cls')