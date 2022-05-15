import gzip
import csv
from my_import import Import
class import_csv(Import):
    def __init__(self,chemin,nom_fichier):
        super().__init__(chemin, nom_fichier)
    
    def importing(self) :
        data=[]
        with gzip.open(self.chemin +'/' + self.nom_fichier, mode='rt') as gzfile :
            synopreader = csv.reader(gzfile, delimiter=';')
            for row in synopreader :
                data.append(row)
        return data

data_example = import_csv('../donnees_meteo/donnees_meteo','synop.201301.csv.gz').importing()
print(data_example)
    

