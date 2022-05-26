from Structure.dataframe import Dataframe
from Statistiques.ecart_type import Ecart_type
import unittest

class Test_Ecart_type(unittest.TestCase):
    def setUp(self):
        self.chiens = Dataframe("chiens", [["Race", "str"], ["Poids", "float"]],
        {0:["Matin", 60], 1:["Jack Russel", 7], 2:["Corgi", 10.1], 3:["Levrier Afghan", 'mq']})

    def test_ecart_type_poids(self):
        self.assertEqual(round(Ecart_type(self.chiens.col('Poids'))._operation(),2), 24.29)

if __name__ == '__main__':
    unittest.main()