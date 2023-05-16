import re

# important note :- 
    # \d Any numeric digit from 0 to 9
    # \D Any character that is not a numeric digit from 0 to 9
    # \w Any letter, numeric digit, or the underscore charecter.
    # \W Any character that is not a letter, numeric digit, or the underscore charecter.
    # \s Any space, tab, or newline charecter.
    # \S Any character that is not a space, tab, or newline.

    # + charecter meance (One or More time)
    # ' ? ' charecter Regular expression that meance (Zero or One time)
    # * charecter meance (Zero or More time)

digitRegex = re.compile(r'\d\s\w')

print(digitRegex.findall('Hell0 Word12 34'))

vowelRegex = re.compile(r'[a-fA-F]') # that meance find small a to f or capital A to F

# vowelRegex = re.compile(r'[aeiouAEIOU]') # that meance r'(a|e|i|o|u)'

print(vowelRegex.findall('Robocop eats Baby Food.'))

doublevowelRegex = re.compile(r'[aeiouAEIOU]{2}')

print(doublevowelRegex.findall('Robocop eats Baby Food.'))

# Negative Charecter Classes 

vowelRegex = re.compile(r'[^aeiouAEIOU]') # ' ^ ' that meance Not in String Content is Display

print(vowelRegex.findall('Robocop eats Baby Food.'))



