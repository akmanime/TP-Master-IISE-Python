class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    def calculer_surface(self):
        print(f"la surface est : {self.hauteur*self.largeur}")
    def calculer_perimetre(self):
        print("le perimetre est : ",2*self.largeur+2*self.hauteur)
        
rect = Rectangle(2,3)
rect.calculer_perimetre()
rect.calculer_surface() 