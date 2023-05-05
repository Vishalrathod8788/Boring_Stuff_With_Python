
# Created on Wed Apr  3 15:53:10 2019

# Author : Vishal Rathod

# myCat = {'size' : 'fat', 'color' : 'red', 'height' : str(162)}

# print('Mycat has ' + myCat['height'])


# Output : Mycat has 162

spam = 42
demo = 24

# print(spam == demo)

spam = {'name' : 'Vishal', 'surname' : 'Rathod', 'age' : str(18)}

demo = {'surname' : 'Rathod', 'name' : 'Vishal', 'age' : str(18)}

# print(spam == demo)

# print('My name is ' + spam['name'] + ' ' + spam['surname'] + ' and my age is ' + spam['age'])

# Output : My name is Vishal Rathod and my age is 18

# print('name' in spam)

# print('Height' not in spam)

# print(spam.keys())
# print(spam.values())
# print(spam.items())

# for i in spam.items():
#     print(i)



print(demo.get('age', str(0)))

print(demo.get('name', ''))

print(demo.set('name', 'VGRcoder'))

print(demo)