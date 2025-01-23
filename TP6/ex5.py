def process_input(user_input):
    try:
        return 10/int(user_input)
    except ValueError:
        print('Valeur erreur')
    except ZeroDivisionError:
        print ('Zero Division Erreur')

process_input(0)