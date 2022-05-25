from Structure.Dataframe import Dataframe
from Statistiques.moyenne import Moyenne
#from Statistiques.Max import Max

data={1:[1, 1.5], 2:[3, 3.4]}
header=[["1", "int"],["2","float"]]
temp = Dataframe("temp", header, data)

Moyenne._operation(temp.col("1"))