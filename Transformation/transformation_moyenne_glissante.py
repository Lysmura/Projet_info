from Transformation.transformation_transformation import Transformation
from Statistiques.moyenne import Moyenne
from Structure.dataframe import Dataframe

class moyenne_glissante(Transformation):
    def __init__(self, df_1 : Dataframe, var):
        super().__init__(df_1,var)

    def _operation(self, pas : int):
        l_moyenne_glissante=[]
        col = self.df_1.col(self.var[0])
        for i in range(len(col)):
            if i+1-pas<0 :
                l_moyenne_glissante.append('mq')
            else :
                temp = [col[elem] for elem in range(i+1-pas , i+1)]
                temp = Moyenne(temp)._operation()
                l_moyenne_glissante.append(temp)
        return l_moyenne_glissante