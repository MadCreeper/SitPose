import json
import os
import sys

import numpy as np


def loadJson(jsonDir):
    # keep 3 digits of float (print)
    np.set_printoptions(precision=3, suppress=1)
    poseJson = open(jsonDir)
    poseData = json.load(poseJson)

    # get first person's data in json
    Arr = poseData['people'][0]["pose_keypoints_2d"]
    poseArr = np.array(Arr)
    poseArr = poseArr.reshape(25, -1)
    return (poseArr)

# print(loadJson('EXAMPLE.json'))
