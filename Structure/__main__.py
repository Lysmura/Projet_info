from Dataframe import *

header=[["Race", "str"]]
data={0:["Matin"], 1:["Jack Russel"], 2:["Corgi"]}
chiens = Dataframe("chien", header, data)

chiens.add_col("poids", [22.4, 4.1, 5.5])
chiens.add_ligne(["Levrier Afghan", 17])
# chiens.add_ligne([13, "Bulldog anglais"])
#chiens.del_col("poids")
print(chiens.data[2])
#print(chiens)
#print(chiens.header)