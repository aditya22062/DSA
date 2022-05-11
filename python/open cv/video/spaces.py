import cv2 as cv
import numpy as np


img=cv.imread('photo/park.jpg')
cv.imshow('Color',img)

#BGR to GRAY

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV HSV=hue saturation value

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
cv.waitKey(0)