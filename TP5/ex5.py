import json

# 1. Créer un dictionnaire Python
etudiants = {
    "etudiants": [
        {"nom": "akram", "age": 22, "note": 16},
        {"nom": "mohamed", "age": 21, "note": 14},
        {"nom": "brahim", "age": 19, "note": 18}
    ]
}

# 2. Enregistrer le dictionnaire dans un fichier JSON
with open("etudiants.json", "w") as fichier_json:
    json.dump(etudiants, fichier_json, indent=4)  # indent pour une meilleure lisibilité


# 3. Lire le fichier JSON et afficher les informations
with open("etudiants.json", "r") as fichier_json:
    data = json.load(fichier_json)
    for etudiant in data["etudiants"]:
        print(f" Nom: {etudiant['nom']}, \n Âge: {etudiant['age']}, \n Note: {etudiant['note']}\n --------")