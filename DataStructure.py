# Author : Vishal Rathod

import pprint

theBoard  = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
             'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
             'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' '}

pprint.pprint(theBoard)

theBoard['mid-M'] = 'X'

theBoard['mid-L'] = 'X'
theBoard['top-M'] = 'O'
theBoard['top-L'] = 'O'
theBoard['top-R'] = 'O'
theBoard['low-R'] = 'X'

pprint.pprint(theBoard)
