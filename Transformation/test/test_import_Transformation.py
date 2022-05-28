from Outils.import_CSV import import_csv
from Structure.dataframe import Dataframe
from Transformation.transformation_select import Select
import unittest

class Test_Transfromation(unittest.TestCase):
    def test_transformation(self):
        header, data = import_csv('Data/synop.csv.gz-20220511/donnees_meteo','synop.201301.csv.gz').importing()
        print(header)
        data_1 = Dataframe('data',header,data)
        
        #test du select
        from Transformation.transformation_select import Select
        new_data = Select(data_1,['numer_sta','dd',''])._operation()
        print(new_data)

        #test du filter
        from Transformation.transformation_filter import Filter
        Tab_filter = Filter(new_data,['dd'],'>',230)._operation()
        print(Tab_filter)

        #test_group_by
        from Transformation.transformation_group_by import Groupby
        group = Groupby(Tab_filter,['numer_sta'])._operation()
        print(group)
        
if __name__ == '__main__':
    unittest.main()
