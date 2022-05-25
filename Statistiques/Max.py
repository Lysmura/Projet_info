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
    def __init__ (self, col):
        super().__init__(col)

    def _operation(self):
        if isinstance(self.col[0], int) is False and isinstance(self.col[0], float) is False :
                raise ValueError("Le format de la variable n'est pas bon")
        if len(self.col) == 0:
            return None
        else :
            max = self.col[0]
            for i in self.col:
                if i > max and i != 'mq':
                    max = i
            return max 