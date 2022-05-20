from abc import ABC ,abstractmethod
from Outils.import_export import Import_export

class export(Import_export, ABC):
    def __init__(self, chemin, nom_fichier):
        super().__init__(chemin, nom_fichier)
    
    @abstractmethod
    def exporting(self, dataframe):
        '''
        '''
        pass

