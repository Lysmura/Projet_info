from email import message_from_binary_file
from Outils.import_JSON import import_json
from Structure.pipeline import Pipeline
from Structure.dataframe import Dataframe
from Statistiques.moyenne import Moyenne
from Statistiques.max import Max
from Statistiques.min import Min
from Statistiques.ecart_type import Ecart_type
from Statistiques.compter import Compter
from Statistiques.univaries import Univaries
from Statistiques.bivaries import Bivaries
from Transformation.transformation_moyenne_glissante import moyenne_glissante
from Outils.my_import import my_import
from Outils.my_export import my_export
from Outils.import_CSV import import_csv
from Transformation.transformation_group_by import Groupby
from Transformation.transformation_join import Join
from Transformation.transformation_select import Select
from Outils.import_export import import_export
from Structure.dataframe import Dataframe
from Statistiques.regression_lineaire import Regression_lineaire
from copy import deepcopy
import random


Test_pip = Pipeline()

#les operations que contient le pipeline sont les suivantes:
#   (df, instanciation d'un objet du package statistiques
#   avec pour attribut la variable sur laquelle l'utilisateur veut travailler ) -> tuple de taille 2
#   (Bool,nom optionnel,transformation ) pour faire une transformation sur un dataframe il faut
#   entrer un tuple avec en premiere valeur un booléen qui indique si l'on veut stocker
#   le dataframe que l'on réalise ou non, pui il faut indiquer éventuellement le nom
#   (en cas de stockage) enfin le dernier élément est l'instanciation d'un objet du package Transformation
#   pour l'import la structure est la même que précédemment à laquelle on retire le Booléen
#   (on stocke par défaut le dataframe importé)

Test_pip.ajouter_operation(('data_1',import_csv('Data/synop.csv.gz-20220511/donnees_meteo','synop.201301.csv.gz')))
Test_pip.ajouter_operation((True,'new_data',Select('data_1',['numer_sta','dd',''])))
print(Test_pip.execution())

#Méthode sans pipeline pour moyenne glissante
header,data = import_json('Data/electricity_data','2013-01.json.gz').importing() #Importer des données
moy_gli = Dataframe('df', header, data) #créer un dataframe
print(moy_gli.header_names()) #trouver le nom des colonnes
print(moyenne_glissante(moy_gli, ['consommation_brute_electricite_rte'])._operation(10)) #Moyenne glissante avec un pas de 10
print(moy_gli.header)

#Méthode sans pipeline pour regression:
col_x = [5,4,15,1,2,4, 2]
col_y = [20,16,45,4,'mq',12,3]
reg = Regression_lineaire(col_x, col_y, 'fois_4') #Dans ce cas les colonnes sont corélées
reg._operation() #execution : un fichier jpg est ajouté dans ExportedFiles

#importation des donnees de janvier 2013
data_1_stockee=Test_pip.ajouter_operation(('data_1',import_csv('Data/synop.csv.gz-20220511/donnees_meteo','synop.201301.csv.gz')))[0]
data_2_stockee=Test_pip.ajouter_operation(('data_2',import_json('Data/electricity_data','2013-01.json.gz')))[0]

#importation des donnees de novembre 2021
header_meteo, data_meteo = import_csv('Data/synop.csv.gz-20220511/donnees_meteo','synop.202111.csv.gz').importing()
header_association_region_idstation, data_association_region_station = import_csv('Data/synop.csv.gz-20220511','postesSynopAvecRegions.csv').importing()
header_electricite, data_electricite=import_json('Data/electricity_data','2021-11.json.gz').importing()
#Creation du dataframe 
Data_meteo_20_01= Dataframe('donnee meteo 03-2021',header_meteo, data_meteo)
Data_elec_11_2021=Dataframe('donnee electricite 11-2021',header_electricite, data_electricite)
Association_region_idstation = Dataframe('asso',header_association_region_idstation, data_association_region_station)
#Reponse aux questions

#Q1: Y a-t-il une relation entre température et consommation électrique?
#On propose la realisation de cette relation dans chaque region
#Associons donc les station aux regionx grace aux dataframe Association_region_idstation
#Nous allons tout d'abord rennomer la variable 'numer_sta' par 'ID'
Data_meteo_20_01.header[0][0]= 'ID'
#Renommons aussi 'region'(table json) par 'Region'(table d'asso id et sta)
Data_elec_11_2021.header[0][0] = 'Region'
#Realisons la jointure par 'ID'
Data_sta_reg=Join(Data_meteo_20_01,Association_region_idstation,['ID'],methode='inter')#left ou right join?
#Realisons la jointure entre cette table et les donnees electricite par 'Region'
Data_temp_meteo_region=Join(Data_sta_reg,Data_elec_11_2021,['Region'],methode='inter')
data_desiree=Groupby(Data_temp_meteo_region,['Region'])
#prenons un exemple de region(Normandie):
#Ici je voulais selectionner les lignes dont la region c'est normandie mais jsp comment faire
#Apres on realise la regression
Regression_lineaire(data_meteo_elec_Normandie,'consommation_brute_electricite_rte','t')

