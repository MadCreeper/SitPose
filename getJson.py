import json
import os
import sys
import numpy as np

def loadJson(jsonDir):
    np.set_printoptions(precision=3, suppress=1) # keep 3 digits of float (print)
    poseJson = open(jsonDir)
    poseData = json.load(poseJson)

    Arr = poseData['people'][0]["pose_keypoints_2d"] # get first person's data in json
    poseArr = np.array(Arr)
    poseArr = poseArr.reshape(18,-1)
    return (poseArr)
    
#print(loadJson('EXAMPLE.json'))