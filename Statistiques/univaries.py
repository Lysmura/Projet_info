from abc import ABC, abstractmethod
from Statistiques.statistiques import Statistiques

class Univaries(ABC, Statistiques) :
    """
    Définie la méthode abstraite des statistiques univariées

    Attributes :
    -----------
        col : list
            ensemble des valeurs prises par une variable

    Methods:
    --------
    operation(col) : float
        Retourne une statistique d'une variable dans une colonne
    """
    def __init__(self, col):
        self.col = col

    @abstractmethod
    def operation(self):
        pass
