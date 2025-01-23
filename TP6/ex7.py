import logging

def log_error(message):
    logging.basicConfig(filename='error.log', level=logging.ERROR)
    logging.error(message)

def read_file(filename):
    try:
        with open(filename, "r") as file:
            contenu = file.read()
            return contenu
    except FileNotFoundError:
        log_error(f"File not found: {filename}")
        print("le fichier n'est pas trouver") #This print is redundant, you have logging now.
        return None # Return None to indicate failure
    finally:
        print("le traitement est terminer")

print(read_file("file.txt"))
print(read_file("file1.txt"))