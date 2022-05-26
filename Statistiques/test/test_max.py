from Structure.dataframe import Dataframe
from Statistiques.max import Max
import unittest

class Test_Moyenne(unittest.TestCase):
    def setUp(self):
        self.chiens = Dataframe("chiens", [["Race", "str"], ["Poids", "float"]],
        {0:["Matin", 60], 1:["Jack Russel", 7], 2:["Corgi", 10.1], 3:["Levrier Afghan", 'mq']})

    def test_moyenne_poids(self):
        self.assertEqual(Max(self.chiens.col('Poids'))._operation(), 60)

if __name__ == '__main__':
    unittest.main()