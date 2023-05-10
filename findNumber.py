import re

# message = 

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 405-555-9999 or my office Line.')

print(mo)