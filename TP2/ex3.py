class CompteBancaire:
    def __init__(self,titulaire,solde=0):
        self.titulaire = titulaire
        self.solde = solde
    def deposer(self,montant):
        self.montant = montant
        self.solde += montant
        print(self.montant)
    def retirer(self,montant):
        self.montant = montant
        self.solde -= montant
        print(self.montant)
    def afficher_solde(self):
        print (self.solde)

#Test 
compte = CompteBancaire("akm",0)
compte.deposer(10000)
compte.retirer(5000)
compte.afficher_solde()
