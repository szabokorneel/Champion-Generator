from functions import teams, menu, addYourTeam, saveTeam, teamsList, playMatch, kilepes
from os import system
from data import betoltes

system('cls')
print (f'Üdvözöljük a Champion Generator-ben!')

print(f'A játék során 8 csapatból, verejtékes mérkőzések eredményeként csak 1 csapat maradhat: A BAJNOK CSAPAT.')

choice = ''
while choice != '4':
    betoltes()
    choice = menu()
    if choice == '0':
        addYourTeam()
    elif choice == '1':
        teamsList()
    elif choice == '2':
        playMatch()
    elif choice == '4':
        kilepes()
        