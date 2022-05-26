from matplotlib.pyplot import sci
import numpy as np
from scipy import stats 
import matplotlib as mp
import Structure.Dataframe as df
from abc import ABC, abstractmethod

class Statistiques(ABC) :
    def __init__(self, X, Y):
        self.X = X 
        self.Y = Y
        self.Results = stats.linregress(x=self.X, y=self.Y)


    def beta(self):
        return self.Results.slope 
    
    def beta0(self):
        return self.Results.intercept

    def Err(self):
        return self.Results.stderr


