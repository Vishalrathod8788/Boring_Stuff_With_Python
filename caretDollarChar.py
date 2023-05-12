import re

beginsWithHelloRegex = re.compile(r'^Hello')
# print(beginsWithHelloRegex.search('Hello There !'))
# print(beginsWithHelloRegex.search('He said "Hello!"'))

endsWithNumberRegex = re.compile(r'world!$')
print(endsWithNumberRegex.search('Hello world!'))



