import os

with open('phrases.txt', mode= 'w', newline='') as f:
    f.write('Hello World')
# 1. Renommer le fichier

os.rename("phrases.txt", "anciennes_phrases.txt")
print("Le fichier 'phrases.txt' a été renommé en 'anciennes_phrases.txt'")

# 2. Supprimer le fichier
"""
os.remove("anciennes_phrases.txt")
print("Le fichier 'anciennes_phrases.txt' a été supprimé.")
"""