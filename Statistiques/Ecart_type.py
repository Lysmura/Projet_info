from Moyenne import _operation
from math import sqrt
import Statistiques.Univaries as Univaries

class Ecart_type(Univaries):
    """
    Calcule l'écart type d'une colonne choisit

    Methods:
    _operation(col) : float
        Retourne la valeur de l'écart type pour une colonne de variables 
        numériques.
    """
    def _operation(self, col):
        try:
            if isinstance(col[0], int) == False and isinstance(col[0], float) == False :
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)

        moyenne = 0
        for i in col:
            if i != 'mq':
                moyenne = moyenne + i
                n = n + 1
        moyenne = moyenne/n

        ecart_type = 0
        for i in col:
            if i != 'mq':
                ecart_type += i - moyenne
        ecart_type = sqrt(ecart_type/n)
        return ecart_type