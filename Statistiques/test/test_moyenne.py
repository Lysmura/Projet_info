import unittest
from Statistiques.moyenne import Moyenne
from Structure.dataframe import Dataframe

class Test_Moyenne(unittest.TestCase):
    def setUp(self):
        self.chiens = Dataframe("chiens", [["Race", "str"], ["Poids", "float"]], {0:["Matin", 60], 1:["Jack Russel", 7], 2:["Corgi", 10.1], 3:["Levrier Afghan", 'mq']})

    def test_moyenne_poids(self):
        self.assertEqual(Moyenne(self.chiens.col('Poids')).operation(), 25.7)

    def test_moyenne_race(self):
        with self.assertRaises(TypeError):
            Moyenne(self.chiens.col('Race')).operation()

if __name__ == '__main__':
    unittest.main()