age = eval(input('Geef je leeftijd: '))
hasPassport = input('Nederlands paspoort: ')

if (age >= 18) & (hasPassport == 'ja'):
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('U mag nog niet stemmen')