import time
from functions import menu, addYourTeam, teamsList, playMatch, kilepes
from os import system
from data import betoltes, mentes

system('cls')
print (f'Üdvözöljük a Champion Generator-ben!')

print(f'A játék során 8 csapatból, verejtékes mérkőzések eredményeként csak 1 csapat maradhat: A BAJNOK CSAPAT.')

choice = ''
while choice != '3':
    betoltes()
    choice = menu()
    if choice == '0':
        addYourTeam()
    elif choice == '1':
        teamsList()
    elif choice == '2':
        playMatch()
    elif choice == '3':
        kilepes()
    else:
        system('cls')
        print('Hibás válasz')
        choice = ''
        time.sleep(1.5)
    mentes()
