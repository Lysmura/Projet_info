from Transformation.transformation_transformation import Transformation
from Structure.Dataframe import Dataframe


class Join(Transformation):
    def __init__(self,df_1,df_2,by,methode='inter'):
        super.__init__(df_1,by,df_2)
        self.methode = methode

    def _operation(self):
        size_1 =len(self.__df_1.header)
        size_2 = len(self.__df_2.header)
        if self.methode == 'inter':
            if size_1 > size_2:
                trans_df = Dataframe('fusion',self.__df_1.header,{})
                var_nocom =[]
                by_1 = self.__df_1.col(self.__var[0])
                by_2 = self.__df_2.col(self.__var[0])
                for i in range(size_2):
                    if self.__df_2.header[i] not in self.__df_1.header: #ici ligne tres sensible à la casse exemple de int et float
                        var_nocom.append(i)
                        trans_df.header.append(self.__df_2.header[i])
                for key in self.__df_1.data.keys():
                    cle_join = self.__df_1.data[key][self.__df_1.num_col(self.__var[0])]
                    if cle_join in by_1 and cle_join in by_2:
                        trans_df.update({cle_join:self.__df_1.data[key]})

                for key,value in self.__df_2.data.items():
                    cle_join = value[self.__df_2.num_col(self.__var)]
                    if cle_join in trans_df.data:
                        for k in var_nocom:
                            trans_df.data[cle_join].append(value[k])
                compteur = 0
                for key in trans_df.keys():
                    trans_df[compteur] = trans_df[key]
                    compteur +=1
                    del trans_df[key]
                return trans_df
            
            else:
                trans_df = Dataframe('fusion',self.__df_2.header,{})
                var_nocom =[]
                by_1 = self.__df_1.col(self.__var[0])
                by_2 = self.__df_2.col(self.__var[0])
                for i in range(size_1):
                    if self.__df_1.header[i] not in self.__df_2.header: #ici ligne tres sensible à la casse exemple de int et float
                        var_nocom.append(i)
                        trans_df.header.append(self.__df_1.header[i])
                for key in self.__df_2.data.keys():
                    cle_join = self.__df_2.data[key][self.__df_2.num_col(self.__var)]
                    if cle_join in by_1 and cle_join in by_2:
                        trans_df.update({cle_join:self.__df_2.data[key]})

                for key,value in self.__df_1.data.items():
                    cle_join = value[self.__df_1.num_col(self.__var)]
                    if cle_join in trans_df.data:
                        for k in var_nocom:
                            trans_df.data[cle_join].append(value[k])
                compteur = 0
                for key in trans_df.keys():
                    trans_df[compteur] = trans_df[key]
                    compteur +=1
                    del trans_df[key]
                return trans_df
        if self.methode == 'left join':
            if size_1 > size_2:
                trans_df = Dataframe('fusion',self.__df_1.header,{})
                var_nocom =[]
                for i in range(size_2):
                    if self.__df_2.header[i] not in self.__df_1.header: #ici ligne tres sensible à la casse exemple de int et float
                        var_nocom.append(i)
                        trans_df.header.append(self.__df_2.header[i])
                for key in self.__df_1.data.keys():
                    cle_join = self.__df_1.data[key][self.__df_1.num_col(self.var[0])]
                    trans_df.update({cle_join: self.__df_1.data[key]})

                for key,value in self.__df_2.data.items():
                    cle_join = value[self.__df_2.num_col[self.__var[0]]]
                    if cle_join in trans_df.data:
                        for k in var_nocom:
                            trans_df.data[cle_join].append(value[k])
                compteur = 0
                for key in trans_df.keys():
                    trans_df[compteur] = trans_df[key]
                    compteur +=1
                    del trans_df[key]
                return trans_df
            
            else:
                trans_df = Dataframe('fusion',self.__df_2.header,{})
                var_nocom =[]
                for i in range(size_1):
                    if self.__df_1.header[i] not in self.__df_2.header: #ici ligne tres sensible à la casse exemple de int et float
                        var_nocom.append(i)
                        trans_df.header.append(self.__df_1.header[i])
                for key in self.__df_2.data.keys():
                    cle_join = self.__df_2.data[key][self.__df_2.num_col(self.__var[0])]
                    trans_df.update({cle_join : self.__df_2.data[key]})

                for key,value in self.__df_1.data.items():
                    cle_join = value[self.__df_1.num_col(self.__var[0])]
                    if cle_join in trans_df.data:
                        for k in var_nocom:
                            trans_df.data[cle_join].append(value[k])
                compteur = 0
                for key in trans_df.keys():
                    trans_df[compteur] = trans_df[key]
                    compteur +=1
                    del trans_df[key]
                return trans_df
        if self.methode == 'right join':
            return Join(self.__df_2,self.__df_1,self.__var,'left join')._operation()