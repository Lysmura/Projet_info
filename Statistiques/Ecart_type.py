from math import sqrt
from Statistiques.Moyenne import Moyenne
from Statistiques.Univaries import Univaries

class Ecart_type(Univaries):
    """
    Calcule l'écart type d'une colonne choisit

    Methods:
    _operation(col) : float
        Retourne la valeur de l'écart type pour une colonne de variables 
        numériques.
    """
    def __init__(self,col):
        super().__init__(col)

    def _operation(self):
        try:
            if isinstance(self.col[0], int) == False and isinstance(self.col[0], float) == False :
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)

        moyenne = Moyenne(self.col)._operation()
        ecart_type = 0
        for i in self.col:
            if i != 'mq':
                ecart_type += (i - moyenne)**2
        ecart_type = sqrt(ecart_type/len(self.col))
        return ecart_type