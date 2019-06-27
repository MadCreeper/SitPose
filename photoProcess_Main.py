import os
import sys
import time

import cv2

from calculateAngle import calcAngle
from calculateAngle import calcIncline
from getJson import loadJson

angleList = [['body_rLeg', 1, 9, 10, 85, 110],
             ['body_lLeg', 1, 9, 13, 85, 110],
             [' rKnee',	9, 10, 11, 85, 100],
             ['lKnee', 12, 13, 14, 85, 100],
             ['rAnkle',	2, 3, 4, 90, 120],
             ['lAnkle',	5, 6, 7, 90, 120]
             ]
inclineList = [['Body', 1, 8, 85, 120],
               ['rLeg'	, 10, 11, 80, 100],
               ['lLeg'	, 13, 14, 80, 100],
               ['rArm'	, 2, 3, 80,	110],
               ['lArm'	, 5, 6,	80,	110],
               ['neck'	, 17, 1, 85, 95]]


# [p1,p2,p3,angleMin,angleMax] p1,p2,p3 refers to the joint map (25 now)
PGDOWN = 2228224
SPACEBAR = 32
ESC = 27


def cv2Hitkey(k, waitTime):  # keyboard control
    t = cv2.waitKeyEx(waitTime)
    # print(t)
    if (t == k):
        return True
    return False


def init():
    print("Input Mode.\n Mode 1: Press 'SPACEBAR' to take screenshot \n Mode 2: Take screenshots automatically\n ESC to end program.\nPress any other key to quit.\n")
    mode = int(input())
    print('Mode = ' + str(mode) + '\n')
    if (mode != 1 and mode != 2):
        sys.exit()
    return (mode)


def checkForAngle(arr):
    for a in angleList:
        # name , p1,p2,p3, minAngle,maxAngle,curAngle
        curAngle = calcAngle(arr, a[1], a[2], a[3])
        print("%s keypoints = %d,%d,%d MinAngle = %d MaxAngle = %d CurAngle = %f" % (
            a[0], a[1], a[2], a[3], a[4], a[5], round(curAngle, 2)))

        if curAngle > a[5]:
            print("Too Big")
        if curAngle < a[4]:
            print("Too Small")
        if a[4] <= curAngle and curAngle <= a[5]:
            print("In Range")


def checkForIncline(arr):
    for a in inclineList:
        # name , p1,p2, minAngle,maxAngle,curAngle
        curAngle = calcIncline(arr, a[1], a[2])
        print("%s keypoints = %d,%d MinAngle = %d MaxAngle = %d CurAngle = %f" % (
            a[0], a[1], a[2], a[3], a[4], round(curAngle, 2)))

        if curAngle > a[4]:
            print("Too Big")
        if curAngle < a[3]:
            print("Too Small")
        if a[3] <= curAngle and curAngle <= a[4]:
            print("In Range")


# call OpenPosedemo.exe
comm = ".\\bin\\OpenPosedemo.exe --render_pose 2 --display 1 --net_resolution 320x176 --image_dir tempImg/  --write_images genImg --write_json genJson --logging_level 3"
# ---------------------------------------
mode = init()
cap = cv2.VideoCapture(0)
totFrame = 0

while(1):

    ret, frame = cap.read()                                          # get a frame
    # show a frame
    cv2.imshow("capture", frame)
    # the directory of the temp image

    # imgName = 'temp1'
    imgName = str(totFrame)
    imgNameFull = "tempImg/" + imgName + ".jpg"
    # this is to reduce LAG in auto mode, while avoid lag in manual mode
    if mode == 2 and cv2Hitkey(ESC, 1):
        break

    if ((mode == 2) | cv2Hitkey(PGDOWN, 1)):  # press pagedown to capture a photo

        cv2.imwrite(imgNameFull, frame)  # ***
        # pass shot picture to OpenPose                                                              # ... process the image / json
        os.system(comm)
        arr = loadJson("genJson/" + imgName + "_keypoints.json")

        print("ANGLE:")
        checkForAngle(arr)
        print("INCLINE ANGLE:")
        checkForIncline(arr)

        # remove the image  # FOR TEST REMOVE THIS LINE ***
        os.remove(imgNameFull)
        print("One Round Done!\n")
    if mode == 1 and cv2Hitkey(ESC, 1):
        break

    totFrame += 1
