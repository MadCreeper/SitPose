import cv2
import sys
import time
import os
cap = cv2.VideoCapture(0)
totFrame=0
while(1):
    
    frame = cap.read() # get a frame
   
    cv2.imshow("capture", frame) # show a frame
    
    if cv2.waitKey(1) & 0xFF == ord('q'):   # when keyboard hits 'q' then take screenshot
        Imgname = "generatedImages/" + "test" + str(totFrame) +  ".jpg"
        cv2.imwrite(Imgname, frame)
     #   os.system("")

    if cv2.waitKey(1) & 0xFF == ord('p'):   # when keyboard hits 'p' then quit
        break

    totFrame+=1   
    time.sleep(0.01)
cap.release()
cv2.destroyAllWindows()