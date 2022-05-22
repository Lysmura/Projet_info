from ecart_type import Ecart_type
from moyenne import Moyenne
from dataframe import Dataframe
from transformation_transformation import Transformation

class Standardiser(Transformation):
    def __init__(self,df,operation,var = None):
        if var != None:
            super.__init__(df,var)
        else:
            super.__init__(df,[df.header[0][0]])
            self.__var = None
        try:
            if operation not in ('centrer','standardiser','normaliser'):
                raise ValueError("l'argument operation doit appartenir à la liste suivante: centrer,standarsiser,normaliser")
        except ValueError as ve:
            print(ve)

    def _opertion(self):
        if self.__var == None:
            var_num = []
            size = len(self.__df_1.header)
            for i in range(size):
                if self.__df_1.header[i][1] == int or self.__df_1.header[i][1] == float:
                    var_num.append([self.__df_1.header[i][0],i])

            if self.__operation == 'centrer':
                for i in var_num:
                    mean = Moyenne().__calcul(self.__df_1.col(i[0]))
                    trans_df = copy(self.__df_1)
                    for key in trans_df.data.keys():
                        trans_df.data[key][i[1]] -= mean
                return trans_df

            if self.__operation == 'normaliser':
                for i in var_num:
                    min = Min().__calcul(self.__df_1.col(i[0]))
                    max = Max().__calcul(self.__df_1.col(i[0]))
                    trans_df = copy(self.__df_1)
                    den = max - min
                    for key in trans_df.data.keys():
                        trans_df.data[key][i[1]] = (trans_df.data[key][i[1]] - min)/den
                return trans_df

            if self.__operation == 'standardiser':
                for i in var_num:
                    ecart_type = ecart_type().__calcul(self.__df_1.col(i[0]))
                    mean = Moyenne().__calcul(self.__df_1.col(i[0]))
                    trans_df = copy(self.__df_1)
                    for key in trans_df.data.keys():
                        trans_df.data[key][i[1]] = (trans_df.data[key][i[1]] - mean)/ecart_type
        
        if self.__var != None:    
            if self.__operation == 'centrer':
                mean = Moyenne().__calcul(self.__df_1.col(self.__var[0]))
                trans_df = copy(self.__df_1)
                for key in trans_df.data.keys():
                    trans_df.data[key][self.__var[1]] -= mean

            if self.__operation == 'normaliser':
                min = Min().__calcul(self.__df_1.col(self.__var[0]))
                max = Max().__calcul(self.__df_1.col(self.__var[0]))
                den = max - min
                trans_df = copy(self.__df_1)
                for key in trans_df.data.keys():
                    trans_df.data[key][self.__var[1]] = (trans_df.data[key][self.__var[1]] - min)/den
                return trans_df

            if self.__operation == 'standardiser':
                ecart_type = ecart_type().__calcul(self.__df_1.col(self.__var[0]))
                mean = Moyenne().__calcul(self.__df_1.col(self.__var[0]))
                trans_df = copy(self.__df_1)
                for key in trans_df.data.keys():
                    trans_df.data[key][self.__var[1]] = (trans_df.data[key][self.__var[1]] - mean)/ecart_type
                return trans_df