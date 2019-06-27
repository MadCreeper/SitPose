from getJson import loadJson
import math
#arr = loadJson('EXAMPLE.json')


def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))


def calc(x1, y1, x2, y2, x3, y3):  # calculate 3-point angle
    d1 = dist(x1, y1, x2, y2)
    d2 = dist(x2, y2, x3, y3)
    d3 = dist(x1, y1, x3, y3)
    # print(d1,d2,d3)
    if d1 == 0 or d2 == 0:
        return -1
    # angle  = (d1)
    return math.acos((d1 ** 2 + d2 ** 2 - d3 ** 2) / (2 * d1 * d2)) * 180 / 3.14159


def calc2(x1, y1, x2, y2):  # calculate 2-point incline angle
    #print("%d %d %d %d\n" % (y1, y2, x1, x2))
    if x1 == x2:
        return 90
    k = (y1 - y2) / (x1 - x2) * (-1)
    # print(k)
    if k >= 0:
        return math.atan(k) * 180 / 3.14159
    else:
        return 180 + math.atan(k) * 180 / 3.14159


def calcAngle(arr, a, b, c):
    return calc(arr[a][0], arr[a][1], arr[b][0], arr[b][1], arr[c][0], arr[c][1])


def calcIncline(arr, a, b):
    return calc2(arr[a][0], arr[a][1], arr[b][0], arr[b][1])


# print(arr)
"""
arr = loadJson('EXAMPLE.json')
print(angle(arr,11,12,13))
"""
