def process_file_and_integer():
    
    try:
        filename = input("Entrez le nom du fichier : ")
        with open(filename, 'r') as file:
            file_contents = file.read()  # Lire tout le contenu du fichier
            print("Contenu du fichier :", file_contents)

        integer_input = input("Entrez un entier : ")
        integer_value = int(integer_input)
        print("Entier valide :", integer_value)

        # Ajoutez ici le traitement que vous voulez effectuer avec les données

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' n'a pas été trouvé.")
    except ValueError:
        print(f"Erreur : '{integer_input}' n'est pas un entier valide.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
        
process_file_and_integer()