class tri():
    @staticmethod
    def fusion(liste1,liste2):
        liste=[]
        i,j=0,0
        while i<len(liste1)and j<len(liste2):
            if liste1[i]<=liste2[j]:
                liste.append(liste1[i])
                i+=1
            else:
                liste.append(liste2[j])
                j+=1
        while i<len(liste1):
            liste.append(liste1[i])
            i+=1
        while j<len(liste2):
            liste.append(liste2[j])
            j+=1
        return liste

    @staticmethod
    def tri_fusion(liste):
        if len(liste)<2:
            return liste[:]
        else:
            milieu=len(liste)//2
            liste1= tri().tri_fusion(liste[:milieu])
            liste2= tri().tri_fusion(liste[milieu:])
            return tri().fusion(liste1,liste2)