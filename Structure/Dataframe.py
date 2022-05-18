
class Dataframe :
    """
    Définie le tableau de données

    Attributes:
    -----------
    nom : str
        intitulé du dataframe
    data : dict
        ensemble des données de la table
    header : list
        noms des variables du dataframe et leur format

    Methods:
    --------
    init(col : list, ligne : list, data : dict, header : list)
        constructeur de la classe
    __len__() : INT
        retourne la longueur du dataframe
    __str__() : str
        retourne une représentation graphique du dataframe
    ligne(numero) : list
        retourne un individu du dataframe
    col(nom : str) : list
        retourne une liste contenant une colonne du dataframe
    del_col(nom : str)
        supprime une colonne du dataframe
    add_col(nom : str, donnee : list)
        ajoute une colonne du dataframe, elle dit avoir un nom ainsi que des données
    del_ligne(numero : list)
        supprime une ou plusieurs lignes du dataframe
    add_ligne(individu : list)
        ajoute une ligne du dataframe
    get_item(numero : int, variable:str): {str, int, float}
        retourne une valeur du dataframe
    modif_item(numero : int, variable : str, nouvelle_valeur : {str, int, float}
        actualise une valeur du dataframe
    """
    def __init__(self, nom, header, data):
        """
        Créer un dataframe constitué d'un dictionnaire 
        contenant chaque ligne, et d'une liste des variables

        Parameters:
        -----------
        nom : str
            intitulé du dataframe
        data : dict
            ensemble des données de la table
        header : list
            noms des variables du dataframe et leur format
            de la forme header=[[nom_var_1,format_var_1],....,[nom_var_n, format_var_n]]
        """
        self.nom = nom
        self.header = header
        self.data = data


    def __len__(self):
        """
        Retourne le nombre de lignes du dataframe

        Returns:
        --------
        int
            nombre de lignes
        """
        return len(self.data)

    def __str__(self):
        str="{self.nom}: \n"
        variables=[]
        for i in len(self.header):
            variables.append(self.header[i][1])
        print(variables)
        for key, value in self.data.items():
            print(key, " ",value)
        return str

    def col(self, nom_col):
        """
        Retourne une colonne

        Parameters:
        -----------
        nom : str
            nom de la variable

        Returns:
        --------
        list
            colonne demandée
        """
        col = []
        id = None
        temp_id = 0
        for i in self.header :
            temp_id += 1
            if i[0] == nom_col:
                id=temp_id
        if id == None :
            print("Mauvais nom de colonne")
        else:
            for key,value in self.data.items():
                col.append[self.data[key][id]]
        return col

    def add_col(self,nom, colonne):
        """
        Ajoute une colonne au dataframe

        Parameters:
        -----------
        nom : str
            nom de la variable
        colonne : list
            colonne à ajouter au dataframe
        """
        if len(colonne) != len(self.data):
            print("Le nombre de données n'est pas bon.")
            raise IndexError
        else:
            if isinstance(colonne[0], float) == True :
                for i in colonne:
                    if isinstance(i, float) == False and i != 'mq' :
                        print("La valeur {i} n'est pas au bon format !")
                        raise TypeError
                        self.header.append([nom, "float"])
                for key,value in self.data.items():
                    temp = value
                    temp.append(colonne[key])
                    self.data[key] = temp
            if isinstance(colonne[0], int) == True :
                for i in colonne:
                    if isinstance(i, int) == False and i != 'mq':
                        print("La valeur {i} n'est pas au bon format !")
                        raise TypeError
                self.header.append([nom, "int"])
                for key,value in self.data.items():
                    temp = value
                    temp.append(colonne[key])
                    self.data[key] = temp
            if isinstance(colonne[0], str) == True :
                for i in colonne:
                    if isinstance(i, str) == False and i != 'mq' :
                        print("La valeur {i} n'est pas au bon format !")
                        raise TypeError
                self.header.append([nom, "str"])
                for key,value in self.data.items():
                    temp = value
                    temp.append(colonne[key])
                    self.data[key] = temp
            else :
                print("Le format des valeurs n'est pas pris en charge.")
                raise TypeError

    def del_col(self, nom):
        """
        Supprime une colonne du dataframe

        Parameters:
        -----------
        nom : str
            nom de la variable
        """
        id = None
        temp_id = 0
        for i in self.header :
            temp_id += 1
            if nom == self.header[i][0]:
                id = temp_id
        if id == None:
            print("La colonne n'existe pas.")
        else :
            for key, value in self.data:
                temp = value
                del temp[id]
                self.data[key] = temp
            del self.header[id]



    def ligne(self, numero):
        """
        Retourne une ligne du dataframe

        Parameters:
        -----------
        numero : int
            numero de la ligne

        Returns:
        --------
        list
            ligne demandée
        """
        if (numero >= len(self.data) or numero < 0) == True:
            print("Cette ligne n'existe pas.")
            raise IndexError
        else :
            return self.data["{numero}"]

    def add_ligne(self, ligne):
        """
        Ajoute une ligne au dataframe

        Parameters :
        -----------
        ligne : list
            données contenues dans la ligne
        """
        if len(ligne) != len(self.header):
            print("Le nombre de données n'est pas bon")
            raise IndexError
        else:
            for i in len(self.header) :
                if self.header[i][1] == "str":
                    if isinstance(ligne[i], str) == False and i != 'mq':
                        print("La valeur numéro {i} est au mauvais format.")
                        raise TypeError
                if self.header[i][1] == "int":
                    if isinstance(ligne[i], int) == False and i != 'mq':
                        print("La valeur numéro {i} est au mauvais format.")
                        raise TypeError
                if self.header[i][1] == "float":
                    if isinstance(ligne[i], float) == False and i != 'mq':
                        print("La valeur numéro {i} est au mauvais format.")
                        raise TypeError
            key = len(self.data)
            self.data[key] = ligne

    def del_ligne(self, numero):
        """
        Supprime une ligne du dataframe
        
        Après avoir retiré l'élement, la fonction réarrange les numéros pour combler le vide

        Parameters:
        -----------
        numero : list[int]
            numéro de.s la.es ligne.s à supprimer
        """
        test = True
        for i in numero :
            if (i > len(self.data) or i < 0) == True:
                test = False
                print("Il n'y a pas de ligne correspondantes au numéro {i}")
        if test == True :
            for key in numero:
                self.data.pop(key)
            nouvelle_taille = len(self.data)
            clefs =[]
            for i in range(nouvelle_taille):
                clefs.append(i)
            self.data=dict(zip(clefs, list(self.data.values())))
            

    #def get_item(self, numero, variable):
    #    retourne une valeur du dataframe
    #def modif_item(numero, variable, nouvelle_valeur): 
    #    actualise une valeur du dataframe