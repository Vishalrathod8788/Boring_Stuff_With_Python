import re

# ' ? ' charecter Regular expression that meance (Zero or One time)

# batRegex = re.compile(r'Bat(wo)+man')

# mo = print(batRegex.search('The Adavtures of Batman'))

# mo = batRegex.search('The Adavtures of Batwowowoman')       // This Error Resolve in + charecter  regular expretion throw

# print(mo.group())

# mo = batRegex.search('The Adavtures of Bataman')
 
# print(mo == None)  

# phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# phoneRegex.search('Hello, My name is vishal rathod my phone number is 415-555-1234')

# demo = phoneRegex.search('Hello, My name is vishal rathod my phone number is 415-555-1234')

# print(demo.group()) 



# + charecter meance (One or More time)

# batRegex = re.compile(r'Bat(wo)+man')

# mo = batRegex.search('The Adavtures of Batwowowoman')

# print(mo.group()) 

# # * charecter meance (Zero or More time)

# regEx = re.compile(r'\+\*\?')

# mo = regEx.search('i learn about +*?+*?+*?+*? regEx Syntax')

# print(mo.group())

# haRegEx = re.compile(r'(Ha){3}') # (Ha){3} That Meance HaHaHa

# mo = haRegEx.search('He said "HaHaHa"')

# Not Hardword  re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?)((\d\d\d-)?\d\d\d-\d\d\d\d(,)?)((\d\d\d-)?\d\d\d-\d\d\d\d(,)?)

phoneRegEx = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegEx.search('My number is are 415-555-1345,254-123-4567,456-123-1234')

print(mo.group())

# {x.y} (at least x, at most y)

# haRegex = re.compile(r'(Ha){3,5}')  # That meance {3,5} is String content Length 3 is min Length and 5 is Max Length 

# print(haRegex.search('He said HaHaHa'))

# print(haRegex.search('He said HaHaHaHa'))

# print(haRegex.search('He said HaHaHaHaHa'))

# print(haRegex.search('He said HaHaHaHaHaHa'))

# print(haRegex.search('He said HaHaHaHaHaHaHa'))

haRegex = re.compile(r'(\d){3,5}?') # ? is represent min Length

mo = haRegex.search('12345678910')
 
print(haRegex.findall('12345678910'))

