import csv
from my_export import export
import Dataframe

class Export(export):
    def __init__(self, separator : str , chemin : str, nom_fichier  ):
        self.separator = separator
        super().__init__(chemin, nom_fichier)
        
    def exporting(self, dataframe : Dataframe):
        with open(self.nom_fichier, mode = 'w', newline='') as csv_file:
            csv_file.write(self.separator.join([dataframe.header]))
            for i in range (0, dataframe.__len__()):
                Ligne = self.separator.join(dataframe.ligne(i)) + "\n"
                csv_file.write(Ligne)
        

