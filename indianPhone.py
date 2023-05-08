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

message = 'Call me +911234567890 tomorrow, or at +916353008705 for my office Line.'

foundNumber = False

for i in range(len(message)) :
    chunk = message[i:i+13]
