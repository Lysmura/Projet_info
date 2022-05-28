from Transformation.transformation_transformation import Transformation
from Structure.dataframe import Dataframe
from copy import deepcopy
from Transformation.transformation_formater import Formater

class Fenetrage(Transformation):
        def __init__(self,df,var,int_date,format_date, int_heure = None):
            try:
                if len(self.var)>2:
                    raise ValueError('La liste de variableest trop longue,elle doit contenir les variables de date')
            except ValueError as ve:
                print(ve)
            super().__init__(df,var)
            self.__int_date = int_date
            self.__format_date = format_date
            self.__format_heure = format_heure
            self.__int_heure = int_heure

        def jour(date,format_date):
            debut = 0
            for i in range(len(format_date)):
                if format_date[i] == 'J':
                    debut = i
                    fin = 0
                    while date[i:-1][fin] == 'J':
                        fin +=1
                    break
            fin += debut
            return date[debut:fin+1]

        def mois(date,format_date):
            debut = 0
            for i in range(len(format_date)):
                if format_date[i] == 'M':
                    debut = i
                    fin = 0
                    while date[i:-1][fin] == 'M':
                        fin +=1
                    break
            fin +=debut
            return date[debut:fin+1]

        @staticmethod
        def annee(date,format_date):
            debut = 0
            for i in range(len(format_date)):
                if format_date[i] == 'A':
                    debut = i
                    fin = 0
                    while date[i:-1][fin] == 'A':
                        fin +=1
                    break
            fin +=debut
            return date[debut:fin+1]
        
        def reste_date(date,format_date):
            debut = -1
            debut = 0
            for i in range(len(format_date),-1):
                if format_date[i] not in ['A','J','M']:
                    debut -=1
            if debut ==-1:
                return False,None
            if debut !=-1:
                return True,date[debut:-1]      

        def _operation(self):
            new_header = deepcopy(self.df_1.header)
            new_data = deepcopy(self.df_1.data)
            trans_df = Dataframe('fenetrage',new_header,new_data)
            for var in self.var:
                trans_df = Formater(trans_df,var,self.df_1.header[self.df_1.num_col(var)][1],str)._operation()
            indice_var = self.df_1.num_col(self.var[0])
            date_inf = self.__int_date[0]
            date_sup = self.__int_date[1]
            for key,value in self.df_1.data.items():
                date_temp = value[indice_var]
                if self.annee(date_temp,self.__format_date) < self.annee(date_inf,self.__format_date) or self.annee(date_temp,self.__format_date) > self.annee(date_sup,self.__format_date):
                    trans_df.del_ligne(key)
                    if self.annee(date_temp,self.__format_date) > self.annee(date_inf,self.__format_date) and self.annee(date_temp,self.__format_date) < self.annee(date_sup,self.__format_date):
                        if self.mois(date_temp,self.__format_date) < self.mois(date_inf,self.__format_date) or self.mois(date_temp,self.__format_date) > self.mois(date_sup,self.__format_date):
                            trans_df.del_ligne(key)
                        if self.mois(date_temp,self.__format_date)> self.mois(date_inf,self.__format_date) and self.mois(date_temp,self.__format_date) < self.mois(date_sup,self.__format_date):
                            if self.jour(date_temp,self.__format_date) < self.jour(date_inf,self.__format_date) or self.jour(date_temp,self.__format_date) > self.jour(date_sup,self.__format_date):
                                trans_df.del_ligne(key)
                            if self.jour(date_temp,self.__format_date) > self.jour(date_inf,self.__format_date) and self.jour(date_temp,self.__format_date) < self.jour(date_sup,self.__format_date):  
                                if len(self.var)==1:
                                    reste_date = self.reste_date(date_temp,self.__format_date)
                                    if reste_date[0]:
                                        if reste_date[1] < self.reste_date(date_inf,self.__format_date)[1] or reste_date > self.reste_date(date_sup,self.__format_date)[1]:
                                            trans_df.del_ligne(key)
                                else:
                                    try:
                                        if self.__int_heure == None:
                                            raise ValueError('Vous avez indiqué une variable pour l\'heure mais pas d\'intervalle')
                                    except ValueError as ve:
                                        print(ve)
                                    indice_heure = self.df_1.num_col(self.var[1])
                                    if value[indice_heure] > self.__int_heure[0] or value[indice_heure] < self.__int_heure[1]:
                                        trans_df.del_ligne(key)
                                    


                            
