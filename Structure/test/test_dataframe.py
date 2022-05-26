from Structure.dataframe import Dataframe
import unittest

class Test_Dataframe(unittest.TestCase):
    def setUp(self):
        self.chiens1 = Dataframe("chiens",
                                [["Race", "str"], ["Poids", "float"]],
                                {0:["Matin"],
                                1:["Jack Russel"],
                                2:["Corgi"],
                                3:["mq"]})

        self.chiens2 = Dataframe("chiens",
                                [["Race", "str"], ["Poids", "float"]],
                                {0:["Matin", 60.0],
                                1:["Jack Russel",7],
                                2:["Corgi", 10.1],
                                3:["mq", 20]})

        self.chiens3 = Dataframe("chiens",
                                [["Race", "str"], ["Poids", "float"]],
                                {0:["Matin", 60.0],
                                1:["Jack Russel",7],
                                2:["Corgi", 10.1],
                                3:["mq", 20],
                                4:["Levrier Afghan", 27]})

    def test_add_col(self):
        chiens = self.chiens1.add_col("Poids", [60.0, 7, 10.1, 20])
        self.assertEqual(chiens, self.chiens2)

    def test_add_ligne(self):
        chien = self.chiens2
        chien.add_ligne(["Levrier Afghan", 27])
        self.assertEqual(chien, self.chiens3)

    def test_mauvais_add_ligne(self):
        with self.assertRaises(TypeError):
            self.chiens3.add_ligne([13, "Bulldog anglais"])

    def test_del_col(self):
        chiens = self.chiens2
        chiens.del_col("Poids")
        self.assertEqual(chiens, self.chiens1)


#print(chiens.ligne(2))
#print(chiens.get_item(2,"poids"))
#print(chiens.header)
#chiens.del_ligne([2])

if __name__ == '__main__':
    unittest.main()
