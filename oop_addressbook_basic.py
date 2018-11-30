class Osoba:
    def __init__(self, imie, nazwisko, adresy=()):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy

    def __repr__(self):
        return f'{self.imie}{self.nazwisko}{self.adresy}'


class Adres:
    def __init__(self, ulica, miasto, stan, kod, panstwo):
        self.ulica = ulica
        self.miasto = miasto
        self.stan = stan
        self.kod = kod
        self.panstwo = panstwo

    def __repr__(self):
        return f'{self.miasto}'


class AddressBook:
    def __init__(self, osoba =()):
        self.osoba = osoba

    def __str__(self):
        return f'{self.osoba}'


osoby = AddressBook([
    Osoba(imie='José', nazwisko='Jiménez', adresy=[
        Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Adres(ulica=None, miasto='Kennedy Space Center', stan=None, kod='32899', panstwo='USA'),
    ]),
    Osoba(imie='Mark', nazwisko='Watney', adresy=[
        Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', stan=None, kod='91109', panstwo='USA'),
        Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    ]),
])

print(osoby)
