import re

# ' ? ' charecter Regular expression

# batRegex = re.compile(r'Bat(wo)?man')

# mo = print(batRegex.search('The Adavtures of Batman'))

# print(mo.group())

# mo = batRegex.search('The Adavtures of Bataman')
 
# print(mo == None)  

# phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# phoneRegex.search('Hello, My name is vishal rathod my phone number is 415-555-1234')

# demo = phoneRegex.search('Hello, My name is vishal rathod my phone number is 415-555-1234')

# print(demo.group()) 


# * charecter meance (Zero or More )

# + charecter meance (One or More)

batRegex = re.compile(r'Bat(wo)+man')

mo = print(batRegex.search('The Adavtures of Batwoman'))

print(batRegex.search('The Adavtures of Batwowowoman'))