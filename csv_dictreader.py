import csv
from pprint import pprint

FILENAME = r'iris.csv'

with open(FILENAME) as file:
    config = csv.DictReader(
        file,
        fieldnames=['sepal_length','sepal_width','petal_length','petal_width','species'],
        delimiter=',',
        lineterminator='\n',
        quoting=csv.QUOTE_NONE)

    for line in config:
        sepal_length = line['sepal_length']
        sepal_width = line['sepal_width']
        petal_length = line['petal_length']
        petal_width = line['petal_width']
        species = line['species']
        pprint(f'{sepal_length} , {sepal_length} , {petal_length} , {petal_width} , {species}')