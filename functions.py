import time
import random
from data import csapatok
from os import system

boldStart = '\033[1;3m'
boldEnd = '\033[0m'

filename = 'csapatok.csv'   
jatszottak = 0
kevert = []
negyeddonto = []
elodonto = []
donto = []
nyertesek = []

def Instrukcio():
    if jatszottak > 0:
        print('A fordulók lejátszásához fordulónként üssön 2-est!\n')
    elif jatszottak > 3:
        print()

def menu():
    system('cls')
    Instrukcio()
    print('0 - Csapatnév megadása')
    print('1 - Csapatok Listázás')
    print('2 - Bajnokság lejátszása')
    print('3 - Saját csapat törlése')
    print('4 - Visszaállítás')
    print('5 - Kilépés')
    return input('Kérem válasszon: ')

def addYourTeam():
    choice = False
    if len(csapatok) < 8:
        while choice != True:
            system('cls')
            bekertNev = input(f'Adja meg saját csapata nevét: ')
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
        print('Maximum egy csapat adható hozzá!')
        time.sleep(3)

def teamsList():
    system('cls')
    print('A jelenlegi csapatok: ')
    for i in range(len(csapatok)):
        print('\t\t    ',csapatok[i])
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

def playTournament():
    global kevert
    global nyertesek
    global jatszottak
    if not jatszottak < 1:
        kevert.clear()
        for nyertes in nyertesek:
            kevert.append(nyertes)
    if jatszottak < 1:
        kevert.clear
        for i in range(len(csapatok)):
            kevert.append(csapatok[i])
        random.shuffle(kevert)
        jatszottak += 1
    for i in range(0,len(kevert)-1,2):
        system('cls')
        print(kevert[i])
        print(kevert[i+1])
        sorsolas = random.randint(0,1)
        if sorsolas == 0:
            print('A kiesett csapat: ',kevert[i])
            kevert[i] = '###'
        else:
            print('A kiesett csapat: ',kevert[i+1])
            kevert[i+1] = '###'
        time.sleep(3)
    nyertesek = []
    for i,kever in enumerate(kevert):
        if kever != "###":
            nyertesek.append(kever)
    if len(kevert) == 1:
        system('cls')
        print(f'{boldStart}A BAJNOK CSAPAT: {kevert[0]}!{boldEnd}')
        time.sleep(3)
    
     

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

def reset():
    system('cls')
    global jatszottak
    jatszottak = 0
    print('Sikeres visszaállítás')
    time.sleep(4)