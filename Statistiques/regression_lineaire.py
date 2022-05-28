from Statistiques.bivaries import Bivaries
from scipy import stats 
import matplotlib.pyplot as plt

class Regression_lineaire(Bivaries):

    def __init__(self, col_x, col_y):
        super().__init__(col_x, col_y)
        self.Results = stats.linregress(x=self.col_x, y=self.col_y)
        self.beta0 = self.Results.intercept
        self.beta1 = self.Results.slope
        self.erreur = self.Results.stderr
        self.R2 = self.Results.rvalue**2

    def _operation(self):
        plt.plot(self.col_x, self.col_y, 'o', label='Data')
        droite_y = [ self.beta0 + self.beta1*x for x in self.col_x]
        plt.plot(self.col_x, droite_y, 'r', label='Droite de regression')
        plt.legend()
        plt.show()