#! python3

# Create a regex for phone numbers

import re

phoneRegex = re.compile(r'''  
# 415-555-1234, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d)))?   # area code (optional)
(\s|-)                      # first seprator 
\d\d\d                      # first 3 digits
-                           # seprator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|x)         # extension word-part (optional)
(\d{2,5}))? 
)                # extension word-number (optional)
''', re.VERBOSE )

# re.compile(r'((\d\d\d) | (\(\d\d\d)))?(\s|-)\d\d\d-\d\d\d\d(((ext(\.)?\s) | x)(\d{2,5}))?')

# Create a regex for email address 

# some.+_thing@(\d{2,5})?.com

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+    # name part
@               # @ symbol
[a-zA-Z0-9_.+]+    # domain name part

''', re.VERBOSE)


# Get the text off the clipboard
text = 'Dr.Barbara Jones x107 870-864-7190 brjones@southark.edu'

# Extract the email/phone numbers from this text
extractPhone = phoneRegex.findall(text)
extractEmail = emailRegex.findall(text)

allPhoneNumbers = []

for phoneNumber in extractPhone:
    allPhoneNumbers.append(phoneNumber[0])


print(allPhoneNumbers) 
print(extractEmail)

# TODO : Copy the extracted email/phone to the clipboard 