from Outils.export_carte import Export_carte
from Structure.dataframe import Dataframe
import unittest

class Test_ExportCarte(unittest.TestCase):

    def test_ExportCarte(self):
        data , header={0: ['Corse',44] ,1: ['Hauts-de-France',22]} , [['region',str],['temp',int]]
        frame = Dataframe('kdjej',header, data)
        Carte = Export_carte('ExportedFiles','regions.test.jpeg')

        Carte.exporting(frame,'temp')

if __name__ == '__main__':
    unittest.main()