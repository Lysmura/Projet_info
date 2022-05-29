import gzip
import json
from Outils.my_import import my_import
from Structure.dataframe import Dataframe

class import_json(my_import):
    """
    Cette classe permet d'importer un fichier json

    Attributes:
    -----------
    chemin : str
        chemin du fichier
    nom_fichier : str
        Nom du fichier

    Methods:
    --------
    init(chemin : str, nom_chemin : str)
        constructeur de la classe
    importing():
        La methode permet d'importer un fichier json
    """
    def __init__(self, chemin, nom_fichier):
        super().__init__(chemin, nom_fichier)

    def importing(self):
        with gzip.open(self.chemin + '/' + self.nom_fichier, mode='rt',encoding="utf-8") as gzfile :
            data = json.load(gzfile)
        list_header = []
        for d in data:
            for k in d['fields'].keys():
                list_header.append(k)

        header = list(set(list_header)) #recuperer tous les noms de variables possibles

        new_data ={}
        for index, dic in enumerate(data):
            list_values=[]
            for h in header: 
                if dic['fields'].get(h):
                    list_values.append(dic['fields'].get(h))
                else: 
                    list_values.append("mq") #il faut combler le vide par les valeurs manquantes vu qu'ils ne sont pas visible dans le fichier json
            new_data[index] = list_values
        
        header = [[h,str] for h in header]
        dict_temp = Dataframe('temporaire',header,new_data)
        
        for j in range (len(header)):
            col = dict_temp.col(header[j][0])
            for i in range(len(col)):
                if col[i] !='mq':
                    header[j][1] = type(col[i])
                    break

        return header,new_data


        



        

