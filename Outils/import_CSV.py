import gzip
import csv
from Outils.my_import import Import

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

        header = [(h,str) for h in header]
        return (header, new_data)


    

