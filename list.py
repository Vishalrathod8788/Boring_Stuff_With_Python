spam = ['Cat', 'rat', 'Dog', 'Elephant']

print(spam)

print(spam[1])

print(spam[0])
print(spam[0][1]) 

spam[1][1] = 'Hello'

print(spam[-1][-1])
 

print(spam[0][1])
print(spam[0][2])

print(spam[1:3]) 

spam[1 : 3] = ['Monkey', 'Donkey']

# print(spam)

print(spam[:3])

spam = ['cat', 'bat', 'rat', 'Elephant']

del spam[2]

print(spam)

print(len('Hello'))

print(len([1,2,3,4]))

print('Hello' + 'World')

print([1,2,3,4,5] + [6,7,8,9,10])
 

print([1,2,3,4] * 2)

print('Hello' * 5)

print(str(4))

print(list('Hello'))

print('Hello' in ['Hi', 'Hy', 'Hello'])

print(42 not in ['42', 'Hello', 'How Are You'])
print(list('Hello'))

name = 'Zophie a cat'

print(name[7])

name[7] = 'Vishal'

newName = name[0:7] + 'The' + name[8 : 12]

print(newName)

spam = [1,2,3,4,5,6,7]

swap = spam

print(spam)

spam[2] = 'VGRcoder'

print(swap)

#  ****   ---->>>>    append Method in List




one = [1,2,1,1,1,]

def eggs(one) :
    one.append('Hello')

spam = [1,2,3,4,5]
eggs(one)

print(spam)