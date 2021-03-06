from Structure.dataframe import Dataframe
from Statistiques.min import Min
import unittest

class Test_Min(unittest.TestCase):
    def setUp(self):
        self.chiens = Dataframe("chiens", [["Race", "str"], ["Poids", "float"]],
        {0:["Matin", 60], 1:["Jack Russel", 7], 2:["Corgi", 10.1], 3:["Levrier Afghan", 'mq']})

    def test_min_poids(self):
        self.assertEqual(Min(self.chiens.col('Poids'))._operation(), 7)

if __name__ == '__main__':
    unittest.main()