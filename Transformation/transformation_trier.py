from Transformation.transformation_transformation import Transformation
from Structure.dataframe import Dataframe
from Transformation.transformation_group_by import Groupby
from utilities.tri import tri

class trier(Transformation):
    def __init__(self,df,var):
        super().__init__(df,var)
    
    def _operation(self):
        col_trier = tri().tri_fusion(self.__df.col(self.__var[0]))
        compteur= 1
        dict_trier={}
        for element in col_trier:
            if element in dict_trier:
                dict_trier[element].append(compteur)
            else:
                dict_trier.update({element:[compteur]})
            compteur +=1
        trans_df = Groupby(self.df_1,self.var)._operation()
        for key,value in trans_df.data.items():
            id = self.df_1.num_col(self.var[0])
            for element in value:
                new_key = dict_trier[element[id]][-1]
                trans_df.update({new_key:element})
            del trans_df.data[key]
        return trans_df
