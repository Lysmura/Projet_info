import gzip
import json
from my_import import Import
class import_json(Import):
    def __init__(self,chemin,nom_fichier):
        super().__init__(chemin, nom_fichier)
    def importing(self):
        with gzip.open(self.chemin + "/" +self.nom_fichier, mode='rt') as gzfile :
            data = json.load(gzfile)
        return data


#Test
# class_import = import_json(chemin='../electricity_data',nom_fichier='/2022-12.json.gz')
# data_json = class_import.importing()
# print(data_json)

