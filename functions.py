import time
from data import csapatok
from os import system
filename = 'csapatok.csv'   

def menu():
    system('cls')
    print('0 - Csapatnév megadása')
    print('1 - Csapatok Listázás')
    print('2 - Meccs lejátszása')
    print('3 - Saját csapat törlése')
    print('4 - Kilépés')
    return input('Kérem válasszon: ')

   
def addYourTeam():
    choice = False
    if len(csapatok) < 8:
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
    else:
        print('Maximum egy csapat adható hozzá')
        time.sleep(3)

def teamsList():
    system('cls')
    print('A jelenlegi csapatok: ')
    for i in range(len(csapatok)):
        print('\t\t     ',csapatok[i])
    time.sleep(3.5)


def deleteYourTeam():
    valasz = False
    while valasz != True:
        system('cls')
        valasz2 = input('Biztosan törölni szeretné csapatát? (i/n): ')
        if valasz2 == 'i':
            if len(csapatok) == 8:
                csapatok.pop(7)
                print('Csapata törlésre került')
                time.sleep(2)
                valasz = True
            else:
                print('Nem adott meg csapatot, így a törlés nem történhet meg!')  
                time.sleep(2)
        elif valasz2 == 'n':
            kilepes()
            valasz = True
        else:
            print('Helytelen válasz')
            time.sleep(2)
            


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