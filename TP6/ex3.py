def read_file(filename):
    try:
        with open(filename , "r") as file:
            contenu = file.read()
            return contenu
    except FileNotFoundError:
        print ("le fichier n'est pas trouver")
    finally :
        print("le traitement est terminer")

print (read_file("file.txt"))