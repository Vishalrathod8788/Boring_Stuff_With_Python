import re

# re.compile(r'(\d\d\d)(-)?\d\d\d-\d\d\d\d')

re.compile(r'''
\d\d\d      # Phone Area Code
-           # first dash
\d\d\d      # fist 3 digit
-
\d\d\d\d''', re.VERBOSE)




