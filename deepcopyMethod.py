import copy

spam = [1,2,3,4,5]

# print(spam)

eggs = copy.deepcopy(spam)

eggs[1] = 'Hello'
print(eggs)

