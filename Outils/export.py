import csv
from my_export import export

class Export(export):
    def __init__(self, header, separator, chemin, nom_fichier  ):
        self.header = header
        self.separator = separator
        super().__init__(chemin, nom_fichier)
        
    def exporting(self, dataframe):
        with open(self.nom_fichier, 'w', newline='') as f:
            writer = csv.writer(f, delimiter = self.separator)
            writer.writerow(self.header)
            writer.writerows(dataframe)
        

