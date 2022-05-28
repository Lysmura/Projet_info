from Transformation.transformation_transformation import Transformation
from Structure.dataframe import Dataframe
from Transformation.transformation_group_by import Groupby

class trier(Transformation):
    def __init__(self,df,var):
        try:
            if isinstance(df,DataFrame) == False:
                raise TypeError("l'argument df doit être un dataframe")
        except TypeError as te:
            print(te)
        self.__df = df
        try:
            test = True
            id = None
            size = len(df.header)
            for i in range(size):
                if df.header[i][0] == var:
                    test = False
                    id = i
            if test :
                raise IndexError("la variable est mal orthographié ou n'appartient pas au dataframe indiqué")
        except IndexError as ie:
            print(ie)
        self.__var= [var,id]
    
    def transform(self):
        col_trier = tri_fusion(self.__df.col(self.__var[0]))
        compteur= 1
        dict_trier={}
        for element in col_trier:
            if element in dict_trier:
                dict_trier[element].append(compteur)
            else:
                dict_trier.update({element:[compteur]})
            compteur +=1
        trans_df = Groupby(self.__df,self.__var).transform()
        for key,value in trans_df.items():
            id = self.__var[1]
            for element in value:
                new_key = dict_trier[element[id]][-1]
                trans_df.update({new_key:element})
            del trans_df[key]
        return trans_df
