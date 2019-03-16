import sys
import time
import os
import cv2
def cv2Hitkey(k, waitTime):  # keyboard control
    t = cv2.waitKeyEx(waitTime)
    print(t)
    if (t == k):
        return True
    return False

cap = cv2.VideoCapture(0)
                                        # get a frame

while (1):
    cv2Hitkey(32, 1)
    ret,frame = cap.read()  
    cv2.imshow("capture", frame)  

cap.release()
cv2.destroyAllWindows()

    