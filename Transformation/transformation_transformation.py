from abc import ABC, abstractmethod
from Structure.dataframe import Dataframe


class Transformation(ABC):
    def __init__(self,df_1,var,df_2 = None):
        
        self.df_1 = df_1
        
        self.df_2 = df_2
        self.var =  var

    @abstractmethod
    def _operation(self):
        pass
