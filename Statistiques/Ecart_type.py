from Moyenne import __calcul
from math import sqrt

class Ecart_type(Univaries):
    """
    Calcule l'écart type d'une colonne choisit

    Methods:
    __operation(col) : float
        Retourne la valeur de l'écart type pour une colonne de variables 
        numériques.
    """
    def __operation(self, col):
        try:
            if (isinstance(col[0], int) == FALSE AND isinstance(col[0], float)) == FALSE:
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)

        moyenne = 0
        for i in col:
            moyenne = moyenne + i
        moyenne = moyenne/len(col)

        ecart_type = 0
        for i in col:
            ecart_type = ecart_type - moyenne
        ecart_type = sqrt(ecart_type/len(col))
        return ecart_type