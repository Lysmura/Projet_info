from Transformation.transformation_transformation import Transformation
from Structure.dataframe import Dataframe
from copy import deepcopy

class Join(Transformation):
    def __init__(self,df_1,df_2,by,methode='inter'):
        super().__init__(df_1,by,df_2)
        self.methode = methode

    def _operation(self):
        super()._operation()
        size_1 =len(self.df_1.header)
        size_2 = len(self.df_2.header)
        if self.methode == 'inter':
            if size_1 >= size_2:
                trans_df = Dataframe('fusion',self.df_1.header,{})
                var_nocom =[]
                by_1 = self.df_1.col(self.var[0])
                by_2 = self.df_2.col(self.var[0])
                for i in range(size_2):
                    if self.df_2.header[i] not in self.df_1.header: #ici ligne tres sensible à la casse exemple de int et float
                        var_nocom.append(i)
                        trans_df.header.append(self.df_2.header[i])
                for value in self.df_1.data.values():
                    cle_join = value[self.df_1.num_col(self.var[0])]
                    if cle_join in by_1 and cle_join in by_2:
                        trans_df.data.update({cle_join:value})

                for key,value in self.df_2.data.items():
                    cle_join = value[self.df_2.num_col(self.var[0])]
                    if cle_join in trans_df.data:
                        for k in var_nocom:
                            trans_df.data[cle_join].append(value[k])
                compteur = 0
                data_temp = deepcopy(trans_df.data)
                for key in data_temp.keys():
                    trans_df.data[compteur] = trans_df.data[key]
                    compteur +=1
                    del trans_df.data[key]
                return trans_df
            
            else:
                trans_df = Dataframe('fusion',self.df_2.header,{})
                var_nocom =[]
                by_1 = self.df_1.col(self.var[0])
                by_2 = self.df_2.col(self.var[0])
                for i in range(size_1):
                    if self.df_1.header[i] not in self.df_2.header: #ici ligne tres sensible à la casse exemple de int et float
                        var_nocom.append(i)
                        trans_df.header.append(self.df_1.header[i])
                for key in self.df_2.data.keys():
                    cle_join = self.df_2.data[key][self.df_2.num_col(self.var[0])]
                    if cle_join in by_1 and cle_join in by_2:
                        trans_df.data.update({cle_join:self.df_2.data[key]})

                for key,value in self.df_1.data.items():
                    cle_join = value[self.df_1.num_col(self.var[0])]
                    if cle_join in trans_df.data:
                        for k in var_nocom:
                            trans_df.data[cle_join].append(value[k])
                compteur = 0
                data_temp = deepcopy(trans_df.data)
                for key in data_temp.keys():
                    trans_df.data[compteur] = trans_df.data[key]
                    compteur +=1
                    del trans_df.data[key]
                return trans_df
        if self.methode == 'left join':
            trans_df = Dataframe('fusion',self.df_1.header,{})
            var_nocom =[]
            for i in range(size_2):
                if self.df_2.header[i] not in self.df_1.header: #ici ligne tres sensible à la casse exemple de int et float
                    var_nocom.append(i)
                    trans_df.header.append(self.df_2.header[i])
            for value in self.df_1.data.values():
                cle_join = value[self.df_1.num_col(self.var[0])]
                trans_df.data.update({cle_join: value})

            for value in self.df_2.data.values():
                cle_join = value[self.df_2.num_col(self.var[0])]
                if cle_join in trans_df.data:
                    for k in var_nocom:
                        trans_df.data[cle_join].append(value[k])

            compteur = 0
            data_temp = deepcopy(trans_df.data)
            for key in data_temp.keys():
                trans_df.data[compteur] = trans_df.data[key]
                del trans_df.data[key]
                if len(trans_df.data[compteur]) == len(trans_df.header):
                    pass
                else:
                    while len(trans_df.data[compteur]) < len(trans_df.header):
                        trans_df.data[compteur].append('mq')
                compteur +=1
            return trans_df
        
        if self.methode == 'right join':
            return Join(self.df_2,self.df_1,self.var,'left join')._operation()
