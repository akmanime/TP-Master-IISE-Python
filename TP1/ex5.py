def factorielle(n):
    if n == 0:  # Cas de base : la factorielle de 0 est 1
        return 1
    else:
        return n * factorielle(n - 1)  # Appel récursif

# Tests
print(factorielle(25))
print(factorielle(0))