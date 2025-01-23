def safe_devision(a,b):
    try :
        result = a/b
    except ZeroDivisionError:
        print('Zero Division error')
    else :
        print ('La Division est bien faite.')
        return result
    finally :
        print('la fonction est terminée')
        
print(safe_devision(2,0))