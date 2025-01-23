def get_positive_integer():
  while True:
    try:
      user_input = input("Entrez un entier positif : ")
      number = int(user_input)
      if number > 0:
        return number
      else:
        print("L'entier doit être strictement positif.")
    except ValueError:
      print("Saisie invalide. Veuillez entrer un entier.")

# Appel de la fonction pour tester
positive_number = get_positive_integer()
print(f"Vous avez saisi l'entier positif : {positive_number}")