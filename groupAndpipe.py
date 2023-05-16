import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

phoneNumRegex.search('My Number is 451-555-1245')

match = phoneNumRegex.search('My Number is 451-555-1245')

print(match.group()) 


# Area Code Group...

phoneNumRegex = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d')

match = phoneNumRegex.search('My Number is 451-555-1245')

print(match.group()) 


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(0))

