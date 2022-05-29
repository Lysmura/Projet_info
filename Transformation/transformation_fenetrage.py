from Transformation.transformation_group_by import Groupby
from Transformation.transformation_rowbind import Row_bind
from Transformation.transformation_transformation import Transformation
from Structure.dataframe import Dataframe
from copy import deepcopy
from Transformation.transformation_trier import Trier
from datetime import datetime

class Fenetrage(Transformation):
        def __init__(self,df,var,format_temps,int_temps):
            super().__init__(df,var)
            self.__int_temps = int_temps  
            self.__format_temps = format_temps
        
        def _operation(self):
            super()._operation()
            self.df_ = self.convert_date(self.df_1,self.var[0],self.__format_temps)
            table_1,liste_table = Groupby(self.df_1,self.var[0])._operation()
            for table in liste_table:
                table = Trier(table,self.var[1],False)._operation()
                #récupere l'heure et verifie si la différence correspond à l'intervalle de temps
                taille_table = len(table)
                indice_courant = 0
                indice_diff = 1
                while indice_diff < taille_table:
                    tour_boucle = 0
                    difference = table.data[indice_courant] - table.data[indice_diff]
                    while difference < self.__int_temps and indice_diff < taille_table:
                        difference = table.data[indice_courant] - table.data[indice_diff]
                        table.del_ligne(indice_diff)
                        indice_diff +=1
                        tour_boucle +=1
                    indice_courant = indice_diff
                    indice_diff +=1
            tableau_final = Dataframe('fenetrage',deepcopy(self.df_1.header),{})
            for table in liste_table:
                tableau_final = Row_bind(tableau_final,table)
            return tableau_final

        @staticmethod
        def convert_date(df,var,format_date):
            for value in df.data.values():
                value[df.num_col(var)] = datetime.strptime(value[df.num_col(var)],format_date)
                            
