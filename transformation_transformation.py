from abc import ABC, abstractmethod
from numpy import var

from pandas import DataFrame

class Transformation(ABC):
    def __init__(self,df_1,var,df_2 = None):
        try:
            if isinstance(df_1,DataFrame) == False:
                raise TypeError("l'argument df_1  doit être des dataframes")
        except TypeError as te:
            print(te)
        self.__df_1 = df_1
        try:
            if isinstance(df_2,DataFrame) == False and df_2 != None:
                raise TypeError("l'argument df_2 doit être un dataframe ou ne doit pas être renseigné")
        except TypeError as te:
            print(te)
        self.__df_2 = df_2
        try:
            if isinstance(var,list) == False:
                raise TypeError("l'argument var doit être une liste de chaine de carcatère pointant une ou plusieurs variable du dataframe")
        except TypeError as te:
            print(te)
        try:
            if any([not isinstance(nom_var,str) for nom_var in var]):
                raise ("les éléments de la liste de variable doivent être des chaînes de caractère")
        except TypeError as te:
            print(te)
        self.__var = []
        if df_2 == None:
            for nom_var in var:
                try:
                    if all([nom_var != nom_colone[0] for nom_colone in df_1.header]) :
                        raise IndexError("la variable {} est mal orthographié ou n'appartient pas au dataframe indiqué".format(nom_var))
                except IndexError as ie:
                    print(ie)
            self.__var =  var
        if df_2 != None:
            for nom_var in var:
                try:
                    if all([nom_var != nom_colone[0] for nom_colone in df_1.header]) and all([nom_var != nom_colone[0] for nom_colone in df_2.header]) :
                        raise IndexError("la variable {} est mal orthographié ou n'appartient pas aux dataframes indiqués".format(nom_var))
                except IndexError as ie:
                    print(ie)
            self.__var =  var
    @abstractmethod
    def _operation(self):
        pass