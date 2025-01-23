import csv

contacts = [
    ["Nom" , "Age" , "Ville"],
    ["mohamed" , "22" , "Laayoune"],
    ["yassine", "27" , "safi"],
    ["oussama" , "24" , "agadir"]
]

with open('contacts.csv', mode= 'w', newline='') as f:
    ecrivain = csv.writer(f)
    ecrivain.writerows(contacts)
    
with open('contacts.csv', mode= 'r', newline='') as f:
    lecteur = csv.reader(f)
    for line in lecteur:
        print(line)