import csv
import os

def ajouter_contact(nom_fichier):
  nom = input("Entrez le nom du contact : ")
  prenom = input("Entrez le prénom du contact : ")
  telephone = input("Entrez le numéro de téléphone : ")
  email = input("Entrez l'adresse email : ")

  with open(nom_fichier, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([nom, prenom, telephone, email])
  print("Contact ajouté avec succès !")

def afficher_contacts(nom_fichier):
    with open(nom_fichier, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        print(f"Nom: {row[0]}, Prénom: {row[1]}, Téléphone: {row[2]}, Email: {row[3]}")


def rechercher_contact(nom_fichier):
  nom_recherche = input("Entrez le nom du contact à rechercher : ")

  with open(nom_fichier, 'r') as csvfile:
    reader = csv.reader(csvfile)
    trouve = False
    for row in reader:
        if row[0].lower() == nom_recherche.lower():
         print(f"Nom: {row[0]}, Prénom: {row[1]}, Téléphone: {row[2]}, Email: {row[3]}")
         trouve = True
         break
        if not trouve:
          print(f"Aucun contact trouvé avec le nom '{nom_recherche}'.")



def supprimer_contact(nom_fichier):
  nom_supprimer = input("Entrez le nom du contact à supprimer : ")
  with open(nom_fichier, 'r') as csvfile:
    reader = csv.reader(csvfile)
    contacts = list(reader)
    
  with open(nom_fichier, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    supprime = False
    for row in contacts:
        if row[0].lower() != nom_supprimer.lower():
          writer.writerow(row)
        else:
          supprime = True
        if supprime:
          print(f"Contact '{nom_supprimer}' supprimé avec succès.")
        else:
          print(f"Aucun contact trouvé avec le nom '{nom_supprimer}'.")

nom_fichier = "contacts.csv"  # Nom du fichier CSV

# Vérification et création du fichier si besoin
if not os.path.exists(nom_fichier):
    with open(nom_fichier, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nom", "Prénom", "Téléphone", "Email"])

while True:
    print("\nMenu:")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Rechercher un contact")
    print("4. Supprimer un contact")
    print("5. Quitter")
    choix = input("Entrez votre choix : ")

    if choix == '1':
        ajouter_contact(nom_fichier)
    elif choix == '2':
        afficher_contacts(nom_fichier)
    elif choix == '3':
        rechercher_contact(nom_fichier)
    elif choix == '4':
        supprimer_contact(nom_fichier)
    elif choix == '5':
        break
    else:
            print("Choix invalide.")