class Import_export:
    def __init__(self, chemin , nom_fichier):
        self.chemin = Import_export.fix_chemin(chemin)
        self.nom_fichier = nom_fichier

    @staticmethod
    def fix_chemin(chemin): 
        nouveau_chemin=''
        for caractere in chemin:
            if caractere == "\\":
                nouveau_chemin += "/"
            else:
                nouveau_chemin += caractere
        return nouveau_chemin
    
