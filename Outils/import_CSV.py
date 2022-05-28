import gzip
import csv
from Outils.my_import import my_import
from Structure.dataframe import Dataframe

class import_csv(my_import):
    def __init__(self,chemin, nom_fichier):
        super().__init__(chemin, nom_fichier)

    def importing(self):

        data=[]
        if self.nom_fichier[-1]=='z':
            with gzip.open(self.chemin + '/' + self.nom_fichier, mode='rt') as gzfile :
                synopreader = csv.reader(gzfile, delimiter=';')
                for row in synopreader :
                    data.append(row)
            header = data[0]
            new_data ={}
            for index, value in enumerate(data[1:]):
                new_data[index]=value 
            header = [[h,str] for h in header]
            dict_temp = Dataframe('temporaire',header,new_data)
            for i in range(len(header)):
                col = dict_temp.col(header[i][0])
                test_1 = True
                test_2= False
                test_3 = True
                if isinstance(col[0],str):    
                    for j in range(len(col)):
                        taille = len(col[0])
                        if len(col[j]) >=1 and col[j][0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
                            header[i][1] = str
                            test_1 =False
                            break
                        if len(col[j])>=2 and (col[j][0]=='0'and col[j][1] != '.') :
                            test_2 = True
                        if len(col[j]) != taille and j>=1:
                            test_3 =False
                            break
                    if test_2 and test_3:
                        header[i][1] = str
                    if not (test_2 and test_3):    
                        if test_1:
                            header[i][1] = float
                            for key, value in new_data.items():
                                if value[i] != 'mq':
                                    if len(value[i])!=0 :
                                        new_data[key][i] = float(value[i])
            
        if self.nom_fichier[-1] == 'v':
            with open( self.chemin + '/' + self.nom_fichier , encoding="utf-8") as csvfile :
                synopreader = csv.reader(csvfile, delimiter=';')
                for row in synopreader :
                    data.append(row)
            
            header = data[0]
            new_data ={}
            for index, value in enumerate(data[1:]):
                new_data[index]=value 
            header = [[h,str] for h in header]   

        return header, new_data
