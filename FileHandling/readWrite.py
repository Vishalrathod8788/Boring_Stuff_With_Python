# import os

# Read mode

# helloFile = open('/home/vishal/Boring_Stuff_With_Python/Hello.txt')
# print(helloFile.read())
# print('Hi \nHello....!')
# helloFile.close()

# helloFile = open('/home/vishal/Boring_Stuff_With_Python/Hello.txt')
# content = helloFile.read()
# print(content)
# helloFile.close()

# Write mode 

helloFile = open('/home/vishal/Boring_Stuff_With_Python/Hyy.txt', 'w')
print(helloFile.write('Hello Vishal\n'))
print(helloFile.write('Hello Vishal\n'))
print(helloFile.write('Hello Vishal\n'))
print(helloFile.write('Hello Vishal\n'))
helloFile.close()