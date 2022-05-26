from Structure.dataframe import Dataframe
from Statistiques.moyenne import Moyenne
#from Statistiques.Max import Max

data={1:[1, 1.5], 2:[3, 3.4]}
header=[["1", "int"],["2","float"]]
temp = Dataframe("temp", header, data)
print(Moyenne(temp.col("1"))._operation())