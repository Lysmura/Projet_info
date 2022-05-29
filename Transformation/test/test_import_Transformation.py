from Outils.import_CSV import import_csv
from Structure.dataframe import Dataframe
from Transformation.transformation_select import Select
from Transformation.transformation_filter import Filter
from Transformation.transformation_group_by import Groupby

import unittest

class Test_Transfromation(unittest.TestCase):
    def setUp(self) -> None:
        header, data = import_csv('Data/synop.csv.gz-20220511/donnees_meteo','synop.201301.csv.gz').importing()
        print(header)
        self.data_1 = Dataframe('data',header,data)


    def  test_select(self):
        new_data = Select(self.data_1,['numer_sta','dd',''])._operation()
        print(new_data)

    def test_filter(self):
        new_data = Select(self.data_1,['numer_sta','dd',''])._operation()
        Tab_filter = Filter(new_data,['dd'],'>',230)._operation()
        print(Tab_filter)

    def test_groupBy(self):
        new_data = Select(self.data_1,['numer_sta','dd',''])._operation()
        Tab_filter = Filter(new_data,['dd'],'>',230)._operation()
        group = Groupby(Tab_filter,['numer_sta'])._operation()
        print(group)
        
if __name__ == '__main__':
    unittest.main()
