import random

print('Hello, What is Your Name ?')
name = input()
secretNumber = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

def  random_number(m):
    return random.randint(0,m)