from Structure.dataframe import Dataframe
from Statistiques.compter import Compter
import unittest

class Test_Compter(unittest.TestCase):
    def setUp(self):
        self.chiens = Dataframe("chiens", [["Race", "str"], ["Poids", "float"]],
        {0:["Matin", 60], 1:["Jack Russel", 7], 2:["Corgi", 10.1], 3:["Jack Russel", 'mq'], 4:["mq", 'mq']})

    def test_frequence(self):
        self.assertEqual(Compter(self.chiens.col('Race'), True)._operation(), {'Matin': 0.2, 'Jack Russel': 0.4, 'Corgi': 0.2, 'mq': 0.2})
    
    def test_effectif(self):
        self.assertEqual(Compter(self.chiens.col('Race'))._operation(), {'Matin': 1, 'Jack Russel': 2, 'Corgi': 1, 'mq': 1})

if __name__ == '__main__':
    unittest.main()