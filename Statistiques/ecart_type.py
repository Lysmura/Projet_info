from math import sqrt
from Statistiques.univaries import Univaries

class Ecart_type(Univaries):
    """
    Calcule l'écart type d'une colonne choisit

    Attributes:
    -----------
    col : list
        colonne du dataframe

    Methods:
    -------
    _operation() : float
        Retourne la valeur de l'écart type pour une colonne de variables 
        numériques.
    """
    def __init__(self, col):
        super().__init__(col)

    def _operation(self):
        try:
            if isinstance(self.col[0], int) is False and isinstance(self.col[0], float) is False :
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)

        moyenne = 0
        n=0
        for i in self.col:
            if i != 'mq':
                moyenne = moyenne + i
                n= n + 1
        moyenne = moyenne/n
        ecart_type = 0
        for i in self.col:
            if i != 'mq':
                ecart_type += (i - moyenne)**2
        ecart_type = sqrt(ecart_type/n)
        return ecart_type
