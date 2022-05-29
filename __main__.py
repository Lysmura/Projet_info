from Structure.dataframe import Dataframe
from Transformation.transformation_moyenne_glissante import moyenne_glissante
l=[]
pas=3
t = Dataframe("chiens",
                                [["Race", "str"], ["Poids", "float"]],
                                {0:["Matin", 60],
                                1:["Jack Russel", 7],
                                2:["Corgi", 10.1],
                                3:["mq", 20]})
print(t)
print(moyenne_glissante(t,["Poids"])._operation(2))