file = 'csapatok.csv'
csapatok = []

def betoltes():
    with open(file, 'r', encoding='utf-8') as forras:
        for row in forras:
            csapatok.append(row.strip())