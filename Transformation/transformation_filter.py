from Transformation.transformation_transformation import Transformation
from Structure.dataframe import Dataframe
import copy

class Filter(Transformation):
    def __init__(self,df,var,critere,valeur):
        super().__init__(df,var)
        self.__critere = critere
        self.__valeur = valeur

    def _operation(self):
        super()._operation(self)
        try:
            if self.__critere not in ('==','<','>','>=','<='):
                raise ValueError("l'argument critere doit appartenir à la liste suivante: ==,<,>,>=,<=")
        except ValueError as ve:
            print(ve)
            return ve
        try:
            if len(self.var) >1:
                raise ValueError("var ne prend qu'une seule var en argument")
        except ValueError as ve:
            print(ve)
            return ve
        try:
            if isinstance(self.__valeur,self.df_1.header[self.df_1.num_col(self.var[0])][1]) == False:
                raise TypeError("la valeur du test n'est pas au même format que la variable")
        except TypeError as te:
            print(te)
            return te
        try:
            if isinstance(self.df_1.header[self.df_1.num_col(self.var[0])][1],str) and self.__critere != '==':
                raise ValueError("le teste demander ne peut être effectué car la variable est du type chaine de caractere")
        except ValueError as ve:
            print(ve)
            return ve

        if self.__critere == '==':
            new_header = copy.deepcopy(self.df_1.header)
            new_dict = copy.deepcopy(self.df_1.data)
            trans_df = Dataframe('filtrage',new_header,new_dict)
            for key,value in self.df_1.data.items():
                if value[trans_df.num_col(self.var[0])] != 'mq' and value[trans_df.num_col(self.var[0])] != '':
                    if value[trans_df.num_col(self.var[0])] != self.__valeur:
                        del trans_df.data[key]
                else:
                    del trans_df.data[key]
            return trans_df
        
        if self.__critere == '>':
            new_header = copy.deepcopy(self.df_1.header)
            new_dict = copy.deepcopy(self.df_1.data)
            trans_df = Dataframe('filtrage',new_header,new_dict)
            for key,value in self.df_1.data.items():
                if value[trans_df.num_col(self.var[0])] != 'mq' and value[trans_df.num_col(self.var[0])] != '':
                    if value[trans_df.num_col(self.var[0])] <= self.__valeur:
                        del trans_df.data[key]
                else:
                    del trans_df.data[key]
            return trans_df

        if self.__critere == '<':
            new_header = copy.deepcopy(self.df_1.header)
            new_dict = copy.deepcopy(self.df_1.data)
            trans_df = Dataframe('filtrage',new_header,new_dict)
            for key,value in self.df_1.data.items():
                if value[trans_df.num_col(self.var[0])] != 'mq' and value[trans_df.num_col(self.var[0])] != '':
                    if value[trans_df.num_col(self.var[0])] >= self.__valeur:
                        del trans_df.data[key]
                else:
                    del trans_df.data[key]
            return trans_df

        if self.__critere == '>=':
            new_header = copy.deepcopy(self.df_1.header)
            new_dict = copy.deepcopy(self.df_1.data)
            trans_df = Dataframe('filtrage',new_header,new_dict)
            for key,value in self.df_1.data.items():
                if value[trans_df.num_col(self.var[0])] != 'mq' and value[trans_df.num_col(self.var[0])] != '':
                    if value[trans_df.num_col(self.var[0])] < self.__valeur:
                        del trans_df.data[key]
                else:
                    del trans_df.data[key]
            return trans_df

        if self.__critere == '<=':
            new_header = copy.deepcopy(self.df_1.header)
            new_dict = copy.deepcopy(self.df_1.data)
            trans_df = Dataframe('filtrage',new_header,new_dict)
            for key,value in self.df_1.data.items():
                if value[trans_df.num_col(self.var[0])] != 'mq' and value[trans_df.num_col(self.var[0])] != '':
                    if value[trans_df.num_col(self.var[0])] > self.__valeur:
                        del trans_df.data[key]
                else:
                    del trans_df.data[key]
            return trans_df
