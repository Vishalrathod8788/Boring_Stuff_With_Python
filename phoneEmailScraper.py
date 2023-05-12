#! python3

# TODO : Create a regex for phone numbers

# TODO : Create a regex for email address

# TODO : Get the text off the clipboard

# TODO : Extract the email/phone numbers from this text

# TODO : Copy the extracted email/phone to the clipboard 

import re, pyperclip

re.compile(r'''  
# 415-555-1234, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
((\d\d\d) | (\(\d\d\d)))?        # area code (optional)
\s|-        # first seprator 
\d\d\d        # first 3 digits
-        # seprator
\d\d\d\d        # last 4 digits
ext(\.)?\s(\d{2,5})        # extension (optional)

''', re.VERBOSE )