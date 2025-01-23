class NegativeAgeError:
    print ('age ne doit pas etre negative')

def set_age(age):
    try:
        if age > 0:
            print(age)
    except NegativeAgeError as e:
        print(e)

set_age(-2)