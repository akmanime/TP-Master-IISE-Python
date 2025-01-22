class Person:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
    @property
    def nom(self):
        return self.__nom
    @property
    def prenom(self):
        return self.__prenom
    @property
    def age(self):
        return self.__age
    
    @age.setter    
    def age(self, age):
        self.__age = age
        
P = Person("Akram" , "Ryad" , 22)
print(P.nom , P.prenom , P.age)
P.age = 23
print(P.age)