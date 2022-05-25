class Dataframe :
    """
    Définie un tableau de données supportant les formats STR, INT et FLOAT.

    Attributes:
    -----------
    nom : str
        intitulé du dataframe
    data : dict
        ensemble des données de la table stocké dans un dictionnaire
        dont la clef est un entier allant de 0 à n (n étant la longueur
        de la table)
    header : list
        noms des variables du dataframe et leur format stocké dans une 
        liste de listes à deux entrées sous forme de string

    Methods:
    --------
    init(nom : str, header :list, data : dict)
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
    add_col(nom : str, colonne : list)
        ajoute une colonne au dataframe, elle doit avoir un nom ainsi que des données
    del_ligne(numero : list)
        supprime une ou plusieurs lignes du dataframe
    add_ligne(individu : list)
        ajoute une ligne du dataframe
    get_item(numero : int, variable:str): {str, int, float}
        retourne une valeur du dataframe
    modif_item(numero : int, variable : str, nouvelle_valeur : {str, int, float})
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
        affichage="{}: \n   ".format(self.nom)
        for i in self.header:
            affichage += i[0] + "   "
        affichage += "\n"
        for key, value in self.data.items():
            affichage += "{} ".format(key) + str(value) + "\n"
        return affichage

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
            if i[0] == nom_col:
                id = temp_id
            temp_id += 1
        if id is None :
            print("Mauvais nom de colonne")
        else:
            for value in self.data.values():
                col.append(value[id])
        return col

    def num_col(self,nom_var):
        for i in range(len(self.header)):
            if nom_var == self.header[i][0]:
                return i
                
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
            if isinstance(colonne[0], float) is True :
                for i in colonne:
                    if (isinstance(i, float) is False and isinstance(i, int) is False) and i != 'mq' :
                        print("La valeur {i} n'est pas au bon format !")
                        raise TypeError
                self.header.append([nom, "float"])
                for key,value in self.data.items():
                    temp = value
                    temp.append(colonne[key])
                    self.data[key] = temp
            elif isinstance(colonne[0], int) is True :
                for i in colonne:
                    if isinstance(i, int) is False and i != 'mq':
                        print("La valeur {i} n'est pas au bon format !")
                        raise TypeError
                self.header.append([nom, "int"])
                for key,value in self.data.items():
                    temp = value
                    temp.append(colonne[key])
                    self.data[key] = temp
            elif isinstance(colonne[0], str) is True :
                for i in colonne:
                    if isinstance(i, str) is False and i != 'mq' :
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
            if nom == i[0]:
                id = temp_id
            temp_id += 1
        if id is None:
            print("La colonne n'existe pas.")
        else :
            for key in self.data.keys():
                temp = self.data[key]
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
        if (numero >= len(self.data) or numero < 0) is True:
            print("Cette ligne n'existe pas.")
            raise IndexError
        else :
            return self.data[numero]

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
            id = 0
            for variable in self.header :
                if variable[1] == "str":
                    if isinstance(ligne[id], str) is False and variable != 'mq':
                        print("La valeur numéro {id} est au mauvais format.")
                        raise TypeError
                if variable[1] == "int":
                    if isinstance(ligne[id], int) is False and variable != 'mq':
                        print("La valeur numéro {id} est au mauvais format.")
                        raise TypeError
                if variable[1] == "float":
                    if (isinstance(ligne[id], float) is False and isinstance(ligne[id], int) is False) and variable != 'mq':
                        print("La valeur numéro {id} est au mauvais format.")
                        raise TypeError
                id += 1
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
            if (i > len(self.data) or i < 0) is True:
                test = False
                print("Il n'y a pas de lignes correspondantes au numéro {i}")
        if test is True :
            if len(numero) == 1:
                self.data.pop(numero[0])
                nouvelle_taille = len(self.data)
                clefs =[]
                for i in range(nouvelle_taille):
                    clefs.append(i)
                self.data=dict(zip(clefs, list(self.data.values())))
            else:
                for key in numero:
                    self.data.pop(key)
                nouvelle_taille = len(self.data)
                clefs =[]
                for i in range(nouvelle_taille):
                    clefs.append(i)
                self.data=dict(zip(clefs, list(self.data.values())))         

    def get_item(self, numero, variable):
        """
        Retourne un élément du dataframe

        Parameters:
        -----------
        numero : int
            numéro de la ligne où récupérer la valeur
        variable : str
            nom de la variable où récupérer la valeur

        Returns:
        --------
        {int, str, float}
            valeur de la case pour la variable et le numéro choisit
        """
        id = None
        temp_id = 0
        for i in self.header :
            if i[0] == variable:
                id = temp_id
            temp_id += 1
        if id is None :
            print("Mauvais nom de variable")
        else :
            return self.data[numero][id]

    def header_names(self):
        """
        
        """
        return [h[0] for h in self.header]

    #def modif_item(numero, variable, nouvelle_valeur):
    #    actualise une valeur du dataframe