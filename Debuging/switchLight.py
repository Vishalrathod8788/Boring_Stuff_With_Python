market_2nd = {'ns' : 'Green', 'ew' : 'Red'}

def switchLight(intersection) :

    for key in intersection.keys() :
        if intersection[key] == 'Green' :
            intersection[key] = 'Yellow'
        elif intersection[key] == 'Red' :
            intersection[key] = 'Green'
        elif intersection[key] == 'Yellow' :
            intersection[key] = 'Red'


print('Before :' + str(market_2nd))
switchLight(market_2nd)
print('After :' + str(market_2nd))