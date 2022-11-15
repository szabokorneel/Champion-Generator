from functions import teams, menu, addYourTeam, saveTeam, teamsList, playMatch
from os import system

system('cls')
print (f'Üdvözöljük a Champion Generator-ben!')

print(f'A játék során 8 csapatból, verejtékes mérkőzések eredményeként csak 1 csapat maradhat: A BAJNOK CSAPAT.')

choice = ''
while choice != '4':
    choice = menu()
    if choice == '0':
        addYourTeam()
    elif choice == '1':
        saveTeam()
    elif choice == '2':
        teamsList()
    elif choice == '3':
        playMatch()
    