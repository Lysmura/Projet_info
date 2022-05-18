import gzip
import json
from my_import import Import



class import_json(Import):
    def __init__(self, chemin, nom_fichier):
        super().__init__(chemin, nom_fichier)
    
    def dataOutput(self):
        with gzip.open(self.chemin + '/' + self.nom_fichier, mode='rt') as gzfile :
            data = json.load(gzfile)
        return data 

    def importing(self):
        #cles = [str(k) for k in range(0,len(data))]
        #lignes = [[0]*len(data[0]['fields']) for k in range(0,len(data))]
        #header = [k for k in data[0]['fields']]
        #L=[]
        #i=0
        # for d in data:
        #     for champ in dictionnaire:
        #         if champ == 'fields':
        #             for k in dictionnaire[champ]:
        #                 L += [dictionnaire[champ][k]]
        #             lignes[i] = L
        #             L = []
        #             i = i + 1
        # new_data = dict()
        # for key, value in zip(cles, lignes):
        #     new_data[key] = value

        data=self.dataOutput()
        list_header = []
        for d in data:
            for k in d['fields'].keys():
                list_header.append(k)
        header = list(set(list_header))
        new_data ={}
        for index, dic in enumerate(data):
            list_values=[]
            for h in header: 
                if dic['fields'].get(h):
                    list_values.append(dic['fields'].get(h))
                else: 
                    list_values.append("mq")
            new_data[index] = list_values

        return (header,new_data)


        
        
        
header, data = import_json('../electricity_data','2013-01.json.gz').importing()

print(data)
print(header)        
        
# data_exemple = import_json('D:/Projet_info/donnee/donnees_electricite','2013-01.json.gz').importing()
# print(data_exemple['2'])

