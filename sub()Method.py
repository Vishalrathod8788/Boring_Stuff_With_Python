import re

# Find And Replace Feture logic in python

nameRegex = re.compile(r'Agent \w+')
print(nameRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
# ['Agent Alice', 'Agent Bob']

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub('Vishal 1\****', 'Agent Alice gave the secret documents to Agent Bob.'))
# Vishal gave the secret documents to Vishal.