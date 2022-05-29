#association station et region
from Outils.import_CSV import import_csv
from Structure.dataframe import Dataframe
from Transformation.transformation_select import Select
from Transformation.transformation_filter import Filter
from Transformation.transformation_group_by import Groupby
from Transformation.transformation_formater import Formater
from Transformation.transformation_join import Join
import unittest

class Test_join(unittest.TestCase):
        header, data = import_csv('Data/synop.csv.gz-20220511/donnees_meteo','synop.201301.csv.gz').importing()
        Dataframe1 = Dataframe('meteo',header,data)
        header2, data2 = import_csv('Data/synop.csv.gz-20220511','postesSynopAvecRegions.csv').importing()
        Dataframe2 = Dataframe('Region-ID',header2, data2)
        trans_df = Join(Dataframe2, Dataframe1,['ID'],'left join')
        print(trans_df)


