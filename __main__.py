from Structure.dataframe import Dataframe
from Statistiques.moyenne import Moyenne
from Statistiques.compter import Compter
#from Statistiques.Max import Max

chiens = Dataframe("chiens", [["Race", "str"], ["Poids", "float"]],
        {0:["Matin", 60], 1:["Jack Russel", 7], 2:["Corgi", 10.1], 3:["Jack Russel", 'mq'], 4:["mq", 'mq']})
print(Compter(chiens.col("Race"), True)._operation())