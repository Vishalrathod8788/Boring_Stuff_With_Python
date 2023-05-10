import re

batRegex = re.compile(r'Bat(wo)?man')

mo = batRegex.search('The Adavtures of Batman')
print(mo.group())
