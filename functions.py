import time
from data import csapatok
from os import system
filename = 'csapatok.csv'   

def menu():
    system('cls')
    print('0 - Csapatnév megadása')
    print('1 - Csapatok Listázás')
    print('2 - Meccs lejátszása')
    print('4 - Kilépés')
    return input('Kérem válasszon: ')


def teams():
    file = open(filename, 'r', encoding = 'utf-8' )
    global cimsor
    cimsor = file.readline() 
    for row in file:
        splitted = row.strip().split(';')
        csapatok[splitted[0]] = int(splitted[1])

def addYourTeam():
    pass


def saveTeam():
    pass


def teamsList():
    pass

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