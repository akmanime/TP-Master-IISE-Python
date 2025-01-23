def convert_to_int(value):
    try :
        return int(value)
    except ValueError:
        print('la valeur non convertible')
        return None
        
print (convert_to_int(12.1))
print (convert_to_int("2.1"))