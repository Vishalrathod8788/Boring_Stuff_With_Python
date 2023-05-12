import re

beginsWithHelloRegex = re.compile(r'^Hello')
beginsWithHelloRegex.search('Hello There !')
print(beginsWithHelloRegex.search('He said "Hello!"'))


