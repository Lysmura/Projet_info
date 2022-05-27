from Outils.import_CSV import import_csv
from Structure.dataframe import Dataframe
from Transformation.transformation_select import Select

header, data = import_csv('synop.csv.gz-20220511\donnees_meteo','synop.201301.csv.gz').importing()
print(header)
data_1 = Dataframe('data',header,data)
#test du select
new_data = Select(data_1,['dd',''])._operation()
print(new_data)

from Transformation.transformation_filter import Filter
#test du filter
Tab_filter = Filter(new_data,['dd'],'>',230)._operation()
print(Tab_filter)

from Transformation.transformation_standardiser import Standardiser
#test du standardiser
tab_centrer = Standardiser(Tab_filter,'standardiser',['dd'])._operation()
print(tab_centrer)