odleglosc = 1337
km = int(odleglosc / 1E3)
mil = float(odleglosc / 1608)
milm = float(odleglosc / 1852)

print(f'Meters: {odleglosc}')  # int
print(f'Kilometers: {km}')  # int
print(f'Miles: {mil}')  # float
print(f'Nautical Miles: {milm}')  # float
print(f'All: {odleglosc}, {km}, {mil}, {milm}')  # int, int, float, float
