from matplotlib.pyplot import sci
import numpy as np
from scipy import stats 
import matplotlib as mp
import Structure.Dataframe as df
from abc import ABC, abstractmethod

class Statistiques(ABC) :
    @abstractmethod
    def __init__(self):
        pass


