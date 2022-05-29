import gzip
import csv
from Outils.my_import import my_import
from Structure.dataframe import Dataframe

class import_csv(my_import):
    def __init__(self,chemin, nom_fichier):
        super().__init__(chemin, nom_fichier)

    def importing(self):
        data=[]
        if self.nom_fichier[-1]=='z': #si le fichier est csv.gz
            with gzip.open(self.chemin + '/' + self.nom_fichier, mode='rt') as gzfile :
                synopreader = csv.reader(gzfile, delimiter=';')
                for row in synopreader :
                    data.append(row)
            header = data[0] #le header est la première ligne de la liste 
            new_data ={}
            for index, value in enumerate(data[1:]):
                new_data[index]=value #remplissage du dictionnaire 
            header = [[h,str] for h in header]#pour le moment on laisse les format en str

        if self.nom_fichier[-1] == 'v':#si le fichier est csv
            with open( self.chemin + '/' + self.nom_fichier , encoding="utf-8") as csvfile :
                synopreader = csv.reader(csvfile, delimiter=';')
                for row in synopreader :
                    data.append(row)
            #on reprend la meme procedure d'au dessus
            header = data[0]
            new_data ={}
            for index, value in enumerate(data[1:]):
                new_data[index]=value 
            header = [[h,str] for h in header]  
        return header, new_data
