class Chien:
    def __init__(self,nom, race,age):
        self.nom = nom
        self.race = race
        self.age = age
        
    def aboyer(self):
        print (f"{self.nom} Woof")

# Test
chien = Chien("rocky" , "labrador" , 10)
chien.aboyer()