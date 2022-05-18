from Dataframe import Dataframe as df

header=[["Race", "str"]]
data={0:"Matin", 1:"Jack Russel", 2:"Corgi"}
donnees = Dataframe("chien", header, data)

donnees.df.col("poids", [12.4, 4.1, 5.5])