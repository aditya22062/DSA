import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype=np.uint8)
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('circle',circle)
cv.imshow('rectanle',rectangle)

#bitwise operation
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise and',bitwise_and)

cv.waitKey(0)