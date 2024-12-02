def comptes_occurences(liste):
    d= {}
    for x in liste:
        if x in d:
            d[x] = d[x] + 1
        else : d[x] = 1
    return d

# Test
print(comptes_occurences(["x","y","i","x"]))