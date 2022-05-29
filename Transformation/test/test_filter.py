from Outils.import_CSV import import_csv
from Structure.dataframe import Dataframe
from Transformation.transformation_select import Select
from Transformation.transformation_filter import Filter
from Transformation.transformation_group_by import Groupby
from Transformation.transformation_formater import Formater

import unittest

class Test_Transfromation(unittest.TestCase):
    def setUp(self) -> None:
        header, data = import_csv('Data/synop.csv.gz-20220511/donnees_meteo','synop.201301.csv.gz').importing()
        print(header)
        self.data_1 = Dataframe('data',header,data)

    def test_formater(self):
        Tab_formater = Formater(self.data_1,['dd'],str,int)._operation()
        Tab_filter = Filter(Tab_formater,['dd'],'>',230)._operation()
        print(Tab_filter)

if __name__ == '__main__':
    unittest.main()