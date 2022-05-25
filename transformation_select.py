from transformation_transformation import Transformation
from Structure.dataframe import Dataframe

class Select(Transformation):
    def __init__(self,df,var):  
        super.__init__(df,var)

    def _operation(self):
        trans_df = copy(self.__df_1)
        col_a_sup =[]
        for var in self.__df_1.header:
            if var[0] not in self.__var:
                col_a_sup.append(var[0])
        for nom_var in col_a_sup:
            trans_df.del_col(nom_var)
        return trans_df