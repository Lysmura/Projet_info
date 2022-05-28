from Outils.import_CSV import import_csv
from Structure.dataframe import Dataframe
import unittest


def From_CSV_to_Dataframe():
    header, data = import_csv('Data/synop.csv.gz-20220511/donnees_meteo','synop.201301.csv.gz').importing()

    data_frame =Dataframe(nom="donnees_meteo", header = header, data = data)
    return data_frame

class Test_DataFrame(unittest.TestCase):

    def test_dataframe(self):
        data_frame = From_CSV_to_Dataframe()

        print(data_frame.header)

        #print(data_frame.col('numer_sta'))
        print(data_frame.ligne(3))

        print(len(data_frame))

        print(data_frame.get_item(3,'numer_sta'))

if __name__ == '__main__':
    unittest.main()