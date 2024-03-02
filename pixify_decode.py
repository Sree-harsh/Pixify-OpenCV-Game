import numpy as np
import cv2
import os
import sys
import time
import random

def decode(image):
    yellow_squares = 0
    red_squares = 0
    shape_squares = 0

    for x in range(100,700,100):
        for y in range(100,700,100):
            pix = image[y,x]
            # print(pix)
            if np.array_equal(pix,np.array([0,255,255])):#pix.any() == np.array([0,255,255]):
                yellow_squares+=1
            elif np.array_equal(pix,np.array([0,0,255])):
                red_squares+=1

    for x in range(150,650,100):
        for y in range(150,650,100):
            if not np.array_equal(image[x-20,y-20],np.array([255,255,255])):
                shape_squares+=1
                continue
            elif not np.array_equal(image[x+20,y-20],np.array([255,255,255])):
                shape_squares+=1
                continue
            elif not np.array_equal(image[x-20,y+20],np.array([255,255,255])):
                shape_squares+=1
                continue
            elif not np.array_equal(image[x+20,y+20],np.array([255,255,255])):
                shape_squares+=1
                continue
        pass
    if yellow_squares*2+red_squares+shape_squares == 32:
        return " "
    else:
        return chr(yellow_squares*2+red_squares+shape_squares+96)
    