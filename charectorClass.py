import re

# important note :- 
    # \d Any numeric digit from 0 to 9
    # \D Any character that is not a numeric digit from 0 to 9
    # \w Any letter, numeric digit, or the underscore charecter.
    # \W Any character that is not a letter, numeric digit, or the underscore charecter.
    # \s Any space, tab, or newline charecter.
    # \S Any character that is not a space, tab, or newline.

digitRegex = re.compile(r'\d\s\w')

print(digitRegex.findall('Hell0 Word12 34'))

vowelRegex = re.compile(r'[aeiou]') # that meance r'(a|e|i|o|u)'

