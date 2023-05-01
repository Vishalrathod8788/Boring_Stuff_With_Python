import random

def getAnswer(answer) :
    if answer == 1 :
        return 'it is certain'
    elif answer == 2 :
        return 'it is decidedly so'
    elif answer == 3 :
        return 'yes'
    elif answer == 4 :
        return 'reply hazy try again'
    elif answer == 5 :
        return 'your statement is no longer relevant'
    elif answer == 6 :
        return 'concentrate and ask again'
    elif answer == 7 :
        return 'my reply is no'
    elif answer == 8 :
        return 'outlook not so good'
    elif answer == 9 :
        return 'very doubtful'
    else :
        return 'no idea'
print('Think of a Yes?no question, and press enteer to see')
input()

print(getAnswer(random.randint(1, 9)))