class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")


class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_moteur(self):
        print(f"Puissance: {self.puissance} ch")
        print(f"Type de moteur: {self.type_moteur}")


class Voiture(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places

    def afficher_info(self):
        Vehicule.afficher_info(self)
        Moteur.afficher_moteur(self)
        print(f"Nombre de places: {self.nombre_de_places}")


class Moto(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        Vehicule.afficher_info(self)
        Moteur.afficher_moteur(self)
        print(f"Type de moto: {self.type_moto}")


# Créer une instance de Voiture
voiture1 = Voiture("Toyota", "Camry", 2023, 200, "Essence", 5)

# Créer une instance de Moto
moto1 = Moto("Harley-Davidson", "Sportster", 2022, 120, "Essence", "Cruiser")

# Afficher les informations de la voiture
print("Informations de la voiture:")
voiture1.afficher_info()
print("\n")