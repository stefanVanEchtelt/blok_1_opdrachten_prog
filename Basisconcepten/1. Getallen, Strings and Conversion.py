cijferICOR = 8
cijferPROG = 8
cijferCSN = 7

allDigits = [cijferICOR, cijferPROG, cijferCSN]

#1
gemiddelde = sum(allDigits) / len(allDigits)

#2
beloning = sum(allDigits) * 30

#3
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van € ' + str(beloning) + ' op!'
print(overzicht)