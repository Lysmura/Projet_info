from Structure.dataframe import Dataframe
from Statistiques.moyenne import Moyenne
from Statistiques.max import Max
from Statistiques.min import Min
from Statistiques.ecart_type import Ecart_type
from Statistiques.compter import Compter

class Pipeline(self,liste_operations):
    """
    Classe définissant un pipeline, son but est d'appliquer une série de fonctions

    Attributes
    ----------
    self.__liste_operations : list
        Liste d'opération et des arguments à appliquer sur le pipeline

    Methods
    -------
    __init__(__liste_operations)
        Createur du pipeline
    ajouter_operation(nom : str, arugments : list)
        Ajoute une nouvelle opération à appliquer au dataframe
    supprimer_operation(numero:int)
        Remove operations to the Pipeline after it's creation
    operations : list
        Retourne une liste des opérations disponibles
    execution(df) : DataFrame
        Execute le pipeline sur un dataframe d'origine
    """

    def __init__(self, __liste_operations):
        self.__liste_operations = []

    def add_operation(self,nom, arguments):
        """
        """
        if nom in ["Statistiques", "Compter"]:
            if isinstance(arguments, str) :
                print("L'argument doit être le nom d'une colonne")
                raise TypeError
            else:
                self.__liste_operations.append([nom,arguments])
        if nom == "Regression linéaire":
            if (isinstance(arguments, list) and len(arguments)==2 
                and isinstance(arguments[0], str) and isinstance(arguments[1], str)) :
                print("L'argument doit être une liste avec le nom de deux colonnes")
                raise TypeError
            else:
                self.__liste_operations.append([nom,arguments])
       # if : #à poursuivre


    #def supprimer_operation(self, numero):
        #h
        

    def execution(self, df : Dataframe):
        for operation in self.__liste_operations:
            nom = operation[0]
            arguments = operation[1]
            if nom == "Statistiques" :
                col = df.col(arguments)
                print({"Moyenne" : Moyenne(col)._operation(),
                        "Max" :  Max(col)._operation(),
                        "Min" : Min(col)._operation(),
                        "Ecart type" : Ecart_type(col)._operation()})
            if nom == "Compter":
                freq = False
                freq = input("Tapez True pour obtenir les fréquences, sinon faites entrée")
                col = df.col(arguments)
                print(Compter(col, freq)._operation())
            if nom == "Regression linéaire" :
                
                
from Transformation.transformation_transformation import Transformation
from Statistiques.univaries import Univaries
from Statistiques.Bivaries import Bivaries
from Outils.import_export import import_export
from Structure.dataframe import Dataframe
from copy import deepcopy

class Pipeline:
    def __init__(self):
        self.__liste_operations = []
        self.__op_possible = [Transformation,Univaries,Bivaries,import_export]
    
    def ajouter_operation(self,operation):
        validation_operation = [isinstance(operation,op_possible) for op_possible in self.__op_possible]
        if any(validation_operation):
            self.__liste_operations.append(operation)
        else:
            print('l\'operation n\'est pas reconnu et n\'a pas été ajouté pour execution')
    
    def supprimer_operation(self,numero : int):
        if numero >=0 and numero < len(self.__liste_operations):
            self.__liste_operations.pop(numero)

    def execution(self):
        trans_df = Dataframe('Resultat',[],{})
        dico_stat = {}
        for i in range(len(self.__liste_operations)):
            if isinstance(self.__liste_operations[i],Univaries):
                dico_stat.update({i : self.__liste_operations[i]._operation()})
