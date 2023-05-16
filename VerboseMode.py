import re

# re.compile(r'(\d\d\d)(-)?\d\d\d-\d\d\d\d')

re.compile(fr'''
\d\d\d      # Phone Area Code
-           # first dash
\d\d\d      # fist 3 digit
-           # secound dash
\d\d\d\d # last 4 digit
\sx\d{2,4}''', re.IGNORECASE | re.VERBOSE | re.DOTALL)