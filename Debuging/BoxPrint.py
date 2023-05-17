"""

***************
*             *
*             *
*             *
***************

"""

def boxPrint(symbol, width, height) :

    if len(symbol) != 1:
        raise Exception("Error: Symbol must be a single character.")
    
    if (width < 2) or (height < 2) :
        raise Exception("Error: Width and height must be greater than 2.")

    print(symbol * width)
    
    for i in range(height - 2) :
        print(symbol + (' ' * (width - 2)) + symbol)
    
    print(symbol * width)

boxPrint('*', 15, 5) 
boxPrint('O', 15, 5)
boxPrint('*', 15, 5)