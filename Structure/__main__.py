from Dataframe import *
from Statistiques.moyenne import *

header=[["Race", "str"]]
data={0:["Matin"], 1:["Jack Russel"], 2:["Corgi"]}
chiens = Dataframe("chien", header, data)

chiens.add_col("poids", [22.4, 4.1, 5.5])
chiens.add_ligne(["Levrier Afghan", 17])
#chiens.add_ligne([13, "Bulldog anglais"])
#chiens.del_col("poids")
#print(chiens.ligne(2))
#print(chiens.get_item(2,"poids"))
#print(chiens.header)
#chiens.del_ligne([2])
print(chiens)