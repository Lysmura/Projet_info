from pyparsing import col
from Outils.my_export import my_export
from Structure.dataframe import Dataframe
from Outils.cartoplot import CartoPlot


class Export_carte(my_export):

    def __init__(self, chemin, nom_fichier):
        super().__init__(chemin, nom_fichier)

    def exporting(self, dataframe : Dataframe, variable : str):
        if len(dataframe.header)>2:
            raise Exception("L'affichage ne se realise qu'avec un dataframe à 2 colonnes")
        if variable not in [dataframe.header[i][0] for i in range(len(dataframe.header))]:
            raise Exception("La donnee {} n'existe pas".format(variable))
        if 'region' not in [dataframe.header[i][0] for i in range(len(dataframe.header))]:
            raise Exception("La carte n'affiche les donnees que par region")

        cp = CartoPlot()
        data={}
        col_variable = dataframe.col(variable)
        region = dataframe.col('region')
        
        for i in range(dataframe.__len__()):
            data.update({region[i]:col_variable[i]})


        fig = cp.plot_reg_map(data = data,x_lim=(-6, 10), y_lim=(41, 52))
        fig.show()
        fig.savefig(self.chemin+"/"+self.nom_fichier)