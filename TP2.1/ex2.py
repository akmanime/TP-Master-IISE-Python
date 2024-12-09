class Voiture:
    def __init__ (self,marque,modele,annee):
        self.marque = marque
        self.modele = modele 
        self.annee = annee
    
    def afficher_info (self):
        print (f"Marque :{self.marque}")
        print ("Modele :"f"{self.modele}")
        print ("Annee :", self.annee)
        
#Test
voiture = Voiture("BMW","M4","2014")
voiture.afficher_info()