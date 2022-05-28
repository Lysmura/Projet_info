from Transformation.transformation_transformation import Transformation
from Structure.dataframe import Dataframe
from copy import deepcopy

class Formater(Transformation):
    def __init__(self,df,var,format_depart,format_final):
        super().__init__(df,var)
        self.__format_depart = format_depart
        self.__format_final = format_final

    def _operation(self):
        try:
            if isinstance(self.df_1.header[self.df_1.num_col(self.var)][1],self.__format_final):
                raise ValueError('La variable est déjà au format désiré')
        except ValueError as ve:
            print(ve)
        try:
            if isinstance(self.df_1.header[self.df_1.num_col(self.var)][1],self.__format_depart):
                raise ValueError('La variable format de depart indiqué est faux')
        except ValueError as ve:
            print(ve)
        new_header = deepcopy(self.df_1.header)
        new_data = deepcopy(self.df_1.data)
        trans_df = Dataframe('formatage',new_header,new_data)
        for value in trans_df.values():
            value[self.df_1.num_col(self.var)] =  self.__format_final(value[self.df_1.num_col(self.var)])
        if self.__format_final == str:
            for value in trans_df.values():
                if str(value[self.df_1.num_col(self.var)])[-2:] == '.0':
                    value[self.df_1.num_col(self.var)] =  str(value[self.df_1.num_col(self.var)]).replace('.0','')
                else:
                    value[self.df_1.num_col(self.var)] = str(value[self.df_1.num_col(self.var)])
        return trans_df
