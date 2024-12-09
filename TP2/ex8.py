class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []
        
    def ajouter_ami(self, ami):
        self.amis.append(ami)
            
    def afficher_amis(self):
        print(f"Amis de {self.prenom} {self.nom} :")
        for ami in self.amis:
            print(f"Nom : {ami.nom}\nPrenom : {ami.prenom}\nAge : {ami.age}\n")
        
# Test
personne1 = Personne("ryad", "akram", 22)
personne2 = Personne("alami", "yassine", 31)
personne3 = Personne("ait nasiri", "Hamza", 65)

personne1.ajouter_ami(personne2)
personne1.ajouter_ami(personne3)

personne1.afficher_amis()