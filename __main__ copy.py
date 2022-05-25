from Statistiques.moyenne import Moyenne
from Statistiques.max import Max
from Statistiques.min import Min
from Statistiques.ecart_type import Ecart_type

col = [-1, 'mq', 1, 2, 4.5, 7]
moy = Moyenne(col)
print(moy._operation())
max = Max(col)
print(max._operation())
min = Min(col)
print(min._operation())
ecart_type = Ecart_type(col)
print(ecart_type._operation())