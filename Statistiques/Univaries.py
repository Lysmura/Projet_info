from abc import ABCMeta

class univarie(ABC, Statistiques) :
    def __init__(self):
        pass
    
    @abstractmethod
    def _operation(self,col):
        pass