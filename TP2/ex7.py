class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
    

class Bibliotheque:
    def __init__(self):
        self.livres = []
    def ajouter_livre(self, livre):
        self.livres.append(livre)
        
    def afficher_livres(self):
        for self.livre in self.livres:
            print(f"Titre :{self.livre.titre}\nAuteur :{self.livre.auteur}\nAnnee de pub :{self.livre.annee_publication}\n")

# Test
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
livre2 = Livre("1984", "George Orwell", 1949)
livre3 = Livre("L'Étranger", "Albert Camus", 1942)

bibliotheque = Bibliotheque()
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)

bibliotheque.afficher_livres()