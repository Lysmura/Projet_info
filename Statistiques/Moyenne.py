import Statistiques.Univaries as Univaries

class Moyenne(Univaries):
    """
    Calcule la moyenne d'une colonne choisit

    Methods:
    _operation(col) : float
        Retourne la valeur moyenne d'une variable numérique dans une colonne
    """
    def __init__ (self,col):
       super().__init__(col)
    
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
        return moyenne