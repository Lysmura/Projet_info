from Statistiques.univaries import Univaries

class Compter(Univaries):
    """
    Compte le nombre de fois qu'une variable quantitative est identique

    Si le format n'est pas str, la fonction retourne une erreure. L'utilisateur peut spécifier
    s'il souhaite la fréquence plutôt que l'effectif.

    Attributes:
    -----------
    freq : bool = True
        si True retourne la fréquence, par défaut False

    Methods:
    --------
    _operation(col) : float
        Retourne la valeur de l'écart type pour une colonne de variables 
        numériques.
    """
    def __init__(self, col, freq = False):
        super().__init__(col)
        self.freq = freq

    def _operation(self):
        try:
            if isinstance(self.col[0], str) is False :
                raise ValueError("Le format de la variable n'est pas bon")
        except ValueError as ve:
            print(ve)
        boulier = {}
        if self.freq is True:
            for i in self.col:
                boulier[i] = self.col.count(i) / len(self.col)
        else :
            for i in self.col:
                boulier[i] = self.col.count(i)
        return(boulier)
