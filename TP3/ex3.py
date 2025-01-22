from abc import ABC, abstractmethod
import math

class Forme(ABC):
  @abstractmethod
  def calculer_surface(self):
    pass

class Cercle(Forme):
  def __init__(self, rayon):
    self.rayon = rayon

  def calculer_surface(self):
    return math.pi * self.rayon**2

class Rectangle(Forme):
  def __init__(self, longueur, largeur):
    self.longueur = longueur
    self.largeur = largeur

  def calculer_surface(self):
    return self.longueur * self.largeur

def afficher_surface(formes):
    for forme in formes:
        surface = forme.calculer_surface()
        print(f"Surface : {surface}")
        
forms = [Cercle(5) , Rectangle(2,3)]
afficher_surface(forms)