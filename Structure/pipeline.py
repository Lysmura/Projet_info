from Structure.dataframe import Dataframe
from Statistiques.moyenne import Moyenne
from Statistiques.max import Max
from Statistiques.min import Min
from Statistiques.ecart_type import Ecart_type
from Statistiques.compter import Compter
from Statistiques.univaries import Univaries
from Statistiques.bivaries import Bivaries
from Outils.my_import import my_import
from Outils.my_export import my_export
from Transformation.transformation_group_by import Groupby
from Transformation.transformation_join import Join
from Transformation.transformation_transformation import Transformation
from Outils.import_export import import_export
from Structure.dataframe import Dataframe
from copy import deepcopy

class Pipeline:
    def __init__(self):
        self.__liste_operations = []
        self.__op_possible = [Transformation,Univaries,Bivaries,import_export]
    
    def ajouter_operation(self,operation):
        if any([any([isinstance(element,op_possible) for element in operation]) for op_possible in self.__op_possible]):
            self.__liste_operations.append(operation)
        else:
            print('l\'operation n\'est pas reconnu et n\'a pas été ajouté pour execution')
    
    def supprimer_operation(self,numero : int):
        if numero >=0 and numero < len(self.__liste_operations):
            self.__liste_operations.pop(numero)

    def execution(self):
        stockage_df = []
        dico_stat = {}
        for operation in self.__liste_operations:
            print(operation)
            if isinstance(operation,Univaries):
                try:
                    if len(stockage_df) == 0:
                        raise ValueError('vous n\'avez importer ou stocker aucun dataframe pour travailler dessus')
                except ValueError as ve:
                    print(ve)
                    return ve
                try:
                    if not isinstance(operation[0],Dataframe):
                        raise ValueError("pour une statistique descriptîve vous devez indiqué le dataframe en première position")
                except ValueError as ve:
                    print(ve)
                    return ve
                try:
                    if operation[0] not in stockage_df:
                        raise IndexError('le dataframe renseigné n\'existe pas')
                except IndexError as ie:
                    print(ie)
                    return ie
                try:
                    if all([operation[1].col != nom_colone[0] for nom_colone in operation[0].header]):
                        raise IndexError("la variable {} est mal orthographié ou n'appartient pas aux dataframes indiqués".format(nom_var))
                except IndexError as ie:
                    print(ie)
                    return ie
                if  (self.__liste_operations[i-1][0] and isinstance(self.__liste_operations[i-1][2],Groupby)):
                    for table in stockage_df[-1]:
                        operation[1].col = table.col(operation[1].col)
                        print('stat pour' +table.nom)
                        print(operation[1].__operation())
                        dico_stat.update({i:operation[1].__operation()})   
                else:
                    for element in stockage_df:
                        if  operation[0] == element.nom:
                            operation[0] = element    
                    operation[1].col = operation[0].col(operation[1].col)
                    print(operation[1].__operation())
                    dico_stat.update({i:operation[1].__operation()})

            if isinstance(operation,Bivaries):
                try:
                    if len(stockage_df) == 0:
                        raise ValueError('vous n\'avez importer ou stocker aucun dataframe pour travailler dessus')
                except ValueError as ve:
                    print(ve)
                    return ve
                try:
                    if not isinstance(operation[0],Dataframe):
                        raise ValueError("pour une statistique descriptîve vous devez indiqué le dataframe en première position")
                except ValueError as ve:
                    return ve
                try:
                    if all([operation[1].col_x != nom_colone[0] for nom_colone in operation[0].header]) or all([operation[1].col_y != nom_colone[0] for nom_colone in operation[0].header]):
                        raise IndexError("une des variables variable est mal orthographié ou n'appartient pas aux dataframes indiqués")
                except IndexError as ie:
                    return ie
                if (self.__liste_operations[i-1][0] and isinstance(self.__liste_operations[i-1][2],Groupby)):
                    for table in stockage_df[-1]:
                        operation[1].col_x = table.col(operation[1].col_x)
                        operation[1].col_y = table.col(operation[1].col_y)
                        print(operation[1].__operation())
                        dico_stat.update({i:operation[1].__operation()})
                else:
                    for element in stockage_df:
                        if  operation[0] == element.nom:
                            operation[0] = element
                    operation[1].col_x = operation[0].col(operation[1].col_x)
                    operation[1].col_y = operation[0].col(operation[1].col_y)
                    print(operation[1].__operation())
                    dico_stat.update({i:operation[1].__operation()})
            if any(isinstance(objet,Transformation) for objet in operation):
                try:
                    if len(stockage_df) == 0:
                        raise ValueError('vous n\'avez importer ou stocker aucun dataframe pour travailler dessus')
                except ValueError as ve:
                    print(ve)
                    return ve
                try:
                    if all([operation[2].df_1 != df_stock.nom for df_stock in stockage_df]):
                        raise IndexError('le dataframe renseigné n\'existe pas')
                except IndexError as ie:
                    print(ie)
                    return ie
                if isinstance(operation[2],Join):
                    try:
                        if all([operation[2].df_2 != df_stock.nom for df_stock in stockage_df]):
                            raise IndexError('le dataframe pour la jointure renseigné n\'existe pas')
                    except IndexError as ie:
                        print(ie)
                        return ie
                if operation[0]:
                    if isinstance(operation[2], Groupby):
                        for element in stockage_df:
                            if  operation[2].df_1 == element.nom:
                                operation[2].df_1 = element
                        df_1 ,df_2 = operation[2]._operation()
                        df_1.nom = operation[1]
                        stockage_df.append(df_1)
                        print(df_1)
                        stockage_df.append(df_2)
                    else:
                        for element in stockage_df:
                            if  operation[2].df_1 == element.nom:
                                operation[2].df_1 = element
                        if operation[2].df_2 != None:
                            for element in stockage_df:
                                if  operation[2].df_2 == element.nom:
                                    operation[2].df_2 = element
                        print(operation[2]._operation())
                        df_1 = operation[2]._operation()
                        df_1.nom = operation[1]
                        stockage_df.append(df_1)
                else:
                    for element in stockage_df:
                            if  operation[1].df_1 == element.nom:
                                operation[1].df_1 = element
                    if operation[1].df_2 != None:
                        for element in stockage_df:
                            if  operation[1].df_2 == element.nom:
                                operation[1].df_2 = element
                    
                    print(operation[1]._operation())
            if any(isinstance(objet,import_export) for objet in operation):
                if isinstance(operation[1],my_import):
                    header,data = operation[1].importing()
                    stockage_df.append(Dataframe(operation[0],header,data))
                    print(Dataframe(operation[0],header,data))
                if isinstance(operation[1],my_export):
                    try:
                        if len(stockage_df) == 0:
                            raise ValueError('vous n\'avez importer ou stocker aucun dataframe pour travailler dessus')
                    except ValueError as ve:
                        print(ve)
                        return ve
                    for element in stockage_df:
                        if  operation[1].dataframe == element.nom:
                            operation[1].dataframe = element
                                    
                    print(operation[1].exporting())
        self.__liste_operations = []
        return stockage_df,dico_stat
