import os 
import datetime
import math 

def rep_courant():
    return os.getcwd()

def date():
    return datetime.datetime.now()
    
def racine_carre():
    nbr = int(input('entrer un nombre : '))
    return math.sqrt(nbr)

print(rep_courant())
print(date())
print(racine_carre())