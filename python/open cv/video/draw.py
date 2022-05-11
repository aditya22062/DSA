import cv2 as cv
import numpy as np

#blank=np.zeros((500,500),dtype=np.uint8)
#cv.imshow('blank',blank)
blank=np.zeros((500,500,3),dtype=np.uint8)
#blank[:]=0,255,0
#cv.imshow('Green',blank)#green blank space
#blank[200:300 , 300:400]=0,255,0
#v.imshow('Specified',blank)#specified region is blank
#2 draw a rectangle
cv.rectangle(blank,(0,0),(250,500),(0,0,255),thickness=2)#thickness=cv.FILLED will completely fill a rectangle
#thickness=-1 will work the same as cv.FILLED
#(blank.shape[1]//2,blak.shape[0]//2) instead of points will give the same result
cv.imshow('rectangle',blank)


cv.waitKey(0)