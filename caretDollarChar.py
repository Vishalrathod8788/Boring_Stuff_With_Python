import re



beginsWithHelloRegex = re.compile(r'^Hello')
# print(beginsWithHelloRegex.search('Hello There !'))
# print(beginsWithHelloRegex.search('He said "Hello!"'))

# endsWithNumberRegex = re.compile(r'world!$')
# print(endsWithNumberRegex.search('Hello world!'))




endsWithNumberRegex = re.compile(r'Hello World!$')

print(endsWithNumberRegex.search('Hello World!'))

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('12361826386x836823684'))
