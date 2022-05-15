import gzip
import csv
from my_import import Import

class import_csv(Import):
    def __init__(self,chemin, nom_fichier):
        super().__init__(chemin, nom_fichier)

    
    def importing(self) :
        data=[]
        with gzip.open(self.chemin + '/' + self.nom_fichier, mode='rt') as gzfile :
            synopreader = csv.reader(gzfile, delimiter=';')
            for row in synopreader :
                data.append(row)
        
        cles=[str(k) for k in range(0,len(data)-1)]
        lignes = data[1:]
        new_data = dict()
        
        for key, value in zip(cles, lignes):
            new_data[key] = value
        
        return new_data

Donnée_exemple = import_csv('D:\Projet_info\donnee\synop.csv.gz-20220511\donnees_meteo','synop.201301.csv.gz').importing()
print(Donnée_exemple)
    

