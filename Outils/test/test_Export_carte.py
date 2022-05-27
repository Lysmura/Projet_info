from Outils.Export_carte import Export_carte
from Structure.dataframe import Dataframe

data , header={0: ['Corse',44] ,1: ['Hauts-de-France',22]} , [['region',str],['temp',int]]
frame = Dataframe('kdjej',header, data)
Carte = Export_carte('ExportedFiles','regions.test.jpeg')

Carte.exporting(frame,'temp')