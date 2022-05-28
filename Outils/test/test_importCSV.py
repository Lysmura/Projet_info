from Outils.import_CSV import import_csv
import unittest

class Test_ImportCSV(unittest.TestCase):
    def test_csv(self):
        #header, data = import_csv('Data/synop.csv.gz-20220511/donnees_meteo','synop.201301.csv.gz').importing()
        header, data = import_csv('Data/synop.csv.gz-20220511','postesSynopAvecRegions.csv').importing()
        print(data)
        print(header)


if __name__ == '__main__':
    unittest.main()