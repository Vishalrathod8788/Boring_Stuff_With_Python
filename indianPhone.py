def indianPhone(num) :
    if len(num) != 13:
        if num[0] == '+' :
            return True
        if num[1] == '9' :
            return True
                
        return False
    for i in range(0, 10) :
        if not num[i].isdecimal() :
            return False
    return True
print(indianPhone('6353008705'))
  