file = 'csapatok.csv'
csapatok = []

def betoltes():
    with open(file, 'r', encoding='utf-8') as forras:
        for row in forras:
            csapatok.append(row.strip())

def mentes():
    with open(file, 'w', encoding='utf-8') as cel:
        for i in range(len(csapatok)):
            cel.write(f'{csapatok[i]}\n')
    csapatok.clear()