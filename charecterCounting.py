
message = 'it was a bright cold day in May, and the clocks were steiking thirteen'

count = {} 

for character in message:
    if character in count:
        count[character] += 1



print(count)