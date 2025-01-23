def file_stats(filename):
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = 0
        num_chars = 0
        for line in lines:
            words = line.split()
            num_words += len(words)
            num_chars += len(line)

    print("Statistiques du fichier :", filename)
    print("Nombre de lignes :", num_lines)
    print("Nombre de mots :", num_words)
    print("Nombre de caractères :", num_chars)
    
file_stats("stats.txt")