def div42by(divideBy) :
    try :
        return 42 / divideBy
    except ZeroDivisionError :
        print('Error: You tried to divide by zero.')
