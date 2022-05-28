from numpy import complex_
from Statistiques.bivaries import Bivaries
from scipy import stats 
import matplotlib.pyplot as plt

class Regression_lineaire(Bivaries):

    def __init__(self, col_x, col_y):
        """
        Retourne une regression linéaire entre deux colonnes

        Dans un premier temps l'operation retire les valeurs manquantes
        Attributes:
        -----------
        col_x : list
            colonne du dataframe
        col_y : list
            colonne du dataframe

        Returns:
        --------
        matplot
            droite de regression
        """
        super().__init__(col_x, col_y)
        self.Results = stats.linregress(x=self.col_x, y=self.col_y)
        self.beta0 = self.Results.intercept
        self.beta1 = self.Results.slope
        self.erreur = self.Results.stderr
        self.R2 = self.Results.rvalue**2

    def _operation(self):
        x = self.col_x
        y = self.col_y
        eleme_supp = []
        for indice in range(len(x)) :
            if x[indice] == "mq":
                eleme_supp.append[indice]
        del x[eleme_supp]
        del y[eleme_supp]
        eleme_supp = []
        for indice in range(len(y)) :
            if y[indice] == "mq":
                eleme_supp.append[indice]
        del x[eleme_supp]
        del y[eleme_supp]
        plt.plot(self.col_x, self.col_y, 'o', label='Data')
        droite_y = [ self.beta0 + self.beta1*x for x in self.col_x]
        plt.plot(self.col_x, droite_y, 'r', label='Droite de regression')
        plt.legend()
        plt.show()
