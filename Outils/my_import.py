from abc import ABC ,abstractmethod
from Outils.import_export import import_export

class my_import(import_export,ABC):
    def __init__(self, chemin , nom_fichier):
        super().__init__(chemin, nom_fichier)
    
    @abstractmethod
    def importing(self):
        '''
        '''
        pass
