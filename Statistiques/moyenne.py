from Statistiques.univaries import Univaries

class Moyenne(Univaries):
    """
    Calcule la moyenne d'une colonne choisit

    Methods:
    operation(col) : float
        Retourne la valeur moyenne d'une variable numérique dans une colonne
    """
    def __init__ (self,col):
        super().__init__(col)

    def operation(self):
        try:
            if isinstance(self.col[0], int) is False and isinstance(self.col[0], float) is False :
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)
        moyenne = 0
        n = 0
        for i in self.col:
            if i != 'mq':
                moyenne = moyenne + i
                n = n + 1
        moyenne = moyenne/n
        return moyenne
