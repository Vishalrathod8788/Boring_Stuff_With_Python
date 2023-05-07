# spam = 'Hello Friends'

# print(spam.upper())

# demo = 'HELLO FRIENDS'

# print(demo.lower())

# spam = 'HELLO WORLD !'
# demo = 'hello world...!' 
# print(demo.islower()) 
# print(spam.isupper())

# print('Hello'.upper().isupper())

# isalpha()
# isalnum()
# istitle()
# isspace()
# isdigit()
# isdecimal()

# print('hello'.isalpha())
# print('hello'.isalnum())
# print('Hello Friends How Are You...?'.istitle())
# print('hello world'.title())
# print('Hello World'[5].isspace())
# print('13456'.isdecimal())

# startwith()
# endwith()

# print('Hello...'.startswith('H'))

# print('How are you...'.endswith('.'))

# join()
# Convert Array into String
spam = ['Cat', 'Dog', 'Monkey', 'Cow', 'Buffelo']

# print(','.join(spam))
demo = '\n\t'.join(spam)

# print(demo)

# split()

print('My name is Vishal Rathod'.split(' '))

# ljust() left Justify
# rjust() Right Justify

print('hello'.rjust(50 , '*'))

print('Hello'.ljust(45, '-') + 'hello')

# Center()
name = input()
print('Helllo'.center(40))

print(name.center(50, '='))


# strip()
# rstrip()
# lstrip()

spam = 'Hello'.rjust(10)

print(spam)
print(spam.strip())

print('         Vishal           '.strip())