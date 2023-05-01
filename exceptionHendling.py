# def div42by(divideBy) :
#     try :
#         return 42 / divideBy
#     except ZeroDivisionError :
#         print('Error: You tried to divide by zero.')

# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(2))

print('How many cats do you have ?')
numCat = input()

try :
    if int(numCat) >= 4 :
        print('That is a lot of cats.')
    else :
        print('How many dogs do you have ?')
except ValueError :
    print('You did not enter a number.')
    
print('Done.')