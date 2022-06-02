from Transformation.transformation_transformation import Transformation
from Structure.dataframe import Dataframe
from copy import deepcopy

class Groupby(Transformation):
    def __init__(self,df,var):
        super().__init__(df,var)

    def _operation(self):
        super()._operation()
        id_var = self.df_1.num_col(self.var[0])
        new_header =  deepcopy(self.df_1.header)
        trans_df = Dataframe('group_by_' + self.df_1.header[id_var][0],new_header,{})
        for key,value in self.df_1.data.items():
            cle_group_by = value[id_var]
            if  cle_group_by not in trans_df.data:
                trans_df.data.update({cle_group_by:[value]})
            else:
                trans_df.data[cle_group_by].append(value)
        compteur = 0
        data_temp = deepcopy(trans_df.data)
        for key in data_temp.keys():
            trans_df.data[compteur] = trans_df.data[key]
            compteur +=1
            del trans_df.data[key]
        table_group_by = []
        for key,value in self.df_1.data.items():
            compteur = 0
            data = {}
            for element in value:
                data.update({compteur:element})
                compteur +=1
            table_group_by.append(Dataframe('table des {}'.format(value[id_var]),deepcopy(self.df_1.header),data))
            value = value[0]
        return trans_df,table_group_by
