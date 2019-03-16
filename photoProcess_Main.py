import sys
import time
import os
import cv2
from getJson import loadJson
from calculateAngle import calcAngle
angleList = ['torso_Rthigh',1,8,9]
PGDOWN = 2228224
SPACEBAR = 32
ESC = 27
def cv2Hitkey(k, waitTime):  # keyboard control
    t = cv2.waitKeyEx(waitTime)
    #print(t)
    if (t == k):
        return True
    return False

def init():
    print("Input Mode.\n Mode 1: Press 'SPACEBAR' to take screenshot \n Mode 2: Take screenshots automatically\n ESC to end program.\nPress any other key to quit.\n")
    mode = int(input())
    print('Mode = ' + str(mode) + '\n')
    if (mode != 1 and mode != 2):
        sys.exit()
    return(mode)
# call OpenPosedemo.exe
comm = ".\\bin\\OpenPosedemo.exe --render_pose 1 --display 0 --net_resolution 320x176 --image_dir tempImg/  --write_images genImg --write_json genJson --logging_level 3"
#---------------------------------------
mode = init()
cap = cv2.VideoCapture(0)
totFrame = 0

while(1):

    ret,frame = cap.read()                                          # get a frame
    cv2.imshow("capture", frame)                                    # show a frame
    imgName = "tempImg/" + "test" + str(totFrame) + ".jpg"          # the directory of the temp image

    if mode == 2 and cv2Hitkey(ESC,1):                                # this is to reduce LAG in auto mode, while avoid lag in manual mode
        break

    if ( (mode == 2) | cv2Hitkey(PGDOWN,1)) : #press pagedown to capture a photo

        cv2.imwrite(imgName, frame) 
        os.system(comm)                                             # pass shot picture to OpenPose                                                              # ... process the image / json
        arr = loadJson("genJson/test" + str(totFrame) + "_keypoints.json")
        #print(arr)
        angle1 = calcAngle(arr, 11, 12, 13)
        print(angle1)
       #  for p in badPostions:
           # print(hint[p])
                                                                  # ... process the image / json
        os.remove(imgName)                                          # remove the image
       
    if mode == 1 and cv2Hitkey(ESC,1):
        break
   
    totFrame += 1
 