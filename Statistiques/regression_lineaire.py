from numpy import complex_
from Statistiques.bivaries import Bivaries
from scipy import stats 
import matplotlib.pyplot as plt

class Regression_lineaire(Bivaries):

    def __init__(self, col_x, col_y, name ="Regression_Lineaire"):
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
        x = col_x
        y = col_y
        for i, elem in enumerate(y):
            if elem == "mq" :
                del x[i]
                del y[i]
        for i, elem in enumerate(x):
            if elem == "mq" :
                del x[i]
                del y[i]

        self.x_col = x
        self.y_col = y
        self.Results = stats.linregress(x=self.x_col, y=self.y_col)
        self.beta0 = self.Results.intercept
        self.beta1 = self.Results.slope
        self.erreur = self.Results.stderr
        self.R2 = self.Results.rvalue**2
        self.name = name

    def _operation(self):
        plt.plot(self.x_col, self.y_col, 'o', label='Data')
        droite_y = [ self.beta0 + self.beta1*x for x in self.x_col]
        plt.plot(self.x_col, droite_y, 'r', label=f'Droite de regression {self.name}')
        plt.legend()
        plt.savefig(f"ExportedFiles/{self.name}.png")
        #plt.show()
