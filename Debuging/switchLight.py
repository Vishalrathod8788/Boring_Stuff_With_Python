market_2nd = {'ns' : 'Green', 'ew' : 'red'}

def switchLight(intersection) :

    for key in intersection.keys() :
        if intersection[key] == 'Green' :
            intersection[key] = 'red'
        elif intersection[key] == 'red' :
            intersection[key] = 'Green'


print(market_2nd)
switchLight(market_2nd)
print(market_2nd)