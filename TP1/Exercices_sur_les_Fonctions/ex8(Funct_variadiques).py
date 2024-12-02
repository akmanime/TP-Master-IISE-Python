def somme_varargs(*args):
    return sum(args)

# Tests
print(somme_varargs(1,2,3,0))
print(somme_varargs(1.5,2,3.1,0))