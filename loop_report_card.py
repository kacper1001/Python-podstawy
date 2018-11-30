oceny = (2, 3, 3.5, 4, 4.5, 5)
lista_ocen = []
dzienniczek = []
lista_ocen = [float(x) for x in oceny]
print(lista_ocen)


while 1:
    niespr_ocena = input('wpisz ocene do dzienniczka:    ')

    if not niespr_ocena:
        break

    niespr_ocena = float(niespr_ocena)

    if niespr_ocena in oceny:
        dzienniczek.append(niespr_ocena)
    else:
        print('Grade is not allowed')
    print(dzienniczek)


srednia = sum(dzienniczek) / len(dzienniczek)

print(srednia)
