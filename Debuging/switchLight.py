market_2nd = {'ns' : 'Green', 'ew' : 'red'}

def switchLight(intersection) :

    for key in intersection.keys() :
        if intersection[key] == 'Green' :
            intersection[key] = 'red'
        elif intersection[key] == 'red' :
            intersection[key] = 'Green'


print('Before :' + str(market_2nd))
switchLight(market_2nd)
print('After :' + str(market_2nd))