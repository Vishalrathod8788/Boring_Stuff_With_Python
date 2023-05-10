import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

phoneNumRegex.search('My Number is 451-555-1245')

match = phoneNumRegex.search('My Number is 451-555-1245')

print(match.group()) 