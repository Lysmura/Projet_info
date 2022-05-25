from abc import ABC, abstractmethod
from Statistiques.Statistiques import Statistiques

class Univaries(Statistiques) :
    def __init__(self, col):
        self.col = col
    
    @abstractmethod
    def _operation(self):
        pass