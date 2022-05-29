from Transformation.transformation_transformation import Transformation
from Structure.dataframe import Dataframe
from Transformation.transformation_group_by import Groupby
from Transformation.transformation_rowbind import Row_bind
from copy import deepcopy
from utilities.tri import tri

class Trier(Transformation):
    def __init__(self,df,var,ASCENDANT=True):
        super().__init__(df,var)
        self.__ascendant = ASCENDANT
    
    def _operation(self):
        table_grouper,liste_tableau = Groupby(self.df_1,self.var)._operation()
        col_trier = tri().tri_fusion(table_grouper.col(self.var[0]))
        table_final = Dataframe('tri',deepcopy(table_grouper),{})
        if self.__ascendant:
            for element in col_trier:
                for table in liste_tableau:
                    if element == table.data[0][table.num_col(self.var)]:
                        table_final = Row_bind(table_final,table)
        else:
            for element in col_trier.reverse():
                for table in liste_tableau:
                    if element == table.data[0][table.num_col(self.var)]:
                        table_final = Row_bind(table_final,table)
        return table_final
