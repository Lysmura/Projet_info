import csv
from Outils.my_export import my_export
from Structure.dataframe import Dataframe

class Export_CSV(my_export):
    def __init__(self, chemin : str, nom_fichier, dataframe : Dataframe ):
        super().__init__(chemin, nom_fichier)
        self.dataframe = dataframe
        
    def exporting(self):
        file_chemin = self.chemin+"/"+self.nom_fichier
        dataframe = self.dataframe
        with open(file_chemin, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(dataframe.header_names()) # ecriture du header
            for i in range(len(dataframe)): 
                writer.writerow(dataframe.ligne(i))

