from abc import ABCMeta

class univarie(ABC, Stattistiques) :
    def __init__(self):
        pass
    
    @abstractmethod
    def __operation(self,col):
        pass