from abc import ABC, abstractmethod
from Statistiques.statistiques import Statistiques

class Univaries(Statistiques) :
    """
    Classe initiant les objets univariés

    Attributes:
    -----------
    col : list
        une colonne de dataframe
    
    Methods:
    -------
    _operation(col) : dict
        calcule de la moyenne stockée dans un dictionnaire
    """
    @abstractmethod
    def __init__(self, col):
        self.col = col
    
    @abstractmethod
    def _operation(self):
        pass