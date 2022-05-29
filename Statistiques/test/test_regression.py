from Statistiques.regression_lineaire import Regression_lineaire
import unittest

class Test_Regression(unittest.TestCase):

    def test_regression_lineaire_norm(self):
        reg = Regression_lineaire([1,1,4,5,6,7,2], [5,7,8,5,3,4,8], name = "Normal")
        print (reg.beta1)
        print (reg.beta0)

        reg._operation()

    def test_regression_lineaire_val_manquantes(self):
        reg = Regression_lineaire(['mq',1,4,5,6,7,'mq'], [5,7,8,5,3,4,8],  name = "Valeurs manquantes")
        print (reg.beta1)
        print (reg.beta0)

        reg._operation()

if __name__ == '__main__':
    unittest.main()