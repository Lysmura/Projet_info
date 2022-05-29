from Transformation.transformation_moyenne_glissante import moyenne_glissante
from Outils.import_JSON import import_json
from Structure.dataframe import Dataframe
import unittest

class Test_moyenne_glissante(unittest.TestCase):
    def test_moyenne_glissante(self):
        header, data = import_json('Data/electricity_data','2013-01.json.gz').importing()
        data_frame =Dataframe(nom="donneeselectr", header = header, data = data)
        moy_gli = moyenne_glissante(data_frame,['consommation_brute_gaz_grtgaz'])._operation(3)
        print(moy_gli)


if __name__ == '__main__':
    unittest.main()