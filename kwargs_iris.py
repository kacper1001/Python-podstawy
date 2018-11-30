FILENAME = r'C:\Users\Administrator\Desktop\kwargs_iris.csv'

try:
    with open(FILENAME, mode='r', encoding='utf-8') as file:
        zawartosc = file.readlines()

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')


def print_iris(sepal_length, sepal_width, *args, **kwargs):
    print(locals())


for record in zawartosc[1:]:
    *dane, gatunek = record
    wartosc = {'gatunek': gatunek}

    print_iris(*dane, **wartosc)
