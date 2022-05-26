from transformation_transformation import Transformation
from Structure.dataframe import Dataframe

class Groupby(Transformation):
    def __init__(self,df,var):
        super.__init__(df,var)

    def _operation(self):
        id_var = self.__df_1.num_col(self.__var[0])
        trans_df = Dataframe('group_by_' + self.__df.header[id_var][0],self.__df_1.header,{})
        for key,value in self.__df.items():
            cle_group_by = value[id_var]
            if  cle_group_by not in trans_df:
                trans_df.update({cle_group_by:[value]})
            else:
                trans_df[cle_group_by].append(value)
        compteur = 0
        for key in trans_df.keys():
            trans_df[compteur] = trans_df[key]
            compteur +=1
            del trans_df[key]
        return trans_df

