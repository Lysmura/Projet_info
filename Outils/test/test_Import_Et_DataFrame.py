from Outils.import_CSV import import_csv
from Structure.Dataframe import Dataframe


def From_CSV_to_Dataframe():
    header, data = import_csv('synop.csv.gz-20220511/donnees_meteo','synop.201301.csv.gz').importing()

    data_frame =Dataframe(nom="donnees_meteo", header = header, data = data)
    return data_frame

data_frame = From_CSV_to_Dataframe()

print(data_frame.header)

#print(data_frame.col('numer_sta'))
print(data_frame.ligne(3))

print(len(data_frame))

print(data_frame.get_item(3,'numer_sta'))
