from unittest import TestCase
from Statistiques.moyenne import Moyenne
from Structure.dataframe import Dataframe

class Test_Moyenne(TestCase):
    def setUp(self):
        self.data = Dataframe("chiens", [["Race", "str"], ["Poids", "float"]], {0:["Matin", 60.4], 1:["Jack Russel", 7], 2:["Corgi", 10.4], 3:["Levrier Afghan", 'mq']})

    def test_average_var1(self):
        self.assertEqual(Average("Var1").apply(self.df)["Var1_Average"], [mean(self.df["Var1"])])