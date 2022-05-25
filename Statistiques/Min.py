from Statistiques.univaries import Univaries

class Min(univaries):
    """
    Calcule la valeur minimum d'une colonne choisit

    Methods:
    _operation(col) : var
        Retourne la valeur minimum d'une variable numérique dans une colonne
    """
    def __init__ (self,col):
        super().__init__(col)

    def _operation(self, col):
        try:
            if isinstance(col[0], int) == False and isinstance(col[0], float) == False :
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)
        if len(col) == 0:
            return None
        else:
            min = col[0]
            for i in col:
                if i < min :
                    min = i
            return min 