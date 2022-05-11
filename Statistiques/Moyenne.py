from re import I


class Min(Univaries):
    """
    Calcule la moyenne d'une colonne choisit

    Methods:
    __calcul(col) : float
        Retourne la valeur moyenne d'une variable numérique dans une colonne
    """
    def __calcul(self, col):
        try:
            if (isinstance(col[0], int) == FALSE AND isinstance(col[0], float)) == FALSE:
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)
        moyenne = 0
        for i in col:
            moyenne = moyenne + i
        moyenne = moyenne/len(col)
        return moyenne