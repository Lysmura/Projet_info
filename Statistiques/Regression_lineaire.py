from Bivaries import Bivaries
from scipy import stats 
class Regression_lineaire(Bivaries):

    def __init__(self, col_x, col_y):
        super.__init__(col_x, col_y)
        self.Results = stats.linregress(x=self.col_x, y=self.col_y)

    def beta(self):
        return self.Results.slope 
    
    def beta0(self):
        return self.Results.intercept

    def Err(self):
        return self.Results.stderr