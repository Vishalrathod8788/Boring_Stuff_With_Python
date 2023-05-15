# import os

# ---Read mode

# helloFile = open('/home/vishal/Boring_Stuff_With_Python/Hello.txt')
# print(helloFile.read())
# print('Hi \nHello....!')
# helloFile.close()

# helloFile = open('/home/vishal/Boring_Stuff_With_Python/Hello.txt')
# content = helloFile.read()
# print(content)
# helloFile.close()

# ---Write mode 

# helloFile = open('/home/vishal/Boring_Stuff_With_Python/Hyy.txt', 'w')
# print(helloFile.write('Hello Vishal\n'))
# print(helloFile.write('Hello Vishal\n'))
# print(helloFile.write('Hello Vishal\n'))
# print(helloFile.write('Hello Vishal\n'))
# helloFile.close()

import shelve

# ---Shelve

shelfFile = shelve.open('mydata')

shelfFile['cat'] = ['Zophile', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']

print(shelfFile['cat'])

shelfFile.close()


shelfFile = shelve.open('Dog')

shelfFile['dog'] = ['Name', 'Age', 'Birthdate', 'Color', 'Height', 'Wight']

print(shelfFile['dog'])

shelfFile.close()

