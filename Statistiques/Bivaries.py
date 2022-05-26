from Statistiques.statistiques import Statistiques
from abc import ABC, abstractmethod
class Bivaries(Statistiques,ABC):
    def __init__(self, col_x, col_y):
        self.col_x = col_x
        self.col_y = col_y
    
    @abstractmethod
    def _operation(col_x, col_y):
        pass