import re

# def isPhoneNumber(text) :
#     if len(text) != 12 :
#         return False
#     for i in range(0, 3) :
#         if not text[i].isdigit() :
#             return False

#     if text[3] != '-' :
#             return False
    
#     for i in range(4, 7) :
#         if not text[i].isdecimal() :
#             return False
        
#     if text[7] != '-' :
#         return False

#     for i in range(8,12) :
#         if not text[i].isdecimal() :
#             return False
    
#     return True

# message = 'Call me 415-555-1011 tomorrow, or at 405-555-9999 or my office Line.'

# foundNumber = False

# for i in range(len(message)) :
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk) :
#         print('Phone number found: ' + chunk)
#         foundNumber = True

# if not foundNumber : 
#     print('Could not find any phone numbers.')

message = 'Call me 415-555-1011 tomorrow, or at 405-555-9999 or my office Line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search(message)

print(mo.group())