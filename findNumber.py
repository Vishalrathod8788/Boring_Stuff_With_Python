import re


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 405-555-9999 or my office Line.') # This is Match Method meance 12 Digit match To Condition is True

print(mo)