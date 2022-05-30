from Structure.pipeline import Pipeline
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
from Outils.import_CSV import import_csv
from Transformation.transformation_group_by import Groupby
from Transformation.transformation_join import Join
from Transformation.transformation_select import Select
from Outils.import_export import import_export
from Structure.dataframe import Dataframe
from copy import deepcopy


Test_pip = Pipeline()

#les operations que contient le pipeline sont les suivantes:
#   (df, instanciation d'un objet du pakcage statistique 
# avec pour attribut la variable sur laquelle l'utilisateur veut travailler ) -> tuple de taille 2
#   (Bool,nom optionnel,transformation ) pour faire une transformation sur un dataframe il faut 
#   entrer un tuple avec en premiere valeur un booléen qui indique si l'on veut stocker
#   le dataframe que l'on réalise ou non, pui il faut indiquer éventuellement le nom 
#    (en cas de stockage) enfin le dernier élément est l'instanciation d'un objet du package Transformation
#   pour l'import la structure est la même que précédemment à laquelle on retire le Booléen
#    (on stocke par défaut le dataframe importé)

Test_pip.ajouter_operation(('data_1',import_csv('Data/synop.csv.gz-20220511/donnees_meteo','synop.201301.csv.gz')))
Test_pip.ajouter_operation((True,'new_data',Select('data_1',['numer_sta','dd',''])))
print(Test_pip.execution())
