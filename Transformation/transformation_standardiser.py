from Statistiques.ecart_type import Ecart_type
from Statistiques.moyenne import Moyenne
from Statistiques.min import Min
from Statistiques.max import Max
from Structure.dataframe import Dataframe
from Transformation.transformation_transformation import Transformation
from copy import deepcopy

class Standardiser(Transformation):
    def __init__(self,df,action,var = None):
        if var != None:
            super().__init__(df,var)
        else:
            super().__init__(df,[df.header[0][0]])
            self.var = None
        self.__action= action

    def _operation(self):
        super()._operation()
        try:
            if self.__action not in ('centrer','standardiser','normaliser'):
                raise ValueError("l'argument operation doit appartenir à la liste suivante: centrer,standarsiser,normaliser")
        except ValueError as ve:
            return ve
        if self.var == None:
            var_num = []
            size = len(self.df_1.header)
            for i in range(size):
                if self.df_1.header[i][1] == int or self.df_1.header[i][1] == float:
                    var_num.append([self.df_1.header[i][0],i])

            if self.__action == 'centrer':
                for i in var_num:
                    mean = Moyenne(self.df_1.col(i[0]))._operation()
                    trans_df = Dataframe('standardisation',deepcopy(self.df_1.header),deepcopy(self.df_1.data))
                    for key in trans_df.data.keys():
                        trans_df.data[key][i[1]] -= mean
                return trans_df

            if self.__action == 'normaliser':
                for i in var_num:
                    min = Min(self.df_1.col(i[0]))._operation()
                    max = Max(self.df_1.col(i[0]))._operation()
                    trans_df = Dataframe('standardisation',deepcopy(self.df_1.header),deepcopy(self.df_1.data))
                    den = max - min
                    for key in trans_df.data.keys():
                        trans_df.data[key][i[1]] = (trans_df.data[key][i[1]] - min)/den
                return trans_df

            if self.__action == 'standardiser':
                for i in var_num:
                    ecart_type = Ecart_type(self.df_1.col(i[0]))._operation()
                    mean = Moyenne(self.df_1.col(i[0]))._operation()
                    trans_df = Dataframe('standardisation',deepcopy(self.df_1.header),deepcopy(self.df_1.data))
                    for key in trans_df.data.keys():
                        trans_df.data[key][i[1]] = (trans_df.data[key][i[1]] - mean)/ecart_type
                return trans_df

        if self.var != None:    
            if self.__action == 'centrer':
                mean = Moyenne(self.df_1.col(self.var[0]))._operation()
                trans_df = Dataframe('standardisation',deepcopy(self.df_1.header),deepcopy(self.df_1.data))
                for key in trans_df.data.keys():
                    trans_df.data[key][self.df_1.num_col(self.var[0])] -= mean
                return trans_df

            if self.__action == 'normaliser':
                min = Min(self.df_1.col(self.var[0]))._operation()
                max = Max(self.df_1.col(self.var[0]))._operation()
                den = max - min
                trans_df = Dataframe('standardisation',deepcopy(self.df_1.header),deepcopy(self.df_1.data))
                for key in trans_df.data.keys():
                    trans_df.data[key][self.df_1.num_col(self.var[0])] = (trans_df.data[key][self.df_1.num_col(self.var[0])] - min)/den
                return trans_df

            if self.__action == 'standardiser':
                ecart_type = Ecart_type(self.df_1.col(self.var[0]))._operation()
                mean = Moyenne(self.df_1.col(self.var[0]))._operation()
                trans_df = Dataframe('standardisation',deepcopy(self.df_1.header),deepcopy(self.df_1.data))
                for key in trans_df.data.keys():
                    trans_df.data[key][self.df_1.num_col(self.var[0])] = (trans_df.data[key][self.df_1.num_col(self.var[0])] - mean)/ecart_type
                return trans_df
        
