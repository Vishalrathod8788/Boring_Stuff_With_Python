def indianPhone(num) :
    if len(num) != 10:
        if num[0] == '+' :
            return True
        
        return False
    for i in range(0, 10) :
        if not num[i].isdecimal() :
            return False
    return True
print(indianPhone('6353008705'))
  