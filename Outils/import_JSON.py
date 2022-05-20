import gzip
import json
from Outils.my_import import Import



class import_json(Import):
    def __init__(self, chemin, nom_fichier):
        super().__init__(chemin, nom_fichier)
    
    def dataOutput(self):
        with gzip.open(self.chemin + '/' + self.nom_fichier, mode='rt') as gzfile :
            data = json.load(gzfile)
        return data 

    def importing(self):
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
        
        header = [(h,str) for h in header]
        return (header,new_data)


        

