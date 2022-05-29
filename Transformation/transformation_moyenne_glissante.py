from Transformation.transformation_transformation import Transformation
from Statistiques.moyenne import Moyenne
from Structure.dataframe import Dataframe

class moyenne_glissante(Transformation):
    def __init__(self, df_1 : Dataframe, var):
        super().__init__(df_1,var)
    
    def _operation(self, pas : int):    
        L=[]
        col = self.df_1.col(self.var[0])
        for i in range(len(col)):
            try:
                col[i] = Moyenne._operation(col[i-pas:i+1])
                L += col[i]
            except IndexError:
                pass
        return L