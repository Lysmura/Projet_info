class import_export:
    def __init__(self, chemin , nom_fichier):
        self.chemin = import_export.fix_chemin(chemin)
        self.nom_fichier = nom_fichier

    @staticmethod
    def fix_chemin(chemin): #cette methode statique permettra de regler le probleme des back et forward slash
        nouveau_chemin=''
        for caractere in chemin:
            if caractere == "\\":
                nouveau_chemin += "/"
            else:
                nouveau_chemin += caractere
        return nouveau_chemin
    
