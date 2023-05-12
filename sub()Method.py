import re

nameRegex = re.compile(r'Agent \w+')
print(nameRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
# ['Agent Alice', 'Agent Bob']

