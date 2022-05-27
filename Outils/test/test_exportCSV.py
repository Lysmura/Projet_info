from unicodedata import name
from Outils.export_CSV import Export_CSV
from Structure.dataframe import Dataframe

data={0:[1, 1.5, "h"], 1:[3, 3.4,"l"], 2:[5, 6, "m"]}
header=[["in", "int"],["fl","float"], ["st", "str"]]
data_frame = Dataframe(nom="test", header=header,data=data)
export_class = Export_CSV(chemin= "ExportedFiles", nom_fichier="test_export_csv.csv", dataframe=data_frame )

export_class.exporting()