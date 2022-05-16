import gzip
import csv
from my_import import Import

class import_csv(Import):
    def __init__(self,chemin, nom_fichier):
        super().__init__(chemin, nom_fichier)

    def dataOutput(self) :
        data=[]
        with gzip.open(self.chemin + '/' + self.nom_fichier, mode='rt') as gzfile :
            synopreader = csv.reader(gzfile, delimiter=';')
            for row in synopreader :
                data.append(row)
        return data

    def importing(self):
        data = self.dataOutput()  
        header = data[0]

        new_data ={}
        for index, value in enumerate(data[1:]):
            new_data[index]=value

        return (header, new_data)

header, data = import_csv('../synop.csv.gz-20220511/donnees_meteo','synop.201301.csv.gz').importing()

print(data)
print(header)
    

