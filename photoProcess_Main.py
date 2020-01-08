import os
import sys
import time

import cv2

from calculateAngle import calcAngle
from calculateAngle import calcIncline
from getJson import loadJson

angleList = [['body_rightLeg身体_右腿', 1, 9, 10, 80, 110],
             ['body_leftLeg', 1, 9, 13, 80, 110],
             [' rightKnee',	9, 10, 11, 80, 100],
             ['leftKnee', 12, 13, 14, 80, 100],
             ['rightElbow',	2, 3, 4, 90, 160],
             ['leftElbow',	5, 6, 7, 90, 160]
             ]
inclineList = [['Body', 1, 8, 85, 120],
               ['rightLeg'	, 10, 11, 80, 100],
               ['leftLeg'	, 13, 14, 80, 100],
               ['rightArm'	, 2, 3, 80,	110],
               ['leftArm'	, 5, 6,	80,	110],
               ['neck_body'	, 17, 1, 60, 80]]


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
            print("Too Big角度过大")
        if curAngle < a[4]:
            print("Too Small角度过小")
        if a[4] <= curAngle and curAngle <= a[5]:
            print("In Range角度正确")


def checkForIncline(arr):
    for a in inclineList:
        # name , p1,p2, minAngle,maxAngle,curAngle
        curAngle = calcIncline(arr, a[1], a[2])
        print("%s keypoints = %d,%d MinAngle = %d MaxAngle = %d CurAngle = %f" % (
            a[0], a[1], a[2], a[3], a[4], round(curAngle, 2)))

        if curAngle > a[4]:
            print("Too Big角度过大")
        if curAngle < a[3]:
            print("Too Small角度过小")
        if a[3] <= curAngle and curAngle <= a[4]:
            print("In Range角度正确")


# call OpenPosedemo.exe
comm = ".\\bin\\OpenPosedemo.exe --render_pose 2 --net_resolution 320x176 --image_dir tempImg/  --write_images genImg --write_json genJson --logging_level 3"
# ---------------------------------------
mode = init()
cap = cv2.VideoCapture(0)
totFrame = 0

while(1):

    ret, frame = cap.read()                                          # get a frame
    # show a frame
    cv2.imshow("capture", frame)
    # the directory of the temp image

    imgName = str(totFrame)

    #  ADD THIS LINE TO FIX INPUT IMAGE
    #imgName = 'temp1'  # *** 

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
        #os.remove(imgNameFull)
        print("One Round Done!\n")
    if mode == 1 and cv2Hitkey(ESC, 1):
        break

    totFrame += 1
