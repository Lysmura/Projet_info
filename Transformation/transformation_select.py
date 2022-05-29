from Transformation.transformation_transformation import Transformation
from Structure.dataframe import Dataframe
import copy

class Select(Transformation):
    def __init__(self,df,var):  
        super().__init__(df,var)

    def _operation(self):
        super()._operation()
        new_header = copy.deepcopy(self.df_1.header)
        new_dict = copy.deepcopy(self.df_1.data)
        trans_df = Dataframe('selection',new_header,new_dict)
        col_a_sup =[]
        for var in self.df_1.header:
            if var[0] not in self.var:
                col_a_sup.append(var[0])
        for nom_var in col_a_sup:
            trans_df.del_col(nom_var)
        return trans_df
