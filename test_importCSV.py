from Outils.import_CSV import import_csv

header, data = import_csv('synop.csv.gz-20220511/donnees_meteo','synop.201301.csv.gz').importing()

print(data)
print(header)