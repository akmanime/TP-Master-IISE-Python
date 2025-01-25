try:
    with open("inexistant.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Erreur : Le fichier 'inexistant.txt' n'a pas été trouvé.")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")