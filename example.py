# print('Hello', end=' ')
# print('world')

spam = 42 # global variable
def eggs():
    spam = 42 # local variable
    print('some code here')
    print('some more code')
    print(spam)

eggs()