from Outils.import_JSON import import_json
import unittest

class Test_ImportJSON(unittest.TestCase):
    def test_importJSON(self):
        header, data = import_json('Data/electricity_data','2013-01.json.gz').importing()

        print(data[0])
        print(header)    

if __name__ == '__main__':
    unittest.main()