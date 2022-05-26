from Statistiques.statistiques import Statistiques

class Univaries(Statistiques) :
    """
    Définie la méthode abstraite des statistiques univariées

    Attributes :
    -----------
        col : list
            ensemble des valeurs prises par une variable

    Methods:
    --------
    _operation(col) : float
        Retourne une statistique d'une variable dans une colonne
    """
    def __init__(self, col):
        self.col = col

    def _operation(self):
        pass
