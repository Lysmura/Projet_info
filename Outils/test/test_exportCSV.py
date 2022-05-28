from unicodedata import name
from Outils.export_CSV import Export_CSV
from Structure.dataframe import Dataframe
import unittest

class Test_Export_CSV(unittest.TestCase):
    def test_import_CSV(self):
        data={0:[1, 1.5, "h"], 1:[3, 3.4,"l"], 2:[5, 6, "m"]}
        header=[["in", "int"],["fl","float"], ["st", "str"]]
        data_frame = Dataframe(nom="test", header=header,data=data)
        export_class = Export_CSV(chemin= "ExportedFiles", nom_fichier="test_export_csv.csv", dataframe=data_frame )
        export_class.exporting()

if __name__ == '__main__':

    unittest.main()