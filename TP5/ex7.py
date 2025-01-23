import os
import shutil

# 1. Créer le fichier journal.txt et ajouter du texte
with open("journal.txt", "w") as f:
  f.write("Ceci est la première ligne du journal.\n")
  f.write("Ceci est la deuxième ligne du journal.\n")
  f.write("Ceci est la troisième ligne du journal.\n")

# 2. Copier le fichier journal.txt vers journal_copie.txt

shutil.copyfile("journal.txt", "journal_copie.txt")
print("Le fichier journal.txt a été copié avec succès dans journal_copie.txt")

# 3. Créer le dossier archives s'il n'existe pas
if not os.path.exists("archives"):
  os.makedirs("archives")

# Déplacer journal_copie.txt vers le dossier archives

shutil.move("journal_copie.txt", "archives/")
print("Le fichier journal_copie.txt a été déplacé avec succès dans le dossier archives.")