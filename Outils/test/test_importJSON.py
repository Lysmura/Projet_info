from Outils.import_JSON import import_json

header, data = import_json('Data/electricity_data','2013-01.json.gz').importing()

print(data)
print(header)    