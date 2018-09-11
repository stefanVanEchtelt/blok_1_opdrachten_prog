a = 6
b = 7
c = a * b / 2
voornaam = 'Stefan'
tussenvoegsel = 'van'
achternaam = 'Echtelt'
mijnnaam = voornaam + ' ' + tussenvoegsel + ' ' + achternaam

#1
print(75 > a & 75 < b)

#2
print(len(mijnnaam) == sum([len(voornaam), len(tussenvoegsel), len(achternaam)]))

#3
print(len(mijnnaam) > 5 * len(tussenvoegsel))

#4
print(tussenvoegsel in achternaam)