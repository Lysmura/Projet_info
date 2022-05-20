from abc import ABC, abstractmethod
import Statistiques

class univarie(ABC, Statistiques) :
    @abstractmethod
    def __init__(self, col):
        self.col = col
    
    @abstractmethod
    def _operation(self):
        pass