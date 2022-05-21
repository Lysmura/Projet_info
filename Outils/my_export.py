from abc import ABC ,abstractmethod
from Outils.import_export import import_export

class my_export(import_export, ABC):
    def __init__(self, chemin, nom_fichier):
        super().__init__(chemin, nom_fichier)
    
    @abstractmethod
    def exporting(self):
        '''
        '''
        pass


