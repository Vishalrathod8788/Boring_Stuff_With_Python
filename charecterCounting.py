import pprint 


message = 'it was a bright cold day in May, and the clocks were steiking thirteen,ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# cout = 0
count = { }
for cout in count :

    for character in message.upper():
        count.setdefault(character, 0)
        count[character] = count[character] + 1

# print(count)

pprint.pprint(count)

print