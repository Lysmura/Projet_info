from abc import ABC, abstractmethod
from Structure.dataframe import Dataframe


class Transformation(ABC):
    def __init__(self,df_1,var,df_2 = None):
        self.df_1 = df_1
        self.df_2 = df_2
        self.var =  var

    @abstractmethod
    def _operation(self):
        try:
            if not isinstance(self.df_1,Dataframe):
                raise TypeError("l'argument df_1  doit être des dataframes")
        except TypeError as te:
            return(te)

        try:
            if not isinstance(self.df_2,Dataframe) and self.df_2 != None:
                raise TypeError("l'argument df_2 doit être un dataframe ou ne doit pas être renseigné")
        except TypeError as te:
            return(te)

        try:
            if not isinstance(self.var,list):
                raise TypeError("l'argument var doit être une liste de chaine de carcatère pointant une ou plusieurs variable du dataframe")
        except TypeError as te:
            return(te)
        try:
            if any([not isinstance(nom_var,str) for nom_var in self.var]):
                raise ("les éléments de la liste de variable doivent être des chaînes de caractère")
        except TypeError as te:
            return(te)
        if self.df_2 == None:
            for nom_var in self.var:
                try:
                    if all([nom_var != nom_colone[0] for nom_colone in self.df_1.header]) :
                        raise IndexError("la variable {} est mal orthographié ou n'appartient pas au dataframe indiqué".format(nom_var))
                except IndexError as ie:
                    return(ie)
        if self.df_2 != None:
            for nom_var in self.var:
                try:
                    if all([nom_var != nom_colone[0] for nom_colone in self.df_1.header]) and all([nom_var != nom_colone[0] for nom_colone in self.df_2.header]) :
                        raise IndexError("la variable {} est mal orthographié ou n'appartient pas aux dataframes indiqués".format(nom_var))
                except IndexError as ie:
                    return(ie)
