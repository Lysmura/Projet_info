from Statistiques.regression_lineaire import Regression_lineaire
import unittest

class Test_Regression(unittest.TestCase):

    def test_regression_lineaire(self):
        reg = Regression_lineaire(['mq',1,4,5,6,7,'mq'], [5,7,8,5,3,4,8])
        reg._operation()

if __name__ == '__main__':
    unittest.main()