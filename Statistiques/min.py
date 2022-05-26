from Statistiques.univaries import Univaries

class Min(Univaries):
    """
    Calcule la valeur minimum d'une colonne choisit

    Methods:
    --------
    _operation(col) : var
        Retourne la valeur minimum d'une variable numérique dans une colonne
    """
    def __init__(self, col):
        super().__init__(col)

    def _operation(self):
        try:
            if isinstance(self.col[0], int) is False and isinstance(self.col[0], float) is False :
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)
        if len(self.col) == 0:
            return None
        else:
            min = self.col[0]
            for i in self.col:
                if i != 'mq':
                    if i < min :
                        min = i
            return min
