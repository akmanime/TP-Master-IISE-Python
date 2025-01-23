while True:
    ajouter = input("Entrez une nouvelle phrase Y/N : ")
    if ajouter.lower() == "y":
        with open('ex2.txt', "a") as f:  # Ouvre le fichier en mode ajout ("append")
            while True:
                print('Tapez f pour terminer.')
                nouvelle_phrase = input("Votre nouvelle ligne : ")
                if nouvelle_phrase.lower() == "f":
                    break
                f.write(nouvelle_phrase + "\n")
    elif ajouter.lower() == "n":
        break
    else:
        print("Veuillez répondre par y/n")
with open ("ex2.txt" , "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)