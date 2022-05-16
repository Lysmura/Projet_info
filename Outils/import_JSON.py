import gzip
import json
from my_import import Import



class import_json(Import):
    def __init__(self, chemin, nom_fichier):
        super().__init__(chemin, nom_fichier)
    
    def importing(self):
        with gzip.open(self.chemin + '/' + self.nom_fichier, mode='rt') as gzfile :
            data = json.load(gzfile)
        cles = [str(k) for k in range(0,len(data))]
        lignes = [[0]*len(data[0]['fields']) for k in range(0,len(data))]
        header = [k for k in data[0]['fields']]
        L=[]
        i=0
        for dictionnaire in data:
            for champ in dictionnaire:
                if champ == 'fields':
                    for k in dictionnaire[champ]:
                        L += [dictionnaire[champ][k]]
                    lignes[i] = L
                    L = []
                    i = i + 1
        
        new_data = dict()
        for key, value in zip(cles, lignes):
            new_data[key] = value
        
        return [header,new_data]
    @staticmethod
    def get_header(data):
        pass
        
        
        
        
        
data_exemple = import_json('D:/Projet_info/donnee/donnees_electricite','2013-01.json.gz').importing()
print(data_exemple['2'])

