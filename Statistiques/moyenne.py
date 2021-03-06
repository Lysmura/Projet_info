from Statistiques.univaries import Univaries

class Moyenne(Univaries):
    """
    Calcule la moyenne d'une colonne choisit
    
    Attributes:
    -----------
    col : list
        colonne du dataframe

    Methods:
    _operation() : float
        Retourne la valeur moyenne d'une variable numérique dans une colonne
    """
    def __init__ (self, col):
        super().__init__(col)

    def _operation(self):
        test = None
        i=0
        while test == None and i < len(self.col):
            if self.col[i] != 'mq':
                test=self.col[i]
            i+=1
        try:
            if isinstance(i, int) is False and isinstance(i, float) is False:
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)
        moyenne = 0
        n = 0
        for i in self.col:
            if i != 'mq':
                moyenne = moyenne + i
                n = n + 1
        if n == 0:
            return 'mq'
        else: 
            moyenne = moyenne/n
            return moyenne
