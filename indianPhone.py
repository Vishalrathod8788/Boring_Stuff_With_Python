def indianPhone(num) :
    if len(num) != 13:        
        return False
    if num[0] == '+' :
        if num[1] == '9' :
            return True
        if num[2] == '1' :
            return True
        return True
    for i in range(0, 10) :
        if not num[i].isdecimal() :
            return False
    return True

message = 'Call me +916353008705 tomorrow, or at +911234567890 for my office Line.'

foundNumber = False

for i in range(len(message)) :
    chunk = message[i:i+13]
    if indianPhone(chunk) :
        print('Phone number found: ' + chunk)
        foundNumber = True

if not foundNumber : 
    print('Could not find any phone numbers.')