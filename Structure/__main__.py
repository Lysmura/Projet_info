from dataframe import Dataframe
chiens1 = Dataframe("chiens",
                                [["Race", "str"]],
                                {0:["Matin"],
                                1:["Jack Russel"],
                                2:["Corgi"],
                                3:["mq"]})

chiens2 = Dataframe("chiens",
                                [["Race", "str"], ["Poids", "float"]],
                                {0:["Matin", 60.0],
                                1:["Jack Russel", 7],
                                2:["Corgi", 10.1],
                                3:["mq", 20]})

chiens3 = Dataframe("chiens",
                                [["Race", "str"], ["Poids", "float"]],
                                {0:["Matin", 60],
                                1:["Jack Russel", 7],
                                2:["Corgi", 10.1],
                                3:["mq", 20],
                                4:["Levrier Afghan", 27]})
chiens1.add_col("Poids", [60.0, 7, 10.1, 20])
print(chiens1)                      
print(chiens2)
print(chiens1 == chiens2)
