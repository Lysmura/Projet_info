import Statistiques.univaries as univaries
import unittest

class Max(univaries):
    """
    Calcule la valeur maximum d'une colonne choisit

    Methods:
    --------
    _operation(col) : var
        Retourne la valeur maximum d'une variable numérique dans une colonne

    Exemples:
    ---------
    """
    def __init__ (self,col):
        super().__init__(col)

    def _operation(self, col):
        if isinstance(col[0], int) is False and isinstance(col[0], float) is False :
                raise ValueError("Le format de la variable n'est pas bon")
        if len(col) == 0:
            return None
        else :
            max = col[0]
            for i in col:
                if i > max :
                    max = i
            return max 