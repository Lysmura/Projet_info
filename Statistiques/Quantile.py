class Quantile(Univaries):
    """
    Calcule la moyenne d'une colonne choisit

    Methods:
    __operation(col) : float
        Retourne la valeur moyenne d'une variable numérique dans une colonne
    """
    def __operation(self, col):
        try:
            if (isinstance(col[0], int) == FALSE AND isinstance(col[0], float)) == FALSE:
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)
