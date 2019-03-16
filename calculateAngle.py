from getJson import loadJson
import math
#arr = loadJson('EXAMPLE.json')

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def calc(x1,y1,x2,y2,x3,y3):
    d1 = dist(x1, y1, x2, y2)
    d2 = dist(x2, y2, x3, y3)
    d3 = dist(x1, y1, x3, y3)
    #print(d1,d2,d3)
    return math.acos((d1 * d1 + d2 * d2 - d3 * d3) / (2 * d1 * d2)) * 180 / 3.14159

def angle(arr, a, b, c):
    return calc(arr[a][0], arr[a][1], arr[b][0], arr[b][1], arr[c][0], arr[c][1])

#print(arr)
"""
arr = loadJson('EXAMPLE.json')
print(angle(arr,11,12,13))
"""

