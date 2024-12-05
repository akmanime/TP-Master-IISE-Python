class Personne:
    def __init__(self,nom,prenom,age):
        self.nom = nom
        self.prenom = prenom
        self.age=age
    def se_presenter(self):
        print(f"Nom :{self.nom}")
        print(f"Prenom :{self.prenom}")
        print(f"Age :{self.age}")
class Etudiant(Personne):
    def __init__(self,matricule):
        self.matricule = matricule
    def etudier(self):
        print(f"matricule :{self.matricule}")
        
# Test
personne = Personne("ryad", "akram", 22)
personne.se_presenter()
etudiant = Etudiant("SH203694")
etudiant.etudier()