import Univaries

class Min(Univaries):
    """
    Calcule la valeur minimum d'une colonne choisit

    Methods:
    __calcul(col) : var
        Retourne la valeur minimum d'une variable numérique dans une colonne
    """
    def __calcul(self, col):
        try:
            if (isinstance(col[0], int) == FALSE AND isinstance(col[0], float)) == FALSE:
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)

        min = col[0]
        for i in col:
            if i < max :
                min = i
        return min 