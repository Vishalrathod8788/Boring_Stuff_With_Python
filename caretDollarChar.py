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

# anything except newline

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: John Last Name: Smith'))

print(nameRegex.findall('First Name: John Last Name: Smith'))