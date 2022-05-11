import Univaries

class Max(Univaries):
    """
    Calcule la valeur maximum d'une colonne choisit

    Methods:
    __calcul(col) : var
        Retourne la valeur maximum d'une variable numérique dans une colonne
    """
    def __calcul(self, col):
        try:
            if isinstance(col[0], int) == FALSE AND isinstance(col[0], float) == FALSE:
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)

        max = col[0]
        for i in col:
            if i > max :
                max = i
        return max 