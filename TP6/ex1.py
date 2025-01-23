def safe_devision(a,b):
    try :
        return a/b
    except ZeroDivisionError:
        print('Zero Division error')

safe_devision(2,0)